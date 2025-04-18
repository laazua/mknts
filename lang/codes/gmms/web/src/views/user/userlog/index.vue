<template>
  <div>
    <el-select v-model="value" clearable placeholder="选择用户">
      <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
    </el-select>
    <el-date-picker v-model="value1" align="right" type="date" placeholder="选择日期" :picker-options="pickerOptions" class="date-sel"></el-date-picker>
    <el-button type="primary" @click="queryUserLog">用户日志查询</el-button>
    <el-table :data="tableData">
      <el-table-column prop="username" label="姓名"></el-table-column>
      <el-table-column prop="record" label="操作"></el-table-column>
      <el-table-column prop="time" label="时间"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getUserLists, getUserLog } from "@/api/index" 
export default {
  data() {
    return {
      tableData: null,
      value: "",
      value1: "",
      options: [],
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now()
        },
        shortcuts: [
          {
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date())
            }
          }, 
          {
            text: '昨天',
            onClick(picker) {
              const date = new Date()
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date)
            }
          }, 
          {
            text: '一周前',
            onClick(picker) {
              const date = new Date()
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date)
            }
          }
        ]
      }
    }
  },
  created() {
    this.getUsers()
  },
  methods: {
    GmtToStr(time) {
      let date = new Date(time)
      let str = date.getFullYear() + '-' + (date.getMonth() + 1) + '-' 
                + date.getDate()
      return str
    },
    getUsers() {
      getUserLists().then(response => {
        response.data.forEach(v => {
          this.options.push({value: v.username, label: v.username})
        })
      })
    },
    queryUserLog() {
      const data = { username: this.value, datetime: this.GmtToStr(this.value1) }
      getUserLog(data).then(response => {
        this.tableData = response.data
      })
    }
  }
}
</script>

<style>
.el-select {
  margin-left: 20px;
  margin-top: 30px;
}
.el-button {
  margin-left: 10px;
  margin-top: 30px;
}
.el-table {
  margin-left:20px;
  margin-top: 20px;
}
.date-sel {
  margin-left: 10px;
  margin-top: 30px;
}
.el-table-column {
  width: auto;
}
</style>