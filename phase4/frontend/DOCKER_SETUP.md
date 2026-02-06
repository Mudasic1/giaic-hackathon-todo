# Next.js Docker Configuration

## Quick Start

Build the Docker image:
```bash
docker build -t nextjs-app .
```

Run the container:
```bash
docker run -p 3000:3000 \
  -e API_URL="https://api.example.com" \
  -e NEXT_PUBLIC_API_URL="https://api.example.com" \
  -e DATABASE_URL="postgresql://user:password@host:5432/db" \
  nextjs-app
```

## Environment Variables

### Required at Build Time
- `NODE_ENV` - Set to "production" (already configured)

### Required at Runtime
- `API_URL` - Backend API endpoint (server-side)
- `NEXT_PUBLIC_API_URL` - Backend API endpoint (client-side)
- `DATABASE_URL` - PostgreSQL connection string for Prisma
- `BETTER_AUTH_SECRET` - Secret key for Better Auth
- `BETTER_AUTH_URL` - Base URL for authentication

### Optional
- `PORT` - Port to run the app (default: 3000)
- `HOSTNAME` - Host to bind (default: 0.0.0.0)

## Docker Compose Example

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://backend:4000
      - NEXT_PUBLIC_API_URL=https://api.example.com
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
      - BETTER_AUTH_SECRET=your-secret-key
      - BETTER_AUTH_URL=http://localhost:3000
    depends_on:
      - db
  
  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Production Deployment

### Build for production:
```bash
docker build \
  --platform linux/amd64 \
  -t myregistry/nextjs-app:latest \
  .
```

### Push to registry:
```bash
docker push myregistry/nextjs-app:latest
```

### Run with environment file:
```bash
docker run -p 3000:3000 --env-file .env.production nextjs-app
```

## Multi-Stage Build Details

1. **deps**: Installs production dependencies
2. **builder**: Installs all dependencies, generates Prisma client, and builds Next.js
3. **runner**: Final optimized image with only runtime files

## Security Features

- Non-root user (nextjs:nodejs with UID/GID 1001)
- Alpine Linux base for minimal attack surface
- No development dependencies in final image
- Health check for container orchestration

## Next.js Configuration

Ensure your `next.config.js` has the following for standalone builds:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  // ... other config
}

module.exports = nextConfig
```

## Troubleshooting

### Build fails on Prisma
Ensure DATABASE_URL is set as a build arg or in your .env file during build

### Health check fails
Create an API health endpoint at `/api/health/route.ts`:
```typescript
export async function GET() {
  return Response.json({ status: 'healthy' }, { status: 200 })
}
```

### Permission errors
The app runs as user `nextjs` (UID 1001). Ensure mounted volumes have correct permissions.
