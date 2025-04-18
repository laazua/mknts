<template>
  <div>
    <el-button class="add-button" type="primary" @click="dialogFormVisible  = true">新增用户</el-button>
    <el-dialog title="添加用户" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="用户名称" :label-width="formLabelWidth">
          <el-input v-model="form.username" autocomplete="off" class="form-button" placeholder="zhangsan"></el-input>
        </el-form-item>
        <el-form-item label="用户密码" :label-width="formLabelWidth">
          <el-input v-model="form.password" autocomplete="off" class="form-button" type="password" placeholder="xxxxxxxxx"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" :label-width="formLabelWidth">
          <el-input v-model="form.password2" autocomplete="off" class="form-button" type="password" placeholder="xxxxxxxxx"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </div>
    </el-dialog>
    <el-table :data="tableData">
      <el-table-column prop="index" label="序号"></el-table-column>
      <el-table-column prop="username" label="姓名"></el-table-column>
      <el-table-column prop="option" label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getUserLists, delUser, register } from "@/api/index"
export default {
  data() {
    return {
      tableData: null,
      dialogFormVisible: false,
      form: {
        username: null,
        password: null,
        password2: null
      },
      formLabelWidth:'200px'

    }
  },
  created() {
    this.getUsers()
  },
  methods: {
    getUsers() {
      getUserLists().then(response => {
        this.tableData = response.data
      })
    },
    handleEdit(index, row) {
      this.$confirm("是否删除" + row.username, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning"
      }).then(() => {
        const data = { "index": index, "username": row.username }
        delUser(data).then(response => {
          if (response.code === 200) {
            this.$message({message: "删除用户: " + row.username + " 成功!", type: "success"})
          } else {
            this.$message({message: "删除用户: " + row.username + " 成功!", type: "warning"})
          }
        })
      })
    },
    addUser() {
      // const data = this.form
      // console.log(data)
      this.$confirm("是否添加该用户", "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning"
      }).then(() => {
        const data = this.form
        register(data).then(response => {
          if (response.code === 200) {
            this.$message({message: "添加用户: " + this.form.username + " 成功!", type: "success"})
            this.dialogFormVisible = false
          } else {
            this.$message({message: "添加用户: " + this.form.username + " 成功!", type: "warning"})
          }
        })
      })
    }
  }
}
</script>

<style>
.el-table {
  margin: 50px;
  width: 100%
}

.add-button {
  margin-top: 40px;
  margin-left: 50px;
}

.el-form-item {
  margin: 20px;
}

.form-button {
  margin-left: 20px;
  width: 500px;
}

.el-table-column {
  width: auto;
}
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>