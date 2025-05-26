<template>
    <section class="task-list">
        <h1>Task List</h1>
        <ul>
            <li v-for="task in tasks" :key="task.id">
                {{ task.name }} - {{ task.status }}
            </li>
        </ul>
    </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";


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

</script>

<style></style>