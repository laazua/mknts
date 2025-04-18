<template>
  <div class="task-manager">
    <h1>Task Manager</h1>
    <el-form @submit.prevent="addTask" class="task-form">
      <el-form-item label="Task Name">
        <el-input v-model="newTask.name" required></el-input>
      </el-form-item>
      <el-form-item label="Pipeline">
        <el-input type="textarea" v-model="newTask.pipeline" required></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" native-type="submit">Add Task</el-button>
      </el-form-item>
    </el-form>

    <el-table :data="tasks" style="width: 100%">
      <el-table-column prop="name" label="Task Name"></el-table-column>
      <el-table-column prop="status" label="Status">
        <template #default="{ row }">
          <el-tag :type="getStatusType(row.status)">{{ row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="Actions">
        <template #default="{ row }">
          <el-button @click="cancelTask(row.id)" :disabled="!canCancel(row.status)">Cancel</el-button>
          <el-button @click="refreshTaskStatus(row.name)" :disabled="isPolling(row.name)">Refresh</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { ElMessage } from 'element-plus'
import axios from 'axios'

const tasks = ref([])
const newTask = ref({ name: '', pipeline: '' })
const pollingIntervals = new Map()

const addTask = async () => {
  try {
    const response = await axios.post('/api/tasks', newTask.value)
    ElMessage.success('Task added successfully')
    newTask.value = { name: '', pipeline: '' }
    const task = response.data
    tasks.value.push(task)
    startPolling(task.name)
  } catch (error) {
    ElMessage.error('Failed to add task')
  }
}

const fetchTaskStatus = async (taskName) => {
  try {
    const response = await axios.get(`/api/tasks/${taskName}/status`)
    const updatedTask = tasks.value.find(t => t.name === taskName)
    if (updatedTask) {
      updatedTask.status = response.data.status
      if (isTaskCompleted(updatedTask.status)) {
        stopPolling(taskName)
      }
    }
  } catch (error) {
    console.error(`Failed to fetch status for task ${taskName}:`, error)
  }
}

const startPolling = (taskName) => {
  if (!pollingIntervals.has(taskName)) {
    const intervalId = setInterval(() => fetchTaskStatus(taskName), 5000)
    pollingIntervals.set(taskName, intervalId)
  }
}

const stopPolling = (taskName) => {
  const intervalId = pollingIntervals.get(taskName)
  if (intervalId) {
    clearInterval(intervalId)
    pollingIntervals.delete(taskName)
  }
}

const isPolling = (taskName) => {
  return pollingIntervals.has(taskName)
}

const refreshTaskStatus = (taskName) => {
  fetchTaskStatus(taskName)
}

const cancelTask = async (taskId) => {
  try {
    await axios.post(`/api/tasks/${taskId}/cancel`)
    ElMessage.success('Task cancelled successfully')
    await fetchTaskStatus(taskId)
  } catch (error) {
    ElMessage.error('Failed to cancel task')
  }
}

const getStatusType = (status) => {
  switch (status) {
    case 'pending': return 'info'
    case 'running': return 'warning'
    case 'completed': return 'success'
    case 'failure': return 'danger'
    case 'cancelled': return ''
    default: return 'info'
  }
}

const canCancel = (status) => {
  return status === 'pending' || status === 'running'
}

const isTaskCompleted = (status) => {
  return ['completed', 'failure', 'cancelled'].includes(status)
}

onMounted(async () => {
  try {
    const response = await axios.get('/api/tasks')
    tasks.value = response.data
    tasks.value.forEach(task => {
      if (!isTaskCompleted(task.status)) {
        startPolling(task.name)
      }
    })
  } catch (error) {
    ElMessage.error('Failed to fetch tasks')
  }
})

onUnmounted(() => {
  pollingIntervals.forEach((intervalId) => clearInterval(intervalId))
})
</script>

<style scoped>
.task-manager {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.task-form {
  margin-bottom: 20px;
}
</style>