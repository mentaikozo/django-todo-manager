<template>
  <v-container fluid>
    <ToolBar />
    <AddTaskButton />
    <v-row justify="start">
      <SideMenu />
      <TaskCards />
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import AddTaskButton from "@/components/AddTaskButton.vue"
import SideMenu from "@/components/SideMenu.vue"
import TaskCards from "@/components/TaskCards.vue"
import ToolBar from "@/components/ToolBar.vue"
</script>

<style scoped></style>
