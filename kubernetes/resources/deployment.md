# Deployment

Kubernetes deployment create creates one deployment kind of object.

#### Sample nginx-deployment.yaml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx-pod
  template:
    metadata:
      name: nginx-pod
      labels:
        app: nginx-pod
    spec:
      containers:
      - name: nginx
        image: nginx
```

#### Some imperative commands
```
# It will fetch all the deployments.
kubectl get deployments

# It will give us the description of the specific deployment
kubectl describe deployments <deployment-name>

# To get the resources like pod, replicasets, services, deployments
kubectl get all

# it will create one deployment named ad http-frontend and its image will be httpd:2.4.alpine and count of the pod will be 1.
kubectl create deployment http-frontend --image=httpd:2.4.alpine

# it will scale the deployment and change the number of the pods 
kubectl scale deployment --replicas=3 httpd-frontend

# It will create a deployment and also record all the changes of the deployment for rollout history.
kubectl create -f nginx-deployment.yaml --record

# If we want to revert to previous version, we must add this record flag
# Update and roll back

# it will give the current rollout status of the deployment. When we change the replicas or the image at that time it will give the information.
kubectl rollout status deployment/nginx-deployment

# It will give us all the rollout history of the Kubernetes deployment rollout
kubectl rollout history deployment/nginx-deployment

# Kubernetes deployment object creates another replicaset and then it will add the pods into the replicaset

# It will revert the latest changes back to the previous version.
kubectl rollout undo deployment/nginx-deployment

# Changes to the existing deployment
# It will change the image of the deployment of the nginx deployment and will record it
kubectl set image deployment nginx-deployment nginx:old-image=nginx:new-image --record

# it will open vi editor and open the current configuration of the nginx-deployment
kubectl edit deployment nginx-deployment
```

#### For rollout Kubernetes has 2 types of strategy
- Recreate strategy
- Rolling strategy

