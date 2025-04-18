<template>
  <div>
    <el-select v-model="value1" clearable placeholder="项目选择">
      <el-option v-for="item in options1" :key="item.value" :label="item.label" :value="item.value"></el-option>
    </el-select>
    <el-button type="primary" @click="fetchZones">提交</el-button>
    <el-select v-model="value2" clearable placeholder="执行操作">
      <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value"></el-option>
    </el-select>
    <el-button type="primary" border strip ref="multipleTable"  tooltip-effect="dark" @click="zoneopt">提交</el-button>
    <el-table :data="tableData" @selection-change="handleSelectionChange" multiple="true">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="server_id" label="区服ID"></el-table-column>
      <el-table-column prop="server_name" label="渠道名称"></el-table-column>
      <el-table-column prop="server_ip" label="区服IP"></el-table-column>
      <el-table-column prop="cmdStatus" label="命令状态"></el-table-column>
    </el-table>
    <!-- 分页区域 -->
    <!-- <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
      :current-page="pageNum" :page-sizes="[10, 20, 50, 100]" :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper" :total="total">
    </el-pagination> -->
  </div>
</template>

<script>
import { getProNames, getZones, zoneCmd } from "@/api/index"
import { title } from '@/settings'
export default {
  data() {
    return {
      tableData: null,
      value1: null,
      value2: null,
      options1: [],
      options2: [
        {
          value: 'check',
          label: '区服检查'
        },
        {
          value: 'start',
          label: '区服启动'
        },
        {
          value: 'stop',
          label: '区服关闭'
        },
        {
          value: 'upconf',
          label: '区服配置更新'
        },
        {
          value: 'upbin',
          label: '区服bin更新'
        }
      ],
      pageNum: 1,
      pageSize: 20,
      multipleSelection: null,
      total: 0,
      retData: null
    }
  },
  created() {
    this.fetchPro()
    // this.fetchZones()
  },
  methods: {
    fetchPro() {
      getProNames().then(response => {
        if (response.code !== 200) {
          this.$message({message: "获取项目信息失败!"})
        } else {
          response.data.forEach(v => {
            this.options1.push({value: v, label: v})
          });
        }
      })
    },
    handleCurrentChange(newPage) {
      this.pageSize = newPage
      this.fetchZones()
    },
    handleSelectionChange(value) {
      this.multipleSelection = value
    },
    handleSizeChange(newSize) {
      this.pageSize = newSize
      this.fetchZones()
    },
    fetchZones() {
      const data = { pageNum: this.pageNum, pageSize: this.pageSize, tb: this.value1 }
      // console.log(data)
      getZones(data).then(response => {
        if (response.code !== 200) {
          this.$message({message: "获取区服信息失败!"})
        } else {
          this.tableData = response.data
        }
      })
    },
    zoneopt() {
      // console.log(this.value2)
      // console.log(this.multipleSelection)
      this.$confirm("是否" + this.value2 + "区服", "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning"
      }).then(() => {
        const data = { zones: this.multipleSelection, cmd: this.value2 }
        zoneCmd(data).then(response => {
          if (response.code !== 200) {
            this.$message({message: this.value2 + "区服失败!"})
          } else {
            this.$message({message: this.value2 + "区服成功!"})
            this.retData = response.data
            this.cmdStatus()
            console.log(response.data)
          }
        })
      })
    },
    cmdStatus(){
      for(let i = 0;i<this.tableData.length; i++) {
        for(let j=0;j<this.retData.length; j++) {
          if(this.tableData[i].server_id === this.retData[j].server_id) {
            this.tableData[i].cmdStatus = this.retData[j].msg
            break
          }
        }
      }
    }
  }
}
</script>

<style>
.el-select {
  margin: 20px;
}
.el-table {
  margin: 20px;
}
.el-pagination {
  margin: 5px;
}
</style>