# Commands and Args

In docker we have ENTRYPOINT and CMD for giving command line arguments, but we can override that using --entrypoint and the extra parameters passed in the docker run command. Same way we can override the existing command in the pod definition file with command and args. ENTRYPOINT will associated with command and CMD will be associated with args. 

Let's say we have a dockerfile like this
```
# ubuntu-sleeper dockerfile

FROM UBUNTU
ENTRYPOINT ["sleep"]
CMD ["10"]
```

And pod definition like this
```
name: ubuntu
image: ubuntu-sleeper
command: ["sleeper2.0"]
args: ["100"]
```

The pod definition file is same as this docker run command `docker run --entry-point=sleeper2.0 ubuntu-sleeper 100`

Copy the content of existing pod into a yaml -> kubectl get pod <pod-name> -o yaml > pod-definition.yaml