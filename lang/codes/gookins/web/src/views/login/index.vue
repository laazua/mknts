<template>
  <div class="login-container">
    <el-card class="login-box">
      <h3 class="login-title">Gookins发版系统</h3>
      <el-form :model="loginForm" :rules="loginRule" label-width="auth">
        <el-form-item label="用户" prop="name">
          <el-input v-model="loginForm.name" placeholder="请输入用户" type="text"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="loginForm.password" placeholder="请输入密码" type="password"></el-input>
        </el-form-item>
        <el-form-item label-width=100px>
          <el-button type="primary" @click="handleLogin">登陆</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { useAuthStore } from '@/store/user.js'
import { userLogin } from '@/api/user.js'

const router = useRouter()
const authStore = useAuthStore()
const loginForm = reactive({
  name: 'admin',
  password: '111111',
})

const vaildName = (rule, value, callback) => {
  if (value === '') callback(new Error('请输入用户'))
  else callback()
}
const vaildPass = (rule, value, callback) => {
  if (value === '') callback(new Error('请输入密码'))
  else callback()
}

const loginRule = reactive({
  name: [{ required: true, validator: vaildName, trigger: 'blur' }],
  password: [{ required: true, validator: vaildPass, trigger: 'blur' }]
})

const handleLogin = async () => {
  try {
    const response = await userLogin(loginForm)
    authStore.setToken(response.token)
    router.push('/')
  } catch (error) {
    ElMessage({
      message: error || 'Login Error',
      type: 'error',
      duration: 5 * 1000
    })
  }
}

</script>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
}

body {
  background-color: rgb(54, 54, 67);
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box {
  width: 300px;
  margin-top: 250px;
  margin-bottom: 250px;
}

.login-title {
  margin-bottom: 20px;
  text-align: center;
}

</style>