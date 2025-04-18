<template>
  <div class="u-table">
    <el-table
      :data="tableData"
      stripe
      size="mini"
      style="width: 100%"
      :cell-style="{ textAlign: 'center' }"
      :header-cell-style="{ textAlign: 'center' }">
      <el-table-column
        prop="name"
        label="姓名"
        width="240">
      </el-table-column>
      <el-table-column
        prop="desc"
        label="描述"
        width="240">
      </el-table-column>
      <el-table-column
        prop="roles"
        label="权限"
        width="240"
        :formatter="roleList">
      </el-table-column>
      <el-table-column
        prop="ctime"
        label="创建时间"
        width="240">
      </el-table-column>
      <el-table-column 
        label="操作"
        width="240">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
    </el-table-column>
    </el-table>
    <div class="u-add">
      <el-button type="primary" icon="el-icon-plus" size="mini" @click="dialogVisible = true">添加用户</el-button>
      <el-dialog 
        title="添加用户" 
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form size="mini">
          <el-form-item label="用户名称" label-width="auto">
            <el-input v-model="addUserForm.name" autocomplete="off" placeholder="username" type="text"></el-input>
          </el-form-item>
          <el-form-item label="用户密码" label-width="auto">
            <el-input v-model="addUserForm.pwd_one" autocomplete="off" placeholder="password" type="password"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" label-width="auto">
            <el-input v-model="addUserForm.pwd_tow" autocomplete="off" placeholder="password" type="password"></el-input>
          </el-form-item>
          <el-form-item label="用户描述" label-width="auto">
            <el-input v-model="addUserForm.desc" autocomplete="off" placeholder="desc: 管理员" type="text"></el-input>
          </el-form-item>
          <el-form-item label="用户权限" label-width="auto">
            <el-checkbox-group v-model="addUserForm.roles">
              <el-checkbox v-for="role in defaultRole" :label="role">{{role}}</el-checkbox>
            </el-checkbox-group>
          </el-form-item>
          <el-form-item label="用户头像" label-width="auto">
            <el-input v-model="addUserForm.avatar" autocomplete="off" placeholder="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif" type="text"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
        <el-button size="mini" @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" size="mini" @click="addUser">确 定</el-button>
      </span>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import { getToken } from '@/utils/auth'
import { GetUserList, AddUser, DelUser } from '@/api/user'

const roles = ['root', 'yunwei']

export default {
  data() {
    return {
      tableData: [],
      dialogVisible: false,
      addUserForm: {
        name: null,
        pwd_one: null,
        pwd_tow: null,
        desc: null,
        roles: roles,
        avatar: "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
      },
      defaultRole: roles
    }
  },
  created() {
    this.getUsers()
  },
  methods: {
    getUsers() {
      const token = getToken()
      GetUserList(token).then(res => {
        this.tableData = res.data
        // console.log(this.tableData)
      }).catch(err => {
        console.log(err)
      })
    },
    roleList(row) {
      let roles = []
      row.roles.forEach(v => {
        roles.push(v)
      }) 
      return roles.join(' ')
    },
    handleClose(done) {
      done();
    },
    addUser() {
      this.$confirm("是否添加用户" + this.addUserForm.name, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        AddUser(this.addUserForm).then((response) => {
          if (response.code === 20000) {
            this.$message({
              message: "添加用户: " + this.addUserForm.name + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: "添加用户: " + this.addUserForm.name + " 失败!",
              type: "warning",
            });
          }
          this.dialogVisible = false;
        });
      });
    },
    handleDelete(index, row) {
      console.log(index, row)
      this.$confirm("是否删除用户" + row.name, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        DelUser(row).then((response) => {
          if (response.code === 20000) {
            this.$message({
              message: "删除用户: " + row.name + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: "删除用户: " + row.name + " 失败!",
              type: "warning",
            });
          }
          this.dialogVisible = false;
        });
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.u-table {
  margin-top: 80px;
  margin-left: 270px;
  .u-add {
    margin-top: 20px;
}
}


</style>
