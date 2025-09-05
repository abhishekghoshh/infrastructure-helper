import requests
import time
import random
import threading

# URLs to test
endpoints = {
    "/hello": {"concurrent_threads": 20, "request_count": 100},
    "/delayed_hello": {"concurrent_threads": 50, "request_count": 200},
}

def make_request(url):
    """Function to make a single HTTP GET request and print the result."""
    try:
        response = requests.get(url, timeout=5)
        print(f"Request to {url}: Status {response.status_code}, Latency {response.elapsed.total_seconds():.4f}s")
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")

def run_test(endpoint_url, concurrent_threads, request_count):
    """
    Runs a load test to a specific endpoint.

    Args:
        endpoint_url (str): The URL to send requests to.
        concurrent_threads (int): The number of threads to use.
        request_count (int): The total number of requests to send.
    """
    print(f"\nStarting load test for {endpoint_url} with {concurrent_threads} threads and {request_count} requests...")
    threads = []
    for _ in range(concurrent_threads):
        thread = threading.Thread(target=make_requests_in_thread, args=(endpoint_url, request_count // concurrent_threads))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(f"Load test for {endpoint_url} finished.")

def make_requests_in_thread(url, num_requests):
    """A thread's task to make a specified number of requests."""
    for _ in range(num_requests):
        make_request(url)
        # Add a small, random delay between requests to simulate real-world traffic patterns
        time.sleep(random.uniform(0.01, 0.1))

if __name__ == "__main__":
    base_url = "http://go-api:8080"
    for endpoint, params in endpoints.items():
        url = f"{base_url}{endpoint}"
        run_test(url, params["concurrent_threads"], params["request_count"])
