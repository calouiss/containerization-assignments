#!/bin/bash

# Test script for validating SecComp profiles
TEST_CONTAINERS=("books-api" "staff-api" "readers-api")

for container in "${TEST_CONTAINERS[@]}"; do
    echo "----------------------------------------"
    echo "Testing $container..."
    
    # Test 1: Verify container starts with profile
    docker compose up -d $container
    if [ $? -eq 0 ]; then
        echo "✓ Container starts successfully with SecComp profile"
    else
        echo "✗ Container failed to start with SecComp profile"
    fi

    # Test 2: Verify API functionality
    curl -f http://localhost:5000/health 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "✓ API endpoints functioning correctly"
    else
        echo "✗ API endpoints not responding"
    fi

    # Test 3: Verify blocked syscalls
    docker exec $container unshare 2>&1 | grep -q "Operation not permitted"
    if [ $? -eq 0 ]; then
        echo "✓ Unauthorized syscalls properly blocked"
    else
        echo "✗ Unauthorized syscalls not blocked"
    fi

done
