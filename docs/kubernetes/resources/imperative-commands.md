# Imperative Commands

- **--dry-run**: By default, all the commands are run with this `--dry-run`. As soon as the command is run, the resource will be created.
- **--dry-run=client**: It will not create the resource; rather, it will check the whole command and tell us whether the command is correct or not.
- **-o yaml > resource-definition.yaml**: This will create the resource definition in a YAML format.

**Create a deployment and save it to a file:**
```sh
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml
```

**Create a service and save it to a file:**
```sh
kubectl expose pod redis --port=6379 --name=redis-service --dry-run=client -o yaml > redis-service.yaml
```

**Create a dry run of the redis service and save it to a file:**
```sh
kubectl create service clusterip redis-service --tcp=6379:6379 --dry-run=client -o yaml > redis-service.yaml
```

**Expose a pod named nginx-pod of type NodePort and save it to a file:**
```sh
kubectl expose pod nginx-pod --port=80 --name=nginx-service --type=NodePort --dry-run=client -o yaml > nginx-service.yaml
```

**Create a service of type NodePort with port 80 and target port 80 with node port 30080 and save it to a file:**
```sh
kubectl create service nodeport nginx-service --tcp=80:80 --node-port=30080 --dry-run=client -o yaml > nginx-service.yaml
```

**Note:**
- The `kubectl expose` command automatically uses the pod's labels as selectors, but you cannot specify the node port. You must add that in the definition file, then you can add the node port.
- The `kubectl create service` command will not use the pod labels as selectors; instead, it will assume selectors as `app: service-name`, and you cannot pass selectors in the definition file.