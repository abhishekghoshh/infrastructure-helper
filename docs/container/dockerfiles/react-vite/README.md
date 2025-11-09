# Minimal React App with Docker & Docker Compose

This project demonstrates a minimal React application (using Vite and TypeScript) with a production-ready Docker and Docker Compose setup.

---

## Table of Contents

- [Minimal React App with Docker \& Docker Compose](#minimal-react-app-with-docker--docker-compose)
  - [Table of Contents](#table-of-contents)
  - [What are JS, TS, JSX, and TSX?](#what-are-js-ts-jsx-and-tsx)
  - [React Basics](#react-basics)
  - [Creating a New React Project with Vite and TypeScript (TSX)](#creating-a-new-react-project-with-vite-and-typescript-tsx)
  - [How Multistage Dockerfile and .dockerignore Improve Build](#how-multistage-dockerfile-and-dockerignore-improve-build)
    - [Multistage Dockerfile](#multistage-dockerfile)
    - [.dockerignore](#dockerignore)
  - [Project Structure](#project-structure)
  - [Dockerfile \& .dockerignore: How They Help](#dockerfile--dockerignore-how-they-help)
    - [Multistage Dockerfile](#multistage-dockerfile-1)
    - [.dockerignore](#dockerignore-1)
  - [How to Run the Project](#how-to-run-the-project)
    - [1. Build and Run with Docker Compose](#1-build-and-run-with-docker-compose)
    - [2. Stopping the App](#2-stopping-the-app)
    - [3. (Optional) Build and Run with Docker Only](#3-optional-build-and-run-with-docker-only)

---





## What are JS, TS, JSX, and TSX?

- **JS (JavaScript):** The standard scripting language for web development. Runs in browsers and on servers (Node.js). File extension: `.js`.
- **TS (TypeScript):** A superset of JavaScript that adds static typing and advanced features. Compiles to JavaScript. File extension: `.ts`.
- **JSX (JavaScript XML):** A syntax extension for JavaScript that lets you write HTML-like code inside JavaScript, mainly used with React. File extension: `.jsx`.
- **TSX (TypeScript XML):** The TypeScript version of JSX, allowing you to use type safety and modern JavaScript features in your React components. File extension: `.tsx`.

---

## React Basics

React is a popular JavaScript library for building user interfaces, especially single-page applications. It uses a component-based architecture, where each UI part is a reusable component. Components can be written using JSX/TSX (JavaScript/TypeScript XML), which lets you write HTML-like code in your JavaScript/TypeScript files.

**TSX** is the TypeScript version of JSX, allowing you to use type safety and modern JavaScript features in your React components.

---

## Creating a New React Project with Vite and TypeScript (TSX)

You can quickly scaffold a new React project using [Vite](https://vitejs.dev/) with TypeScript support:

```sh
# Using npm
npm create vite@latest my-react-app -- --template react-ts

# Using yarn
yarn create vite my-react-app --template react-ts

# Using pnpm
pnpm create vite my-react-app -- --template react-ts
```

Then install dependencies and start the dev server:

```sh
cd my-react-app
npm install
npm run dev
```

This will start a local development server and open your new React + TypeScript app in the browser.

---

## How Multistage Dockerfile and .dockerignore Improve Build

### Multistage Dockerfile

A multistage Dockerfile uses multiple `FROM` statements to create separate build and production stages. In this project:

- The first stage (`node:22.19.0-alpine`) installs dependencies and builds the React app.
- The second stage (`nginx:alpine`) copies only the final build output (static files) into a clean, lightweight Nginx image.

**Benefits:**
- Only production-ready files are included in the final image (no source code, no build tools, no node_modules).
- Results in a much smaller, more secure, and faster-to-deploy image.
- Faster builds on subsequent runs due to Docker layer caching.

### .dockerignore

The `.dockerignore` file tells Docker which files and folders to exclude from the build context (the files sent to the Docker daemon during build).

**Benefits:**
- Prevents unnecessary files (like `node_modules`, logs, test files, local configs) from being sent to Docker, reducing build time and context size.
- Keeps the final image clean and free of development artifacts.

**Summary:**
Using both a multistage Dockerfile and a well-crafted `.dockerignore` ensures your builds are fast, efficient, and produce small, production-ready images.


---


## Project Structure

```
blogs/
├── Dockerfile                # Multi-stage build for React app
├── docker-compose.yml        # Compose file for container orchestration
├── .dockerignore             # Files/folders to exclude from Docker build
├── public/                   # Static assets
├── src/                      # React components and source code
│   ├── App.tsx               # Main React component
│   └── ...
├── package.json              # Project dependencies and scripts
└── ...
```

**Key React Component:**
- `src/App.tsx`: Main entry point for your React UI. You can add more components in the `src/` directory.

---


## Dockerfile & .dockerignore: How They Help

### Multistage Dockerfile
A multistage Dockerfile uses multiple `FROM` statements to create separate build and production stages:
- The first stage (`node:22.19.0-alpine`) installs dependencies and builds the React app.
- The second stage (`nginx:alpine`) copies only the final build output (static files) into a clean, lightweight Nginx image.

**Benefits:**
- Only production-ready files are included in the final image (no source code, no build tools, no node_modules).
- Results in a much smaller, more secure, and faster-to-deploy image.
- Faster builds on subsequent runs due to Docker layer caching.

### .dockerignore
The `.dockerignore` file tells Docker which files and folders to exclude from the build context (the files sent to the Docker daemon during build):
- Prevents unnecessary files (like `node_modules`, logs, test files, local configs) from being sent to Docker, reducing build time and context size.
- Keeps the final image clean and free of development artifacts.

**Summary:**
Using both a multistage Dockerfile and a well-crafted `.dockerignore` ensures your builds are fast, efficient, and produce small, production-ready images.

---


## How to Run the Project

### 1. Build and Run with Docker Compose
```sh
cd blogs
docker-compose up --build
```
The app will be available at [http://localhost:3000](http://localhost:3000)

### 2. Stopping the App
```sh
docker-compose down
```

### 3. (Optional) Build and Run with Docker Only
```sh
cd blogs
docker build -t minimal-dockerfiles-blogs .
docker run -d -p 3000:80 --name react-app-container minimal-dockerfiles-blogs
```

---

Feel free to explore the `src/` directory to see and modify the React components!
