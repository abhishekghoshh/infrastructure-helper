# Imperative Commands

Before we begin, familiarize with the two options that can come in handy while working with the below commands:
- `--dry-run`: By default, as soon as the command is run, the resource will be created. If you simply want to test your command, use the `--dry-run=client` option. This will not create the resource, instead, tell you whether the resource can be created and if your command is right.
- `-o yaml`: This will output the resource definition in YAML format on screen.

Use the above two in combination to generate a resource definition file quickly, that you can then modify and create resources as required, instead of creating the files from scratch.

## POD

**Create an NGINX Pod:**
```sh
kubectl run nginx --image=nginx
```

**Generate POD Manifest YAML file (-o yaml). Don't create it (--dry-run):**
```sh
kubectl run nginx --image=nginx --dry-run=client -o yaml
```

## Deployment

**Create a deployment:**
```sh
kubectl create deployment --image=nginx nginx
```

**Generate Deployment YAML file (-o yaml). Don't create it (--dry-run):**
```sh
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml
```

**Generate Deployment with 4 Replicas:**
```sh
kubectl create deployment nginx --image=nginx --replicas=4
```

**You can also scale a deployment using the kubectl scale command:**
```sh
kubectl scale deployment nginx --replicas=4
```

**Another way to do this is to save the YAML definition to a file and modify:**
```sh
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml
```

You can then update the YAML file with the replicas or any other field before creating the deployment.

## Service

**Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379:**
```sh
kubectl expose pod redis --port=6379 --name=redis-service --dry-run=client -o yaml
```

**Or:**
```sh
kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml
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

**Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:**
```sh
kubectl expose pod nginx --port=80 --name=nginx-service --type=NodePort --dry-run=client -o yaml
```

**Or:**
```sh
kubectl create service nodeport nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml
```

**Note:**
- The `kubectl expose` command automatically uses the pod's labels as selectors, but you cannot specify the node port. You must add that in the definition file, then you can add the node port.
- The `kubectl create service` command will not use the pod labels as selectors; instead, it will assume selectors as `app: service-name`, and you cannot pass selectors in the definition file.

## HPA

Horizontal Pod Autoscaler (HPA) automatically scales the number of pods in a deployment based on observed CPU utilization or other select metrics.

**Create an HPA for a deployment:**
```sh
kubectl autoscale deployment <deployment-name> --cpu-percent=50 --min=1 --max=10
```

**Check the status of the HPA:**
```sh
kubectl get hpa
```

