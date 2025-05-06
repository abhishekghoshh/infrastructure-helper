## Git project initialization

**How to initialize a Git repo:**  
Everything starts from here. The first step is to initialize a new Git repo locally in your project root.  
You can do so with the command below:  
```
git init
```

**Create a git-tracked repository inside a new directory**
```
git init [dir_name]
```

## Add a remote repository in Git

**Display if the repo is from the remote**
```
git remote
```

**How to see remote URLs in Git:**  
You can see all remote repositories for your local repository with this command:  
```
git remote -v
```

**Add a remote repository to your local repository**  
Just replace `<url_to_remote>` with your remote repo URL.
```
git remote add <remote> <url_to_remote>
git remote add origin <http or ssh url>
```

**How to get more info about a remote repo in Git:**  
Just replace `origin` with the name of the remote obtained by running the `git remote -v` command.  
```
git remote show origin
```

**Remove a connection to a remote repo called `<remote>`**
```
git remote rm <remote>
```

**Rename a remote connection**
```
git remote rename <old_name> <new_name>
```

**To get the contents of remote branches in Git without automatically merging:**  
This lets you update the remote without merging any content into the local branches.  
You can call `git merge` or `git checkout` to do the merge.  
```
git remote update
```
