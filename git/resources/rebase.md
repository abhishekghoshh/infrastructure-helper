## How to use Git rebase (REWRITE HISTORY)
```
# You can transfer completed work from one branch to another using git rebase
# Apply commits of the current working branch and apply them to the HEAD of [branch] to make the history of your branch more linear
# Rebase the current branch onto <branch_name>. <branch_name> can be a commit ID, branch name, a tag, or a relative reference to HEAD.
# Reapplies commits on the current branch onto the tip of the specified branch.

git rebase branch_name

# Git Rebase can get really messy if you don't do it properly. 
# Before using this command I suggest that you re-read the official documentation [here](https://git-scm.com/book/it/v2/Git-Branching-Rebasing)

# How to run rebase interactively in Git. You can run git rebase interactively using the -i flag.
# It will open the editor and present a set of commands you can use.
# Interactively rebase current branch onto <base>. Launches editor to enter commands for how each commit will be transferred to the new base.

# git rebase -i <base>
git rebase -i master

# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit

# There can be conflict while doing git rebase
# Solve the conflicts like normal merge conflict, do git add and git rebase --continue
```
