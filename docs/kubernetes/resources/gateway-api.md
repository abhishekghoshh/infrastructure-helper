# Gateway API

## Youtube
- [Mastering Kubernetes: Service and Network APIs (Service, Ingress, GatewayAPI)](https://www.youtube.com/watch?v=-1H0BeN9hIk)
- [GATEWAY API - Ingress is DEAD! Long live Ingress](https://www.youtube.com/watch?v=5D4Eh5XBLxU)
- [Gateway API Explained: The Future of Kubernetes Networking](https://www.youtube.com/watch?v=xaZ87iSvMAI)



## Refferences
- [From kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/gateway/)
- [Gateway API documentation](https://gateway-api.sigs.k8s.io/)
- [From google cloud](https://cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)
- [Gateway API v1.2: WebSockets, Timeouts, Retries, and More](https://kubernetes.io/blog/2024/11/21/gateway-api-v1-2/)

## Premise

To be generally available, web applications running on Kubernetes need to be exposed outside the cluster. This can be achieved in several ways. The simplest method to expose a service or API endpoint outside a Kubernetes cluster is to assign a service type of NodePort. The drawback of this approach is that the service runs on a non-standard port number. Additionally, each cluster has a limited number of ports assigned to its NodePort pool. These limitations can be overcome by using either the Ingress API or the Gateway API. While the Ingress API has been widely adopted in the Kubernetes world, it has its own drawbacks. Notably, a strong reliance on annotations in Ingress manifests makes the Ingress API inflexible and difficult to write generic templates for in Helm charts. The Gateway API overcomes these drawbacks by providing a generic, easy-to-templatize, and extensible way to define resources that provide an ingress of traffic to Kubernetes-hosted endpoints. In the following sections, we will compare the two approaches.

## Ingress API

HTTP and HTTPS network services can be exposed outside the Kubernetes cluster using Ingress resources, provided as part of the Ingress API. Traffic is routed using rules defined within the Ingress resource. Before Ingress resources can be defined, the cluster must have at least one Ingress Controller running. This Ingress Controller service is typically exposed using a LoadBalancer service type.

The Ingress API is widely adopted by Kubernetes users and well-supported by vendors with many implementations (Ingress controllers) available.

Ingress API resource organization

![Ingress Workflow](../assets/ingress-workflow.svg)

## Limitations of the Ingress API

- **Limited features**: The Ingress API only supports TLS termination and simple content-based request routing of HTTP traffic.
- **Reliance on annotations for extensibility**: The annotations approach to extensibility leads to limited portability as every implementation has its own supported extensions that may not translate to any other implementation.
- **Insufficient permission model**: The Ingress API is not well-suited for multi-team clusters with shared load-balancing infrastructure.

## Gateway API

The Gateway API is an official Kubernetes project being worked on by the Kubernetes Network SIG, representing the next generation of Ingress, Load balancing, and Service Mesh APIs. It focuses on L4 and L7 routing within Kubernetes. It has been designed from the outset to be generic, expressive, and role-oriented.

## Features of the Gateway API

The following design goals drive the concepts of Gateway API. These demonstrate how Gateway aims to improve upon current standards like Ingress.

- **Role-oriented**: Gateway is composed of API resources that model organizational roles that use and configure Kubernetes service networking.
- **Portable**: This isn't an improvement but rather something that should stay the same. Just as Ingress is a universal specification with numerous implementations, Gateway API is designed to be a portable specification supported by many implementations.
- **Expressive**: Gateway API resources support core functionality for things like header-based matching, traffic weighting, and other capabilities that were only possible in Ingress through custom annotations.
- **Extensible**: Gateway API allows for custom resources to be linked at various layers of the API. This makes granular customization possible at the appropriate places within the API structure.

## Gateway API Resource Model

**GatewayClass** - GatewayClass is a cluster-scoped resource that defines a set of Gateways that share a common configuration and behavior. A cluster needs to have at least one GatewayClass, which is handled by a Gateway Controller, similar to an Ingress Controller. A Gateway Controller may handle more than one GatewayClass.

**Gateway** - A Gateway describes how traffic can be translated within a cluster. As is evident from the name, it acts as a gateway between traffic outside the cluster and traffic within the cluster.

**Route Resources** - Route resources define protocol-specific rules for mapping requests from a Gateway to Kubernetes Services. Route resources included in the API currently are:

- **HTTPRoute** - Used for multiplexing HTTP or terminated HTTPS connections.
- **GRPCRoute** - Used for idiomatically routing gRPC traffic.
- **TLSRoute (experimental)** - Used for multiplexing TLS connections, discriminated via SNI.
- **TCPRoute and UDPRoute (experimental)** - used for mapping one or more TCP or UDP ports to a single backend. These may be used to terminate TLS, where appropriate.

![Gateway Resource model](../assets/gateway-resource-model.png)

## Examples

The example snippets below illustrate the differences between the YAML manifests used to create Ingress API and Gateway API resources. Both examples create traffic routes to the same Service resource.

Installation of an Ingress Controller and Gateway Controller are outside the scope of this document.

### Ingress API

The following snippets applied in order will create an IngressClass resource which will then be referenced by the Ingress resource created next.

IngressClass
```yaml
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  labels:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
    app.kubernetes.io/version: 1.12.0-beta.0
  name: nginx
spec:
  controller: k8s.io/ingress-nginx
```

Ingress
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: science-portal-ingress
  namespace: skaha-system
  annotations:
    spec.ingressClassName: nginx
spec:
  ingressClassName: nginx
  rules:
  - host: canfar.e4r.internal
    http:
      paths:
      - path: /science-portal
        pathType: Prefix
        backend:
          service:
            name: science-portal-tomcat-svc
            port:
              number: 8080
```

### Gateway API

The following snippets applied in order will first create a GatewayClass resource, which will then be referenced by a Gateway resource created next. Finally, the Gateway resource will be referenced by an HTTPRoute resource which will be created at the last step.

GatewayClass
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: envoy-gateway-class
spec:
  controllerName: gateway.envoyproxy.io/gatewayclass-controller
```

Gateway
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: envoy-canfar-gateway
spec:
  gatewayClassName: envoy-gateway-class
  listeners:
  - name: canfar-gateway-http-envoy
    protocol: HTTP
    port: 80
    allowedRoutes:
      namespaces:
        from: All
  - name: canfar-gateway-https-envoy
    protocol: HTTPS
    port: 443
    allowedRoutes:
      namespaces:
        from: All
    hostname: "canfar.e4r.internal"
    tls:
      certificateRefs:
      - kind: Secret
        group: ""
        name: canfar-gateway-tls
```

HTTPRoute
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: envoy-canfar-gateway-httproutes
  namespace: skaha-system
spec:
  hostnames:
  - "canfar.e4r.internal"
  parentRefs:
  - name: envoy-canfar-gateway
    namespace: default
  rules:
  - backendRefs:
    - name: science-portal-tomcat-svc
      port: 8080
    matches:
    - path:
        type: PathPrefix
        value: /science-portal
```

### Example for Canfar deployment using Gateway API

The following snippet is an example to deploy Canfar using Gateway API.

Canfar Deployment using Gateway API
```yaml
# STEP 1: Create a GatewayClass with a Gateway Controller of your choice.
# A GatewayClass helps to define a set of Gateway resources that use the same controller.
# This example uses the Envoy Gateway Controller. The controller name has to be set appropriately for other Gateway Controllers.
 
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: envoy-gateway-class
spec:
  controllerName: gateway.envoyproxy.io/gatewayclass-controller
  # The controllerName refers to the controller that will be using to manage Gateways of this class
 
---
# STEP 2: Create a Gateway for Canfar and attach the GatewayClass created in STEP 1.
# A Gateway helps to expose services and linked to a specific GatewayClass.
 
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: envoy-canfar-gateway
spec:
  gatewayClassName: envoy-gateway-class
  # The Gateway is associated with the GatewayClass created earlier.
  listeners:
  - name: canfar-gateway-http-envoy
    protocol: HTTP
    port: 80
    allowedRoutes:
      namespaces:
        from: All
    # This listener will accept HTTP traffic on port 80 from any namespace.
  - name: canfar-gateway-https-envoy
    protocol: HTTPS
    port: 443
    allowedRoutes:
      namespaces:
        from: All
    # This listener will accept HTTPS traffic on port 443 from any namespace.
    hostname: "canfar.e4r.internal"
    # Define a hostname for the gateway.
    tls:
      certificateRefs:
        - kind: Secret
          group: ""
          name: canfar-gateway-tls
        # The TLS configuration references a Secret containing the TLS certificate.
 
---
# STEP 3: Create an HTTPRoute for services in Canfar and attach it to the Gateway created in STEP 2.
# HTTPRoute defines routing rules based on HTTP paths, which direct traffic to backend services.
 
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: envoy-canfar-gateway-httproutes
  namespace: skaha-system
spec:
  hostnames:
    - "canfar.e4r.internal"
    # HTTPRoute applies to traffic matching this hostname.
  parentRefs:
    - name: envoy-canfar-gateway
      namespace: default
    # This HTTPRoute is attached to the 'envoy-canfar-gateway' Gateway defined earlier.
  rules:
    # Define routing rules for various paths
    - backendRefs:
        - name: gms
          port: 8080
      matches:
        - path:
            type: PathPrefix
            value: /gms
    - backendRefs:
        - name: reg
          port: 8080
      matches:
        - path:
            type: PathPrefix
            value: /reg
    - backendRefs:
        - name: science-portal-tomcat-svc
          port: 8080
      matches:
        - path:
            type: PathPrefix
            value: /science-portal
    - backendRefs:
        - name: skaha-tomcat-svc
          port: 8080
      matches:
        - path:
            type: PathPrefix
            value: /skaha
 
---
# STEP 4: Create a Gateway for Harbor and attach the GatewayClass created in STEP 1.
# A second Gateway exposing Harbor services, similar to the Canfar Gateway.
 
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: envoy-harbor-gateway
spec:
  gatewayClassName: envoy-gateway-class
  # The same GatewayClass is used for Harbor.
  listeners:
  - name: harbor-gateway-http-envoy
    protocol: HTTP
    port: 80
    allowedRoutes:
      namespaces:
        from: All
    # This listener will accept HTTP traffic on port 80 from any namespace.
 
  - name: harbor-gateway-https-envoy
    protocol: HTTPS
    port: 443
    allowedRoutes:
      namespaces:
        from: All
    # This listener will accept HTTPS traffic on port 443 from any namespace.
    hostname: "harbor.e4r.internal"
    # Define a hostname for the Harbor gateway.
    tls:
      certificateRefs:
        - kind: Secret
          group: ""
          name: harbor-gateway-tls
        # The TLS configuration references a Secret containing the TLS certificate.
 
---
# STEP 5: Create an HTTPRoute for the services in Harbor and attach it to the Gateway created in STEP 4.
# Similar to the Canfar HTTPRoute, this defines routing rules for Harbor services.
 
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: harbor-httproutes
  namespace: harbor
spec:
  hostnames:
    - "harbor.e4r.internal"
    # HTTPRoute applies to traffic matching this hostname.
  parentRefs:
    - name: envoy-harbor-gateway
      namespace: default
    # This HTTPRoute is attached to the 'envoy-harbor-gateway' Gateway defined earlier.
  rules:
    # Define routing rules for various paths within Harbor
    - backendRefs:
        - name: harbor-portal
          port: 80
      matches:
        - path:
            type: PathPrefix
            value: /
    - backendRefs:
        - name: harbor-core
          port: 80
      matches:
        - path:
            type: PathPrefix
            value: /c
    - backendRefs:
        - name: harbor-core
          port: 80
      matches:
        - path:
            type: PathPrefix
            value: /chartrepo
    - backendRefs:
        - name: harbor-core
          port: 80
      matches:
        - path:
            type: PathPrefix
            value: /v2
    - backendRefs:
        - name: harbor-core
          port: 80
      matches:
        - path:
            type: PathPrefix
            value: /service
    - backendRefs:
        - name: harbor-core
          port: 80
      matches:
        - path:
            type: PathPrefix
            value: /api
```