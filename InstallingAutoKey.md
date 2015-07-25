<h1>Installing AutoKey</h1>
<br />
<h1>General Information</h1>
<b>First time installation:</b>
<p>
AutoKey can be installed from a repository, a deb package or built from source.  Carefully following the instructions for the appropriate method should seamlessly install AutoKey.  For the details, see the sections <i>Installing AutoKey from a Repository</i> and <i>Building and installing from a deb package</i>.<br>
</p><p>
<b>Upgrades from previous versions:</b>
</p><p>
<ol>
<li>If you already have AutoKey installed, you do not need to remove the previous version of AutoKey in order to upgrade.<br>
</li>
<li>You Must quit AutoKey and make sure the AutoKey icon is not in the <i>Notification Area</i> or <i>System Tray</i> prior to starting the installation.<br>
</li>
<li>You should backup <font color='#880080'>~/.config/autokey</font> or at least copy the directory to somewhere in your home directory prior to doing an upgrade.  That is the only thing that you need to back up.  AutoKey will make an additional backup copy of your configuration file before it upgrades it to v0.80 format.<br>
</li>
<li>Again, as I said at the beginning, please follow the instructions very carefully for either method.  A single typo or misspelling can cause the installation to fail.<br>
</li>
</ol>
<h3>Installing AutoKey from a Repository</h3>
</p><p>
Using a repository to install AutoKey in Ubuntu is easy. When installed from a repository, AutoKey will be automatically installed—with all dependencies and kept up to date by your package manager.<br>
</p><p>
Note that most of the time either method of automatic installation from a repository described below will install the latest version—but not all of the time.  If you want to be sure that you are installing the latest version then compare the listed version <a href='http://code.google.com/p/autokey/downloads/list'>here</a>, with the version offered from the repository sources described below.  If the version shown there is more recent (higher number) than the ones in your repositories—and you want the newer version—you will have to download it and build the package from source (see: <i>Installing AutoKey from source code</i>).<br>
</p><p>
There are two different repositories to choose from:<br>
</p><p>
<b>The Ubuntu Repositories</b>
</p><p>
Since AutoKey is already available in the Ubuntu repositories, you can use any of the software installation programs that came with your version of Ubuntu to install AutoKey—the same way you install standard Ubuntu packages.  Examples of software installation programs are: Synaptic, Adept, Ubuntu Software Center, apt or any other Ubuntu installation program that you prefer.<br>
</p><p>
<b>Using AutoKey's PPA</b>
</p><p>
If you are new to Ubuntu, I am sure you are wondering what a PPA is.  PPA stands for <i>Personal Package Archive</i> and is a way for individuals who have created programs for Ubuntu to create and maintain a repository that the software installation programs in Ubuntu can use to install them.  This allows you to install their packages in the same way you install standard Ubuntu packages as well as automatically receive update notices.  They are not checked or monitored by the creators of Ubuntu and they are not responsible for any problems—nor do they want to hear about them.  You install software from PPAs at your own risk.<br>
</p><p>
Using <a href='https://launchpad.net/~cdekter/+archive/ppa/+index#'>AutoKey's PPA</a> is the best way to keep AutoKey updated.  To use the PPA, you have to add it to your system's repository list.  This can be done using the command line in a terminal (which probably seems intimidating, but is actually the easiest) or using your favorite Ubuntu software installer.<br>
</p><p>
Both methods are described under the heading "Adding this PPA to your system" on AutoKey's PPA page.<br>
</p><p>
<b>Using the Command Line to Add the Repository:</b>
</p><p>
The link <a href='https://launchpad.net/+help/soyuz/ppa-sources-list.html'>Read about installing</a> describes how to use the command line in a terminal to add the repository and the software key.  Most problems you will have using this method will be from typos or not specifying your version of Ubuntu correctly.<br>
</p><p>
NOTE: Before you use the instructions below, make sure you close any software installation program that may be running—or you will get an error message.  To avoid errors, only one program at a time is allowed to use the repository.<br>
</p><p>
The following commands only work if you are using Lucid (10.04) or a later version of Ubuntu.<br>
</p><p>
Each command must be entered separately into a terminal and then the Enter key must be pressed to run it.<br>
</p><p>
This command makes the PPA available to to your package management system.<br>
<p></p>
<font color='#880080'>sudo add-apt-repository ppa:cdekter/ppa</font>
</p><p>
The next command downloads the list of currently available software for all of the software packages available from the repositories you have configured, including AutoKey's.  This might take a few minutes to finish.<br>
</p><p>
<font color='#880080'>sudo apt-get update</font>
</p><p>
Once this is done, your favorite software installation program "should" automatically be able to see and use the updates.  If it does not, then use the <i>Reload/Update Package Information</i> icon or menu selection in your software installation program.<br>
</p><p>
If you are using an earlier version of Ubuntu, the instructions for earlier versions are on the PPA page as well.<br>
</p><p>
<b>Using Your Favorite Installation Program</b>
</p><p>
If you want to use your favorite software installer, on the  <a href='https://launchpad.net/~cdekter/+archive/ppa/+index#'>PPA page</a>, the instructions are under the sub-heading "<i>Technical details about this PPA</i>".  Just click on the arrow to the left of the heading and the instructions will appear.  Be sure to select your version in the text box to the right of the sub-heading <i>"Display sources.list entries for:"</i>.  The entries for the version you selected will appear in the box below.<br>
</p><p>
Since each of the different software installation programs you might be using will have a different method of adding a repository, you will have to figure out how to use your personal preference by reading its documentation or man page.<br>
</p><p>
<b>Other Linux versions</b>
</p><p>
For all Linux versions that <b>do not</b> include AutoKey in their packaging system, you will have to build a package from source.  The latest source code can be found <a href='http://code.google.com/p/autokey/downloads/list'>here</a>.<br>
</p><p>
Building from source will work on any Linux distro that has Python <font color='#880080'>Distutils</font> available (the setup infrastructure that AutoKey uses underneath .deb files, which are the files Ubuntu uses for its packaging system). This comes with the caveat that it will probably require some fiddling to get it working.  In most cases the .deb files for Ubuntu <i>probably</i> will not work for other distros without modification since the paths inside the <font color='#880080'>.deb</font> file can and often do change from one distro to another and sometimes change between versions of the same distro.<br>
</p><p>
If you build from source, the only way to be notified of any upgrades is to 'star' the project on the Google Code site which requires having a Google account. You will then be sent an email when a new version is uploaded.<br>
</p><p>
Currently for Debian, Ubuntu, and many Ubuntu derivatives such as Linux Mint, running this command in the terminal will install AutoKey.  Or you can use the software installer of your choice:<br>
</p><p>
<font color='#880080'>sudo apt-get install autokey</font>
</p><p>
If you get an error message indicating that the file was not found, then your distro does not provide a binary package for AutoKey.<br>
</p><p>
Distros such as Arch Linux and Fedora (and possibly others that I do not know about) have provided binary packages for installing AutoKey in the past and hopefully will continue to do so.  Fedora is the only distro that I know of that has built <font color='#880080'>rpm</font> packages for AutoKey.<br>
</p><p>
If you know of any other Linux distro that provides AutoKey binary package files in their repository, please post that distro's name on the AutoKey forum and, if possible, a link to the information about the package.<br>
</p><p>
<b>Problems or Questions</b>
</p><p>
If you have a problem or questions (or just want to join in the discussion), join the <a href='http://groups.google.com/group/autokey-users'>AutoKey Users group</a> and post your questions there.  You can—and should—search this forum for information on how to do what you are having problems with as well as for information about any installation problem you are having, before you post your question.<br>
</p><p>
If you have a problem that you want to post and request help with, please read the troubleshooting guide before you post your question and provide the information that it recommends.  The troubleshooting guide and all other online documentation is located  <a href='http://code.google.com/p/autokey/w/list'>here</a>.<br>
</p><p>
<h3>Installing AutoKey from source code.</h3>
</p><p>
<b>Requirements</b>
</p><p>
Installing the python source code for AutoKey requires a full Debian package build.  You cannot install AutoKey using only the <font color='#880080'>setup.py</font> script contained in the <font color='#880080'>autokey-(version).tar.gz</font> source file.<br>
</p><p>
Before you try to build the Debian package, make sure that the packages <font color='#880080'>build-essential</font> and <font color='#880080'>cdbs</font> (the common build system for Debian packages) are installed on your system.  Without these packages, you can not build the AutoKey Debian package.<br>
</p><p>
The program <font color='#880080'>cdbs</font> and <font color='#880080'>build-essential</font> will be in your repository and can be installed using apt, Synaptic, etc.<br>
</p><p>
<b>Pre-Build Safety Issues:</b>
</p><p>
If you are upgrading from an older version of AutoKey, before starting to build the <font color='#880080'>.deb</font> package and install the the new version of AutoKey, you should:<br>
</p><p>
<ol>
<li>
Turn off AutoKey if is currently running (i.e. using the Quit choice in the pop-up menu that appears when the  AutoKey icon in the system tray is left clicked with the mouse).<br>
</li>
<li>
Then, backup—BUT DO NOT DELETE—your <font color='#880080'>~/.config/autokey</font> directory or at least copy the contents to somewhere safe on your hard drive.<br>
</li>
<li>
If you are upgrading an existing version of AutoKey, your phrases and scripts will be automatically converted (if necessary) to the new version and installed ready for immediate use.<br>
</li>
</ol>
</p><p>
At this point you are ready to start the build process.  There are 3 explanations of how to build and install the packages:<br>
</p><p>
<ol>
<li>
Version <b>A</b>, for experts (the short version).<br>
</li>
<li>
Version <b>B</b>, for knowledgeable people who want an overview of the steps.<br>
</li>
<li>
Version <b>C</b>, For those who don't know anything about installing or building software packages but want to learn.<br>
</li>
</ol>
<b>Version A:</b>
</p><p>
If you use Python and know how to build a Debian package this is all the information you need:<br>
</p><p>
<ol>
<li>
Download the version of your choice from the <a href='http://code.google.com/p/autokey/downloads/list'> download page</a> to your hard drive and extract the tarball.<br>
</li>
<li>
Then, run these commands from inside the directory the extraction created:</li>
<ol>
<li><font color='#880080'>dpkg-buildpackage -us -uc</font></li>
<li><font color='#880080'>cd ../</font></li>
<li><font color='#880080'>sudo dpkg -i autokey-gtk<i>(version).deb autokey-common</i>(version).deb</font></li>
</ol>
<li>
AutoKey is installed at this point and can be started in a terminal using <font color='#880080'>autokey-gtk</font> for normal use or <font color='#880080'>autokey-gtk -l</font> for full logging output in the terminal.  You can also start it from your desktop's menu for selecting applications.<br>
</li>
</ol>
</p><p>
You can now delete the AutoKey files and directories in the directory you built the Debian packages in. They are no longer needed.<br>
</p><p>
<b>Version B:</b>
</p><p>
If you know how to build a Debian package from Python source code, but don't do it often enough to remember all of the detailed steps, here they are:<br>
</p><p>
<ol>
<li>
Download the version of your choice from the <a href='http://code.google.com/p/autokey/downloads/list'> download page</a> to your hard drive.<br>
</li>
<li>
Move or download the source code to a local directory of your choice.<br>
</li>
<li>
Open a terminal window in that directory.<br>
</li>
<li>
un-tar the source code tarball using <font color='#880080'>tar xvzf &lt;filename></font> or your file manager.<br>
</li>
<li>
cd to the directory just created by the tar command, called <font color='#880080'>autokey-x.xx.x</font> (change x.xx.x to the version number on the filename you downloaded)<br>
</li>
<li>
Type in this command and press enter:<br>
<p>
<font color='#880080'>dpkg-buildpackage -us -uc</font>
</p><p>
Make sure the word "aborting" does not appear in the output after you type the command—if it does, it will usually be in the first 10 to 20 lines.  If everything works correctly, the output from this command will be 8 or more screen-fulls long and the last line will be:<br>
</p><p>
<font color='#880080'>dpkg-buildpackage: full upload; Debian-native package (full source is included)</font>
</p>
</li>
<li>
Type in:<br>
<br />
<font color='#880080'>cd ../</font>
<br />
and press enter to move up to the directory the newly created <font color='#880080'><code>*</code>.deb</font> files are in.<br>
</li>
<li>
Type in this command and press Enter.  It ALL needs to be on a single line in the terminal:<br>
<p>
<font color='#880080'>sudo dpkg -i autokey-gtk<i>(version).deb autokey-common</i>(version).deb</font>
</p><p>
Replace (version) with the version numbers used in the newly created <font color='#880080'><code>*</code>.deb</font> files. In the terminal window, the output for this command (if successful) will be around 15 lines long.</p>
</li>
<li>
AutoKey is installed at this point and should be started in a terminal using <font color='#880080'>autokey-gtk</font> for normal use or <font color='#880080'>autokey-gtk -l</font> for full logging output in the terminal.  You can also start it from the desktop's drop down menu for selecting applications.<br>
</li>
</ol>
</p><p>
Once the Icon appears in the system tray, you can left click on it, Open the Main Window and create scripts and phrases as well as configure it to start automatically every time you start up your computer.<br>
</p><p>
You can now delete the AutoKey directory where you built the Debian packages. They are no longer needed.<br>
</p><p>
<b>Version C:</b>
</p><p>
<ol>
<li>
For those not familiar with installing or building software packages who want to learn, here are the detailed steps to build and install AutoKey:<br>
</li>
<li>
First, download the version of your choice from the <a href='http://code.google.com/p/autokey/downloads/list'>download page</a> to your hard drive.<br>
</li>
<li>
Then move the file to the directory that you use to build or compile other software, if you have one.  If you do not have one, it is a good idea to create a new directory, anywhere in your home directory, to use to extract and uncompress the file and to build the <font color='#880080'>.deb</font> package in.  I created a directory called install, but what you name it is not important.<br>
</li>
<li>
You then need to open a terminal window and change to the directory where you wish to build the package.  If you created a directory in your Download folder called install you would use this command to change to that directory:<br>
<p>
<font color='#880080'>cd ~/Downloads/install</font>
</p><p>
in the terminal window.<br>
</p>
</li>
<li>
Once the source code file is in position and your terminal is showing the right directory in its window you are ready to uncompress the source code file.<br>
<p>
AutoKey's files are packaged with the program <font color='#880080'>tar</font> and compressed with the program <font color='#880080'>gzip</font> this results in a file with a name like; <font color='#880080'>autokey-(version).tar.gz</font>.  These files are commonly called tarballs.  (I guess because they were created with tar and everything was all wrapped up and compressed into a single ball containing many different files.)<br>
</p><p>
The universal method of uncompressing <font color='#880080'>.tar.gz</font> files is to enter this command in the terminal window:<br>
</p><p>
<font color='#880080'>tar xvzf autokey(version).tar.gz</font>
</p><p>
You will of course have to replace <font color='#880080'>(version)</font> with the version numbers on the package you downloaded.<br>
</p><p>
Many file managers like Konqueror will let you right click on the file name and chose to extract the highlighted file from a list of different choices.  <i>Extract Here</i>, if available, is usually the best choice.  There are many different file managers and there is no way I could explain how to use all of them.  So, if you want to use your file manager to uncompress and extract files, you will have to research how to do this yourself.<br>
</p>
My only advice is to ALWAYS do the extraction in an empty directory.  If something goes wrong it can be messy ....<br>
</li>
<li>
When the tarball is uncompressed, it creates a new directory called <font color='#880080'>autokey-x.xx.x</font> (x.xx.x will be the version number of the AutoKey package you are building).<br>
</li>
<li>
You now have to move to that directory using this cd command in the terminal:<br>
<p>
<font color='#880080'>cd autokey-x.xx.x</font>
</p>
<p>Change x.xx.x to the numbers of the new directory.</p>
</li>
<li>
Once you are in the new AutoKey directory, enter the following command in the terminal window to build the AutoKey package.  Press enter to start the build.<br>
<p>
<font color='#880080'>dpkg-buildpackage -us -uc</font>
</p><p>
Make sure the word <i>aborting</i> does not appear in the output after you type the command—if it does, it will usually be in the first 10 to 20 lines.  If it does appear, the package was not built and you can not continue.  If everything works correctly, the output from this command will be 8 or more screen-fulls long and the last line will be:<br>
</p><p>
<blockquote><font color='#880080'>dpkg-buildpackage: full upload; Debian-native package (full source is included)</font>
</p>
Success .… You have just created the <font color='#880080'>.deb</font> package/file and can now proceed to the installation part.<br>
</li>
<li>
In the terminal window enter the following command and press enter.<br>
<p>
<font color='#880080'>cd ../</font>
</p><p>
This moves up one directory (out of the AutoKey directory that extracting the tarball created).  This is where the package build process put the <font color='#880080'><code>*</code>.deb</font> files it created.<br>
</p>
</li>
<li>
Now we install the <font color='#880080'><code>*</code>.deb</font> files.  First we want to know what they are called.  In the terminal type:<br>
<p>
<font color='#880080'>ls</font>
</p>
and press enter.  This will list all the files in the directory the terminal is in.  You have to use the numbers from the <font color='#880080'><code>*</code>.deb</font> files to replace the <font color='#880080'>(version)</font> place holder in the command in step 11 below.<br>
</li>
<li>
It is really easy to mistype the following command or accidentally start the process before you get everything correct, so I suggest you use the command line's built in expansion feature to create the command.  First copy and paste (or type in):<br>
<p>
<font color='#880080'>sudo dpkg -a autokey-g</font>
</p><p>
in the terminal window and then press the Tab key.<br>
</p><p>
This should expand to: <font color='#880080'>sudo dpkg -i autokey-gtk<i>(your version).deb</font> with a space at the end. Then, at the end of this command, copy and paste (or type in):<br>
</p></i><p>
<font color='#880080'>autokey-c</font>
</p><p>
making sure you do not overwrite the space and then press the Tab key, which will expand the filename and the end result in the terminal should look like this:<br>
</p><p>
<font color='#880080'>sudo dpkg -i autokey-gtk<i>(your version).deb autokey-common</i>(your version).deb</font>
</p><p>
In the terminal, this should all appear in a single line.<br>
</p>
</li>
<li>
Press enter to start the installation.<br>
<p>
Once started, it will ask you for your login password.  Once you have entered your password and pressed enter, it will start the installation process.<br>
</p><p>
In the terminal, the output for this command (if successful) will be only around 15 lines long.<br>
</p>
</li>
<li>
You are now finished with the installation.<br>
</li>
</ol>
<p>
<b>Starting AutoKey:</b>
</p><p>
You can start AutoKey from the terminal by typing <font color='#880080'>autokey-gtk</font> and pressing enter or you can start it from the desktop's drop down menu for selecting applications.  Once the Icon appears in the system tray, you can left click on it and create scripts and phrases as well as configure it to start automatically every time you start up your computer.<br>
</p><p>
Later, if you have problems, you can start AutoKey with full logging output using the command <font color='#880080'>autokey-gtk -l</font> and it will list every step it takes in the terminal window.<br>
</p><p>
<h3>Installation Related Issues</h3>
</p><p>
<h3>Moving AutoKey scripts and phrases from computer to computer.</h3>
</p><p>
The individual folders (Top Level Folders) and file pairs containing information about the phrases and scripts are stored in the <font color='#880080'>~/.config/autokey/data</font> folder.  In each Top Level Folder, there are two files per each phrase or script.  They both have the same name, but different extensions, and one of them is a "hidden" file (it has a period at the front of the name and can not be seen unless the file manager or the program you use in a terminal is told to display them).  An example pair would be; <font color='#880080'>.tt.json</font> and <font color='#880080'>tt.txt</font>.  The <font color='#880080'><code>*</code>.txt</font> file contains the name of the script or phrase that is displayed in AutoKey. (see the section below <i>How to re-import pre-v0.80 <font color='#880080'><code>*</code>.json</font> files</i>, for a definition of a <font color='#880080'>.json</font> file)<br>
</p><p>
Make sure you include the "hidden" <font color='#880080'><code>*</code>.json</font> files as well as the <font color='#880080'><code>*</code>.txt</font> files when you transfer individual file pairs and/or complete folders—or the scripts and phrases will not work.<br>
</p><p>
<b>Duplicating or Cloning ALL your scripts and phrases to a new system.</b>
<br /><br />
You do this by replacing the entire <font color='#880080'>~/.config/autokey/</font> folder and all its sub-folders in the "receiving" computer with the <font color='#880080'>~/.config/autokey/</font> folder from the "original" computer.  This will make the "receiving" computer identical to the "original" computer.<br>
</p><p>
<b>Merging one system's scripts and phrases with a second computer.</b>
<br /><br />
Merging is done by copying all of the contents of any sub-folder in the "original" computer's <font color='#880080'>~/.config/autokey/data</font> folder to the sub-folder of your choice in the "receiving" computer's <font color='#880080'>~/.config/autokey/data</font> folder.<br>
</p><p>
A step by step description of merging is: copy the "contents" (i.e. files, not folders) of any one of the sub-folders (Top Level Folders) from the "original" computer's <font color='#880080'>~/.config/autokey/data</font> folder into a sub-folder (i.e. existing or newly created Top Level Folder) in the "receiving" computer's <font color='#880080'>~/.config/autokey/data</font> folder.<br>
</p><p>
Once all of this is finished, when you close and restart AutoKey all of the transferred folders, scripts and phrases will appear in AutoKey's main menu along with all Top Level Folders, phrases and scripts that were in the "receiving" computer's sub-folder prior to the transfer.<br>
</p><p>
<b>Warning:</b> If a filename in the "original" computer is identical to the one in the "receiving" computer—the one in the "receiving" computer will be overwritten.  If they both have identical contents—this is not a problem.  If they are not identical, then the original phrases/scripts in the "receiving" computer will be replaced by the new phases and scripts.  You will usually get a warning that this is fixing to happen—except when you use programs like cp or mv from the console.<br>
</p><p>
In a few rare cases, merges can cause duplicate script or phrase names in the main menu of the "receiving" computer.  You can change the "description:" line in the <font color='#880080'><code>*</code>.txt</font> file—in order to solve this type of file name conflict.  Please make a backup of the individual files you are editing or of the entire directory, before you edit these files.<br>
</p><p>
<b>Copying specific phrases or scripts from one computer to another:</b>
</p><p>
If you move the pair of files into one of the sub-folders in the "receiving" computer's <font color='#880080'>~/.config/autokey/data</font> folder, when you restart AutoKey it will read and include that script or phrase.  Note, that the above "Warning" about overwriting files applies here as well.  You can copy as many of these "pairs" of files at one time as you want.  Just remember that you have to restart AutoKey before they will be available.<br>
</p><p>
<b>How to re-import pre version 0.80.x <font color='#880080'><code>*</code>.json`</font> files</b>
</p><p>
A <font color='#880080'><code>*</code>.json</font> file is a configuration file.  In the case of version <font color='#880080'>0.80.x</font>  or later of AutoKey, each one contains the information about an individual script or phrase that you created.  They are plain text (ASCII) files and, if edited, you MUST use a text editor like nano, gedit or kate.  If you use a word processor to edit them, it will insert word processor codes that will make the <font color='#880080'><code>*</code>.json</font> and <font color='#880080'><code>*</code>.txt</font> files unusable.<br>
</p><p>
The <font color='#880080'><code>*</code>.json</font> files are "hidden" files (they have a period at the front of the name and can not be seen unless the file manager or the program you use in a terminal is told to display them) and have a matching <font color='#880080'><code>*</code>.txt</font> file paired with them.  Both the "hidden" <font color='#880080'><code>*</code>.json</font> file and the <font color='#880080'><code>*</code>.txt</font> file must be present for the phrase or script to work.<br>
</p><p>
Versions of AutoKey prior to <font color='#880080'>0.80.x</font> used a single <font color='#880080'><code>*</code>.json</font> file to contain ALL information about ALL scripts and phrases.  When upgrading, this single file has to be converted into matched pairs of files for each phrase or script and stored in a "Top Level Folder".<br>
</p><p>
AutoKey version <font color='#880080'>0.08.x</font> will automatically import and convert version <font color='#880080'>0.71.x</font> or earlier <font color='#880080'>autokey.json</font> files to the new format.<br>
</p><p>
The following instructions assume that you already have a running version of AutoKey <font color='#880080'>0.80.x</font> installed.<br>
</p><p>
<ol>
<li>
Quit AutoKey and make sure the AutoKey icon is not in the <i>Notification Area</i> or <i>System Tray</i>.<br>
</li>
<li>
If you have created scripts for version <font color='#880080'>0.80.x</font> and you want to preserve your current scripts and phrases, "COPY" the <font color='#880080'>~/.config/autokey/data</font> folder to somewhere else in your home directory for safekeeping.<br>
</li>
<li>
Then, delete these two files in the original folder: <font color='#880080'>~/.config/autokey/autokey.json</font> and <font color='#880080'>~/.config/autokey/autokey.json~</font>
</li>
<li>
If you want to re-import the backup file of earlier versions of AutoKey that were automatically created by AutoKey during an upgrade to version <font color='#880080'>0.80.x</font>, you need to rename <font color='#880080'>~/.config/autokey/autokey.json(old version)</font> to <font color='#880080'>~/.config/autokey/autokey.json</font>.  In my case the file to be renamed was <font color='#880080'>autokey.json0.71.2</font>.<br>
</li>
<li>
If you want to use a previous backup or copy of an "autokey.json" file that you made, or one from a different computer, "move" the current <font color='#880080'>~/.config/autokey/autokey.json</font> to somewhere safe—or delete it if you do not want to save it. Then copy and paste in the version that you want to convert.<br>
</li>
<li>
The first time you start AutoKey, it will automatically import the older <font color='#880080'>autokey.json</font> file and convert it to the new version <font color='#880080'>0.80</font> format as well as make a backup of it.<br>
</li>
<li>
Now your newly converted and backed up scripts and phrases can be copied, moved, replaced or merged as described in the section, <i>Moving AutoKey scripts and phrases from computer to computer</i> above.<br>
</li>
</ol>
</p><p></blockquote>

<br />
November 2011<br>
<br />
Original author, Keith W. Daniels<br>
<br />
Edited by Joseph Pollock<br>
</p>