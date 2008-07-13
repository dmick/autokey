#!/usr/bin/env python

import sys, os, os.path, threading, gamin, string, time, ConfigParser
import iomediator

CONFIG_FILE = "../../config/abbr.ini"
LOCK_FILE = ".autokey.lck"

# Local configuration sections
CONFIG_SECTION = "config"
METHOD_OPTION = "method"
ABBR_SECTION = "abbr"

KEY_LOCK = threading.Lock()

# TODO: this totally fails to account for unicode systems!
WORD_CHARS = list("`'~" + string.ascii_letters)

def synchronized(lock):
    """
    Synchronisation decorator
    """
    def wrap(f):
        def newFunction(*args, **kwargs):
            lock.acquire()
            try:
                return f(*args, **kwargs)
            finally:
                lock.release()
        return newFunction
    return wrap

def escape_text(text):
    #text = text.replace("\\", "\\\\"
    return text.replace('"','\\\"')  

class ExpansionService:
    
    def __init__(self, trayIcon=None):
        self.trayIcon = trayIcon
        
        # Read configuration
        config = ConfigParser.ConfigParser()
        config.read([CONFIG_FILE])
        self.interfaceType = config.get(CONFIG_SECTION, METHOD_OPTION)
        self.abbreviations = dict(config.items(ABBR_SECTION))
        
        # Set up config file monitoring
        self.monitor = gamin.WatchMonitor()
        self.monitor.watch_file(CONFIG_FILE, lambda x, y: True)
        time.sleep(0.5)
        self.monitor.handle_events()
    
    def start(self):
        self.mediator = iomediator.IoMediator(self, self.interfaceType)
        self.mediator.start()
        self.inputStack = []
        self.ignoreCount = 0
    
    def pause(self):
        self.mediator.pause()
    
    def tempsendstring(self, string):
        """
        @deprecated: do not use!
        """        
        self.mediator.send_string(string)
        
    def is_running(self):
        try:
            return self.mediator.isAlive()
        except AttributeError:
            return False
        
    def switch_method(self, method):
        if self.is_running():
            self.pause()
            restart = True
        else:
            restart = False
        
        self.interfaceType = method
        
        if restart:
            self.start()
            
    def shutdown(self):
        if self.is_running():
            self.pause()
        self.monitor.stop_watch(CONFIG_FILE)
        try:
            config = ConfigParser.ConfigParser()
            config.read([CONFIG_FILE])        
            config.set(CONFIG_SECTION, METHOD_OPTION, self.interfaceType)
            fp = open(CONFIG_FILE, 'w')
            config.write(fp)
        except Exception:
            pass
        finally:
            fp.close()
        
    def handle_keypress(self, key):        
        # Check for modification of config file
        if self.monitor.event_pending() > 0:
            self.__loadAbbreviations()
        self.monitor.handle_events() # flush any remaining events
        
        # Ignore keys received after sending an expansion
        if self.ignoreCount > 0:
            self.ignoreCount -= 1
            return
        
        if key == iomediator.KEY_BACKSPACE:
            # handle backspace by dropping the last saved character
            self.inputStack = self.inputStack[:-1]

        elif key in WORD_CHARS:
            # Key is a character (i.e. not a modifier)
            self.inputStack.append(key)
            
        else:
            # Key is a character and not a word character
            expansion = self.__attemptExpansion()
            if expansion is not None:
                self.mediator.send_backspace(len(self.inputStack) + 1)
                
                # Shell expansion
                text = os.popen('/bin/echo -e "%s"' % escape_text(expansion.string)).read()
                text = text[:-1] # remove trailing newline
                
                self.mediator.send_string(text)
                
                if expansion.ups > 0:
                    self.mediator.send_up(expansion.ups)
                
                if expansion.lefts > 0:
                    self.mediator.send_left(expansion.lefts)
                
                if key is not None:
                    self.mediator.send_key(key)

                self.ignoreCount = len(text) + len(self.inputStack) + 1
                self.mediator.flush()
                
            self.inputStack = []
                
        if not self.__possibleMatch():
            self.inputStack = []
            
        print self.inputStack
        
    def __possibleMatch(self):
        input = ''.join(self.inputStack)

        if '~' in input:
            return True

        for key in self.abbreviations.keys():
            if key.startswith(input):
                return True
        
        return False
        
    def __attemptExpansion(self):
        try:
            input = ''.join(self.inputStack)
            values = input.split('~')
            if len(values) > 1:
                try:
                    return Expansion(self.abbreviations[values[0]] % tuple(values[1:]))
                except TypeError:
                    print "Badly formatted abbreviation argument"
                    return None
            elif '%%' in self.abbreviations[input]:
                try:
                    firstpart, secondpart = self.abbreviations[input].split('%%')
                    # count lefts and ups
                    rows = secondpart.split('\n')
                    lefts, ups = len(rows[0]), len(rows) - 1
                    result = Expansion(''.join([firstpart, secondpart]))
                    result.lefts = lefts
                    result.ups = ups
                    return result
                except ValueError:
                    print "Badly formatted abbreviation argument"
                    return None
            else:
                return Expansion(self.abbreviations[input])
        except KeyError:
            return None
        
    def __loadAbbreviations(self):
        try:
            p = ConfigParser.ConfigParser()
            p.read([CONFIG_FILE])
            self.abbreviations = dict(p.items(ABBR_SECTION))
            if self.trayIcon is not None:
                self.trayIcon.config_reloaded()
        except Exception, e:
            self.trayIcon.config_reloaded("Abbreviations have not been reloaded.\n" + str(e))
        
class Expansion:
    
    def __init__(self, string):
        self.string = string
        self.ups = 0
        self.lefts = 0    
    