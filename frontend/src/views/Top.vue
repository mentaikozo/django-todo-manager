<template>
  <v-container>
    <ToolBar />
    <AddTaskButton />
    <TaskCards />
  </v-container>
</template>

<script setup lang="ts">
import AddTaskButton from "@/components/AddTaskButton.vue"
import TaskCards from "@/components/TaskCards.vue"
import ToolBar from "@/components/ToolBar.vue"
</script>

<style scoped></style>
