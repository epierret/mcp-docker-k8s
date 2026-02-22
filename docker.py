import docker

# Connect to the local Docker daemon
client = docker.from_env()

# Run an Nginx container in the background
container = client.containers.run("nginx", name="container-test", detach=True)

# Rename the container
container.rename("prod")
print(f"The container has been renamed to: {container.name}")

# List running containers
print("\nCurrently running containers:")
for c in client.containers.list():
    print(f"- {c.name} ({c.status})")

# Pull the Redis image
redis_image = client.images.pull("redis")
print(f"\nRedis image downloaded: {redis_image.tags}")