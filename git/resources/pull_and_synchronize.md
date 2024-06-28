## Pull changes (Fetch + Merge)
```
# If other team members are working on your repository, you can retrieve 
# the latest changes made to the remote repository with the command below
# Fetch changes from the remote and merge current branch with its upstream.
# Fetch the specified remote's copy of current branch and immediately merge it into the local copy.

git pull


# Fetch the remote's copy of current branch and rebases it into the local copy. Uses git rebase instead of merge to integrate the branches.
git pull --rebase <remote>
```



## Synchronizing repositories
```
# Retrieves change from a remote repository, including new branches and commit.
git fetch

# This command will download the changes from a remote repo but will not perform a merge on your local branch (as git pull does that instead).
# Download all commits and branches from the remote without applying them on the local repo
# Fetch changes from the remote, but not update tracking branches.

git fetch remote


# Fetch changes from the remote but not merge with the working tree
git fetch remote-name
git fetch origin

# Fetches a specific <branch>, from the repo. Leave off <branch> to fetch all remote refs.
git fetch <remote> <branch>


# Delete remote Refs that were removed from the remote repository.
git fetch --prune [remote]

# Only download the specified `branch` from the `remote`
git fetch <remote> <branch>

# Merge the fetched changes if accepted
# If the remote repository has changes you want to merge with your local, then this command will do that for you:

git merge <remote>/<branch>
git merge origin/main
```
