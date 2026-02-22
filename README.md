
# 🚀 Projects – Docker & MCP Agent

This repository showcases **Python automation, Docker container management, and MCP server integration** on a Linux VM.
It demonstrates DevOps workflows, container lifecycle automation, and programmatic orchestration using Python and Claude Desktop.

---

## 🐳 Project 1 – Docker Containers with Python SDK

This project uses **Python Docker SDK** to manage containers and images. 

### 🛠 Prerequisites

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip -y

# Upgrade pip
python3 -m pip install --upgrade pip

# Install Docker SDK for Python
python3 -m pip install docker

# Ensure Docker is installed and running
docker --version
```

### 🐍 Running the Script

The script performs the following tasks:

1. Launch an **Nginx** container in the background
2. Rename the container
3. List currently running containers
4. Pull the latest **Redis** image

```bash
python3 script-docker.py
```

#### Example Python Snippet

```python
import docker

client = docker.from_env()

# Run Nginx container
container = client.containers.run("nginx", name="container-test", detach=True)

# Rename container
container.rename("prod")
print(f"The container has been renamed to: {container.name}")

# List running containers
for c in client.containers.list():
    print(f"- {c.name} ({c.status})")

# Pull Redis image
redis_image = client.images.pull("redis")
print(f"Redis image downloaded: {redis_image.tags}")
```

### 📦 Verify Containers & Images

```bash
docker ps        # List running containers
docker images    # List downloaded images
```

### 🌌 Example Output (Visual Placeholder)

```
Containers running:
- prod (Up 10s)
- <other containers>

Images downloaded:
- nginx:latest
- redis:latest
```


## 🤖 Project 2 – MCP Agent for Docker Cluster

This project will demonstrates creating an **agent** that interacts with a Docker cluster through an **MCP server** on a Linux VM via Claude Desktop.

The agent automates tasks like starting/stopping containers, pulling images, and monitoring container status.



### 💡 Portfolio Purpose

* 🐍 Python automation for Docker tasks and container lifecycle
* 🔧 Integration with MCP server via Claude Desktop
* 📦 Dynamic container/image management
* 🚀 Professional DevOps workflow demonstration for portfolio

next step kubernetes sdk and mcp server 
