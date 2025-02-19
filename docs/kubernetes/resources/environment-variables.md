# Environment variables

We can pass environment variables in these 3 ways.
- Using env 
- Using config map key valueFrom -> configMapKeyRef
- Using secret key valueFrom ->secretKeyRef


```
# Using env in the pod specification
spec:
  name: postgres
  image: postgres
  env:
  - name: POSTGRES_PASSWORD
    value: MY_SECRET_PASSWORD

# Using configMapKeyRef in the pod specification
spec:
  name: postgres
  image: postgres
  env:
  - name: POSTGRES_PASSWORD
    valueFrom:
      configMapKeyRef:
        name: posgtres-config
        key: password
        name: postgres-secret
        key: password

# Using secretKeyRef in the pod specification
spec:
  name: postgres
  image: postgres
  env:
  - name: POSTGRES_PASSWORD
    valueFrom:
      secretKeyRef:
        name: postgres-secret
        key: password
```
We can either use configMapKeyRef where we can pass keys, or we can use configMapRef where we can directly pass the configMap. Same goes with Secrets. We can either use secretKeyRef or secretRef.

We can create configMap with these 3 ways
- By passing all the values in command.
- By passing the properties file or yaml file in the command
- By using the deifinition file.


#### Some imperative commands
```
#  It will create a configmap with color blue
Kubectl create configmap app-config --from-literal app-color=blue

# It weill create a config file with theapp.properties content
kubectl create configmap app-config --from-file /path/app.properties

# It will create a configMap with app-config definition file
kubectl apply -f app-config.yaml

# It will fetch all the config maps
kubectl get cm/configmaps

# It will describe the config map app-config
kubectl describe configmap app-config
```

#### Sample config map and pod definition yaml
```
# nginx config map
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-configmap
data:
  name: nginx
  tier: frontend
  work: loadbalancing

# pod defination
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
      envFrom:
        - configMapRef:
            name: nginx-configmap
```

#### config map stores everything in plain text format, which is not suitable for storing password, that's why we need secrets.
We can create secret with these 3 ways.
- By passing all the values in command.
- By passing the properties file or yaml file in the command
- By using the deifinition file.

```
# It will create a secret with color blue.
Kubectl create secret generic app-secret --from-literal app-color=blue

# It will create a secret with the app-secret.properties file.
Kubectl create secret generic app-secret --from-file app-secret.properties
```

```
# app.properties
db_host=postgres
db_password=root
db_name=database

# app-sercret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
data:
  db_host: cG9zdGdyZXMNCg==
  db_password: cm9vdA0K
  db_name: ZGF0YWJhc2UNCg==

# nginx-with-secret
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx
    envFrom:
      - secretRef:
          name: app-secret
```
There are some other ways to store the information. That is Helm secrets, HarshiCorp vault etc.

