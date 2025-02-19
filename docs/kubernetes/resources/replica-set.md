# ReplicaSet

ReplicaSet is a group of same pods where we can scale in(reduce) or scale out(increase) the number of the pods.
```
# it will create a replicaset from the definition file.
kubectl create/apply -f <replicaset-definition.yaml>

# to get all the replicaset in the default namespace
kubectl get replicateset

# to get all the replicaset in the default namespace
kubectl describe replicaset

# to delete the replicaset
kubectl delete replicaset <replicaset-name>
```

#### Sample replica set configuration yaml
```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
  labels:
    type: frontend
spec:
  selector:
    matchLabels:
      name: nginx-pod
      type: frontend
  replicas: 1
  template:
    metadata:
      labels:
        name: nginx-pod
        type: frontend
    spec:
      containers:
        - name: nginx
          image: nginx
```

labels under template section and mathLabels under selector should be same. That is how replicate set identifies the pod and controls the number of the pods. If we try to delete any pod or anyhow any pod got crashed, then Kubernetes automatically brings another pod in.

#### Scale commands
```
# replace the previous nginx-repicaset with the current replicas given in the definition file
kubectl replace -f nginx-replicaset.yaml

# it will override the replicas given in the yaml
kubectl scale --replicas=6 -f nginx-replicaset.yaml

# it will open an editor and show the current configuration of the replicaset then we can easily scale out.
kubectl edit replicaset nginx-replicaset

# it will scale out an existing replicaset
kubectl scale --replicas=6 replicaset nginx-replicaset
```