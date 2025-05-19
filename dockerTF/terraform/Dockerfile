# Use the official Nginx image
FROM nginx:alpine

# Remove the default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy custom HTML page to nginx html directory
#COPY index.html /usr/share/nginx/html/

# Copy from remote Repo
COPY aquashopcr01/ /usr/share/nginx/html/

# Expose port 8000
EXPOSE 8000