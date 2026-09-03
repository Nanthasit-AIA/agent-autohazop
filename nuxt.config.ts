// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite';
export default defineNuxtConfig({
  ssr: false,
  nitro: {
    preset: 'static',
    // Dev-only. Lets one origin (and so one tunnel) cover the SPA and both
    // backends: leave the API bases empty and requests stay same-origin.
    devProxy: {
      // The matched prefix is stripped before forwarding, so it has to be part
      // of the target or the backend sees /config instead of /api/config.
      '/api': {target: 'http://127.0.0.1:8000/api', changeOrigin: true},
      '/socket.io': {target: 'http://127.0.0.1:5000/socket.io', changeOrigin: true, ws: true},
    },
  },
  app: {
    head: {
      title: 'AAH.APP',
      link: [
        {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
      ]
    },
  },
  runtimeConfig: {
    public: {
      // Baked at build time - nitro preset is 'static'. Set these before `nuxt generate`.
      extractApiBase: process.env.NUXT_PUBLIC_EXTRACT_API_BASE || 'http://localhost:8000',
      hazopApiBase: process.env.NUXT_PUBLIC_HAZOP_API_BASE || 'http://localhost:5000',
      // Shared secret sent with every API call. Empty means the backends are open.
      demoToken: process.env.NUXT_PUBLIC_DEMO_TOKEN || '',
    },
  },

  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['./app/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
    server: {
      // Vite refuses unknown Host headers, which blocks any tunnel hostname.
      // Leading dot = allow all subdomains, so a new quick tunnel just works.
      allowedHosts: ['.trycloudflare.com'],
    },
  },

  modules: [
    '@nuxt/content',
    '@nuxt/eslint',
    '@nuxt/image',
    '@nuxt/scripts',
    '@nuxt/test-utils',
    '@nuxt/ui'
  ]
})