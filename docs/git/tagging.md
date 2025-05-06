## Tagging Commits

### List All Tags
```sh
git tag
```

### Create a Tag
Create a tag reference named `<tag-name>` for the current commit. Add commit SHA to tag a specific commit instead of the current one.

```sh
git tag [tag-name] [commit sha]
```

### Create an Annotated Tag
Create a tag object named `<tag-name>` for the current commit.

```sh
git tag -a [tag-name] [commit sha]
```

### Remove a Tag
Remove a tag from the local repository.

```sh
git tag -d [tag-name]
```

### Create an Annotated Tag with a Custom Message
Creates an annotated tag at the current commit with a custom message.

```sh
git tag -a <tag-name> -m <message>
```
