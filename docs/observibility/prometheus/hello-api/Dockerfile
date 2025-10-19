# Use a multi-stage build to create a small final image.

# Stage 1: Build the Go application
FROM golang:1.25-alpine AS builder

WORKDIR /app

# Copy go mod and sum files and download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the application source code
COPY . .

# Build the Go application binary
# RUN CGO_ENABLED=0 go build -o /go-api-server
RUN go build -o /go-api-server


# Stage 2: Create the final production image
FROM alpine:3.18

# Install ca-certificates to enable HTTPS connections
RUN apk add --no-cache ca-certificates

# Set the working directory
WORKDIR /app

# Copy the compiled binary from the builder stage
COPY --from=builder /go-api-server /app/go-api-server

# Expose the port the application runs on
EXPOSE 8080

# The command to run the application
CMD ["/app/go-api-server"]
