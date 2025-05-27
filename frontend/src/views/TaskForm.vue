<template>
  <div :class="`.text-h3`">新しいタスク</div>
  <v-text-field label="タスク名" v-model="taskName"></v-text-field>
  <v-btn color="success" @click="submit">保存</v-btn>

</template>

<script lang="ts" setup>
import { ref } from 'vue'

const taskName = ref('')

const submit = () => {
  console.log('タスクを保存:', taskName.value)
}
</script>