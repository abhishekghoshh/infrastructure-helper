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
