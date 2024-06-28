## Generate new ssh key 
ssh-keygen -t ed25519 -C "your_email@example.com"

## ssh related files

- ~/.ssh/config
- ~/.ssh/id_ed25519
- ~/.ssh/id_ed25519.pub

When you generate new SSH keys using ssh-keygen and change the default key name, the keys are saved in the directory you specify. If you don't specify a directory, the keys are saved in the current working directory.


### Contents of ~/.ssh/config
    Host *
       AddKeysToAgent yes
       UseKeychain yes
       IdentityFile ~/.ssh/id_ed25519



### Multiple github account in a single machine
    # Default GitHub account (Old account, if any)
    Host github.com
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_ed25519
    
    # New GitHub account
    Host github.com-personal
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_ed25519_personal


`git remote set-url origin git@github.com-personal:abhishekghoshh/github-helper.git`

`git clone git@github.com-personal:abhishekghoshh/github-helper.git`


Also set the git config user.email and user.name otherwise it will take the default


### Check ssh configuration is correct or not
    ssh -T git@github.com
    ssh -T git@github.com-personal

### To check ssh key list
    ssh-add -l

### To add a key in ssh key set
    ssh-add  ~/.ssh/id_ed25519_personal

#### while git push using git ssh if you see it is showing other user and it has no access(which is normal) change the git remote url



## Working with git sha and blob files
```
# get SHA1 for a file
get ls-files -s

# get type of object (blob or tree)
git cat-file -t  SHA1 for Object

# get size of Object (blob or tree)
git cat-file -s SHA1 for Object

# get content of the Object (blob or tree)
git cat-file -p SHA1 for Object

# Shows the details of a specific commit, including its changes.
git show

# Display content of commit
git show sha1 of commit
```



