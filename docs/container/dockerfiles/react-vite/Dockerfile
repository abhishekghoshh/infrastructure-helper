# Production-ready Dockerfile for React app using Vite
FROM node:22.19.0-alpine AS build

WORKDIR /app

COPY package.json package-lock.json* yarn.lock* pnpm-lock.yaml* ./

# Install dependencies
RUN npm install --frozen-lockfile || yarn install --frozen-lockfile || pnpm install --frozen-lockfile

COPY . .

# Build the app
RUN npm run build || yarn build || pnpm build

# --- Production image ---
FROM nginx:alpine

# Copy built assets from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom nginx config if you have one
# COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
