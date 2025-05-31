<template>
  <v-container fluid v-show="loaded">
    <ToolBar />
    <AddTaskButton />
    <v-row justify="start">
      <SideMenu />
      <TaskCards :tasks="tasks" />
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import AddTaskButton from "@/components/AddTaskButton.vue"
import SideMenu from "@/components/SideMenu.vue"
import TaskCards from "@/components/TaskCards.vue"
import ToolBar from "@/components/ToolBar.vue"
import axios from "axios"

const tasks = ref([]);
const loaded = ref(false)

const fetchTasks = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/tasks/")
    tasks.value = response.data
    loaded.value = true
  } catch (error) {
    console.error("Error fetching tasks:", error)
  }
}

onMounted(() => {
  fetchTasks()
})

</script>

<style scoped></style>
