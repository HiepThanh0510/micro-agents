#!/bin/bash

# Start Ollama service in the background
ollama serve &
pid=$!

# Pause for Ollama to start
sleep 5

# Download the model
echo "🔴 Creating $LLM_NAME..."
ollama run $LLM_NAME --verbose
set parameter num_ctx 2048
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid
