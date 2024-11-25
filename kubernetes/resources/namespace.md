# Namespace

NameSpace is a way to segregate different resources like dev,qa,prod etc. Default namespace is default.

#### Sample dev-namespace.yaml
```
apiVersion: v1
kind: NameSpace
metadata:
  name: dev
```
#### Some imperative commands
```
# to create a namespace
Kubectl create -f dev-namepace.yaml

# To get all the pod inside dev namespace
kubectl get pods --namespace=dev

# If we have to set the dev namespace permanently then we can keep it inside the KubeConfig
Kubectl config set-context $( kubectl config current-context ) -namespace=dev

# To limit the resources using in a specific namespace we can use resource quota
# to get all the namspaces
kubectl get ns

# To get count of the namespaces
kubectl get ns --no-headers | wc -l
```

In pod-definition.yaml in metadata we can add namespace to mention the namespace where the pod will be deployed
```
# nginx-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  namespace: dev
  labels:
    app: nginx-pod
spec:
  containers:
    - name: nginx
      image: nginx
```

```
# to get the pods in dev namespace 
kubectl -n dev get pods --no-header

# In which namespace the nginx pod is deployed?
Ans: kubectl get pods --all-namespaces | grep nginx

# In the same namespace we can connect to another pod via pod name but to connect with other resources in another namespace we have to maintain we proper format.
# Resource-name.namespace.resource-type.domain
# example: db-service.dev.svc.cluster.local
# db-service is the name of the resource, dev is the namespace, svc is the resource type, cluster.local is he domain
```