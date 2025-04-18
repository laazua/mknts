<template>
  <div>
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="svn资源更新" name="svnup">
        <el-select v-model="value" clearable placeholder="项目选择">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
        <el-button type="primary" @click="svnUpdate">提交</el-button>
        <el-table :data="tableData">
          <el-table-column prop="host" label="主机"></el-table-column>
          <el-table-column prop="result" label="结果"></el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="bin文件更新" name="binup">
        <div>bin file up</div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import { getProNames, svnUpHost } from "@/api/index"
export default {
  data() {
    return {
      tableData: [],
      options: [],
      value: null,
      activeName: "svnup"
    }
  },
  created() {
    this.getProName()
  },
  methods: {
    handleClick(tab, event) {
      // console.log(tab, event);
    },
    getProName() {
      getProNames().then(response => {
        if (response.code !== 200) {
          this.$message({message: "获取项目信息失败!"})
        } else {
          response.data.forEach((v) => {
            this.options.push({value: v, label: v})
          });
        }
      })
    },
    svnUpdate() {
      this.$confirm("是否更新svn资源", "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning"
      }).then(() => {
        const data = { tb: this.value }
        svnUpHost(data).then(response => {
        if (response.code === 200) {
          response.data.forEach(value => {
            this.tableData.push({host: value[0], result: value[1]})
          })
        }
      })
      })
    }
  }
};
</script>

<style scoped>
.el-tabs {
  margin: 40px;
  height: 890px;
}
.el-select {
  margin: 20px;
}
</style>