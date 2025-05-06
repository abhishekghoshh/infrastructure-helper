## Pull changes (Fetch + Merge)

**If other team members are working on your repository, you can retrieve the latest changes made to the remote repository with the command below:**  
Fetch changes from the remote and merge the current branch with its upstream. Fetch the specified remote's copy of the current branch and immediately merge it into the local copy.
```sh
git pull
```

**Fetch the remote's copy of the current branch and rebase it into the local copy:**  
Uses `git rebase` instead of merge to integrate the branches.
```sh
git pull --rebase <remote>
```

## Synchronizing repositories

**Retrieves changes from a remote repository, including new branches and commits:**
```sh
git fetch
```

**This command will download the changes from a remote repo but will not perform a merge on your local branch (as `git pull` does that instead):**  
Download all commits and branches from the remote without applying them on the local repo. Fetch changes from the remote, but not update tracking branches.
```sh
git fetch remote
```

**Fetch changes from the remote but not merge with the working tree:**
```sh
git fetch remote-name
git fetch origin
```

**Fetches a specific `<branch>` from the repo:**  
Leave off `<branch>` to fetch all remote refs.
```sh
git fetch <remote> <branch>
```

**Delete remote refs that were removed from the remote repository:**
```sh
git fetch --prune [remote]
```

**Only download the specified `branch` from the `remote`:**
```sh
git fetch <remote> <branch>
```

**Merge the fetched changes if accepted:**  
If the remote repository has changes you want to merge with your local, then this command will do that for you:
```sh
git merge <remote>/<branch>
git merge origin/main
```

**Git `pull` is the same as fetching `origin master` and then merging `origin/master`:**
```sh
git fetch origin master
git merge origin/master

git pull origin master
```