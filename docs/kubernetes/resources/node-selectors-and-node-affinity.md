# Node selectors and Node Affinity


#### To label a node
```
kubectl label node <node-name> key=value
```

#### The specific pod with specific node with nodeSelector with key value will be placed on that node.
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  namespace: default
  labels:
    app: nginx-pod
spec:
  nodeSelector:
    app: color
  containers:
    - name: nginx
      image: nginx
```

#### Node selector is easy to use but lack the advanced features that is why we are using node Affinity. Here also at first, we must label the node
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  namespace: default
  labels:
    app: nginx-pod 
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
            - key: size
              operator: In
              values:
              - "Large"
              - "Medium"
  containers:
    - name: nginx
      image: nginx
```
To place this nginx pod we must label the node with Large or Medium else pod will not be executed in the node.

#### There are 3 types of operators:
- In: If the any value from values is there in the labels in the node
- No: If the values from the values are there not in labels of thr node
- Exists: If the key exists in the label of the node

#### There are 3 types of nodeAffinity selectors.
- **requiredDuringSchedulingIgnoredDuringExecution**:
    - During scheduling : Label is required in the node other wise pod will not be executed
    - During execution : In if there is any change in label in node then pod will ignore that and continue executing
- **prefferedDuringSchedulingIgnoredDuringExecution**:
    - During scheduling : It will try to find the node with the label. If it does not find the node, then it tries to place the pod in any node
    - During execution : In if there is any change in label in node then pod will ignore that and continue executing
- **requiredDuringSchedulingRequiredDuringExecution**:
    - During scheduling : Label is required in the node otherwise pod will not be executed
    - During execution : In if there is any change in label in node then pod should have that label other wise it will stop executing

With the combination of taints and node affinity we can specify that which pod will place on which node.