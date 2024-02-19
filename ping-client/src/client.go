package main

import (
	"fmt"
	"math/rand"
	"net"
	"net/http"
	"os"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	log "github.com/sirupsen/logrus"
)

var (
	pingCounter = prometheus.NewCounter(prometheus.CounterOpts{
		Name: "pings_total",
		Help: "Total number of ping messages sent.",
	})
)

func main() {
	host := "ping-pong-server" // Change this to your desired host
	port := "5000"             // Change this to your desired port
	metricsHost, _ := os.Hostname()
	metricsPort := "8000"
	intervalMin := 5  // Minimum interval in seconds
	intervalMax := 15 // Maximum interval in seconds
	log.SetLevel(log.DebugLevel)

	http.Handle("/metrics", promhttp.Handler())
	prometheus.MustRegister(pingCounter)
	go func() {
		log.Info("Start metrics handler")
		metricsEndpoint := metricsHost + ":" + metricsPort
		log.Debugf("Listening on %s", metricsEndpoint)
		err := http.ListenAndServe(metricsEndpoint, nil)
		if err == nil {
			log.Error("Failed to start metrics handler")
			return
		}

	}()

	log.Println("Start sending Pings")
	for {
		sendMessage(host, port)
		sleepTime := rand.Intn(intervalMax-intervalMin) + intervalMin
		time.Sleep(time.Duration(sleepTime) * time.Second)
	}
}

func sendMessage(host, port string) {
	message := "ping"
	addr := fmt.Sprintf("%s:%s", host, port)
	conn, err := net.Dial("tcp", addr)
	if err != nil {
		log.Errorf("Failed to connect to %s: %v\n", addr, err)
		return
	}
	defer conn.Close()

	_, err = conn.Write([]byte(message))
	if err != nil {
		log.Errorf("Failed to send message to %s: %v\n", addr, err)
		return
	}
	pingCounter.Inc()
	log.Debugf("Sent '%s' to %s\n", message, addr)

}
