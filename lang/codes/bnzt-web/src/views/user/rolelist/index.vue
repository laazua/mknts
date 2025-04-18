<template>
  <div class="parent-box">
    <el-button
      type="primary"
      size="small"
      icon="el-icon-plus"
      @click="dialogVisible = true"
      >新增角色</el-button
    >
    <el-dialog
      title="新增用户"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <el-form>
        <el-form-item label="角色名称" label-width="auto">
          <el-input
            v-model="form.name"
            autocomplete="off"
            placeholder="rolename"
          ></el-input>
        </el-form-item>
        <el-form-item label="角色描述" label-width="auto">
          <el-input
            v-model="form.desc"
            autocomplete="off"
            placeholder="管理员"
          ></el-input>
        </el-form-item>
        <el-form-item label="角色菜单" label-width="auto">
          <el-input
            v-model="form.menu"
            autocomplete="off"
            placeholder="[user, operation, player]"
          ></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="small" @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" size="small" @click="addRole"
          >确 定</el-button
        >
      </span>
    </el-dialog>
    <el-table
      :data="tableData"
      style="width: 100%"
      :row-class-name="tableRowClassName"
    >
      <el-table-column prop="id" label="ID" width="auto"> </el-table-column>
      <el-table-column prop="name" label="角色名称" width="auto">
      </el-table-column>
      <el-table-column prop="roledesc" label="角色描述" width="auto">
      </el-table-column>
      <el-table-column prop="menu" label="拥有权限" width="auto">
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="auto">
        <template slot-scope="scope">
          <el-tooltip
            class="item"
            effect="dark"
            content="在数据库中删除记录"
            placement="top"
          >
            <el-button
              type="danger"
              size="mini"
              icon="el-icon-delete"
              @click="delRole(scope.row)"
              >删除</el-button
            >
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { GetRoleList, DelRole, AddRole } from "@/api/index";
export default {
  data() {
    return {
      dialogVisible: false,
      tableData: [],
      form: {
        name: "",
        desc: "",
        menu: "",
      },
    };
  },
  created() {
    this.roleList();
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
    roleList() {
      GetRoleList().then((response) => {
        response.data.forEach((v) => {
          this.tableData.push({
            id: v.ID,
            name: v.Rolename,
            roledesc: v.Roledesc,
            menu: v.MainMenu,
          });
        });
      });
    },
    addRole() {
      this.$confirm("是否添加" + this.form.name, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        AddRole(this.form).then((response) => {
          if (response.code === 200) {
            this.$message({
              message: "添加角色: " + this.form.name + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: "删除角色: " + this.form.name + " 失败!",
              type: "warning",
            });
          }
          this.dialogVisible = false;
        });
      });
    },
    delRole(row) {
      this.$confirm("是否删除" + row.name, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        DelRole(row).then((response) => {
          if (response.code === 200) {
            this.$message({
              message: "删除角色: " + row.name + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: "删除角色: " + row.name + " 失败!",
              type: "warning",
            });
          }
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