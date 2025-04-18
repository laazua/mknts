<template>
  <div class="parent-box">
    <el-button type="primary" size="small" icon="el-icon-plus" @click="dialogAddUserVisible = true">新增用户</el-button>
    <el-dialog
    title="新增用户"
    :visible.sync="dialogAddUserVisible"
    width="30%"
    :before-close="handleClose">
      <el-form>
        <el-form-item  label="用户名称" label-width="auto">
          <el-input v-model="addForm.name" autocomplete="off" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item label="用户密码" label-width="auto">
          <el-input v-model="addForm.passone" autocomplete="off" type="password" placeholder="password"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" label-width="auto">
          <el-input v-model="addForm.passtow" autocomplete="off" type="password" placeholder="password"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="small" @click="dialogAddUserVisible = false">取 消</el-button>
        <el-button type="primary" size="small" @click="addUser">确 定</el-button>
      </span>
    </el-dialog>
    <el-table
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
      <el-table-column prop="id" label="ID" width="auto"> </el-table-column>
      <el-table-column prop="name" label="用户名称" width="auto"></el-table-column>
      <el-table-column prop="roles" label="用户所属角色" width="auto"></el-table-column>
      <el-table-column fixed="right" label="操作" width="auto">
        <template slot-scope="scope">
          <el-tooltip class="item" effect="dark" content="删除该用户在数据库中的记录" placement="top">
            <el-button type="danger" size="mini" icon="el-icon-delete" @click="delUser(scope.row)">删除</el-button>
          </el-tooltip>
          <el-tooltip class="item" effect="dark" content="更新数据库中的字段:[username, hspass, rolename]" placement="top">
            <el-button type="warning" size="mini" icon="el-icon-edit" @click="dialogUpdUserVisible = true">更新</el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
    title="更新用户"
    :visible.sync="dialogUpdUserVisible"
    width="30%"
    :before-close="handleClose">
      <el-form>
        <el-form-item label="用户名称" label-width="auto">
          <el-input v-model="updForm.name" autocomplete="off" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item label="字段名称" label-width="auto">
          <el-input v-model="updForm.column" autocomplete="off" placeholder="可更新的字段:[username, hspass, rolename]"></el-input>
        </el-form-item>
        <el-form-item label="字段内容" label-width="auto">
          <el-input v-model="updForm.value" autocomplete="off" placeholder="字段对应的值"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="small" @click="dialogUpdUserVisible = false">取 消</el-button>
        <el-button type="primary" size="small" @click="updUser">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { GetUserLists, AddUser, UpdateUser, DelUser } from "@/api/index";
export default {
  data() {
    return {
      tableData: [],
      dialogAddUserVisible: false,
      dialogUpdUserVisible: false,
      addForm: {
        name: "",
        passone: "",
        passtow: "",
      },
      updForm: {
        name: "",
        column: "",
        value: "",
      },
    };
  },
  created() {
    this.userList();
  },
  methods: {
    handleClose(done) {
      done();
    },
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex % 2 === 1) {
        return "warning-row";
      } else if (rowIndex % 2 === 0) {
        return "success-row";
      }
      return "";
    },
    userList() {
      GetUserLists().then((response) => {
        response.data.forEach((v) => {
          this.tableData.push({ id: v.ID, name: v.Username, roles: v.Role });
        });
      });
    },
    addUser() {
      this.$confirm("是否添加用户" + this.addForm.name, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        AddUser(this.addForm).then((response) => {
          if (response.code === 200) {
            this.$message({
              message: "添加用户: " + this.addForm.name + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: "添加用户: " + this.addForm.name + " 失败!",
              type: "warning",
            });
          }
          this.dialogAddUserVisible = false;
        });
      });
    },
    delUser(row) {
      this.$confirm("是否删除" + row.name, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        DelUser(row).then((response) => {
          if (response.code === 200) {
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
        });
      });
    },
    updUser() {
      this.$confirm("是否更新用户" + this.updForm.name, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        UpdateUser(this.updForm).then((response) => {
          if (response.code === 200) {
            this.$message({
              message: this.updForm.name + "更新成功" + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: this.updForm.name + "更新失败" + " 失败!",
              type: "warning",
            });
          }
          this.dialogUpdUserVisible = false;
        });
      });
    },
  },
};
</script>
<style scoped>
.parent-box {
  margin: 40px;
}
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>