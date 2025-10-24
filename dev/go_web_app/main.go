package main

import (
	"fmt"
	"net/http"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	name := os.Getenv("APP_NAME")
	if name == "" {
		name = "Simple Go App"
	}
	fmt.Fprintf(w, "Hello from %s! 🚀", name)
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Server running on port 8181")
	http.ListenAndServe(":8181", nil)
}
