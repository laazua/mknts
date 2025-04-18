<template>
  <div class="parent-box">
    <el-date-picker
      v-model="value"
      type="daterange"
      size="small"
      align="right"
      format="yyyy-MM-dd"
      range-separator="至"
      start-placeholder="开始日期"
      end-placeholder="结束日期"
      value-format="yyyy-MM-dd">
    </el-date-picker>
    <el-input v-model="zone" size="small" placeholder="区服" style="width:120px;margin-left:10px"></el-input>
    <el-button type="primary" size="small" icon="el-icon-search" style="margin-left:10px" @click="gradeDist">搜索</el-button>
    <el-table
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
    <el-table-column
        prop="grade"
        label="等级"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="gradeNum"
        label="当前等级用户数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="percentNum"
        label="总用户占比(%)"
        width="auto">
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { GradeDist } from '@/api/operation'
import { GradeDistNum } from '@/utils/operation'
export default {
data() {
  return {
    value: '',
    tableData: [],
    zone: '',
    listLoading: false,
  }
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
  gradeDist() {
    const data = {stime: this.value[0], etime: this.value[1], zone: this.zone}
    GradeDist(data).then(response => {
      console.log(response)
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