from os import error
import requests
import unittest
import time

def get_prometheus_metric(promQl):
    prometheus_url = 'http://prometheus:9090'
    query = f'{prometheus_url}/api/v1/query?query={promQl}'

    try:
        response = requests.get(query)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'success':
            # Extracting the metric value from the response
            result = data['data']['result']
            # Check if the result is not empty and contains 'metric' and 'value' keys
            if result and 'metric' in result[0] and 'value' in result[0]:
                metric_value = result[0]['value'][1]
                return metric_value
            else:
                raise Exception("Metric value not found in the response.")
        else:
                raise Exception("Metric value not found in the response.")
    except requests.exceptions.RequestException as e:
        error(f"Error fetching metric from Prometheus: {e}")
    except Exception as e:
        error(f"Error fetching metric from Prometheus: {e}")

class PingPongTesting(unittest.TestCase):

    def test_pings_almost_equals_pongs(self):
        self.assertAlmostEqual(int(get_prometheus_metric('sum(pings_total)')),int(get_prometheus_metric('sum(pongs_total)')), delta=10)
    def test_pings_and_pongs_count_equals_replicas(self):
        self.assertEqual(int(get_prometheus_metric('count(pings_total)')), int(get_prometheus_metric('count(pongs_total)')))
    def test_not_pings_received(self):
        self.assertTrue(int(get_prometheus_metric('sum(not_pings_received_total)')) != 0)


if __name__ == '__main__':
    sleepTime = 100
    print(f'Sleep {sleepTime} seconds..')
    time.sleep(sleepTime)
    print(f'Start testing..')
    unittest.main()