# Docker Assignment 1 – MyApp Containerization

This assignment 1 demonstrates secure Docker image creation, container validation, and image publishing to DockerHub and AWS ECR.

---

## Task Overview
- **Task 1:** Dockerfile creation with multi-stage build and security best practices  
- **Task 2:** Build, run, and validate the container  
- **Task 3:** Publish Docker image to DockerHub and AWS ECR  

---

## 1. Build the Docker Image

Build the image using the Dockerfile in this repository:

```bash
docker build -t myapp:1.0 .
