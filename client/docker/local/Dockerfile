FROM docker.io/node:24-alpine3.22 as base

# First stage
FROM base as node-build

RUN apk add --no-cache libc6-compat

COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./

RUN \
    if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
    elif [ -f package-lock.json ]; then npm ci; \
    elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm i; \
    else echo "Lockfile not found" && exit 1; \
    fi

# Second stage
FROM base as node-run

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

COPY --from=node-build /node_modules ./node_modules

COPY . ${APP_HOME}

RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001 -G nodejs

RUN chown -R nextjs:nodejs ${APP_HOME}

USER nextjs

CMD ["npm", "run", "dev"]