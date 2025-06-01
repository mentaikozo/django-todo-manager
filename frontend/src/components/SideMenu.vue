<template>
  <v-col cols="12" md="2">
    <v-card flat class="pa-4">
      <div class="text-h6 mb-2">Filters</div>
      <v-divider></v-divider>
      <div class="d-flex mt-2 text-body-1">
        Tags
      </div>
      <v-checkbox v-for="tag in tags" :key="tag" v-model="selected" :label="tag" :value="tag" />
    </v-card>
  </v-col>
</template>

<script setup lang="ts">
import { ref, watch } from "vue"
import Task from "@/types"

const props = defineProps<{ tasks: Task[] }>()

const tags = ref<string[]>([])
const selected = ref<string[]>([])

function getUniqueTags(tasks: Task[]) {
  const uniqueTags = new Set<string>()
  props.tasks.forEach(task => {
    task.tags.forEach(tag => uniqueTags.add(tag))
  })
  return Array.from(uniqueTags)
}

// onMountedではprops.tasksは空で受け取ってしまう
// watchにてtasksの中身が変わったらtagsを更新
watch(
  () => props.tasks,
  (newTasks) => {
    tags.value = getUniqueTags(newTasks)
    console.log("Updated tags:", tags.value)
  },
  // 最初にも実行されるようにする
  { immediate: true }
)

</script>

<style scoped></style>