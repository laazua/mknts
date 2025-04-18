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
      value-format="yyyy-MM-dd">>
    </el-date-picker>
    <el-input v-model="zone" size="small" placeholder="区服" style="width:120px;margin-left:10px"></el-input>
    <el-button type="primary" size="small" icon="el-icon-search" style="margin-left:10px" @click="countData">搜索</el-button>
    <el-table
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
    <el-table-column
        prop="date"
        label="日期"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="num"
        label="总注册数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="numCount"
        label="新增账号"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="countDau"
        label="账号DAU"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="payPercent"
        label="付费率"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="numPay"
        label="充值人数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="countPay"
        label="充值次数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="payMon"
        label="充值金额"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="arpu"
        label="ARPU"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="arppu"
        label="ARPPU"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="numPay"
        label="新增充值人数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="newPayMon"
        label="新增充值金额"
        width="auto">
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { CountData } from '@/api/operation'
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
  countData() {
    const data = {stime: this.value[0], etime: this.value[1], zone: this.zone}
    CountData(data).then(response => {
      console.log(response.data)
    })
  }
}
}
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