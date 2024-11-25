# Pods

```
# it will run a new pod with image.
kubectl run <pod_name> --image=<image_name>

# it will run a new pod called nginx with image as nginx
kubectl run nginx --image=nginx

# to get all the pods
kubectl get pods

# to get more details for the pods
kubectl get pods -o wide

# it will give us the detailed info about the specific pod
kubectl describe pod <pod-name>
```


Kubernetes yaml file must contain these fields -> apiVersion, kind, metadata, spec


#### Sample pod configuration yaml
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  tier: frontend
spec:
  containers:
    - name: nginx
      image: nginx
```

#### Some other commands to interact with the pod
```
# to create a pod with this yaml file.
kubectl apply/create -f nginx-pod.yaml

# to give more description of the nginx pod
kubectl describe pod nginx

# it will open a vi editor where we can change the pod definition file also this is a in memory pod definition file which is maintained by Kubernetes.
kubectl edit pod nginx

# to delete the nginx pod
kubectl delete pod nginx

# delete all the pods.
kubectl delete --all pods

# delete all resources in namespace.
kubectl delete all --all -n <name-space>

# It will not create any pod rather it's a imperative style of writing definition file where a pod definition file will created with the necessary fields.
kubectl run redis --image=redis --dry-run=client -o yaml > redis-pod.yaml
```