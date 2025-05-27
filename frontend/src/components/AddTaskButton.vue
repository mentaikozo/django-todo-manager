<template>
  <v-row align="end">
    <v-col cols="12">
      <v-btn color="primary" @click="addNewTask">
        <v-icon start icon="mdi-plus"></v-icon>
        新しいタスク
      </v-btn>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">

function addNewTask() {
  this.$router.push({ name: 'TaskForm' });
}
</script>

<style scoped></style>