## Git log
```
# How to see your commit history in Git:
# This command shows the commit history for the current repository:
git log

# Only display commits that have the specified file.
git log -- <file>


# List commit history of current branch. -n count limits list to last n commits
git log [-n count]

# How to see your commit history including changes in Git:
# This command shows the commit's history including all files and their changes:

git log -p


# How to see minimal git log with commit id and message only:
# This command list of commits with commit id and commit message.

git log --oneline

# display all commits from local and remote
git log --oneline --all

# List one commit per line (-n tag can be used to limit the number of commits displayed (e.g. -5))
git log --oneline [-n]

# Log commits after some date (A sample value can be 4th of October, 2020 - "2020-10-04" or keywords such as "yesterday", "last month", etc.)
git log --oneline --after="YYYY-MM-DD"

# Log commits before some date (Both --after and --before tags can be used for date ranges)
git log --oneline --before="last year"

# How to show the commit log as a graph in Git:
# We can use `--graph `to get the commit log to show as a graph. Also,
`--oneline` will limit commit messages to a single line.

git log --graph --oneline


# How to show the commit log as a graph of all branches in Git:
# Does the same as the command above, but for all branches.

git log --graph --oneline --all


# --graph flag draws a text based graph of commits on left side of commit msgs. --decorate adds names of branches or tags of commits shown.
git log --graph --decorate

# An overview with reference labels and history graph. One commit per line.
git log --oneline --graph --decorate

# How to see log stats in Git:
# This command will cause the Git log to show some statistics about the changes in each commit, including line(s) changed and file names.

git log --stat


# show all commit logs with indication of any paths that moved
git log --stat -M

# Search for commits with a commit message that matches <pattern>.
git log --grep=<pattern>


# How to check the current commits log of a remote repo in Git
# Commit after commit, Git builds up a log. You can find out the remote repository log by using this command:

git log origin/main


# show the commits on branchA that are not on branchB
git log branchB..branchA

# show the commits that changed file, even across renames
# Lists version history for a file, including renames
git log --follow [file]


# List commits that are present on the current branch and not merged into ref. A ref can be a branch name or a tag name.
git log ref .

# List commit that are present on ref and not merged into current branch.
git log .ref


# Lists version history for the current branch from certain author
git log --author=[name]

# Shows who changed what and when in file
git blame [file]


# List operations (e.g. checkouts or commits) made on local repository.
# display all commits even the hidden ones
# Show a log of changes to the local repository's HEAD.
# Add --relative-date flag to show date info or --all to show all refs.

git reflog
```
