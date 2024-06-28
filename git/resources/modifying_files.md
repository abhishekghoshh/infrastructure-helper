## How to add a file to the staging area in Git:
```
# The command below will add a file to the staging area. 
# Just replace filename with the name of the file you want to add to the staging area.

git add fileName

# How to add all files in the staging area in Git. If you want to add all files in your project to the staging area, 
# you can use a wildcard . and every file will be added for you. -all works the same

git add .

# How to add only certain files to the staging area in Git
# With the asterisk in the command below, you can add all files starting with 'fil' in the staging area.

git add fil*

# How to see changes using "git add -p":
# This command opens a prompt and asks if you want to stage changes or not, and includes other options.

git add -p
```

## git rename/remove file
```
# How to remove tracked files from the current working tree in Git:
# This command expects a commit message to explain why the file was deleted.
# Remove file from working directory and staging area
# Removes a file from both the working directory and the repository, staging the deletion.

git rm filename


# remove git repo
git rm -rf .git/

# How to rename files in Git:
# This command stages the changes, then it expects a commit message.
# Moves or renames a file or directory in your Git repository.

git mv oldfile newfile
```


## resetting the files
```
# Discard changes [restore last commit to the working tree]
git restore file-name

# unstage files 
git restore --staged file-name


# Reset staging area to match most recent commit, but leave the working directory unchanged.
git reset

# Reset staging area and working directory to match most recent commit and overwrites all changes in the working directory.
git reset --hard

# unstage a file while retaining the changes in working directory
git reset [file]

# Move the current branch tip backward to <commit>, reset the staging area to match, but leave the working directory alone.
git reset <commit>

# Undo the latest commit but leave the working directory unchanged
# to change version of file[ Moving between commits]. Change HEAD [ retrieve commit to staging area]
git reset HEAD~1

# clear staging area, rewrite working tree from specified commit
# Same as previous, but resets both the staging area & working directory to match. Deletes uncommitted changes, and all commits after <commit>.
# Moves the branch pointer to a specified commit, discarding all changes in the staging area and the working directory, effectively resetting the repository to the specified commit.

git reset --hard [commit]

# Discard all changes of the latest commit (no easy recovery) [ be carefull]
git reset --hard HEAD~1

# Switches the current branch to the target reference, leaving a difference as an uncommitted change. When --hard is used,
# all changes are discarded. It's easy to lose uncommittedchanges with --hard.

# git reset [--hard] [target reference]


# Moves the branch pointer to a specified commit, preserving the changes in the staging area and the working directory.
git reset --soft <commit>


# Instead of HEAD~n, you can provide commit hash as well. Changes after that commit will be destroyed
# How to revert staged changes in Git:
# You can use the -p option flag to specify the changes you want to reset.

git reset HEAD filename
git reset HEAD -p
```
