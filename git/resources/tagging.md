## Tagging commits
```
# List all tags.
git tag

# Create a tag reference named name for current commit. 
# Add commit sha to tag a specific commit instead of current one.

git tag [tag-name] [commit sha]


# Create a tag object named name for current commit.
git tag -a [tag-name] [commit sha]

# Remove a tag from local repository
git tag -d [tag-name]

# Creates an annotated tag at the current commit with a custom message.
git tag -a <tag-name> -m <message>
```
