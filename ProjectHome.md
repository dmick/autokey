AutoKey is a desktop automation utility for Linux and X11. It allows you to manage collection of scripts and phrases, and assign abbreviations and hotkeys to these. This allows you to execute a script or insert text on demand in whatever program you are using.

AutoKey features a subset of the capabilities of the popular Windows-based [AutoHotkey](http://www.autohotkey.com), but is not intended as a full replacement. For a Linux-based implementation of AutoHotkey, see [IronAHK](http://github.com/polyethene/IronAHK). AutoKey's GUI features a number of concepts and features inspired by the Windows program [PhraseExpress](http://www.phraseexpress.com).

### Project Status ###
AutoKey has now reached v0.90 and is (from the point of view of the developer) feature complete. It is built using current toolkits (GTK3 and QT4) so should be reasonably future-proof. We are actively looking for maintainers to assist with fixing minor bugs. At this stage no new feature work is planned, but patches may be considered.

### Features ###
  * Python scripting engine allows you to automate virtually any task that can be accomplished via the keyboard and/or mouse
  * Built-in code editor with autocomplete and calltips
  * Scripts are plain Python files that can be edited in any text editor
  * Similarly, phrases are stored as plain text files
  * Create collections of phrases/scripts in folders, and assign a hotkey or abbreviation to the folder to display a popup menu
  * Regular expressions can be used to filter windows by their title or class, to exclude hotkeys/abbreviations from triggering in certain applications
  * Scripts, phrases and folders can be attached to the notification icon menu, allowing you to select them without assigning a hotkey or abbreviation

### Getting it ###

Source archives are available on the [downloads page](http://code.google.com/p/autokey/downloads/list). Users of Debian/Ubuntu can follow the instructions to add the [PPA](http://launchpad.net/~cdekter/+archive/ppa). .deb package files can also be downloaded directly from the PPA for installation on other distributions that provide dpkg or a similar program.

### Getting Started ###
Hopefully, AutoKey's UI should be easy enough for everyone up to and including beginners to understand. You can read the BeginnersGuide, or follow this excellent [tutorial](http://saravananthirumuruganathan.wordpress.com/2010/04/14/autokey-linux-utility-for-text-substitution-hotkeys-and-desktop-automation/) For examples on how to use the scripting feature, see the SampleScripts wiki page.

There is also an nice tutorial available on [YouTube](http://www.youtube.com/watch?v=4KV_B6dBFHA).

### Getting Help ###
If you're stuck and need some help, visit the [AutoKey Users](http://groups.google.com/group/autokey-users) group.

### Support Us ###
Donations of any size are welcomed - you can donate via [Paypal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=L333CPRZ6J8JC)

Bugs and feature requests may be logged in the the issue tracker on this site.