import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  // WSL2環境でのホットリロード
  server: {
    watch: {
      usePolling: true,
    },
  },
  //@でパスを読めるようにする
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    }
  }
})
