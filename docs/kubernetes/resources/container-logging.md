# Container logging

```
docker run -d kodecloud/event-simulator 
docker log -f <container-name>

# this is how we can check the logs of a docker container after running it in detached mode. 
# We can do the same with Kubernetes.
kubectl create -f event-simulator.yaml

# To get logs of a specific pod
kubectl logs -f event-simulator-pod

# To get the logs of a specific container of a specific pod
kubectl logs -f <pod-name> <container-name>
```



#### Monitoring Solutions:
1.	Prometheus
2.	Elastic stack
3.	Datadog
4.	Dynatree

Kubernetes runs an agent on each node known as kubelet which is responsible for receiving instruction from Kubernetes master server. It has a subcomponent known as container advisor, it is responsible for retrieving performance metrics from pods and exposing them to kubelet api.

```
# To enable the metric server on minikube
minikube addons enable metrics-server

# To find the node with max using the resources
kubectl top node

# To find the pod with the max using resources.
kubectl top pod
```