# Readiness and liveness probe

**Readiness probe**: Sometimes container is up that does not mean that the container is ready for external communication like Jenkins takes time to boot up. So, we can configure an api or a script to check the container is ready or not.

**Liveness probe**: It is way to check periodically that the application is healthy or not, otherwise it destroys the container and starts a new one.

There are 3 ways to check:
1.	httpGet 
2.	tcpSocket
3.	start-up script

we can also add `initialDelaySeconds`, `periodSeconds`, `failureThreshold` configure other options

#### With http api
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
      readinessProbe:
        httpGet:
          path: /api/ready
          port: 8080
          httpHeaders:
          - name: Custom-Header
            value: Awesome
        initialDelaySeconds: 10
        periodSeconds: 5
        failureThreshold: 8
      livenessProbe:
        httpGet:
          path: /api/ready
          port: 8080
          httpHeaders:
          - name: Custom-Header
            value: Awesome
        initialDelaySeconds: 10
        periodSeconds: 5
        failureThreshold: 8
```

#### With a socket connection check
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
      readinessProbe:
        tcpSocket:
          port: 8080
      livenessProbe:
        tcpSocket:
          port: 8080
```

#### checking by starting a process
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
      readinessProbe:
        exec:
        - "cat"
        - "/app/ready"
      livenessProbe:
        exec:
        - "cat"
        - "/app/ready"
```
