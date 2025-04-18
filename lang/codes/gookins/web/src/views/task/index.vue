<template>
  <div class="task-manager">
    <el-button type="primary" @click="openDrawer(null)" :icon="Plus" size="small">新增任务</el-button>
    
    <el-table v-if="!loading && tasks.length > 0" :data="tasks" style="width:100%;margin-top:20px;">
      <el-table-column prop="ID" label="ID" width="80" />
      <el-table-column prop="Name" label="任务名称" width="120" />
      <el-table-column prop="Description" label="任务描述" width="120" />
      <el-table-column prop="PipeLine" label="流水任务" width="200">
        <template #default="scope">
          <div v-if="scope.row" class="pipeline-content">{{ scope.row.PipeLine }}</div>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="360">
        <template #default="scope">
          <el-button size="small" @click="openDrawer(scope.row)">更新</el-button>
          <el-button 
            size="small" 
            type="primary" 
            @click="runTask(scope.row)"
            :loading="scope.row.status === 'running'"
            :disabled="scope.row.status === 'running' || scope.row.disabled"
          >
            运行
          </el-button>
          <el-button 
            size="small" 
            type="danger" 
            @click="cancelTask(scope.row)"
            :disabled="scope.row.status !== 'running'"
          >
            取消
          </el-button>
          <el-button 
            size="small" 
            :type="scope.row.disabled ? 'success' : 'warning'"
            @click="toggleTaskDisabled(scope.row)"
          >
            {{ scope.row.disabled ? '启用' : '禁用' }}
          </el-button>
        </template>
      </el-table-column>
      <el-table-column label="状态">
        <template #default="scope">
          <el-tag :type="getStatusType(scope.row.status)">
            {{ getStatusText(scope.row.status) }}
          </el-tag>
          <el-tag v-if="scope.row.disabled" type="info" class="ml-2">已禁用</el-tag>
        </template>
      </el-table-column>
    </el-table>
    <el-empty v-else-if="!loading && tasks.length === 0" description="暂无任务" />
    <el-skeleton v-else :rows="5" animated />

    <el-drawer v-model="drawerVisible" :title="editingTask ? '更新任务' : '新增任务'" size="40%">
      <el-form :model="taskForm" label-width="100px" @submit.prevent="submitTask">
        <el-form-item label="任务名称">
          <el-input v-model="taskForm.Name" />
        </el-form-item>
        <el-form-item label="任务描述">
          <el-input v-model="taskForm.Description" />
        </el-form-item>
        <el-form-item label="流水任务">
          <el-input
            v-model="taskForm.PipeLine"
            type="textarea"
            :rows="5"
            placeholder="请输入YAML格式的流水线任务"
          />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitTask">{{ editingTask ? '更新' : '添加' }}</el-button>
          <el-button @click="drawerVisible = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-drawer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, reactive } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { getTasks, addTask, updateTask, deleteTask, apiRunTask, taskStatus, apiCancelTask, apiToggleTaskDisabled } from '@/api/task.js'

const tasks = ref([])
const drawerVisible = ref(false)
const editingTask = ref(null)
const loading = ref(true)
const taskForm = reactive({
  Id: '',
  Name: '',
  Description: '',
  PipeLine: '',
})
const pollingIntervals = new Map()

const fetchTasks = async () => {
  try {
    loading.value = true
    const response = await getTasks()
    tasks.value = response.data
  } catch (error) {
    ElMessage.error('获取任务列表失败')
  } finally {
    loading.value = false
  }
}

const updateTaskStatus = async (task) => {
  try {
    const response = await taskStatus(task.Name)
    const newStatus = response.data
    task.status = newStatus

    if (newStatus === 'completed' || newStatus === 'cancelled' || newStatus === 'failed') {
      stopPolling(task.Name)
    }
  } catch (error) {
    console.error(`更新任务状态失败: ${task.Name}`, error)
    stopPolling(task.Name)
  }
}

const startPolling = (taskName) => {
  if (!pollingIntervals.has(taskName)) {
    const intervalId = setInterval(() => updateTaskStatus(tasks.value.find(t => t.Name === taskName)), 1000)
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

const openDrawer = (task) => {
  editingTask.value = task
  if (task) {
    Object.assign(taskForm, {
      Id: task.Id,
      Name: task.Name,
      Description: task.Description,
      PipeLine: task.PipeLine
    })
  } else {
    Object.assign(taskForm, {
      Id: '',
      Name: '',
      Description: '',
      PipeLine: ''
    })
  }
  drawerVisible.value = true
}

const submitTask = async () => {
  try {
    if (editingTask.value) {
      await updateTask(taskForm)
      ElMessage.success('任务更新成功')
    } else {
      await addTask(taskForm)
      ElMessage.success('任务添加成功')
    }
    drawerVisible.value = false
    await fetchTasks()
  } catch (error) {
    ElMessage.error(editingTask.value ? '更新任务失败' : '添加任务失败')
  }
}

const runTask = async (task) => {
  if (task.disabled) {
    ElMessage.warning('该任务已被禁用，无法运行')
    return
  }
  try {
    await apiRunTask({
      Id: task.Id,
      Name: task.Name,
      Description: task.Description,
      PipeLine: task.PipeLine
    })
    task.status = 'running'
    ElMessage.success('任务开始运行')
    startPolling(task.Name)
  } catch (error) {
    ElMessage.error('运行任务失败: ' + error)
  }
}

const cancelTask = async (task) => {
  try {
    await ElMessageBox.confirm('确定要取消该任务吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
    
    await apiCancelTask(task.Name)
    task.status = 'cancelled'
    ElMessage.success('任务已取消')
    stopPolling(task.Name)
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('取消任务失败: ' + error)
    }
  }
}

const toggleTaskDisabled = async (task) => {
  try {
    const action = task.disabled ? '启用' : '禁用'
    await ElMessageBox.confirm(`确定要${action}该任务吗？`, '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
    
    await apiToggleTaskDisabled(task.Name)
    task.disabled = !task.disabled
    ElMessage.success(`任务已${action}`)
    
    if (task.disabled && task.status === 'running') {
      await cancelTask(task)
    }
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('操作失败: ' + error)
    }
  }
}

const statusMap = {
  pending: { type: 'info', text: '等待中' },
  running: { type: 'warning', text: '运行中' },
  completed: { type: 'success', text: '已完成' },
  cancelled: { type: 'info', text: '已取消' },
  failed: { type: 'danger', text: '失败' },
  success: { type: 'success', text: '成功' }
}

const getStatusType = (status) => statusMap[status]?.type || 'info'
const getStatusText = (status) => statusMap[status]?.text || '未知'

onMounted(() => {
  fetchTasks()
})

onUnmounted(() => {
  pollingIntervals.forEach((intervalId) => clearInterval(intervalId))
})
</script>

<style scoped>
.task-manager {
  padding: 20px;
}

.pipeline-content {
  max-width: 200px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
