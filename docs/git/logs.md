## Git log

**How to see your commit history in Git:**  
This command shows the commit history for the current repository.  
```sh
git log
```

**Show the commit history of a remote branch:**
```sh
git log origin/master
```

**Show the commit history of a specific branch:**
```sh
git log <branch-name>
```

**Only display commits that have the specified file:**  
```sh
git log -- <file>
```

**List commit history of the current branch (-n count limits list to last n commits):**  
```sh
git log [-n count]
```

**How to see your commit history including changes in Git:**  
This command shows the commit's history including all files and their changes.  
```sh
git log -p
```

**How to see a minimal git log with commit ID and message only:**  
This command lists commits with commit ID and commit message.  
```sh
git log --oneline
```

**Display all commits from local and remote:**  
```sh
git log --oneline --all
```

**List one commit per line (-n tag can limit the number of commits displayed, e.g., -5):**  
```sh
git log --oneline [-n]
```

**Log commits after some date:**  
A sample value can be "2020-10-04" or keywords such as "yesterday", "last month", etc.  
```sh
git log --oneline --after="YYYY-MM-DD"
```

**Log commits before some date:**  
Both `--after` and `--before` tags can be used for date ranges.  
```sh
git log --oneline --before="last year"
```

**How to show the commit log as a graph in Git:**  
We can use `--graph` to display the commit log as a graph. Adding `--oneline` limits commit messages to a single line.  
```sh
git log --graph --oneline
```

**How to show the commit log as a graph of all branches in Git:**  
Does the same as the command above but for all branches.  
```sh
git log --graph --oneline --all
```

**Show a graph with branch names or tags:**  
```sh
git log --graph --decorate
```

**An overview with reference labels and history graph (one commit per line):**  
```sh
git log --oneline --graph --decorate
```

**How to see log stats in Git:**  
This command will show statistics about changes in each commit, including lines changed and file names.  
```sh
git log --stat
```

**Show all commit logs with indication of any paths that moved:**  
```sh
git log --stat -M
```

**Search for commits with a commit message that matches `<pattern>`:**  
```sh
git log --grep=<pattern>
```

**How to check the current commit log of a remote repo in Git:**  
Find out the remote repository log using this command:  
```sh
git log origin/main
```

**Show the commits on `branchA` that are not on `branchB`:**  
```sh
git log branchB..branchA
```

**Show the commits that changed a file, even across renames:**  
Lists version history for a file, including renames.  
```sh
git log --follow [file]
```

**List commits present on the current branch but not merged into ref (a branch name or a tag name):**  
```sh
git log ref .
```

**List commits present on ref but not merged into the current branch:**  
```sh
git log .ref
```

**Lists version history for the current branch from a certain author:**  
```sh
git log --author=[name]
```

**Shows who changed what and when in a file:**  
```sh
git blame [file]
```

**Show the commit log with a custom format:**
```sh
git log --pretty
```

**Show the commit log with file names only:**
```sh
git log --name-only
```

**List operations (e.g., checkouts or commits) made on the local repository:**  
Display all commits, including hidden ones. Show a log of changes to the local repository's `HEAD`.  
Add `--relative-date` flag to show date info or `--all` to show all refs.  
`reflog` shows all the actions we have done in this repo, if we have done any `git reset --hard` then also we could revert back to the previous state.
```sh
git reflog
```
