package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

// Creates a simple http server with timeout support
// call it with: curl "http://localhost:8000/hello"

func Hello(w http.ResponseWriter, r *http.Request) {
	log.Println("called /hello")

	if r.Method != http.MethodGet {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	fmt.Fprintf(w, "Hello!\n")
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/hello", Hello)

	server := http.Server{
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
		Addr:         ":8000",
		Handler:      mux,
	}

	log.Println("listening on port 8000\n")
	if err := server.ListenAndServe(); err != nil {
		log.Fatalln(err)
	}
}
