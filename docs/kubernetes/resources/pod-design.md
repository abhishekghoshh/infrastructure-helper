# Pod Design

Labels and selectors are standard methods to group things together. We can keep these labels under metadata. These labels are used to identify a specific pod by the service, replica set, and deployment. Though one label is sufficient to identify, we can use as many labels as we want.

Alongside labels, we can also add annotations. They are used to save build information and other documentation purposes.

## Finding Pods by Label

**Find the pods where the label is `env=dev`:**
```sh
kubectl get pods -l env=dev
```

**Find the count of the pods with this label:**
```sh
kubectl get pods -l env=dev --no-headers | wc -l
```

**Find all the objects in the `prod` environment:**
```sh
kubectl get all -l env=prod
```

**Count all the objects in the `prod` environment:**
```sh
kubectl get all -l env=prod --no-headers | wc -l
```

**Find all the pods with all these labels:**
```sh
kubectl get pods -l env=prod,bu=finance,tier=frontend
```

## Deployment Rollouts

When we first create a deployment, it creates a rollout, and a new rollout creates a new deployment revision. When there is a change in deployment like an image update, it creates a new rollout which again creates a revision. This helps us to keep track of the changes.

There are two types of deployment strategies:

- **Recreate**: Destroy all the containers, then create the containers with changes. During the period when the older version is down, the application becomes inaccessible.
- **Rolling update**: In this strategy, some of the old containers are down and new containers with changes are started in their place. If there is no mention of the deployment strategy in the YAML file, this strategy becomes the default.

If we perform the `kubectl describe deployment <deployment-name>`, we can see the events of how containers went down and up. When there is an upgrade, the deployment object internally creates a replica set and then fills that with the new containers and deletes the containers from the old replica set.

## Rollback

**To undo a change, use the following command:**
```sh
kubectl rollout undo deployment/<deployment-name>
```

In rollback, the deployment object creates another replica set and fills that.

## Summary of Commands

**Create a deployment from a definition file:**
```sh
kubectl create -f <deployment-definition.yml>
```

**Get the list of deployments:**
```sh
kubectl get deployments
```

**Apply changes to a deployment from a definition file:**
```sh
kubectl apply -f <deployment-definition.yml>
```

**Set a new image for a deployment:**
```sh
kubectl set image deployment/<deployment-name> nginx=nginx:1.9.1
```

**Check the status of a rollout:**
```sh
kubectl rollout status deployment/<deployment-name>
```

**View the rollout history of a deployment:**
```sh
kubectl rollout history deployment/<deployment-name>
```

**Undo the last rollout:**
```sh
kubectl rollout undo deployment/<deployment-name>
```

## Updating a Deployment

Here are some handy examples related to updating a Kubernetes Deployment:

Creating a deployment, checking the rollout status and history:

In the example below, we will first create a simple deployment and inspect the rollout status and the rollout history:

```sh
master $ kubectl create deployment nginx --image=nginx:1.16
deployment.apps/nginx created

master $ kubectl rollout status deployment nginx
Waiting for deployment "nginx" rollout to finish: 0 of 1 updated replica are available...
deployment "nginx" successfully rolled out

master $ kubectl rollout history deployment nginx
deployment.extensions/nginx
REVISION CHANGE-CAUSE
1     <none>
```

Using the --revision flag:

Here the revision 1 is the first version where the deployment was created.

You can check the status of each revision individually by using the --revision flag:

```sh
master $ kubectl rollout history deployment nginx --revision=1
deployment.extensions/nginx with revision #1
 
Pod Template:
 Labels:    app=nginx    pod-template-hash=6454457cdb
 Containers:  nginx:  Image:   nginx:1.16
  Port:    <none>
  Host Port: <none>
  Environment:    <none>
  Mounts:   <none>
 Volumes:   <none>
master $
```