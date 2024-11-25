# Security context

In each container there can be multiple processes running and there can be multiple processes running. 

These processes are separated by their namesapces. By default, docker runs every process as root user, but we can change it with the following command.
`docker run --user=1000 ubuntu sleep 10`

docker limits the capabilities of the root user inside the container. It is not the same root user as the host machine root user.
Via linux capabilities we can add or remove capabilities of the root user inside the container.

```
# It will run ubuntu container with MAC_ADMIN privilege
Docker run --cap-add MAC_ADMIN ubuntu

# It will drop the privilege of kill a process
docker run --cap-drop kill ubuntu

# It will add all the privileges
docker run --privileged ubuntu
```

This can be configured in the Kubernetes as well. In the pod level and in the container level.
```
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: ubuntu-pod
    image: ubuntu
    securityContext:
      runAsUser: 1000
      capabilities:
        add: ["MAC_ADMIN","KILL"]
```

There are 2 types of accounts in Kubernetes space:
- **User Account** : Human user such as admin or developer
- **Service Account** : Account created by application to interact with the Kubernetes clusters like monitoring app or build tools such as Jenkins.

```
# It will create a service account named as dashboard-serviceaccount. 
# It will also create a secret with a token automatically. Now with this token we can call kubernetes api. 
Kubectl create serviceaccount dashboard-serviceaccount

# Like the following 
# curl https://192.168.56.70/api -insecure --header "Authorization Bearer #TOKEN"
```

We can create a service account, assign that right permission using role-based access control mechanism and expose the service account token and use it to configure the third-party application to authenticate Kubernetes api.

But in latest version we have to create the token manually and then we have to bind it with service account.  kubectl create sa dashboard-sa

#### We can create a secret from the service account
```
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: dashboard-sa-token
  annotations:
    kubernetes.io/service-account.name: "dashboard-sa"
```
If the third-party application is hosted in the same Kubernetes, then we can mount the service account token as volume.

We can edit the service account inside the POD, but we cannot change the service account of the deployment. 
After change there will be a new rollout deployment.


```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx-pod
  template:
    metadata:
      labels:
        app: nginx-pod
    spec:
      containers:
      - name: nginx
        image: nginx
      serviceAccountName: nginx-serviceaccount
      automountServiceAccountToken: false
```

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    volumeMounts:
    - mountPath: /var/run/secrets/tokens
      name: vault-token
  serviceAccountName: build-robot
  volumes:
  - name: vault-token
    projected:
      sources:
      - serviceAccountToken:
          path: vault-token
          expirationSeconds: 7200
          audience: vault
```
```
# By default, there is service account that is default service account.
# It will fetch all the service account
Kubectl get serviceaccount

# It will describe the default service account
kubectl describe serviceaccount default

# With this command we can fetch the token from sa.
kubectl describe secret <token-from- sa>
```

This default service account is associated with image pull registry and image pull secrets. 
We can also change it. For reference check [this](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account)
