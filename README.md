# Docker Assignments – Multi-Container App

This repository contains **Assignment 1 and Assignment 2**, implementing a Flask-based microservices application running behind an Nginx reverse proxy.

---

## ✅ Assignment 1 (Done)
- Containerized a simple Flask application  
- Added `/health` endpoint  
- Built and ran Docker image  
- Verified API responses  

---

## ✅ Assignment 2 (Done)
- Separated app into 3 microservices:
  - books_api  
  - readers_api  
  - staff_api
- Added individual Dockerfiles + health checks  
- Created `docker-compose.yml` with frontend & backend networks  
- Added Nginx reverse proxy routing:
  - `/api/books`
  - `/api/readers`
  - `/api/staff`
- Added `architecture.md` 

---

## 🚀 Run the App
```sh
docker-compose up --build
