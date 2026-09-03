# AGENT-AUTO-HAZOP

## Layout

| Path | What it is |
|---|---|
| `app/` | Nuxt 4 SPA (static, `ssr: false`). |
| `services/pid-extract/` | P&ID extraction service. Calls the LiteLLM proxy; stores inputs and results in Blob. Containerized and deployed to Azure. See its README. |
| `backend/` | Flask + Socket.IO HAZOP agent. Runs locally on port 5000. |
| `infra/` | Azure deployment for the extraction service. See `infra/README.md`. |

The SPA talks to two backends. Both are build-time settings baked into the static bundle
(`nuxt.config.ts` → `runtimeConfig.public`):

- `NUXT_PUBLIC_EXTRACT_API_BASE` — default `http://localhost:8000`
- `NUXT_PUBLIC_HAZOP_API_BASE` — default `http://localhost:5000`

## Run everything locally

```bash
cp .env.example .env      # then fill in LITELLM_API_KEY
```
```bash
docker compose up --build   # extraction service on :8000
```
```bash
npm run dev:s               # SPA on :3000 + HAZOP backend on :5000
```

# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
# AGENT-AUTO-HAZOP
