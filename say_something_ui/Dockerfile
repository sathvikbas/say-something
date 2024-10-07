# Use an official Node.js image as the base image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json and install Node.js dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the project files
COPY . .

# Expose the port the React app runs on (3000 by default in dev mode)
EXPOSE 3000

# Command to run the React development server
CMD ["npm", "start"]
