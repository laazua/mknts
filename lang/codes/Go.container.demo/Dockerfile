# Use Alpine Linux as the base image
FROM alpine:latest


# Set up a working directory
WORKDIR /app


# Copy the binaries from the build environment to the Alpine image
COPY . /app/


# Expose the port on which the application is running (if needed)
EXPOSE 9999


# Run the executable file
CMD ["./test"]




# Command line run: CGO_ENABLED=0 GOOS=linux go21 build -a -installsuffix cgo -o test .
## Use Alpine Linux as the base image
FROM alpine:latest


# Set up a working directory
WORKDIR /app


# Copy the binaries from the build environment to the Alpine image
COPY . /app/


# Expose the port on which the application is running (if needed)
EXPOSE 9999


# Run the executable file
CMD ["./test"]




# Command line run: CGO_ENABLED=0 GOOS=linux go21 build -a -installsuffix cgo -o test .
#    -ldflags '-extldflags "-static"' 
