# Imperative Commands

- **--dry-run** : by default all the command is run with this --dry-run. As soon as the command is run the resource will be created. 
- **--dry-run=client** : It will not create the resource rather it will check the whole command and tell us that the command is correct or not.
- **-o yaml > resource-definition.yaml** : this will create the resource definition in an yaml format

```
# It will first check the command is correct or not. If it is correct then will create one nginx-deployment file with the configuration given
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml

# it will create a redis-service yaml with the configuration given
kubectl expose pod redis --port=6379 --name=redis-service --dry-run=client -o yaml > redis-service.yaml

# it will create a dry run of the redis service and save it in redis-service.yaml
kubectl create service clusterip redis-service --tcp=6379:6379 --dry-run=client -o yaml > redis-service.yaml

# It will expose pod named as nginx pod type of NodePort
kubectl expose pod nginx-pod --port=80 --name=nginx-service --type=NodePort --dry-run=client -o yaml > nginx-service.yaml

# It will create a service of nodeport with port 80 and tagetport 80 with nodeport 30080
kubectl create service nodeport nginx-service --tcp=80:80 --node-port=30080 --dry-run=client -o yaml > nginx-service.yaml

# kubectl expose command automatically use the pods labels as the selctors but we can not specify the nodeport. 
# We must add that in the definition file then we can add the nodeport.
# Kubectl create service command will not use the pod labels as selectors 
# instead it will assume selectors as app: service-name and we can not pass selector in the definition file.
```