import { createRouter, createWebHistory } from 'vue-router'
import Top from '@/views/Top.vue'
import TaskForm from '@/views/TaskForm.vue'


const routes = [
  { path: '/', name: 'Top', component: Top },
  { path: '/new-task', name: 'TaskForm', component: TaskForm },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router