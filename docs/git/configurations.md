## Git configurations

### Check if installation is successful on any platform
```
git --version
```

### Ignoring files

**Create a .gitignore file and commit it.**  
Show all commit logs with indication of any paths that moved.  
To ignore files, create a `.gitignore` file in your repository with a line for each pattern.  
File ignoring will work for the current and subdirectories where `.gitignore` file is placed. In this example, all files are ignored in the `logs` directory (excluding the `.gitkeep` file), whole `tmp` directory, and all files `*.swp`.  

```
logs/
*.notes
pattern*/
/logs *
!logs/.gitkeep
/tmp
*.swp
EOF
```

### Commands for viewing and modifying git configurations

**System-wide ignore pattern for all local repositories**
```
git config --global core.excludesfile [file]
```

**How to check your Git configuration:**  
The command below returns a list of information about your git configuration, including username and email:  
```
git config -l / git config --list
```

**Get the value of a single key**
```
git config --get <key>
```

**Configure your email**
```
git config user.email [your.email@domain.com]
```

**Configure your name**
```
git config user.name [your-name]
```

**How to set up your Git username:**  
With the command below, you can configure your username:  
```
git config --global user.name "Abhishek Ghosh"
```

**How to set up your Git user email:**  
This command lets you set up the user email address you'll use in your commits.  
All git projects under the current user  
```
git config --global user.email "abhishek.ghosh@gmail.com"
```

**Local directory, single project (this is the default tag)**
```
git config --local user.email "my_email@example.com"
```

**For all users on the current machine**  
```
git config --system user.email "my_email@example.com"
```

**Set automatic command-line coloring for Git for easy reviewing**
```
git config --global color.ui auto
```

**How to cache your login credentials in Git:**  
You can store login credentials in the cache so you don't have to type them in each time. Just use this command:  
```
git config --global credential.helper cache
```

**Create shortcut for a Git command.**  
E.g. `alias.glog "log --graph --oneline"` will set `git glog` equivalent to `git log --graph --oneline`.  
```
git config --global alias.<alias-name> <git-command>
```

**Create an alias named gc for the `git commit` command**
```
git config --global alias.gc commit
gc -m "New commit"
```

**Create an alias named ga for the `git add` command**
```
git config --global alias.ga add
```

**Set text editor used by commands for all users on the machine.**  
`<editor>` arg should be the command that launches the desired editor (e.g., `vi`).
```
git config --system core.editor <editor>
```

**Open the global configuration file in a text editor for manual editing.**
```
git config --global --edit
```