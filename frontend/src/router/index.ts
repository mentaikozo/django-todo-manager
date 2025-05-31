import { createRouter, createWebHistory } from 'vue-router'
import Top from '@/views/Top.vue'
import TaskForm from '@/views/TaskForm.vue'


const routes = [
  { path: '/', name: 'Top', component: Top },
  { path: '/tasks/new', name: 'NewTask', component: TaskForm },
  { path: '/tasks/:id', name: 'TaskDetail', component: TaskForm, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router