// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite';
export default defineNuxtConfig({
  ssr: false,
  nitro: {preset: 'static'},
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
    },
  },

  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['./app/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
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