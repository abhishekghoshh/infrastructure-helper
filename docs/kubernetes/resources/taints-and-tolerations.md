# Taints and Tolerations

It helps to set restrictions to what pod to schedule in which node.

Suppose we have 3 nodes and 4 pods, and we have applied a taint blue on node-A and we have added tolerant to pod-B so only pod-B is capable to be allocated in node-A. But in the same time pod-B can also be allocated to another node. Taints imposes a rule on the node that it will only be accepting pods with specific tolerations, but it does not impose any rule on pods. 

There are 3 taint effects.
- NoExecute
- PrefferNoSchedule
- NoSchedule

```
# It will impose a taint with key value with taint effect
Kubectl nodes <node-name> key=value:taint-effect

kubectl nodes node-a color:blue:NoSchedule
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
  tolerations:
    - key: "color"
      operator: "Equal"
      value: "blue"
      effect: "NoSchedule"
  containers:
    - name: nginx
      image: nginx
```
```
# By default, the master node has some taints that prevents any pods to schedule on master.

# to find the taints applied on the node
Kubectl describe node <node-name> | grep Taint

# It will impose a taint with key value with taint effect.
kubectl nodes <node-name> key=value:taint-effect -

# To see a pod in which node
Kubectl get pods -o wide
```