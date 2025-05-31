<template>
  <v-container class="d-flex align-start justify-start">
    <v-row>
      <v-col>
        <div :class="`text-h5 pb-4`">
          {{ taskId ? "Task Detail" : "Create New Task" }}
        </div>

        <v-form @submit.prevent="submitForm" v-model="formValid">
          <v-text-field width="400" v-model="task.name" label="タスク名" :rules="[rules.required]" required />

          <v-select max-width="200" v-model="task.status" label="ステータス" :items="statusChoices" item-title="label"
            item-value="value" />

          <v-text-field max-width="200" v-model="task.progress" label="進捗" suffix="%" :rules="[rules.required]" />

          <v-text-field max-width="200" v-model.number="task.priority" label="優先度 (1〜10)" type="number"
            :rules="[rules.required, rules.min, rules.max]" />

          <v-combobox max-width="300" v-model="task.tags" label="タグ" multiple chips clearable />

          <v-textarea width="800" v-model="task.notes" label="メモ" rows="4" auto-grow />

          <div class="d-flex justify-start">
            <v-btn color="primary" type="submit">
              {{ taskId ? "Update" : "Save" }}
            </v-btn>
          </div>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue"
import router from "@/router"
import axios from "axios"
import { useRoute } from "vue-router"

const route = useRoute()
const taskId = route.params?.id as string | undefined

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

onMounted(async () => {
  if (taskId) {
    try {
      const response = await axios.get(`http://localhost:8000/api/tasks/${taskId}/`)
      console.log(response.data)
      task.value = response.data
    } catch (error) {
      console.error("Error fetching task:", error)
    }
  }
})

const submitForm = async () => {
  if (!formValid.value) return

  try {
    if (taskId) {
      const response = await axios.put(`http://localhost:8000/api/tasks/${taskId}/`, task.value)
      console.log("Task updated successfully:", response.data)
    } else {
      const response = await axios.post("http://localhost:8000/api/tasks/", task.value)
      console.log("Task saved successfully:", response.data)
    }
    router.push({ name: "Top" })
  } catch (error) {
    console.error("Error processing tasks:", error)
  }
}
</script>
