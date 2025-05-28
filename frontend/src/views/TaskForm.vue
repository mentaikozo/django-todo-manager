<template>
  <div :class="`text-h3 pa-3`">新しいタスク</div>

  <v-form @submit.prevent="submitForm" v-model="formValid">
    <v-text-field v-model="task.name" label="タスク名" :rules="[rules.required]" required />

    <v-select v-model="task.status" label="ステータス" :items="statusChoices" item-title="label" item-value="value" />

    <v-text-field v-model="task.progress" label="進捗" suffix="%" :rules="[rules.required]" />

    <v-text-field v-model.number="task.priority" label="優先度 (1〜10)" type="number"
      :rules="[rules.required, rules.min, rules.max]" />

    <v-combobox v-model="task.tags" label="タグ" multiple chips clearable />

    <v-textarea v-model="task.notes" label="メモ" rows="4" auto-grow />

    <v-btn color="primary" type="submit">保存</v-btn>
  </v-form>

</template>

<script lang="ts" setup>
import { ref } from "vue"
import router from "@/router"
import axios from "axios"

const formValid = ref()

const task = ref({
  name: '',
  status: 0,
  progress: '0%',
  priority: 1,
  tags: [] as string[],
  notes: '',
})

const statusChoices = [
  { value: 0, label: '未' },
  { value: 1, label: '済' },
]

const rules = {
  required: (v: any) => !!v || '必須項目です',
  min: (v: number) => v >= 1 || '1以上で入力してください',
  max: (v: number) => v <= 10 || '10以下で入力してください',
}

const submitForm = () => {
  if (!formValid.value) return

  try {
    const response = axios.post("http://localhost:8000/api/tasks/", task.value);

    console.log("Task saved successfully:", response.data);
    router.push({ name: 'Top' });
  } catch (error) {
    console.error("Error creating tasks:", error);
  }
}
</script>
