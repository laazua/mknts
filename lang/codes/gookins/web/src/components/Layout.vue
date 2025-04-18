<template>
  <el-container class="layout-container">
    <el-header>
      <div class="header-content">
        <h2 @click="toggleSidebar" style="cursor: pointer;">Gookins管理系统</h2>
        <div class="user-info">
          <span>欢迎，{{ username }}</span>
          <el-button type="primary" size="small" @click="handleLogout">退出登录</el-button>
        </div>
      </div>
    </el-header>
    <el-container>
      <el-aside :width="sidebarWidth">
        <Sidebar :is-collapsed="isSidebarCollapsed" />
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import Sidebar from '@/components/Sidebar.vue'
import { useAuthStore } from '@/store/user.js'

const router = useRouter()
const username = ref('管理员')
const authStore = useAuthStore()
const isSidebarCollapsed = ref(false)

const sidebarWidth = computed(() => isSidebarCollapsed.value ? '60px' : '200px')

const toggleSidebar = () => {
  isSidebarCollapsed.value = !isSidebarCollapsed.value
}

const handleLogout = () => {
  console.log('登出...')
  authStore.cleanToken()
  router.push('/login')
}
</script>

<style scoped>

.layout-container {
  height: 100vh;
}

.el-header {
  background-color: #34577a;
  color: white;
  line-height: 60px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
}

.user-info span {
  margin-right: 15px;
}

.el-aside {
  background-color: #1c2a3a;
  color: white;
  transition: width 0.3s;
}

.el-main {
  background-color: #E9EEF3;
}
</style>