## Introduction

Git is a distributed version control system that helps developers collaborate on projects of any scale. Linus Torvalds, the developer of the Linux kernel, created Git in 2005 to help control the Linux kernel's development.

### What is a Distributed Version Control System?

A distributed version control system is a system that helps you keep track of changes you've made to files in your project. This change history lives on your local machine and lets you revert to a previous version of your project with ease in case something goes wrong.

Git makes collaboration easy. Everyone on the team can keep a full backup of the repositories they're working on on their local machine. Then, thanks to an external server like BitBucket, GitHub or GitLab, they can safely store the repository in a single place. This way, different members of the team can copy it locally and everyone has a clear overview of all changes made by the whole team.

Git has many different commands you can use. And I've found that these fifty are the ones I use the most often (and are therefore the most helpful to remember).

### Basic Definitions
- **git**: an open source, distributed version-control system
- **GitHub**: a platform for hosting and collaborating on Git repositories
- **Commit**: a state of the code base. A snapshot of the project you can come back to. A Git object, a snapshot of your entire repository compressed into a SHA
- **Branch**: A copy of the project used for working in an isolated environment without affecting the main project. a reference to a commit; can have a tracked upstream. A lightweight movable pointer to a commit
- **Local repo or repository**: A local directory containing code and files for the project
- **Remote**: An online version of the local repository hosted on services like GitHub, GitLab, and BitBucket. A common repository on GitHub that all team member use to exchange their changes
- **Clone**: The act of making a clone or copy of a repository in a new directory. A local version of a repository, including all commits and branches
- **fork**: A copy of a repository on GitHub owned by a different user
- **Git merge**: The process of combining two branches together
- **pull request**: a place to compare and discuss the differences introduced on a branch with reviews, comments, integrated tests, and more
- **HEAD**: representing your current working directory, the HEAD pointer can be moved to different branches, tags, or commits
- **Tag**: a reference (standard) or an object (annotated)

### More Advanced Definitions
- **.gitignore file**: A file that lists other files you want git not to track (e.g. large data folders, private info, and any local files that shouldn't be seen by the public.)
- **Staging area**: a cache that holds changes you want to commit next.
- **Git stash**: another type of cache that holds unwanted changes you may want to come back later
- **Commit ID or hash**: a unique identifier for each commit, used for switching to different save points.
- **HEAD (always capitalized letters)**: a reference name for the latest commit, to save you having to type Commit IDs. HEAD\~n syntax is used to refer to older commits (e.g. HEAD\~2 refers to the second-to-last commit).
- **ssh authentication**: You can access and write data in repositories on github.com using the ssh(Secure shell protocol). When you connect via ssh, you authenticate using a private key file saved on your local machine.

### What is a Branch?
Branches are special "copies" of the code base which allow you to work on different parts of a project and new features in an isolated environment. Changes made to the files in a branch won't affect the "main branch" which is the main project development channel.

### What is a Repository?
A repository or a repo is any location that stores code and the necessary files that allow it to run without errors. A repo can be both local and remote. A local repo is typically a directory on your machine while a remote repo is hosted on servers like GitHub.

### A Note on Cloning
There are two primary methods of cloning a repository - HTTPS syntax and SSH syntax. While SSH cloning is generally considered a bit more secure because you have to use an SSH key for authentication, HTTPS cloning is much simpler and the recommended cloning option by GitHub.

HTTPS: `git clone https://github.com/your_username/repo_name.git`

SSH: `git clone git@github.com:user_name/repo_name.git`
