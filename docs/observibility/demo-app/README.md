# Prometheus, Grafana, and Go API Monitoring Stack

This project provides a complete, containerized environment for monitoring a simple Go REST API using **Prometheus** for metric collection and **Grafana** for visualization. It also includes a Python-based load tester to simulate traffic and generate metrics.

---

## Components

### 1. Go REST API (`go-rest-api`)

A simple Go application with two HTTP endpoints: `/hello` and `/delayed_hello`. It is instrumented with Prometheus client libraries to expose custom metrics.

**Metrics Used:**

- **`go_api_http_requests_total`**:  
	A Counter metric that increments each time an HTTP request is received. Useful for tracking the total number of requests served.

- **`go_api_active_connections`**:  
	A Gauge metric representing the number of currently active HTTP connections. Ideal for measuring current connections, memory usage, or queue size.

- **`go_api_http_duration_seconds`**:  
	A Summary metric measuring the duration of each HTTP request. Useful for calculating quantiles (e.g., p99, p95) and understanding request latency.

---

### 2. Prometheus

Prometheus is an open-source monitoring system that collects and stores metrics as time-series data. It works on a "pull" model, scraping metrics from configured targets (our Go API) at regular intervals.

- **`prometheus.yml`**:  
	The configuration file for Prometheus. It tells Prometheus where to find our Go API's `/metrics` endpoint and how often to scrape it.

---

### 3. Grafana

Grafana is an open-source data visualization and analytics platform. It connects to various data sources (like Prometheus) and allows you to create customizable dashboards.

- **`grafana-dashboard.json`**:  
	A pre-configured Grafana dashboard for our Go API metrics. Import this file into Grafana to get started quickly.

---

### 4. Load Tester

A simple Python script using the `requests` library to simulate traffic to our Go API. It makes concurrent requests to both the `/hello` and `/delayed_hello` endpoints to generate realistic load and populate the metrics in Prometheus.

---

## Getting Started

Follow these steps to set up and run the entire monitoring stack.

### Prerequisites

- Docker and Docker Compose installed on your machine.

---

### Step 1: Set up the Go API

Navigate to the `go-rest-api` directory and initialize the Go module:

```sh
cd go-rest-api
go mod init go-rest-api
go mod tidy
```

---

### Step 2: Run the Docker Compose Stack

From the root directory of the project, run:

```sh
docker-compose up -d --build
```

This command will:

- Build the Go API and Load Tester Docker images.
- Start Prometheus, Grafana, and both custom services.
- The load tester will immediately start sending requests to the Go API.

---

### Step 3: Access the Services

- **Go API**: [http://localhost:8080](http://localhost:8080)
- **Prometheus UI**: [http://localhost:9090](http://localhost:9090)  
	Check the "Targets" page to confirm that the go-api service is being scraped.
- **Grafana UI**: [http://localhost:3000](http://localhost:3000)  
	Default login: `admin` / `admin` (you will be prompted to change the password on first login).

---

### Step 4: Import the Grafana Dashboard

1. In Grafana, click the **Dashboards** icon on the left.
2. Click **New Dashboard → Import**.
3. Copy the entire content of the `grafana-dashboard.json` file and paste it into the "Import via panel json" text area.
4. Click **Load**.
5. On the next screen, select **Prometheus** from the dropdown menu.
6. Click **Import**.

You should now see a dashboard displaying your Go API metrics, populated by the running load tester.

---

## Go API Code Breakdown

This section explains the Go code in `main.go` to help you understand how the metrics are instrumented.

```go
package main

import (
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	httpRequestsTotal = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "go_api_http_requests_total",
			Help: "Total number of HTTP requests.",
		},
		[]string{"endpoint"},
	)

	httpRequestDuration = prometheus.NewSummaryVec(
		prometheus.SummaryOpts{
			Name:       "go_api_http_duration_seconds",
			Help:       "HTTP request duration in seconds.",
			Objectives: map[float64]float64{0.5: 0.05, 0.9: 0.01, 0.99: 0.001},
		},
		[]string{"endpoint"},
	)

	activeConnections = prometheus.NewGauge(
		prometheus.GaugeOpts{
			Name: "go_api_active_connections",
			Help: "Number of active HTTP connections.",
		},
	)
)

func init() {
	prometheus.MustRegister(httpRequestsTotal)
	prometheus.MustRegister(httpRequestDuration)
	prometheus.MustRegister(activeConnections)
}

func promMiddleware(next http.Handler, endpoint string) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		activeConnections.Inc()
		httpRequestsTotal.WithLabelValues(endpoint).Inc()
		log.Printf("Received request for endpoint %s", endpoint)

		next.ServeHTTP(w, r)

		duration := time.Since(start).Seconds()
		httpRequestDuration.WithLabelValues(endpoint).Observe(duration)
		activeConnections.Dec()
	})
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Hello, world!"))
}

func delayedHelloHandler(w http.ResponseWriter, r *http.Request) {
	delay := time.Duration(rand.Intn(1500)+500) * time.Millisecond
	time.Sleep(delay)

	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Delayed hello!"))
}

func main() {
	http.Handle("/hello", promMiddleware(http.HandlerFunc(helloHandler), "hello"))
	http.Handle("/delayed_hello", promMiddleware(http.HandlerFunc(delayedHelloHandler), "delayed_hello"))
	http.Handle("/metrics", promhttp.Handler())

	log.Println("Go API server started on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatalf("could not start server: %v\n", err)
	}
}
```

---

### Code Explanation

- **`package main`**: Declares the package as main, making it an executable program.
- **Imports**: Brings in packages for logging, random number generation, time, HTTP handling, and Prometheus client library.
- **Metric Variables**:  
	- `httpRequestsTotal`: CounterVec for total HTTP requests, labeled by endpoint.
	- `httpRequestDuration`: SummaryVec for request durations, labeled by endpoint.
	- `activeConnections`: Gauge for current active HTTP connections.
- **`init()`**: Registers metrics with Prometheus.
- **`promMiddleware`**: Middleware to instrument handlers with metrics.
- **Handlers**:  
	- `helloHandler`: Returns a simple string.
	- `delayedHelloHandler`: Returns a string after a random delay (500ms-2000ms).
- **`main()`**: Registers handlers and starts the HTTP server on port 8080.

---

You now have a full monitoring stack for a Go API, complete with metrics collection, visualization, and load testing.
