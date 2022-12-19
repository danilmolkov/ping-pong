from prometheus_client import start_http_server, Summary, Counter

# Create a metric to track time spent and requests made.
PINGS_TOTAL = Counter('pings_total' , 'Total Pings')

def startMetricHandle():
    # Start up the server to expose the metrics.
    start_http_server(8000)
    return True