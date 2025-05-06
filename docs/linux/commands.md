# Linux Most Used Commands Cheatsheet

### Update and Upgrade
```sh
apt-get update & apt-get upgrade -y
```

### User Management Commands
**sudo - execute a command as another user or with elevated privileges**

Run command with the security privileges of the superuser (Super User DO).
```sh
sudo
```

**whoami - display the current user name**

Displays the username of the current user.
```sh
whoami
```

**Display who is logged in**

Shows a list of users currently logged into the system.
```sh
who 
```

**Show the user you are logged in as and the groups you are part of**

Displays the current user and the groups they belong to.
```sh
id
```

**Show the groups you are part of**

Lists all the groups the current user is a member of.
```sh
groups
```

**useradd - add a new user to the system**

Creates a new user account.
```sh
sudo useradd <user-name>
sudo adduser <user-name> <other-parameters>
sudo useradd harry
```

**passwd - change the password for a user**

Changes the password for a specified user.
```sh
sudo passwd <user-name>
```

**To change the password of a user**

Locks the password of a specified user.
```sh
sudo passwd -l <user-name>
```

**To remove a newly created user**

Deletes a user account and their home directory.
```sh
sudo userdel -r <user-name>
```

**userdel - delete a user from the system**

Deletes a user account.
```sh
sudo userdel harry
```

**To add a user to a group**

Adds a user to a specified group.
```sh
sudo usermod -a -G GROUPNAME USERNAME
```

**To remove a user from a group**

Removes a user from a specified group.
```sh
sudo deluser USER GROUPNAME
```

**su - switch user to become another user**

Switches to another user account.
```sh
su <user-name>
su john
```

**finger - displays all the information about user**

Displays information about all users logged in.
```sh
apt-get install finger
```

**Shows information of all the users logged in**

Displays information about all users logged in.
```sh
finger
```

**Gives information of a particular user**

Displays information about a specified user.
```sh
finger <user-name>
```

**to exit from a logged in shell**

Exits the current shell session.
```sh
exit
```

### Information About a Program
**which - locate a program or command in the system path**

Locates the path of a specified command.
```sh
which <command-name>
which vim
```

**Find binary / source / manual for command**

Finds the binary, source, and manual page for a specified command.
```sh
where <command-name>
whatis <command-name>
```

**man - manual for a command**

Displays the manual page for a specified command.
```sh
man <command-name>
man ls
```

**To navigate and search**

Navigates and searches within the manual page.
```sh
ctrl + f
ctrl + b
g
G
/string  -> search
h  -> to display help
q  -> for quit
```

**Search all man files for ifconfig**

Searches all manual pages for the term "ifconfig".
```sh
man -k ifconfig
```

**Search all man files for the string in quotes**

Searches all manual pages for the specified string.
```sh
man -k "copy files"
```

### Screen Shortcuts
**Start a screen session**

Starts a new screen session.
```sh
screen
```

**Resume a screen session**

Resumes a detached screen session.
```sh
screen -r
```

**Show your current screen sessions**

Lists all current screen sessions.
```sh
screen -list
```

**Activate commands for screen**

Activates screen commands.
```sh
CTRL-A
```

**Create a new instance of terminal**

Creates a new terminal instance within the screen session.
```sh
CTRL-A c
```

**Go to the next instance of terminal**

Switches to the next terminal instance within the screen session.
```sh
CTRL-A n
```

**Go to the previous instance of terminal**

Switches to the previous terminal instance within the screen session.
```sh
CTRL-A p
```

**Show current instances of terminals**

Lists all terminal instances within the screen session.
```sh
CTRL-A "
```

**Rename the current instance**

Renames the current terminal instance within the screen session.
```sh
CTRL-A A
```

### History and Command Execution
**Clears the screen**

Clears the terminal screen.
```sh
clear
```

**Resets the terminal display**

Resets the terminal display settings.
```sh
reset
```

**history - display a list of previously executed commands**

Displays a list of previously executed commands.
```sh
history
```

**Shows the stuff typed - add a number to limit the last n items**

Displays the last n commands executed.
```sh
history n
```

**Execute a specific command from history**

Executes a specific command from the history list.
```sh
!<history-number-of-command>
!102
```

**Add timestamp to history**

Adds a timestamp to each command in the history list.
```sh
HISTTIMEFORMAT="%Y-%m-%d %T "
# Add this variable to .bashrc/.zshrc to make it permanent
```

**Interactively search through previously typed commands**

Searches interactively through the command history.
```sh
ctrl + r
```

**To forward search (works in ZSH for me but not bash)**

Searches forward through the command history.
```sh
ctrl + s
```

**Execute the last command typed that starts with 'value'**

Executes the last command that starts with the specified value.
```sh
![value]
# Run last command starting with cd
!cd
```

**Print to the console the last command typed that starts with 'value'**

Prints the last command that starts with the specified value.
```sh
![value]:p
# Print last command starting with cd
!cd:p
```

**Execute previous command**

Executes the previous command.
```sh
!!
```

**Print to the console the last command typed**

Prints the previous command.
```sh
!!:p
```

**Execute previous command in sudo mode**

Executes the previous command with sudo.
```sh
sudo !!
```

**Last argument of previous command**

Uses the last argument of the previous command.
```sh
!$
```

**Last argument of previous command**

Uses the last argument of the previous command.
```sh
ALT-.
```

**All arguments of previous command**

Uses all arguments of the previous command.
```sh
!*
```

**Run previous command, replacing abc with 123**

Replaces a string in the previous command and executes it.
```sh
^abc^123
```

### Bash Variables
**Show environment variables**

Displays all environment variables.
```sh
env
```

**Output value of $NAME variable**

Displays the value of the specified variable.
```sh
echo $NAME
```

**Create a new variable**

Creates a new variable.
```sh
VARIABLE_NAME=value
```

**Remove a variable**

Removes a specified variable.
```sh
unset
```

**Set $NAME to value, to set value of an environment variable**

Sets the value of an environment variable.
```sh
export NAME=value
```

**Executable search path**

Displays the executable search path.
```sh
$PATH
```

**Home directory**

Displays the home directory.
```sh
$HOME 
~
```

**Current shell**

Displays the current shell.
```sh
$SHELL
```

**Remove a variable**

Removes a specified variable.
```sh
unset
```

### Command Execution
**Run command A and then B, regardless of success of A**

Runs command A and then command B, regardless of the success of command A.
```sh
[command-a]; [command-b]
```

**Run command B if A succeeded**

Runs command B if command A succeeded.
```sh
[command-a] && [command-b]
```

**Run command B if A failed**

Runs command B if command A failed.
```sh
[command-a] || [command-b]
```

**Run command A in background**

Runs command A in the background.
```sh
[command-a] &
```

**Run command A and then pass the result to command B**

Runs command A and then passes the result to command B.
```sh
[command-a] | [command-b]
```

**stderr of cmd1 to cmd2**

Redirects stderr of command A to command B.
```sh
[command-a] |& [command-b]
```

**Run cmd in a subshell**

Runs a command in a subshell.
```sh
cmd &
```

### Help and Information
**Offers help**

Displays help for a specified command.
```sh
[command] -h
```

**Offers help**

Displays help for a specified command.
```sh
[command] --help
```

**Offers help**

Displays help for a specified command.
```sh
info [command]
```

**Show the help manual for [command]**

Displays the manual page for a specified command.
```sh
man [command]
```

**Gives a one-line description of [command]**

Displays a one-line description of a specified command.
```sh
whatis [command]
```

**Searches for command with keywords in description**

Searches for commands with keywords in their descriptions.
```sh
apropos [search-pattern]
```

**Open line in the editor to write a command**

Opens a line in the editor to write a command.
```sh
ctrl + x then ctrl + e
```

**Matrix style animation in command line**

Displays a matrix-style animation in the command line.
```sh
cmatrix
```

**Zoom in to the command prompt**

Zooms in to the command prompt.
```sh
ctrl +
```

**Zoom out in the command prompt**

Zooms out in the command prompt.
```sh
ctrl -
```

### File and Directory Management
**ls - list the files and directories in the current directory**

Lists the files and directories in the current directory.
```sh
ls
```

**In a list format, Long listing format**

Lists files and directories in a long listing format.
```sh
ls -l
ls -l <file-name>
```

**Long listing of parent directory**

Lists files and directories in the parent directory in a long listing format.
```sh
ls -l ..
```

**-a means files in the current directory including hidden files**

Lists all files, including hidden files, in the current directory.
```sh
ls -a
```

**All files in list format**

Lists all files in the current directory in a list format.
```sh
ls -al
```

**Long listing with Human readable file sizes**

Lists files and directories in a long listing format with human-readable file sizes.
```sh
ls -lh
```

**Entire content of folder recursively**

Lists the entire content of a folder recursively.
```sh
ls -R
```

**Entire content of folder recursively in reverse order**

Lists the entire content of a folder recursively in reverse order.
```sh
ls -r
```

**Sort by last modified**

Sorts files and directories by last modified date.
```sh
ls -t
```

**Sort by file size**

Sorts files and directories by file size.
```sh
ls -S
```

**One file per line**

Lists one file per line.
```sh
ls -1
```

**Comma separated output**

Lists files and directories in a comma-separated format.
```sh
ls -m
```

**Quoted output**

Lists files and directories with quoted output.
```sh
ls -Q
```

**List files in /etc**

Lists files in the /etc directory.
```sh
ls /etc
# List files in the /var directory
ls -a /var/
```

**tee - redirect output to both a file and the console**

Redirects output to both a file and the console.
```sh
ls | tee file.txt
```

### Traverse Directory
**pwd - print the current working directory**

Prints the current working directory.
```sh
pwd
```

**cd - change the current directory**

Changes the current directory.

**Go to Home directory**
```sh
cd
```

**Change directory e.g. cd Documents**

Changes to the specified directory.
```sh
cd [folder]
cd /usr/bin
cd /<click-tab>
```

**Go to Home directory**
```sh
cd ~
```

**Go to the root of drive**
```sh
cd /
```

**Go to the previous directory**
```sh
cd -
```

**Move 1 levels up**
```sh
cd ..
```

**Push and pop directories**

Pushes and pops directories from the directory stack.
```sh
pushd <dir-name>
popd <dir-name>
```

**Root directory marker(#) and user directory marker(/)**

**. represent Current folder, e.g. ls .**

Represents the current folder.
**.. represent Parent/enclosing directory, e.g. ls ..**

Represents the parent/enclosing directory.

### File Operations
**Opens a file (as if you double clicked it)**

Opens a file as if you double-clicked it.
```sh
open .
xdg-open
```

**Opens the file using the nano editor**

Opens a file using the nano editor.
```sh
nano [file]
```

**Opens the file using the vim editor**

Opens a file using the vim editor.
```sh
vim [file]
```

**touch - create a new empty file or update the timestamp of an existing file**

Creates a new empty file or updates the timestamp of an existing file.
```sh
touch <file-name>
touch shayan.txt
```

**Multiple files at one time**

Creates multiple files at one time.
```sh
touch <file-name-1> <file-name-2>
```

**Create 10 files in a single go**

Creates 10 files in a single go.
```sh
touch <file-name>{0..10}
```

**Do not update anything just change the modified timestamp**

Changes the modified timestamp of an existing file without updating its content.
```sh
touch <already-existed-file>
```

**echo - display text or variables to the console**

Displays text or variables to the console.
```sh
echo "hello world"
```

**Single arrow (>) will override the content**

Overrides the content of a file.
```sh
echo "hello world" > test.txt
```

**Double arrow (>>) will append the content**

Appends content to a file.
```sh
echo "hello world" >> test.txt
```

**Truncate a file**

Truncates a file to zero size.
```sh
truncate -s 0 <file-name>
```

**rm - remove files or directories**

Removes files or directories.
```sh
rm <file-name>
```

**-v for verbose**

Removes files or directories with verbose output.
```sh
rm -v <file-name>
rm <file-name-1> <file-name-2>
rm example.txt
```

**-r for recursive, delete directly and all its contents**

Removes directories and their contents recursively.
```sh
rm -r <non-empty-dir>
```

**-i for interactive, Remove with confirmation**

Removes files or directories with confirmation.
```sh
rm -ri <non-empty-dir>
```

**Force removal without confirmation**

Forces removal of files or directories without confirmation.
```sh
rm -f [file]
```

**This command will delete everything in the system**

Deletes everything in the system (use with caution).
```sh
rm -rf /
```

**mkdir - create a new directory**

Creates a new directory.
```sh
mkdir <dir-name>
```

**Create a new directory called test**

Creates a new directory called test.
```sh
mkdir test
```

**-p will create all the nested folders if that is not present already**

Creates nested directories if they do not already exist.
```sh
mkdir -p /dir1/dir2/dir3
```

**Make directory and subdirectory in a single command**

Creates a directory and subdirectory in a single command.
```sh
mkdir -p test2/test2
```

**Make multiple directories**

Creates multiple directories.
```sh
mkdir test2 test3 
```

**rmdir - Remove directory (only operates on empty directories)**

Removes an empty directory.
```sh
rmdir <dir-name>
```

**Deletes the text.txt file in the directory called test**

Deletes a file in a specified directory.
```sh
rmr test/text.txt
```

**cp - copy files or directories**

Copies files or directories.
```sh
cp [file] [dir]
cp <file-name> <file-name-with-path>
```

**Copies text.txt to a new file called text2.txt**

Copies a file to a new file.
```sh
cp [file] [newfile]
cp text.txt text2.txt
```

**Copy dir-1 content to dir-1-copy folder, -r is needed as folder is not empty**

Copies the content of a directory to another directory.
```sh
cp -r <dir-1> <dir-1-copy>
```

**mv - move or rename files or directories**

Moves or renames files or directories.
```sh
mv <file-name> <file-name-with-path>
```

**Renames the file to a new filename**

Renames a file to a new filename.
```sh
mv [file] [new-filename]
mv example.txt backup/
```

**Moves text.txt to a different directory**

Moves a file to a different directory.
```sh
mv text.txt test/
```

**Moves all txt files to a different directory**

Moves all files with a .txt extension to a different directory.
```sh
mv *.txt test/
```

**List all files and subfolders and files within subfolders within the test directory**

Lists all files and subfolders within a specified directory.
```sh
tree /etc
```

**Divides the file into x columns**

Divides the content of a file into x columns.
```sh
pr -x
```

**Assigns a header to the file**

Assigns a header to the content of a file.
```sh
pr -h
```

**Denotes the file with Line Numbers**

Adds line numbers to the content of a file.
```sh
pr -n
```

**Prints "c" copies of the File**

Prints multiple copies of a file.
```sh
lp -nc , lpr c
```

**Specifies name of the printer**

Specifies the name of the printer.
```sh
lp-d lp-P
```

### File Content Operations
**cat - concatenate and display files**

Concatenates and displays files.
```sh
cat <file-name>
cat <file-name> | sort
cat example.txt
cat <file-1> <file-2> <file-3>
```

**Creates a new file**

Creates a new file.
```sh
cat > filename
```

**Joins two files (file1, file2) and stores the output in a new file (file3)**

Joins two files and stores the output in a new file.
```sh
cat file1 file2 > file3
```

**Concatenate multiple files**

Concatenates multiple files.
```sh
cat <file-1> <file-2> <file-3> > <file-name>
```

**Copies file contents to clipboard**

Copies file contents to the clipboard.
```sh
pbcopy < [file]
```

**Paste clipboard contents**

Pastes clipboard contents.
```sh
pbpaste
```

**Paste clipboard contents into file**

Pastes clipboard contents into a file.
```sh
pbpaste > [file]
```

**sort - sort lines of text in a file or input**

Sorts lines of text in a file or input.
```sh
cat file.txt
# banana
# orange
# apple
sort file.txt
# apple
# banana
# orange
```

**Sort numeric values**

Sorts numeric values.
```sh
sort -n numeric-files
```

**uniq - remove duplicate lines from a file or input**

Removes duplicate lines from a file or input.
```sh
cat file.txt
# apple
# orange
# banana
# apple
# banana
uniq file.txt
# apple
# orange
# banana
```

**Output file content delivered in screensize chunks**

Outputs file content in screensize chunks.
```sh
less <file-name>
```

**Get type of file**

Gets the type of a file.
```sh
file <file-1>
```

**head/tail - display the first/last few lines of a file or input**

Displays the first few lines of a file or input.
```sh
head <file-name>
head -f <file-name>
head file.txt
```

**Displays the first 10 lines of the file**

Displays the first 10 lines of a file.
```sh
head cloud-init.log
```

**Displays the first 5 lines of the file**

Displays the first 5 lines of a file.
```sh
head -n 5 cloud-init.log
```

**Show distribution**

Displays the distribution information.
```sh
head -n1 /etc/issue
```

**Display last 10 lines**

Displays the last 10 lines of a file.
```sh
tail <file-name>
```

**Output last lines of file as it changes, follow the file**

Outputs the last lines of a file as it changes.
```sh
tail -f <file-name>
```

**Compare two files**

Compares two files.
```sh
cmp <file-name-1> <file-name-2>
```

**Compares the two text files**

Compares two text files.
```sh
diff <file-name-1> <file-name-2>
```

### IO Redirection
**Tell command to read content from a file**

Tells a command to read content from a file.
```sh
[command] < [file]
```

**Output of cmd2 as file input to cmd1**

Uses the output of one command as the input to another command.
```sh
cmd1 <(cmd2)
```

**Push output to file, keep in mind it will get overwritten**

Pushes the output of a command to a file, overwriting the file.
```sh
[command] > [file]
```

**Append output to existing file**

Appends the output of a command to an existing file.
```sh
[command] >> [file]
```

**Discard stdout of cmd**

Discards the stdout of a command.
```sh
cmd > /dev/null
```

**Error output (stderr) of cmd to file**

Redirects the stderr of a command to a file.
```sh
cmd 2> file
```

**stdout to same place as stderr**

Redirects the stdout of a command to the same place as stderr.
```sh
cmd 1>&2
```

**stderr to same place as stdout**

Redirects the stderr of a command to the same place as stdout.
```sh
cmd 2>&1
```

**Every output of cmd to file**

Redirects all output of a command to a file.
```sh
cmd &> file
```

### Find and Locate
**Find the files in a directory**

Finds files in a directory.
```sh
find <dir-name> -name <name-of-file>
find /Users -name "file.txt"
find <other-parameters>
```

**Find files starting with name in dir**

Finds files starting with a specified name in a directory.
```sh
find /dir/ -name name*
```

**Find files owned by name in dir**

Finds files owned by a specified user in a directory.
```sh
find /dir/ -user name
```

**Searches within /var and subdirectories**

Searches for files within a specified directory and its subdirectories.
```sh
find /var -name *.log
```

**Find files modified less than num minutes ago in dir**

Finds files modified less than a specified number of minutes ago in a directory.
```sh
find /dir/ -mmin num
```

**locate - locate any file on the system**

Locates any file on the system.
```sh
locate file.txt
```

**Displays directory containing cloud-init.log**

Displays the directory containing a specified file.
```sh
locate cloud-init.log
```

**Displays directory containing cloud-init.log and ignores case**

Displays the directory containing a specified file, ignoring case.
```sh
locate -I cloud-init.log
```

### Search and Grep
**Search for all lines that contain the pattern**

Searches for all lines that contain a specified pattern.
```sh
grep [search_pattern] [files]
grep "Tom" file.txt
```

**Search for all lines that contain the case-insensitive pattern**

Searches for all lines that contain a specified pattern, ignoring case.
```sh
grep -i [search_pattern] [file]
```

**Recursively search in all files in specified directory for all lines that contain the pattern**

Recursively searches for all lines that contain a specified pattern in a directory.
```sh
grep -r [search_pattern] [dir]
```

**Search for all lines that do NOT contain the pattern**

Searches for all lines that do not contain a specified pattern.
```sh
grep -v [search_pattern] [file]
```

**Show matched part of file only**

Shows only the matched part of a file.
```sh
grep -o [search_pattern] [file]
```

**Spotlight search for files (names, content, other metadata)**

Performs a spotlight search for files based on names, content, and other metadata.
```sh
mdfind [search_pattern]
mdfind skateboard
```

**Spotlight search for files named like pattern in the given directory**

Performs a spotlight search for files named like a specified pattern in a directory.
```sh
mdfind -onlyin [dir] -name [pattern]
```

### File Permissions
**chmod - change the permissions of a file or directory**

Changes the permissions of a file or directory.
```sh
chmod <file-name> <file-mod>
chmod +x <file-name>
chmod 700 file.txt
```

**Change mode of file to 775**

Changes the mode of a file to 775.
```sh
chmod 775 file
```

**Recursively chmod folder to 600**

Recursively changes the mode of a folder to 600.
```sh
chmod -R 600 folder
```

**chown - change the owner of a file or directory**

Changes the owner of a file or directory.
```sh
chown <user-name> <file-name>
```

**Change file owner to user and group to group**

Changes the owner and group of a file.
```sh
chown user:group file
```

**Change the user as well as group for a file or directory**

Changes the owner and group of a file or directory.
```sh
chown user:group filename
```

```sh
chown new_owner example.txt
```

### Network Commands
**Print or set system name**

Prints or sets the system name.
```sh
hostname
```

**ifconfig - display or configure network interfaces**

Displays or configures network interfaces.
```sh
ifconfig
```

```sh
ip address
ip address | grep eth0
ip address | grep eth0 | grep inet
ip address | grep eth0 | grep inet | awk '{print $2}'
```

**ssh - connect to a remote server securely**

Connects to a remote server securely.
```sh
ssh username@ip-address
```

**scp - securely copy files between systems**

Securely copies files between systems.
```sh
scp myfile.txt user@remotehost:/home/user/
```

**Display files in the current directory of a remote computer**

Displays files in the current directory of a remote computer.
```sh
dir
```

**Change directory to "dirname" on a remote computer**

Changes the directory to a specified directory on a remote computer.
```sh
cd "dirname"
```

**Upload 'file' from local to remote computer**

Uploads a file from the local computer to a remote computer.
```sh
put file
```

**Download 'file' from remote to local computer**

Downloads a file from a remote computer to the local computer.
```sh
get file
```

**Logout**

Logs out from the remote computer.
```sh
quit
```

### Networking Commands
**For dns**

Displays DNS information.
```sh
cat /etc/resolv.conf
resolvectl status
```

**ping - test network connectivity**

Tests network connectivity.
```sh
ping <ip-address>
ping 8.8.8.8
```

**Test the destination at 8.8.8.8 by sending five ICMP packets**

Tests network connectivity by sending a specified number of ICMP packets.
```sh
ping -c 5 8.8.8.8
```

**Print the route packets take to network host**

Prints the route packets take to a network host.
```sh
traceroute <url>
```

**netstat - display network connection information**

Displays network connection information.
```sh
netstat
netstat -tulpn
```

**Display the route table**

Displays the route table.
```sh
netstat -r
```

**Display open connections for a specific port**

Displays open connections for a specific port.
```sh
netstat -np | grep "80"
```

```sh
ss 
ss -tulpn
```

**route - view or configure network routing tables**

Views or configures network routing tables.
```sh
route [options] [add/delete/show]
```

**Allow port 80 to the system**

Allows port 80 to the system.
```sh
sudo ufw allow 80
sudo ufw enable
sudo ufw status
```

```sh
wget <downloadable-url>
```

```sh
curl <url>
curl <downloadable-url> > <file-name>
```

### System Information
**uname - display system information**

Displays system information.
```sh
uname
uname -r
```

**Show system and kernel**

Displays system and kernel information.
```sh
uname -a
```

**Gives free RAM on your system**

Displays free RAM on the system.
```sh
free
```

### Disk Usage
**df - display disk space usage**

Displays disk space usage.
```sh
df
df -H
```

**du - display disk usage by file or directory**

Displays disk usage by file or directory.
```sh
du
```

**Display file or file system status**

Displays file or file system status.
```sh
stat
```

**mount - mount a file system**

Mounts a file system.
```sh
mount
mount | column -t
sudo mount /dev/sdb1 /mnt/usb
```

**umount - unmount a file system**

Unmounts a file system.
```sh
sudo umount /mnt/usb
```

### Process Commands
**ps - display information about running processes**

Displays information about running processes.
```sh
ps
ps aux
```

**Gives the status of a particular process**

Displays the status of a particular process.
```sh
ps PID
```

**To send a process to the background**

Sends a process to the background.
```sh
bg
```

**To run a stopped process in the foreground**

Runs a stopped process in the foreground.
```sh
fg
```

**Display current jobs**

Displays current jobs.
```sh
jobs
```

**Run a command immune to hangups**

Runs a command immune to hangups.
```sh
nohup
```

**Gives the Process ID (PID) of a process**

Displays the Process ID (PID) of a process.
```sh
pidof
```

**Starts a process with a given priority**

Starts a process with a given priority.
```sh
nice
```

**Changes priority of an already running process**

Changes the priority of an already running process.
```sh
renice
```

**top - display system resource usage and processes**

Displays system resource usage and processes.
```sh
top
```

**htop - an interactive process viewer and system monitor**

Displays an interactive process viewer and system monitor.
```sh
htop
```

**kill - terminate a process**

Terminates a process.
```sh
kill [PID]
```

**kill can take different flags, -9 is for SIGKILL, -15 is for SIGTERM**

Terminates a process with a specified signal.
```sh
kill -9 <process-id>
kill -15 <process-id>
```

**-l to list all the flags**

Lists all the flags for the kill command.
```sh
kill -l
```

**Kill process with name name**

Terminates a process with a specified name.
```sh
pkill <process-name>
```

**Kill process with name name forcefully**

Terminates a process with a specified name forcefully.
```sh
pkill -9 <process-name>
```