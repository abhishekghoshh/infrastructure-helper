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
	// Create a new counter vector for total HTTP requests.
	httpRequestsTotal = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "go_api_http_requests_total",
			Help: "Total number of HTTP requests.",
		},
		[]string{"endpoint"},
	)

	// Create a new summary vector for request duration.
	// A summary calculates quantiles and total sum and count.
	httpRequestDuration = prometheus.NewSummaryVec(
		prometheus.SummaryOpts{
			Name:       "go_api_http_duration_seconds",
			Help:       "HTTP request duration in seconds.",
			Objectives: map[float64]float64{0.5: 0.05, 0.9: 0.01, 0.99: 0.001},
		},
		[]string{"endpoint"},
	)

	// Create a new gauge for active connections.
	// Gauges are used for values that can go up and down.
	activeConnections = prometheus.NewGauge(
		prometheus.GaugeOpts{
			Name: "go_api_active_connections",
			Help: "Number of active HTTP connections.",
		},
	)
)

// Register the metrics with the Prometheus default registry.
func init() {
	prometheus.MustRegister(httpRequestsTotal)
	prometheus.MustRegister(httpRequestDuration)
	prometheus.MustRegister(activeConnections)
}

// Logging and metrics middleware
func promMiddleware(next http.Handler, endpoint string) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		activeConnections.Inc() // Increment active connections on request start
		httpRequestsTotal.WithLabelValues(endpoint).Inc()
		log.Printf("Received request for endpoint %s", endpoint)

		next.ServeHTTP(w, r)

		duration := time.Since(start).Seconds()
		httpRequestDuration.WithLabelValues(endpoint).Observe(duration)
		activeConnections.Dec() // Decrement active connections on request completion
	})
}

// Handler for the /hello endpoint
func helloHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Hello, world!"))
}

// Handler for the /delayed_hello endpoint
func delayedHelloHandler(w http.ResponseWriter, r *http.Request) {
	// Simulate a random delay between 500ms and 2000ms
	delay := time.Duration(rand.Intn(1500)+500) * time.Millisecond
	time.Sleep(delay)

	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Delayed hello!"))
}

func main() {
	// Register HTTP handlers with Prometheus middleware
	http.Handle("/hello", promMiddleware(http.HandlerFunc(helloHandler), "hello"))
	http.Handle("/delayed_hello", promMiddleware(http.HandlerFunc(delayedHelloHandler), "delayed_hello"))
	http.Handle("/metrics", promhttp.Handler())

	log.Println("Go API server started on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatalf("could not start server: %v\n", err)
	}
}
