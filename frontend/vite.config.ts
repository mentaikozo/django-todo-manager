import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  // WSL2環境でのホットリロード
  server: {
    watch: {
      usePolling: true,
    },
  },
})
