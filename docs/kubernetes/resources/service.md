# Service

For accessing the pods from the outside of the container we need service.

There are three types of services.
- **NodePort**
- **ClusterIP** : Internal communication of pods. Service definition is almost same as the NodePort. Here type is ClusterIP. TargetPort is where the backend is exposed, and Port is where the service is exposed. Type ClusterIp is the default service type.
- **LoadBalancer** : With the NodePort service we can make external facing application available on the port of the worker nodes.
Let's say we have four cluster and one each server there are one frontend app deployed. With NodePort we can make external traffic forwarded to frontend pod but again for that we will have 4 urls for 4 services. So, need to have a loadbalancer here. We can have an external VM where nginx is deployed and then it will loadbalance 4 urls but it will be a complicated thing to manage. So we can use the inbuilt loadbalancer of different cloud platforms like Azure,GCP or AWS.

#### Sample nginx service yaml
```
#nginx-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  ports:
    - port: 80	
      targetPort: 80	# where the pod will listen (for nginx its 80)
      nodePort: 30008	# In this port the service will be accesible
  selector:
    app: nginx-pod 	# to connect with specific pods via pod's label
```

NodePort can range from 30000 to 32767. The work of the NodePort is to listen to a particular port and forward it to another node.


#### Some service commands
```
# for creating nginx-service with nginx-deployment.yaml
Kubectl create -f nginx-deployment.yaml

# To get all the services
kubectl get services

# To get details of the specific service, if there is no endpoint then the service is not attached to any pod.
kubectl describe service <service_name>

# to get the url of the NodePort service, but only for minikube
minikube service nginx-service --url

# Imperative style of creating service:

# It will create a service named as nginx-service of type NodePort with specific port and targetPort and it will match labels of the deployment of nginx-deplpyment 
# and NodePort will be be assigned randomly in the range of 30000 to 32767
kubectl expose deployment nginx-deployment --name=nginx-service --target-port=80 --port=80 --type=NodePort

# It will do just the same as previous just that it will save all the configurations in the nginx-service.yaml
kubectl expose deployment nginx-deployment --name=nginx-service --target-port=80 --port=80 --type=NodePort --dry-run=client -o yaml > nginx-service.yaml
```

If we have a connection like this:
- Voting-app -> frontend app for gathering the votes which will save the votes in redis
- Result-app -> frontend app for showing the votes which will fetch votes from postgres
- Redis -> save the votes from in a in memory store
- Postgres -> save the votes in relational db
- Worker-app -> It will constantly fetch the vote count from redis and constantly update the vote count in postgres

So, our setup will be like this:
- Deploy the pods/deployment
- Create the ClusterIP service for Redis and postgres
- Create the NodePort service for Voting-app and Result-app
