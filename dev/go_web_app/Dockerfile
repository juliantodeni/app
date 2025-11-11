# Stage 1: Build the Go binary
FROM golang:1.25 AS builder
WORKDIR /app
COPY . .
# RUN go mod init myapp || true
# RUN go mod tidy
RUN go mod download
#RUN go build -o server main.go

# These args come automatically from Buildx
ARG TARGETOS
ARG TARGETARCH

# Build for the correct architecture
RUN CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o server main.go

# Stage 2: Run the binary
FROM alpine:3.20
WORKDIR /app
COPY --from=builder /app/server .
ENV APP_NAME="Dockerized Go App"
EXPOSE 8181
CMD ["./server"]
