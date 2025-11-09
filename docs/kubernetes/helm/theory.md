# Helm short theory

## What is Helm?

**It is a Kubernetes Package Manager.** <br>
Helm is a tool that simplifies the deployment and management of applications on Kubernetes, functioning as a package manager. It uses "charts," which are pre-configured packages of Kubernetes resources, to enable users to deploy applications with a single command, ensuring consistency and reducing errors. Helm can create new charts, package them into chart archive files, interact with chart repositories, and manage the release cycle of charts installed with Helm.

## Main Components

- **Helm Client:**
    * The Helm client is a command-line interface (CLI) for end users that can be installed on any system.
    * It is responsible for local chart development, managing repositories and releases, interfacing with the Helm library, sending charts to be installed, and requesting upgrades or uninstallations.

- **Charts:**
    * Charts are Helm's package format.
    * A chart is a bundle of information necessary to create an instance of a Kubernetes application.
    * Charts contain YAML files with metadata and templates that are rendered into Kubernetes manifest files.
    * The `Chart.yaml` file defines the application metadata, such as name, version, and dependencies.

- **Repositories:**
    * Repositories are storage locations where Helm charts are stored and shared.
    * They allow teams to share charts of various applications.

- **Releases:**
    * A release is a running instance of a chart, combined with a specific configuration.
    * It represents a chart deployed into an environment, and Helm manages multiple versions of releases across different environments, including installations, upgrades, and rollbacks.

- **Helm Library:**
    * The Helm library provides the logic for executing Helm operations.
    * It interfaces with the Kubernetes API server to combine a chart and configuration to build a release.
    * It installs charts, and manages upgrades and uninstallations.

- **Revision History and Rollbacks:**
    * Helm maintains a history of all releases, allowing users to roll back to previous versions if needed.
    * Each upgrade or installation creates a new revision.
    * Rollbacks can be performed to revert to a specific revision.

## Why Should We Use Helm?

- **Simplicity:** Helm simplifies the deployment and management of Kubernetes applications by providing a single command to deploy complex applications. This reduces the learning curve and makes it easier for teams to manage their applications.

- **Revision History:** Helm maintains a history of all releases, allowing easy rollbacks to previous versions. This is particularly useful for recovering from failed deployments or reverting to a known good state.

- **Dynamic Configuration:** Helm supports dynamic configuration through values files, enabling users to customize their deployments without modifying the underlying charts. This allows for flexible and reusable configurations.

- **Consistency:** Helm ensures consistent deployments across environments by using pre-configured charts. This reduces the risk of human error and ensures that applications are deployed in a predictable manner.

- **Intelligent Deployments:** Helm manages the order in which resources are created, ensuring that dependencies are resolved correctly. This prevents issues that can arise from resources being created in the wrong order.

- **Lifecycle Hooks:** Helm supports lifecycle hooks, allowing users to execute custom actions at different points during the deployment process. This can be used to perform tasks such as database migrations or configuration updates.

- **Security:** Helm allows downloading secured charts from central repositories, ensuring that only trusted and verified charts are used. This enhances the security of the deployment process.

## Helm Templating Engine

Helm uses a **templating engine** to dynamically generate Kubernetes manifests. It allows developers to define templates with placeholders that get replaced with actual values during deployment.

### Key Features

- Uses **Go templates** for defining Kubernetes resources.
- Supports **values.yaml** for injecting dynamic configurations.
- Enables **control structures** like loops (`range`) and conditionals (`if`).
- Allows reusability with **partials** and **functions**.

### Example

A basic **Deployment** template (`templates/deployment.yaml`):

```yaml
{% raw %}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-app
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: my-container
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
{% endraw %}
```

## Workflow of Helm

1. **Load the Chart and its Dependencies:**
    * Helm fetches the chart from the local directory or a remote repository.
    * It also fetches any dependencies specified in the `Chart.yaml` file.

2. **Parse the values.yaml:**
    * Helm reads the `values.yaml` file to get the configuration values.
    * These values can be overridden by passing custom values during the `helm install` or `helm upgrade` commands.

3. **Generate the YAML:**
    * Helm uses the templating engine to combine the chart templates with the values from `values.yaml`.
    * This generates the final Kubernetes manifest files.

4. **Parse the YAML to Kubernetes Objects and Validate:**
    * Helm parses the generated YAML files into Kubernetes objects.
    * It validates these objects to ensure they are correctly formatted and can be accepted by the Kubernetes API server.

5. **Generate YAML and Send to Kubernetes:**
    * Helm sends the validated Kubernetes objects to the Kubernetes API server.
    * The API server processes these objects and creates the corresponding resources in the cluster.


## Applying a Helm Chart

To manage Helm repositories, use the following commands:

**List existing repositories:**
```sh
helm repo list
```

**Create a new helm chart in your local directory with some preexisting files:**
```sh
helm create <chart-name>
```

**Add a new repository:**
```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

**List repositories again to confirm addition:**
```sh
helm repo list
```

**Remove a repository:**
```sh
helm repo remove bitnami
```

**Add the repository back:**
```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

To search the repository, use the following commands:

**Search for a specific chart:**
```sh
helm search repo mysql
```

**Search for charts related to a keyword:**
```sh
helm search repo database
```

**Search for charts with version information:**
```sh
helm search repo database --versions
```

**Updating the local repositories:**
```sh
helm repo update
```

To apply a Helm chart, use the following command:

**Install a Helm chart:**
```sh
helm install release-name my-chart -f values.yaml
```

**Specify a namespace:**
```sh
helm install release-name my-chart -f values.yaml -n namespace
```

**Use a custom values file:**
```sh
helm install release-name my-chart -f custom-values.yaml -n namespace
```

**Install a chart from the current directory:**
```sh
helm install release-name . -f <values-path>
```

## Upgrading an Existing Release

To upgrade an existing release, use the following command:

**Upgrade a Helm chart:**
```sh
helm upgrade release-name my-chart -f values.yaml
```

**Specify a namespace:**
```sh
helm upgrade release-name my-chart -f values.yaml -n namespace
```

**Use a custom values file:**
```sh
helm upgrade release-name my-chart -f custom-values.yaml -n namespace
```

**Reuse the existing values of the previous revision:**
```sh
helm upgrade release-name my-chart --reuse-values
```

**Upgrade a chart from the current directory:**
```sh
helm upgrade release-name . -f <values-path>
```


## Viewing Values of Charts

To see the values of a Helm chart, use the following commands:

**How to see which values we can configure in a helm chart:**
```sh
helm show values <chart-name>
```

**Get the custom values used during installation:**
```sh
helm get values <release-name>
```

**Get all values (default + custom) of a deployed chart:**
```sh
helm get values <release-name> --all
```

**Get values from a specific revision:**
```sh
helm get values <release-name> --revision <revision-number>
```

**Specify a namespace:**
```sh
helm get values <release-name> -n <namespace>
```

## Setting Values Inline

You can supply values to a Helm chart directly from the command line using the `--set` flag instead of using a values file.

**Supply inline values to helm chart using `--set` command:**
```sh
helm install release-name my-chart --set key1=value1,key2=value2
```

**Set nested values:**
```sh
helm install release-name my-chart --set image.tag=latest,service.port=8080
```

**Set array values:**
```sh
helm install release-name my-chart --set replicas=3 --set env[0].name=ENV_VAR --set env[0].value=production
```

**Combine with values file (inline values take precedence):**
```sh
helm install release-name my-chart -f values.yaml --set image.tag=v2.0.0
```

**Use with upgrade command:**
```sh
helm upgrade release-name my-chart --set image.tag=latest,replicas=5
```

## Checking Helm Releases

To check all the Helm releases, use the following command:

**List all Helm releases:**
```sh
helm ls
```

**Specify a namespace:**
```sh
helm ls -n namespace
```

**List all releases across all namespaces:**
```sh
helm ls -A
```

## Uninstalling a Release

To uninstall a release, use the following command:

**Uninstall a Helm release:**
```sh
helm uninstall release-name
```

**Specify a namespace:**
```sh
helm uninstall release-name -n namespace
```

## Helm Templating Debugging and Dry Run

Helm provides debugging options to inspect how templates are rendered before actual deployment.

**The key parameters are:**

- **`--dry-run`**: Simulates the deployment without applying changes.
- **`--debug`**: Provides detailed output, including rendered templates and values.

### Simulating an Installation with Debugging

**To see how Helm renders the templates without deploying:**
```sh
helm install my-release my-chart --dry-run --debug
```

### Checking How an Upgrade Would Modify an Existing Release

**To check how an upgrade would modify an existing release:**
```sh
helm upgrade my-release my-chart --dry-run --debug
```

### Rendering Templates Without Applying

**To render templates without applying:**
```sh
helm template my-release my-chart --debug
```

**To compile the output to a file:**
```sh
helm install --dry-run --debug <chart-name> . >> compiled-output.yaml
```

It generates all the templates without release information and it does not talk to the Kubernetes server, whereas the `--dry-run` talks to the kube server in order to validate the objects.
```sh
helm template <chart-name> -f <values.yaml-file>
```

## Additional Helm Commands

**To install a chart from a repository:**
```sh
helm install apache bitnami/apache --namespace=web
```

**To upgrade a chart from a repository:**
```sh
helm upgrade apache bitnami/apache --namespace=web
```

**To roll back to a previous revision:**
```sh
helm rollback apache 1 --namespace=web
```

**To uninstall a release:**
```sh
helm uninstall apache
```

Helm stores the release information in the secret. Helm also deletes the release history automatically whenever we uninstall the charts. To maintain the history we have to mention `--keep-history` flag while uninstalling.
```sh
helm uninstall chart-name --keep-history
```

**Get the release information from the stored secret:**
```sh
kubectl get secret sh.helm.release.v1.<chart-name>.<version-name> -o yaml
```

**Get the release notes of any installed charts:**
```sh
helm get notes <chart-name>
```

**Get all the values of any installed charts (but only the custom values):**
```sh
helm get values <chart-name>
```

**Get all the values of any installed charts (default + custom):**
```sh
helm get values <chart-name> --all
```

**Get all the values of any installed charts for a particular revision (2nd revision):**
```sh
helm get values <chart-name> --revision 2
```

**Get all the manifests of any installed charts of the current release:**
```sh
helm get manifest <chart-name>
```

**Get all the manifests of any installed charts of a particular revision:**
```sh
helm get manifest <chart-name> --revision 2
```

**Create a package of a Helm chart:**
It creates an index.yaml file that contains information about the chart package. </br>
If your directory contains more than one chart, then the index.yaml file will specify all packages inside it.</br>
```sh
helm package <chart-name>
```

**If You Are Inside the Chart Directory**
```sh
helm package .
```


**If You Are One Level Above the Chart Directory**
```sh
helm package ./todo-app-chart
```

**If the Chart is Somewhere Else**
```sh
helm package /Users/your-name/projects/my-helm-charts/todo-app-chart
```

**Combining with Output Directory**
```sh
# This packages the chart at './todo-app-chart'
# and puts the .tgz file into the './packages' directory
helm package ./todo-app-chart --destination ./packages
```



**To index the packages of a Helm chart:**
```sh
helm repo index .
```

**To publish the charts in a helm repository like nexus or github pages use this command**
```sh
helm repo add 
```


## Validating the charts

**Linting the helm chart:**
```sh
helm lint .
```

**Rendering templates to check syntax:**
```sh
helm template .
```

**Rendering templates with release name:**
```sh
helm template <release-name> .
```

**Dry run installation to validate against Kubernetes API:**
```sh
helm install <release-name> . --dry-run
```
