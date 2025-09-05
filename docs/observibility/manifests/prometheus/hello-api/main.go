package main

import (
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	// A Prometheus Counter to track the number of requests made to the API.
	httpRequestsTotal = promauto.NewCounter(prometheus.CounterOpts{
		Name: "go_api_http_requests_total",
		Help: "Total number of HTTP requests made to the Go API.",
	})
	// A Prometheus Gauge to track a custom metric, which we'll update on each request.
	activeConnections = promauto.NewGauge(prometheus.GaugeOpts{
		Name: "go_api_active_connections",
		Help: "The number of active connections to the Go API.",
	})
	// A Prometheus Histogram to track request duration with different buckets.
	httpDuration = promauto.NewHistogramVec(prometheus.HistogramOpts{
		Name:    "go_api_http_duration_seconds",
		Help:    "Duration of HTTP requests to the Go API.",
		Buckets: prometheus.DefBuckets,
	}, []string{"endpoint"})
)

// helloHandler is a simple handler that increments our metrics.
func helloHandler(w http.ResponseWriter, r *http.Request) {
	// Start a timer for the request duration
	timer := prometheus.NewTimer(httpDuration.WithLabelValues("/hello"))
	defer timer.ObserveDuration()

	// Increment the total requests counter.
	httpRequestsTotal.Inc()

	// Set the gauge to a random value to demonstrate its use.
	// In a real application, this would be a real measurement.
	activeConnections.Set(float64(httpRequestsTotal) * 0.5)

	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Hello, World! Metrics updated."))
}

// delayedHelloHandler is a handler that simulates a variable delay.
func delayedHelloHandler(w http.ResponseWriter, r *http.Request) {
	// Start a timer for the request duration
	timer := prometheus.NewTimer(httpDuration.WithLabelValues("/delayed_hello"))
	defer timer.ObserveDuration()

	// Simulate a random delay between 50ms and 500ms
	delay := time.Duration(rand.Intn(450)+50) * time.Millisecond
	time.Sleep(delay)

	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Hello, World! (Delayed)"))
}

func main() {
	// Register the Prometheus metrics handler.
	http.Handle("/metrics", promhttp.Handler())

	// Register a simple endpoint for demonstration purposes.
	http.HandleFunc("/hello", helloHandler)
	http.HandleFunc("/delayed_hello", delayedHelloHandler)

	log.Println("Go API server started on :8080")
	// Start the HTTP server.
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatalf("could not start server: %v", err)
	}
}
