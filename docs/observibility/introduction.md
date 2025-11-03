# Introduction


## Overview of Observability Components

Observability in modern infrastructure relies on a set of specialized tools, each designed to collect, store, and analyze different types of telemetry data. Below is a broad overview of key components and their roles:

### Metrics Databases

- **Prometheus**: An open-source system monitoring and alerting toolkit. Prometheus is widely used for collecting and storing time-series data (metrics) from applications and infrastructure. It excels at querying and alerting on metrics data.
- **Mimir**: A scalable, multi-tenant time-series database built by Grafana Labs. Mimir is designed to handle large-scale metric workloads and is often used as a backend for Prometheus-compatible queries.

### Logs Database

- **Loki**: A horizontally scalable, highly available log aggregation system inspired by Prometheus. Loki stores and indexes logs, making it easy to correlate logs with metrics and traces for troubleshooting.

### Tracing Database

- **Tempo**: A distributed tracing backend that stores and queries trace data. Tempo helps track requests as they flow through microservices, making it easier to identify bottlenecks and latency issues.

### Profiling Database

- **Pyroscope**: A continuous profiling platform that collects and stores profiling data (such as CPU and memory usage) over time. Continuous profiling helps developers understand resource consumption and optimize application performance.

### Instrumentation

Instrumentation is the process of adding code or agents to applications and infrastructure to collect telemetry data. There are several approaches:
1. **Source Instrumentation**: Involves modifying application code using SDKs or libraries to emit telemetry data, which is then sent to an OpenTelemetry backend.
2. **Binary Instrumentation**: Uses agents (such as the OpenTelemetry Collector or Grafana Alloy) that attach to running applications to collect telemetry without modifying source code.
3. **External Instrumentation**: Tools like Grafana Beyla use eBPF (extended Berkeley Packet Filter) to automatically instrument applications at the kernel level, requiring no code changes.

### OpenTelemetry Concepts

- **OTLP (OpenTelemetry Protocol)**: A standard protocol for transmitting telemetry data (metrics, logs, traces) between components.
- **Collectors**: Services (like OpenTelemetry Collector or Grafana Alloy) that receive, process, and export telemetry data from various sources.
- **Signals**: The three primary types of telemetry data—metrics, logs, and traces.
- **Context and Semantic Conventions**: Standards for propagating context across services and defining consistent naming for telemetry data.

### Additional Tools

- **k6**: An open-source tool for load testing and performance monitoring of applications.
- **Grafana**: A visualization platform for querying, analyzing, and displaying metrics, logs, and traces from various data sources.
- **Incident Response**: Tools like Alertmanager and Grafana OnCall help manage alerts and coordinate incident response workflows.

These components together form the foundation of a robust observability stack, enabling teams to monitor, troubleshoot, and optimize their systems effectively.