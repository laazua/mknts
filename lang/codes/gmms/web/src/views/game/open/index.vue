<template>
  <div>
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="项目创建" name="createpro">
        <el-form :model="form1">
          <el-form-item label="项目名称">
            <el-input v-model="form1.proname" utocomplete="off" placeholder="syf"></el-input>
          </el-form-item>
          <el-button type="primary" @click="createPro">提交</el-button>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="游戏开服" name="openGame">
        <el-form :model="form2">
          <el-form-item label="IP地址">
            <el-input v-model="form2.ip" autocomplete="off" placeholder="127.0.0.1"></el-input>
          </el-form-item>
          <el-form-item label="区服ID">
            <el-input v-model="form2.serverid" autocomplete="off" placeholder="1"></el-input>
          </el-form-item>
          <el-form-item label="项目名称">
            <el-input v-model="form2.proname" autocomplete="off" placeholder="syf_test"></el-input>
          </el-form-item>
          <el-button type="primary" @click="openServe">提交</el-button>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import { createProName, openServeZone } from "@/api/index"
export default {
  data() {
    return {
      form1: {
        proname: null,
      },
      form2: {
        ip: null,
        serverid: null,
        proname: null
      },
      activeName: "createpro"
    }
  },
  methods: {
    handleClick(tab, event) {
      // console.log(tab, event);
    },
    openServe() {
      // console.log(this.form2)
      this.$confirm("是否创建项目: " + this.form2.proname + "_" + this.form2.serverid, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning"
      }).then(() => {
        openServeZone(this.form2).then(response => {
          if (response.code === 200) {
            this.$message({message: "开服: " + this.form2.proname + "_" + this.form2.serverid + " 成功!", type: "success"})
          } else {
            this.$message({message: "开服: " + this.form2.proname + "_" + this.form2.serverid + " 成功!", type: "warning"})
          }
        })
      })
    },
    createPro() {
      this.$confirm("是否创建项目: " + this.form1.proname, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning"
      }).then(() => {
        createProName(this.form1).then(response => {
          if (response.code === 200) {
            this.$message({message: "创建项目: " + this.form1.proname + " 成功!", type: "success"})
          } else {
            this.$message({message: "创建项目: " + this.form1.proname + " 成功!", type: "warning"})
          }
        })
      })
    }
  }
}
</script>

<style>
.el-tabs {
  margin:30px
}
.el-form {
  margin-top: 70px;
  margin-left: 500px;
  margin-right: 500px;
}
/* .el-button {
  margin-left: 560px;
} */
</style>