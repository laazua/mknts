<template>
  <div class="block">
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="姓名"
        width="320">
      </el-table-column>
      <el-table-column
        prop="action"
        label="操作"
        width="320">
      </el-table-column>
      <el-table-column
        prop="ctime"
        label="日期"
        width="320">
      </el-table-column>
    </el-table>
    <el-input v-model="value" size="mini" style="width:200px; margin-top:20px" placeholder="查询名字"></el-input>
    <el-button type="primary" size="mini" style="margin-left:10px" @click="getLog">查询</el-button>
  </div>
</template>

<script>
// import { getToken } from '@/utils/auth'
import { GetLog } from '@/api/log'

export default {
  data() {
    return {
      value: null,
      tableData: null,
    }
  },
  methods: {
    getLog() {
      console.log(this.value)
      GetLog(this.value).then(res => {
        this.tableData = res.data
      }).catch(err => {
        console.log(err)
      })
    }
  },

}
</script>

<style>
.block {
  margin-top: 80px;
  margin-left: 320px;
}
</style>