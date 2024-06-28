## How to commit changes in the editor in Git:
```
# This command will open a text editor in the terminal where you can write a full commit message.
# A commit message is made up of a short summary of changes, an empty line, and a full description of the changes after it.
git commit

# How to commit changes with a message in Git:
# You can add a commit message without opening the editor. This command lets you only specify a short summary for your commit message.
git commit -m "your commit message here"

# How to commit changes (and skip the staging area) in Git:
# You can add and commit tracked files with a single command by using the -a and -m options or -am option.
git commit -a -m "your commit message here"
git commit -am "your commit message here"

# How to amend the most recent commit in Git, --amend` allows you to modify and add changes to the most recent commit
# edit commit message. Replace the last commit with the staged changes and last commit
# combined. Use with nothing staged to edit the last commit's message

git commit --amend
git commit --amend -m "[New commit message]"

!!Note!!: fixing up a local commit with amend is great and you can push it to a shared repository after you've fixed it. 
# But you should avoid amending commits that have already been made public.

# Creates a new note and associates it with an object (commit, tag, etc.).
git notes add
```


## How to see a specific commit in Git:
```
# This command shows a specific commit.
# Replace commit-id with the id of the commit that you find in the commit log after the word commit.

git show commit-id

# show any object in Git in human-readable format
git show [SHA]
```




## TEMPORARY COMMITS(Temporarily store modified, tracked files in order to change branches())
```
# Saving staged and unstaged changes to stash for a later use (see below for the explanation of a stash)
# Put current changes in your working directory into stash for later use.
git stash

# Stashing staged, unstaged and untracked files as well
git stash -u

# Stashing everything (including ignored files)
git stash --all

# Reapply previously stashed changes and empty the stash
# Apply stored stash content into working directory, and clear stash.
git stash pop

# Reapply previously stashed changes and keep the stash
git stash apply

# Dropping changes in the stash, discard the changes from top of stash stack
# Delete a specific stash from all your previous stashes.
git stash drop

# Lists all stashes in the repository.
git stash list
```





## How to rollback to previous commit
```
# git revert will create a new commit that is the opposite of everything in the given commit.
# We can revert the latest commit by using the head alias like this:

git revert HEAD

# How to rollback an old commit in Git. You can revert an old commit using its commit id. 
# This opens the editor so you can add a commit message. Undo a single given commit, 
# without modifying commits that come after it (a safe reset) May result in revert conflicts
# Create a new commit, reverting changes from the specified commit. It generates an inversion of changes. 

git revert comit_id_here


# Undoes the changes introduced by the specified commit, but does not create a new commit.
git revert -no-commit <commit> 

# Shows which files would be removed from working directory. Use the -f flag in place of the -n flag to execute the clean.
git clean -n
```
