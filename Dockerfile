FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed (none for basic bot)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Define build arguments (these will be provided during build)
ARG BOT_TOKEN
ARG WEBHOOK_URL
ARG WEBHOOK_SECRET

# Set them as environment variables inside the container
ENV BOT_TOKEN=$BOT_TOKEN
ENV WEBHOOK_URL=$WEBHOOK_URL
ENV WEBHOOK_SECRET=$WEBHOOK_SECRET

COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the bot
CMD ["python", "main.py"]