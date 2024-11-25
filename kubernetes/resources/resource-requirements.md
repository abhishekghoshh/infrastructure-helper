# Resource requirements

```
# By default, in Kubernetes there is not restriction on usage and cpu usage.  
# With the Limit range we can set the default memory and cpu of a pod in any namespace. 
# With resource block of the pod definition, we can also restrict the default and maximum memory usage.
# It will create the memory limit of the container in any namespace
Kubectl apply -f mem-limit-range.yaml
```

```
apiVersion: v1
kind: LimitRange
metadata:
  name: mem-limit-range
  namespace: dev
spec:
  limits:
  - default:
      memory: "512Mi" #cpu usage
    defaultRequest:
      memory: "256Mi" #Memory usage
    type: Container
```

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  namespace: default
  labels:
    app: nginx-pod
spec:
  containers:
    - name: nginx
      image: nginx
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```