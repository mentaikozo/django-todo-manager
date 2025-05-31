<template>
  <v-row align="end">
    <v-col cols="12" class="d-flex justify-end">
      <v-btn color="primary" @click="addNewTask">
        <v-icon start icon="mdi-plus"></v-icon>
        <div class="text-button">New Task</div>
      </v-btn>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import router from '@/router';

function addNewTask() {
  router.push({ name: 'NewTask' });
}
</script>

<style scoped></style>