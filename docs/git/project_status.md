## Local Repository Status

**How to check a repository's status in Git**  
This command will show the status of the current repository including staged, unstaged, and untracked files.  
Show modified files in the working directory, staged for your next commit.  
```
git status
```

**For a short brief:**
```
git status -s
```

**Displays ignored files in addition to the regular status output:**
```
git status --ignored
```

## Local changes in Repository

**How to see changes made before committing them using `diff` in Git**  

**View unstaged changes by default:**  
You can pass a file as a parameter to only see changes on a specific file.  
Shows uncommitted changes since the last commit.  
Diff of what is changed but not staged.  
```
git diff
git diff all_checks.py
```

**View changes that are staged but not yet committed:**  
We can call `diff` with the `--staged` flag to see any staged changes.  
```
git diff --staged
```

**Show difference between staged changes and last commit:**
```
git diff --cached
```

**Display the difference between the current directory and the last commit:**
```
git diff HEAD
```

**Show the differences between two commits (should provide the commit IDs):**
```
git diff <commit_id_1> <commit_id_2>
```

**Compare a single `<file>` between two branches:**
```
git diff <branch_1> <branch_2> <file>
```

**Show the diff of what is in `branchA` that is not in `branchB`**
```
git diff branchB...branchA
```

**Show difference between working directory and last commit:**
```
git diff HEAD
```
