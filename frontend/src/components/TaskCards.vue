<template>
  <v-row justify="start">
    <v-col cols="12">
      <v-card>
        <v-list>
          <v-list-item v-for="task in tasks" :key="task.id" @click="goTaskDetail(task.id)">
            <div class="d-flex align-center w-100">
              <div class="mr-4 task-name">{{ task.name }}</div>
              <div class="clamp-text">{{ task.notes }}</div>
            </div>
          </v-list-item>
        </v-list>
      </v-card>
      <!-- <v-card :color="getTaskColor(task.status)" @click="goTaskDetail(task.id)">
        <v-card-title>{{ task.name }}</v-card-title>
        <v-card-subtitle>{{ task.status }} ({{ task.progress }})</v-card-subtitle>
        <v-card-text>
          <div class="clamp-text" v-html="renderMarkdown(task.notes)"></div>
        </v-card-text>
      </v-card> -->
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import router from "@/router";
import axios from "axios";
import DOMPurify from "dompurify";
import { marked } from "marked";

const tasks = ref([]);

const fetchTasks = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/tasks/");
    tasks.value = response.data;
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
};

onMounted(() => {
  fetchTasks();
});

function getTaskColor(status: number) {
  if (status === 1) {
    return "success";
  } else {
    return "info";
  }
}

function renderMarkdown(markdownText) {
  return DOMPurify.sanitize(marked(markdownText))
}

function goTaskDetail(id: number) {
  router.push({ name: 'TaskDetail', params: { "id": id } });
}

</script>

<style scoped>
.task-name {
  font-weight: bold;
  min-width: 150px;
  max-width: 150px;
}

.clamp-text {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
}
</style>