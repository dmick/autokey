### What are the dependency packages for AutoKey? ###
On Debian or Ubuntu you can get the dependencies by typing:

```
apt-get install python-gtk2 python-gtksourceview2 python-glade2 python-xlib python-notify python-pyinotify wmctrl
```

Note that if you installed AutoKey from a .deb or using apt-get, these dependencies will automatically be installed for you.

### What is the license of AutoKey? ###
AutoKey is published under GNU GPL v3 license.

### Does AutoKey work with scripts which were written with the popular AutoHotKey Windows application? ###
No. AutoKey's built-in Python scripting is arguably much more powerful than the AHK language and makes it possible to do many of the things that AutoHotKey scripts can do on Windows, in addition to some things AHK doesn't support.

### Is AutoKey available on Microsoft Windows? ###
No. There are similar alternatives on Windows like [PhraseExpress](http://www.phraseexress.com) and [AutoHotKey](http://www.autohotkey.com/)

### Can I temporarily suspend/resume AutoKey? ###
To toggle !Autokey from suspend/resume, use the hotkey which you have specified in Settings -> Advanced Settings -> Special Hotkeys->Use a hotkey to toggle expansions. Alternatively this can be controlled from the notification icon's popup menu.

### What are the trigger characters? ###
The default trigger characters are dependent on your locale. They are any characters that are not normally considered part of a word. For English locales, these are characters like Enter (Return), Tab, Space and punctuation, among others.

### Where is my configuration information stored? Can I move those to other machines? ###
By default AutoKey stores your settings under ~/.config/autokey. You can of course create AutoKey folders anywhere you wish as well, using "Create New Top-Level Folder". Folders containing phrases and scripts can be freely copied between machines using your favourite file manager, or synchronised using a program such as Dropbox.

### I like this project and would like to donate some money. Where do I donate? ###
Thanks for your support.You can use the following link to donate [Donate](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=L333CPRZ6J8JC)