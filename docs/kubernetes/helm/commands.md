
## Applying a Helm Chart

To manage Helm repositories, use the following commands:

List existing repositories:

```sh
helm repo list
```

Add a new repository:

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

List repositories again to confirm addition:

```sh
helm repo list
```

Remove a repository:

```sh
helm repo remove bitnami
```

Add the repository back:

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

To search the repository, use the following commands:

Search for a specific chart:

```sh
helm search repo mysql
```

Search for charts related to a keyword:

```sh
helm search repo database
```

Search for charts with version information:

```sh
helm search repo database --versions
```

Updating the local repositories
```sh
helm repo update
```

To apply a Helm chart, use the following command:

```sh
helm install release-name my-chart -f values.yaml
```

To specify a namespace:

```sh
helm install release-name my-chart -f values.yaml -n namespace
```

To use a custom values file:

```sh
helm install release-name my-chart -f custom-values.yaml -n namespace
```

To install a chart from the current directory:

```sh
helm install release-name . -f <values-path>
```

## Upgrading an Existing Release

To upgrade an existing release, use the following command:

```sh
helm upgrade release-name my-chart -f values.yaml
```

To specify a namespace:

```sh
helm upgrade release-name my-chart -f values.yaml -n namespace
```

To use a custom values file:

```sh
helm upgrade release-name my-chart -f custom-values.yaml -n namespace
```

To resuse the existing values of the previous revision
```sh
helm upgrade release-name my-chart --reuse-values
```



To upgrade a chart from the current directory:

```sh
helm upgrade release-name . -f <values-path>
```

## Checking Helm Releases

To check all the Helm releases, use the following command:

```sh
helm ls
```

To specify a namespace:

```sh
helm ls -n namespace
```

To list all releases across all namespaces:

```sh
helm ls -A
```

## Uninstalling a Release

To uninstall a release, use the following command:

```sh
helm uninstall release-name
```

To specify a namespace:

```sh
helm uninstall release-name -n namespace
```

## Helm Templating Debugging and Dry Run

Helm provides debugging options to inspect how templates are rendered before actual deployment.

**The key parameters are:**

- **`--dry-run`**: Simulates the deployment without applying changes.
- **`--debug`**: Provides detailed output, including rendered templates and values.

### Simulating an Installation with Debugging

To see how Helm renders the templates without deploying:

```sh
helm install my-release my-chart --dry-run --debug
```

### Checking How an Upgrade Would Modify an Existing Release

To check how an upgrade would modify an existing release:

```sh
helm upgrade my-release my-chart --dry-run --debug
```

### Rendering Templates Without Applying

To render templates without applying:

```sh
helm template my-release my-chart --debug
```

To compile the output to a file:

```sh
helm install --dry-run --debug <chart-name> . >> compiled-output.yaml
```

## Additional Helm Commands

To install a chart from a repository:

```sh
helm install apache bitnami/apache --namespace=web
```

To upgrade a chart from a repository:

```sh
helm upgrade apache bitnami/apache --namespace=web
```

To roll back to a previous revision:

```sh
helm rollback apache 1 --namespace=web
```

To uninstall a release:

```sh
helm uninstall apache
```

helm stores the release informations in the secret. Helm also delete the release history automatically whenever we uninstall the charts. To maintain the history we have to mention `--keep-history` flag while uninstalling

```sh
helm uninstall chart-name --keep-history
```

