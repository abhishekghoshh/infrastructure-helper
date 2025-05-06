## Git branching model

**List all branches**
```
git branch
git branch --list
```

**List all branches with remote branches**
```
git branch -a
```

**How to create a new branch in Git:**  
By default, you have one branch, the main branch. With this command, you can create a new branch. Git won't switch to it automatically - you will need to do it manually with the next command.
```
git branch branch_name
```

**How to list branches in Git:**  
You can view all created branches using the `git branch` command. It will show a list of all branches and mark the current branch with an asterisk and highlight it in green.
```
git branch
```

**How to delete a branch in Git:**  
When you are done working with a branch and have merged it, you can delete it using the command below. Remove selected branch, if it is already merged into any other. (-D instead of -d forces deletion.)
```
git branch -d branch_name
```

**Force delete a local branch (whether merged or unmerged)**
```
git branch -D <branch>
```

**Rename the current branch to `<new_name>`**
```
git branch -m <new_name>
```

**How to check remote branches that Git is tracking:**  
This command shows the name of all remote branches that Git is tracking for the current repository:
```
git branch -r
```

**Display list commit in different branches**
```
git branch -v
```

**Display tracked branches**
```
git branch -vv
```

## Switch branches

**How to switch to a newly created branch in Git:**  
When you want to use a different or a newly created branch you can use this command:
```
git checkout branch_name
git switch branch_name
```

**How to create a branch in Git and switch to it immediately.**  
In a single command, you can create and switch to a new branch right away.
```
git checkout -b branch_name
```

**Checking out (switching to) older commits.**  
Checks out the third-to-last commit
```
git checkout HEAD~3
```

**Checking out (switching to) older commits**
```
git checkout <commit_id>
```

**How to revert unstaged changes in Git:**
```
git checkout filename
```

## How to merge two branches in Git

**To merge the history of the branch you are currently in with the `branch_name`, you will need to use the command below:**  
Merging a branch into the main branch. Join specified `[branch_name]` branch into your current branch (the one you are on currently).
```
git checkout main
git merge branch_name
```

**Merging a branch and creating a commit message**
```
git merge --no-ff <other_branch>
```

**How to abort a conflicting merge in Git:**  
If you want to throw a merge away and start over, you can run the following command:
```
git merge --abort
```
