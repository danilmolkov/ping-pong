from prometheus_client import start_http_server, Counter

# Create a metric to track time spent and requests made.
PONGS_TOTAL = Counter('pongs_total' , 'Total Pongs' , ['address'])
NOT_PINGS_TOTAL = Counter('not_pings_received_total', 'Not a ping received', ['address'])

def startMetricHandle():
    # Start up the server to expose the metrics.
    start_http_server(8000)
    return True