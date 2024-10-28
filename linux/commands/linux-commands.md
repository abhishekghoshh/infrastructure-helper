# linux most used commands cheetsheet


```
apt-get update & apt-get upgrade -y
```


#### User management commands of linux
```
# sudo - execute a command as another user or with elevated privileges
# Run command with the security privileges of the superuser (Super User DO)
# Execute a command as another user, typically the superuser.
sudo

# whoami - display the current user name
whoami

# Display who is logged in
who 

# Show the user you are logged in as and the groups you are part of
id

# Show the groups you are part of
groups

# useradd - add a new user to the system, Create a new user account
sudo useradd <user-name>
sudo adduser <user-name> <other-parameters>
sudo useradd harry

# passwd - change the password for a user
sudo passwd <user-name>

# To change the password of a user
sudo passwd -l <user-name>

# To remove a newly created user
sudo userdel -r <user-name>

# userdel - delete a user from the system
sudo userdel harry

# To add a user to a group, Modify user account properties
sudo usermod -a -G GROUPNAME USERNAME

# To remove a user from a group
sudo deluser USER GROUPNAME

# su - switch user to become another user, 
# Substitute user identity to become superuser or another user.
su <user-name>
su john


# finger - displays all the information about user
apt-get install finger

# Shows information of all the users logged in
finger

# Gives information of a particular user
finger <user-name>

# to exit from a logged in shell
exit
```

#### Information about a program
```
# which - locate a program or command in the system path
which <command-name>
which vim

where <command-name>
whatis <command-name>

# Find binary / source / manual for command
whereis <command-name>


```

```
# man - manual for a command
# the synopsis section under man output gives the syntax of the command
man <command-name>
man ls
# To navigate and search 
ctrl + f
ctrl + b
g
G
/string  -> search
h  -> to display help
q  -> for quit

# Search all man files for ifconfig
man -k ifconfig

# Search all man files for the sting in quotes
man -k "copy files"
```


#### Screen shortcut
```
# Start a screen session.
screen

# Resume a screen session.
screen -r

# Show your current screen sessions.
screen -list

# Activate commands for screen.
CTRL-A

# Create a new instance of terminal.
CTRL-A c

# Go to the next instance of terminal.
CTRL-A n

# Go to the previous instance of terminal.
CTRL-A p

# Show current instances of terminals.
CTRL-A "

# Rename the current instance.
CTRL-A A
```



```
# Clears the screen
clear

# Resets the terminal display
reset

# history - display a list of previously executed commands,
history

# Shows the stuff typed - add a number to limit the last n items
history n

!<history-number-of-command>
!102

HISTTIMEFORMAT="%Y-%m-%d %T "
add this variable to .bashrc/.zshrc to make it permenant


# Interactively search through previously typed commands
ctrl + r

# to forward search (works in ZSH for me but not bash)
ctrl + s

# Execute the last command typed that starts with 'value'
![value]
# Run last command starting with cd
!cd

# Print to the console the last command typed that starts with 'value'
![value]:p
Print last command starting with cd
!cd:p

# execute previous command
!!

# Print to the console the last command typed
!!:p

# execute previous command in sudo mode
sudo !!


# Last argument of previous command
!$

# Last argument of previous command
ALT-.

# All arguments of previous command
!*

# Run previous command, replacing abc with 123
^abc^123



# Bash Variables

# Show environment variables
env

# Output value of $NAME variable
echo $NAME

# Create a new variable
VARIABLE_NAME= value

# Remove a variable
unset

# Set $NAME to value, to set value of an environment variable
export NAME=value

# Executable search path
$PATH

# Home directory
$HOME 
~

# Current shell
$SHELL

# Remove a variable
unset



# Run command A and then B, regardless of success of A
[command-a]; [command-b]

# Run command B if A succeeded
[command-a] && [command-b]

# Run command B if A failed
[command-a] || [command-b]

# Run command A in background, & is to run the command in background
[command-a] &

# Run command A and then pass the result to command B e.g ps auxwww | grep google
[command-a] | [command-b]

# stderr of cmd1 to cmd2
[command-a] |& [command-b]

# Run cmd in a subshell
cmd &



# Offers help
[command] -h

# Offers help
[command] --help

# Offers help
info [command]

# Show the help manual for [command]
man [command]

# Gives a one-line description of [command]
whatis [command]

# Searches for command with keywords in description
apropos [search-pattern]


# open line in the editor to write a command
ctrl + x then ctrl + e



# matrix style animation in command line
cmatrix

# zoom in to the command prompt
ctrl +
# zoom out in the command prompt
ctrl -

```


```

# ls - list the files and directories in the current directory
ls

# in a list format, Long listing format
ls -l
ls -l <file-name>

# Long listing of parent directory
ls -l ..

# -a means files in the current directory including hidden files
ls -a

# all files in list format
ls -al

# Long listing with Human readable file sizes
ls -lh

# Entire content of folder recursively
ls -R

# Entire content of folder recursively in reverse order
ls -r

# Sort by last modified
ls -t

# sort by file size
ls -S

# One file per line
ls -1

# comma separated output
ls -m

# Quoted output
ls -Q

# list files in /etc
ls /etc
# List files in the /var directory
ls -a /var/



# tee - redirect output to both a file and the console
ls | tee file.txt

```

#### Traverse directory
```
# pwd - print the current working directory
pwd

# cd - change the current directory

# go to Home directory
cd

# Change directory e.g. cd Documents
cd [folder]
cd /usr/bin
cd /<click-tab>

# go to Home directory
cd ~

# go to the root of drive
cd /

# go to the previous directory
cd -

# Move 1 levels up
cd ..




pushd <dir-name>
popd <dir-name>


# root directory marker(#) and user directory marker(/)

# . respresent Current folder, e.g. ls .
# .. resposent Parent/enclosing directory, e.g. ls ..

```

```
# Opens a file ( as if you double clicked it )
open .
xdg-open

# Opens the file using the nano editor
nano [file]

# Opens the file using the vim editor
vim [file]


# touch - create a new empty file or update the timestamp of an existing file
touch <file-name>
touch shayan.txt

# multiple files at one time
touch <file-name-1> <file-name-2>

# create 10 files in a single go
touch <file-name>{0..10}

# do not update anything just change the modified timestamp
touch <already-existed-file>





# echo - display text or variables to the console
echo "hello world"

# single arrow (>) will override the content
echo "hello world" > test.txt

# double arrow (>>) will append the content
echo "hello world" >> test.txt




truncate -s 0 <file-name>

# rm - remove files or directories
rm <file-name>

# -v for verbose
rm -v <file-name>
rm <file-name-1> <file-name-2>
rm example.txt

# -r for recusrive, delete directly and all its contents, Remove a directory and contents
rm -r <non-empty-dir>

# -i for interactive, Remove with confirmation
rm -ri <non-empty-dir>

# Force removal without confirmation
rm -f [file]

# this command will delete everything in the system
rm -rf /


# mkdir - create a new directory
mkdir <dir-name>

# Create a new directory called test
mkdir test

# -p will create all the nested folders if that is not present already, 
mkdir -p /dir1/dir2/dir3

# Make directory and subdirectory in a single command
mkdir -p test2/test2

#  Make multiple directories
mkdir test2 test3 




# rmdir - Remove directory ( only operates on empty directories )
rmdir <dir-name>

# Deletes the text.txt file in the directory called test
rmr test/text.txt


# cp - copy files or directories, Copy file to directory
cp [file] [dir]
cp <file-name> <file-name-with-path>

# Copies text.txt to a new file called text2.txt, Overwrites the existing text2.txt with a copy of text.txt
cp [file] [newfile]
cp text.txt text2.txt

# copy dir-1 content to dir-1-copy folder, -r is needed as folder is not empty
cp -r <dir-1> <dir-1-copy>


# mv - move or rename files or directories, Move/Rename, e.g. mv file1.ad /tmp
mv <file-name> <file-name-with-path>

# Renames the file to a new filename
mv [file] [new-filename]
mv example.txt backup/

# Moves text.txt to a different directory
mv text.txt test/

# Moves all txt files to a different directory
mv *.txt test/



# List all files and subfolders and files within subfolders within the test directory
tree /etc



# Divides the file into x columns
pr -x

# Assigns a header to the file
pr -h

# Denotes the file with Line Numbers
pr -n

# Prints "c" copies of the File
lp -nc , lpr c

# Specifies name of the printer
lp-d lp-P
```

```
# cat - concatenate and display files, Concatenate to screen
cat <file-name>
cat <file-name> | sort
cat example.txt
cat <file-1> <file-2> <file-3>

# Creates a new file
cat > filename

# Joins two files (file1, file2) and stores the output in a new file (file3)
cat file1 file2 > file3

cat <file-1> <file-2> <file-3> > <file-name>


# Copies file contents to clipboard
pbcopy < [file]

# Paste clipboard contents
pbpaste

# Paste clipboard contents into file, pbpaste > paste-test.txt
pbpaste > [file]


# sort - sort lines of text in a file or input
cat file.txt
# banana
# orange
# apple
sort file.txt
# apple
# banana
# orange

sort -n numeric-files # -n for numberic values


# uniq - remove duplicate lines from a file or input
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


# Output file content delivered in screensize chunks
less <file-name>

# Get type of file1
file <file-1>


# head/tail - display the first/last few lines of a file or input

# display first 10 lines
head <file-name>
head -f <file-name>
head file.txt

# Displays the first 10 lines of the file
head cloud-init.log

# Displays the first 5 lines of the file
head -n 5 cloud-init.log

# Show distribution
head -n1 /etc/issue


# display last 10 lines
tail <file-name>

# Output last lines of file1 as it changes, follow the file
tail -f <file-name>


cmp <file-name-1> <file-name-2>

# Compares the two text files
diff <file-name-1> <file-name-2>



```


#### IO Redirection
```
# Tell command to read content from a file, Input of cmd from file
[command] < [file]

# Output of cmd2 as file input to cmd1
cmd1 <(cmd2)

# Push output to file, keep in mind it will get overwritten, Standard output (stdout) of cmd to file
[command] > [file]

# Append output to existing file, Append stdout to file
[command] >> [file]

# Discard stdout of cmd
cmd > /dev/null

# Error output (stderr) of cmd to file
cmd 2> file

# stdout to same place as stderr
cmd 1>&2

# stderr to same place as stdout
cmd 2>&1

# Every output of cmd to file
cmd &> file
```


```
# find the files in a directory
find <dir-name> -name <name-of-file>
find /Users -name "file.txt"
find <other-parameters>

# Find files starting with name in dir
find /dir/ -name name*

# Find files owned by name in dir
find /dir/ -user name

# Searches within /var and subdirectories
find /var -name *.log

# Find files modifed less than num minutes ago in dir
find /dir/ -mmin num

# locate - locate any file on the system, Find file (quick search of system index)
locate file.txt

# Displays directory containing cloud-init.log
locate cloud-init.log

# Displays directory containing cloud-init.log and ignores cas
locate -I cloud-init.log







# Search for all lines that contain the pattern,
grep [search_pattern] [files]
grep "Tom" file.txt

# Search for all lines that contain the case-insensitive pattern
grep -i [search_pattern] [file]

# Recursively search in all files in specified directory for all lines that contain the pattern
grep -r [search_pattern] [dir]

# Search for all lines that do NOT contain the pattern, Inverted search
grep -v [search_pattern] [file]

# Search for all lines that do NOT contain the pattern
grep -v [search_pattern] [file]

# Show matched part of file only
grep -o [search_pattern] [file]







# Spotlight search for files (names, content, other metadata),
mdfind [search_pattern]
mdfind skateboard

# Spotlight search for files named like pattern in the given directory
mdfind -onlyin [dir] -name [pattern]
```


#### file permissions
```
# The first digit represents the owner of the file/directory
# The second digit represents the group that the file/directory belongs to
# The third digit represents all other users
# 0 (no permission)
# 1 (execute only)
# 2 (write only)
# 3 (write and execute)
# 4 (read only)
# 5 (read and execute)
# 6 (read and write)
# 7 (read, write, and execute)

# r for read permission
# w for write permission
# x for execute permission
# -= for no permission

# chmod - change the permissions of a file or directory
chmod <file-name> <file-mod>
chmod +x <file-name>
chmod 700 file.txt

# Change mode of file to 775
chmod 775 file

# Recursively chmod folder to 600
chmod -R 600 folder



# chown - change the owner of a file or directory
chown <user-name> <file-name>

# Change file owner to user and group to group
chown user:group file

# change the user as well as group for a file or directory
chown user:group filename

chown new_owner example.txt
```


```
# Print or set system name.
hostname

# ifconfig - display or configure network interfaces, Display all network interfaces
ifconfig

ip address
ip address | grep eth0
ip address | grep eth0 | grep inet
ip address | grep eth0 | grep inet | awk '{print $2}
```

```
# ssh - connect to a remote server securely, Secure Shell client for remote login.
ssh username@ip-address

# scp - securely copy files between systems
scp myfile.txt user@remotehost:/home/user/

# Display files in the current directory of a remote computer
dir

# change directory to "dirname" on a remote computer
cd "dirname"

# upload 'file' from local to remote computer
put file

# Download 'file' from remote to local computer
get file

# Logout
quit
```



Networking command
```
# for dns
cat /etc/resolv.conf
resolvectl status


# ping - test network connectivity, Test the destination at 8.8.8.8 by sending ICMP packets
ping <ip-address>
ping 8.8.8.8

# Test the destination at 8.8.8.8 by sending five ICMP packets
ping -c 5 8.8.8.8


# Print the route packets take to network host.
traceroute <url>


# netstat - display network connection information
# Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
netstat
netstat -tulpn

#  Display the route table
netstat -r

# isplay open connections for a specific port
netstat -np | grep "80"

ss 
ss -tulpn


# route - view or configure network routing tables
# Show or manipulate the IP routing table.
route [options] [add/delete/show]


# allow port 80 to the system
sudo ufw allow 80
sudo ufw enable
sudo ufw status


wget <downloadable-url>

curl <url>
curl <downloadable-url> > <file-name>
```

```
# uname - display system information
uname
uname -r

# Show system and kernel
uname -a
```


```
# Gives free RAM on your system
free
```

```
# df - display disk space usage, free space on storage devices
df
df -H

# du - display disk usage by file or directory
du

# Display file or file system status
stat

# mount - mount a file system
# Show mounted filesystems
mount
mount | column -t
sudo mount /dev/sdb1 /mnt/usb

# umount - unmount a file system
sudo umount /mnt/usb
```

#### Process command
```
# ps - display information about running processes
# Show snapshot of processes
ps
ps aux

# Gives the status of a particular process
ps PID

# To send a process to the background
bg

# To run a stopped process in the foreground
fg

# Display current jobs
jobs

# Run a command immune to hangups.
nohup

# Gives the Process ID (PID) of a process
pidof


# Starts a process with a given priority
nice

# Changes priority of an already running process
renice


# top - display system resource usage and processes, Displays active processes. Press q to quit
# Show real time processes
top

# htop - an interactive process viewer and system monitor in a human readable format
htop

# kill - terminate a process
kill [PID]

# kill can take different flags, -9 is for SIGKILL, -15 is for SIGTERM
# -9 for forcefull termination, -15 is for gracefull shutdown
kill -9 <process-id>
kill -15 <process-id>

# -l to list all the flags
kill -l

# Kill process with name name
pkill <process-name>

# Kill process with name name with forcefully
pkill -f <process-name>

# Kill all processes with names beginning name
killall
```


```
# tar create or extract compressed archive files
# x: extract files from an archive
# t: list the contents of an archive
# r: append files to an existing archive
# z: use gzip compression
# j: use bzip2 compression
# cf: create file
# xf: extract file
tar cf archive.tar file1 file2 file3

zip <zip-file-name> <content-file-or-folder>
unzip <zip-file-name>


# gzip - compress files
gzip file.txt

# gunzip - decompress compressed files
gunzip file.txt.gz
```

```
# systemctl - control system services and settings

# Start the nginx service
sudo systemctl start <service-name>

# Check the status of the nginx service
sudo systemctl status <service-name>

# Stop the nginx service
sudo systemctl stop <service-name>


systemctl start nginx
systemctl status nginx
systemctl stop nginx


# service - control system serv
service apache2 start
```

```
# uptime - display system uptime and load average
uptime

sudo reboot
sudo shutdown -h now


# date - display or set the system date and time
date
```


```

neofetch
```

```
# edit the ~/.bash_prompt to create custom prompt in command line
# find the sample prompt here https://www.learnlinux.tv/10-linux-terminal-tips-and-tricks-to-enhance-your-workflow/
# add that into .bashrc/.zshrc and comment out the PS1 command 
# add the source ~/.bash_prompt
```



```
# Sed command is mostly used to replace the text in a file
sed <pattern-or-text> <file-name>

echo 'Hello, world!' | sed 's/world/universe'   => Hello, universe!


# search in a text or file
# Displays any lines of the file ssh_config that include the term user
grep user /etc/ssh/ssh_config

# Use quotes if the string has spaces, -i option: Ignore upper/lower case
grep -i "COMMAND LINE" /etc/ssh/ssh_config

# Search all files in the etc directory
grep -R 127.0.0.1 /etc/

# Sends search results to a text file
grep user /etc/ssh/ssh_config > sample.txt
ls | grep crontab



# run in every 2 second
watch <command-name>

awk

sed

rsync
```


ln: Create links between files.
wc: Count words, lines, and characters in a file
pstree: Display a tree of processes.
hostname: Print or set system name.

screen: Terminal multiplexer with detach and reattach capabilities.
tmux: Terminal multiplexer similar to screen.

#### Text Editing and Manipulation:
nano: Basic text editor.
vim: Advanced text editor.
emacs: Another powerful text editor.
sed: Stream editor for filtering and transforming text.
awk: Pattern scanning and text processing language.
cut: Extract sections from each line of files.
paste: Merge lines of files.
sort: Sort lines of text files.
uniq: Report or filter out repeated lines in a file.
tr: Translate or delete characters.
tee: Read from standard input and write to standard output and files simultaneously.


#### File Transfer and Networking:
scp: Securely copy files between hosts.
rsync: Remote file synchronization utility.
wget: Retrieve files from the web using HTTP, HTTPS, and FTP.
curl: Transfer data with URLs.
ssh-keygen: Generate SSH keys for secure authentication.
ssh-copy-id: Copy SSH keys to a remote server's authorized_keys file.



#### Miscellaneous:
history: Display command history.
alias: Create command aliases.
watch: Execute a program periodically, showing output fullscreen.
man: Display the manual pages for commands.