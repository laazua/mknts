<template>
  <div>
    <el-button plain @click="centerDialogVisible  = true" type="primary" :icon="Plus" size="small">
      新增用户
    </el-button>

    <hr class="my-4" />

    <el-dialog v-model="centerDialogVisible" width="500" center>
      
      <el-form
        style="max-width: 600px"
        :model="userForm"
        status-icon
        :rules="userRule"
        label-width="auto"
        v-loading="loading"
      >
        <el-form-item label="用户名称" prop="name">
          <el-input v-model="userForm.name" />
        </el-form-item>
        <el-form-item label="用户密码" prop="password">
          <el-input v-model="userForm.password" type="password" autocomplete="off" />
        </el-form-item>
        <el-form-item label="确认密码" prop="checkPass">
          <el-input v-model="userForm.checkPass" type="password" autocomplete="off" />
        </el-form-item>
      </el-form>

      <template #footer>
        <div class="dialog-footer">
          <el-button @click="centerDialogVisible = false" size="small">取消</el-button>
          <el-button type="primary" @click="submitUserForm" size="small">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>

    <el-table :data="users">
      <el-table-column prop="ID" label="ID" width="100" />
      <el-table-column prop="Name" label="姓名" width="150" />
      <el-table-column prop="CreatedAt" label="创建时间" width="360"/>
      <el-table-column prop="UpdatedAt" label="更新时间" width="360"/>
      <el-table-column prop="DeletedAt" label="删除时间" width="360"/>
    </el-table>
    <!-- <br>
    <div>
      <hr class="my-4" />
      <el-pagination
      size="small"
      background
      :hide-on-single-page="showPage"
      layout="prev, pager, next"
      :total="userTotal"
      class="mt-4"
      />
    </div> -->
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { getUsers, addUser } from '@/api/user.js'

const users = ref([])
const userTotal = users.value.length
// const showPage = ref(false)
const loading = ref(false)
const centerDialogVisible = ref(false)

const userForm = reactive({
  name: '',
  password: '',
  checkPass: '',
})

const validateUsername = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请输入用户'))
  } else {
    callback()
  }
}

const validatePassword = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('密码必须大于6位'))
  } else {
    callback()
  }
}

const validateCheckPass = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('密码必须大于6位'))
  } else if (value !== userForm.password) {
    callback(new Error('两次密码不一致'))
  } else {
     callback()
  }
}

const userRule =  reactive({
  name: [{ required: true, validator: validateUsername, trigger: 'blur' }],
  password: [{ required: true, validator: validatePassword, trigger: 'blur' }],
  checkPass: [{ required: true, validator: validateCheckPass, trigger: 'change' }]
})

const submitUserForm = async () => {
  loading.value = true
  try {
    const data = reactive({
      name: userForm.name,
      password: userForm.password
    })
    const response = await addUser(data)
    if (response.code==200) {
      ElMessage({
      message: response.message || 'Add User Success',
      type: 'success',
      duration: 5 * 1000
    })
    }
    userForm.name = ''
    userForm.password = ''
    userForm.checkPass = ''
    loading.value = false
  } catch (error) {
    ElMessage({
      message: error || 'Add User Error',
      type: 'error',
      duration: 5 * 1000
    })
    loading.value = false
  }
  centerDialogVisible.value = false
}

const cancelForm = () => {
  userForm.name = ''
  userForm.password = ''
  userForm.checkPass = ''
  centerDialogVisible.value = false
}

onMounted(async ()=>{
  try {
    const response = await getUsers()
    users.value = response.data
  } catch (error) {
    ElMessage({
      message: error || 'Get Users Error',
      type: 'error',
      duration: 5 * 1000
    })
  }
})

</script>