# Containerization Assignments: Completed

This repository contains Assignments 1–4, implementing a Flask microservices application using Docker, Nginx reverse proxy, and SecComp security.

---

## ✅ Assignment 1 –  Docker Image Creation, Validation, and Publishing
- Containerized simple Flask app
- Added /health endpoint
- Built & tested Docker image

---

## ✅ Assignment 2 - Multi-Container Application Deployment
- Split into 3 microservices: books_api, readers_api, staff_api
- Added Dockerfiles + health checks
- Configured docker-compose.yml (frontend & backend networks)
- Added Nginx routing:
  - /api/books
  - /api/readers
  - /api/staff
- Added architecture diagram (architecture.md)

---

## ✅ Assignment 3 - Docker Runtime Management and Production Configuration
- Verified Nginx routing to all microservices
- Ensured all APIs respond correctly through /api/...
- Confirmed stable multi-container startup using:

docker-compose up --build

---

## ✅ Assignment 4 - Container Security with SecComp Profiles
- SecComp Profiles
  - Added custom profiles for all services
  - Integrated profiles into docker-compose.yml

- Validation
  - Added script: validate-seccomp.sh
- Checks:
  - Containers start under SecComp
  - Blocked syscalls are detected
  - APIs remain functional
- Stress Testing
  - Added stress-test.py to send 1000 requests per service
  - All services passed with 0 failed requests

./validate-seccomp.sh
python stress-test.py

