## Push changes

**How to push changes to a remote repo in Git:**  
When all your work is ready to be saved on a remote repository, you can push all changes using the command below:
```
git push
```

**Push a copy of local branch named branch to the remote repo**
```
git push <remote_repo> branch~
```

**Delete a remote branch named branch (-d tag only works locally)**
```
git push <remote_repo> :branch
git push <remote_repo> --delete branch
```

**How to push a new branch to a remote repo in Git:**  
If you want to push a branch to a remote repository you can use the command below. Just remember to add `-u` to create the branch upstream. Push local branch to remote repository. Set its copy as an upstream.
```
git push -u origin branch_name
```

**How to force a push request in Git:**  
(`-f` flag or `--force` flag) This command will force a push request. This is usually fine for pull request branches because nobody else should have cloned them. But this isn't something that you want to do with public repos. Do not use the `--force` flag unless you're absolutely sure you know what you're doing.
```
git push -f origin branch_name
```

**How to remove a remote branch in Git:**  
If you no longer need a remote branch you can remove it using the command below:
```
git push --delete origin branch_name_here
```

**Push all of your local branches to the specified remote.**
```
git push <remote> --all
```

**Push local changes to the remote.**  
Use `--tags` to push tags. Tags aren't automatically pushed when you push a branch or use the `--all` flag. The `--tags` flag sends all of your local tags to the remote repo.
```
git push [--tags] [remote]
git push <remote> --tags
```
