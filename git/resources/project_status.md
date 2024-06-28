## How to check a repository's status in Git:
```
# This command will show the status of the current repository including staged, unstaged, and untracked files.
# show modified files in working directory, staged for your next commit

git status

# for short brief
git status -s

# Displays ignored files in addition to the regular status output.
git status -ignored
```


## How to see changes made before committing them using "diff" in Git:
```
# You can pass a file as a parameter to only see changes on a specific file.
# git diff shows only unstaged changes by default. Shows uncommitted changes since the last commit
# diff of what is changed but not staged

git diff
git diff all_checks.py

# diff of what is staged but not yet commited, We can call diff with the --staged flag to see any staged changes.
git diff --staged

# Show difference between staged changes and last commit
git diff --cached

# Display the difference between the current directory and the last commit
git diff HEAD

# Show the differences between two commits (should provide the commit IDs)
git diff <commit_id_1> <commit_id_2>

# Compare a single <file> between two branches
git diff <branch_1> <branch_2> <file>

# show the diff of what is in branchA that is not in branchB
git diff branchB...branchA

# Show difference between working directory and last commit.
git diff HEAD
```
