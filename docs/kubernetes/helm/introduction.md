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