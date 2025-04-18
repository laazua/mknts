<template>
  <div class="parent-box">
    <el-tooltip class="item" effect="dark" content="开发人员操作此功能" placement="right">
      <el-button type="primary" size="small" icon="el-icon-plus" @click="dialogVisible = true">新增权限</el-button>
    </el-tooltip>
    <el-dialog
    title="新增用户"
    :visible.sync="dialogVisible"
    width="30%"
    :before-close="handleClose">
      <el-form>
        <el-form-item label="权限名称" label-width="auto">
          <el-input v-model="form.permdesc" autocomplete="off" placeholder="[user,operation,player]"></el-input>
        </el-form-item>
        <el-form-item label="父 路 径" label-width="auto">
          <el-input v-model="form.namepath" autocomplete="off" placeholder="[/user,/operation,/player]"></el-input>
        </el-form-item>
        <el-form-item label="权限描述" label-width="auto">
          <el-input v-model="form.subdesc" autocomplete="off" placeholder="[用户列表,角色列表,...]"></el-input>
        </el-form-item>
        <el-form-item label="子 路 径" label-width="auto">
          <el-input v-model="form.subpath" autocomplete="off" placeholder="[/user, /role, /perm]"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="small" @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" size="small" @click="addPerm">确 定</el-button>
      </span>
    </el-dialog>
    <el-table
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
      <el-table-column
      prop="id"
      label="ID"
      width="auto">
      </el-table-column>
    <el-table-column
        prop="name"
        label="权限名称"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="mmenu"
        label="父路径"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="smenu"
        label="子路径"
        width="auto">
    </el-table-column>
    <el-table-column
        fixed="right"
        label="操作"
        width="auto">
        <template slot-scope="scope">
          <el-tooltip class="item" effect="dark" content="开发人员操作此功能" placement="top">
            <el-button type="danger" size="mini" icon="el-icon-delete" @click="delPerm(scope.row)">删除</el-button>
          </el-tooltip>
        </template>
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { GetPermList, AddPerm, DelPerm } from "@/api/index"
export default {
data() {
  return{
    tableData: [],
    dialogVisible: false,
    form: {
      permdesc: '',
      namepath: '',
      subdesc: '',
      subpath: ''
    }
  }
},
created() {
  this.permList()
},
methods: {
  handleClose(done) {
    done()
  },
  tableRowClassName({row, rowIndex}) {
    if (rowIndex % 2 === 1) {
      return 'warning-row';
    } else if (rowIndex % 2 === 0) {
      return 'success-row';
    }
    return '';
  },
  permList() {
    GetPermList().then(response => {
      // console.log(response.data)
      response.data.forEach(v => {
        this.tableData.push({id: v.ID, name: v.Permdesc, mmenu: v.Namepath, smenu: v.Subpath})
      })
    })
  },
  addPerm() {
    this.$confirm("是否添加" + this.form.permdesc, "提示", {
      confirmButtonText: "是",
      cancelButtonText: "否",
      type: "warning"
    }).then(() => {
      AddPerm(this.form).then(response => {
        if (response.code === 200) {
          this.$message({message: "添加权限: " + this.form.permdesc + " 成功!", type: "success"})
        } else {
          this.$message({message: "添加权限: " + this.form.permdesc + " 失败!", type: "warning"})
        }
        this.dialogVisible = false
      })
    })
  },
  delPerm() {
    this.$confirm("是否删除" + row.name, "提示", {
      confirmButtonText: "是",
      cancelButtonText: "否",
      type: "warning"
    }).then(() => {
      DelPerm(row).then(response => {
        if (response.code === 200) {
          this.$message({message: "删除权限: " + row.name + " 成功!", type: "success"})
        } else {
          this.$message({message: "删除权限: " + row.name + " 失败!", type: "warning"})
        }
      })
    })
  }
}
}
</script>

<style>
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