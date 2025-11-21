# Argo CD


> see this official documentation [Getting Started](https://argo-cd.readthedocs.io/en/stable/getting_started/#getting-started)
> We can create very gitops and devsecops pipeline using git+jenkins+helm+argoCD


## Configure

```sh
# Create an namespace called argocd
kubectl create namespace argocd

# Apply a stable version of argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Find the intial credential
# User name is admin
# To find the intial password of the argocd
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

# expose argocd server
kubectl port-forward svc/argocd-server -n argocd 8080:443
```




## Medium

- [Installing ArgoCD on Minikube and deploying a test application](https://medium.com/@mehmetodabashi/installing-argocd-on-minikube-and-deploying-a-test-application-caa68ec55fbf)
- [Installing Argo CD on Minikube — GitOps with Argo CD](https://medium.com/@eftech93/installing-argo-cd-on-minikube-gitops-with-argo-cd-c451d4a06459)
- [Deploying a Chat Application in Minikube with Argo CD: A Comprehensive Guide](https://medium.com/@eftech93/deploying-a-chat-application-in-minikube-with-argo-cd-a-comprehensive-guide-a7e252fc38a0)
- [ArgoCD Simplified: Production Deployment Guide](https://medium.com/@mhrznamn068/argocd-simplified-production-deployment-guide-00ab8ab03e23)
- [Designing a Maintainable GitOps Architecture: How I Scaled My Promotion Flow from a Simple Line to a System That Withstands Change](https://medium.com/@zxc0905fghasd/designing-a-maintainable-gitops-architecture-how-i-scaled-my-promotion-flow-from-a-simple-line-to-830320e6248f)
- [ArgoCD + GitHub Actions: A Complete GitOps CI/CD Workflow for Kubernetes Applications](https://medium.com/@mehmetkanus17/argocd-github-actions-a-complete-gitops-ci-cd-workflow-for-kubernetes-applications-ed2f91d37641)



## Courses

- [GitOps with ArgoCD](https://notes.kodekloud.com/docs/GitOps-with-ArgoCD/Introduction/Course-Introduction)


## Youtube

- [ArgoCD Personal playlist](https://www.youtube.com/playlist?list=PL67qvtIf7Oxs7e6z2o0kzCR-z27Q3VDyq)


## Udemy

- [Argo CD Essential Guide for End Users with Practice](https://udemy.com/course/argo-cd-essential-guide-for-end-users-with-practice/)