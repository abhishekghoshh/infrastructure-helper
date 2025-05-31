# Jenkins Helm Chart

This Helm chart deploys **Jenkins** on a Kubernetes cluster with:

- A dedicated **ServiceAccount** and **RBAC** permissions
- **Persistent storage** using `hostPath` for local environments like Minikube
- Optional **Ingress** to expose Jenkins via hostname
- Support for **Kubernetes-based Jenkins agent pods**

---

## Folder Structure

```
helm/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── pv-pvc.yaml
│   ├── serviceaccount.yaml
│   └── rbac.yaml
└── README.md
```

---

## 📘 Reference

> We can also use the official helm chart https://github.com/jenkinsci/helm-charts


This setup is inspired by:

- [Dynamic Jenkins Agents with Kubernetes](https://jsarvabhowma1.medium.com/dynamic-jenkins-agents-with-kubernetes-8f9010120ba7)
- [Blue-Green Deployment of Node.js App Using Jenkins and Istio on Minikube](https://medium.com/@shahebazsayed07/blue-green-deployment-of-node-js-app-using-jenkins-and-istio-on-minikube-kubernetes-cluster-a4925ca6cf73)
- [How to Use Kubernetes Pods As Jenkins Agents](https://www.youtube.com/watch?v=ZXaorni-icg)
    - [How-to-Use-Kubernetes-Pods-As-Jenkins-Agents.md](https://gist.github.com/darinpope/67c297b3ccc04c17991b22e1422df45a)
- [How to Push a Docker Image to Docker Hub Using Jenkins](https://www.youtube.com/watch?v=alQQ84M4CYU)

## 🛠️ Prerequisites

- Kubernetes cluster (e.g., Minikube, Kind)
- Helm v3+
- Ingress Controller (NGINX or Istio)
- Jenkins storage directory created on host

---

## 🚀 Installation

Make sure your Minikube node has the correct hostPath directory created and permission set:

```bash
minikube ssh
sudo mkdir -p /mnt/data/jenkins
sudo chown -R 1000:1000 /mnt/data/jenkins
exit

# install helm chart
helm upgrade --install jenkins . --namespace jenkins --create-namespace 
```

---

## Access Jenkins

```sh
# Add to /etc/hosts
echo "$(minikube ip) jenkins.local" | sudo tee -a /etc/hosts

# Alternative way
minikube addons enable ingress
# After the addon is enabled, please run "minikube tunnel" and your ingress resources would be available at "127.0.0.1"
echo "$(127.0.0.1) jenkins.local" | sudo tee -a /etc/hosts
minikube tunnel

# Access in browser
http://jenkins.local
```

---

## Get Jenkins Admin Password

```sh
kubectl exec -n jenkins -it deploy/jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword
```


## How to install harbor in helm and push OCI image in harbor
```sh
helm upgrade --install harbor harbor/harbor \
  --namespace harbor \
  --create-namespace \
  -f harbor-values.yaml

helm uninstall harbor -n harbor
```