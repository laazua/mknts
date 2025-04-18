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
    <el-button type="primary" size="small" icon="el-icon-search" style="margin-left:10px" @click="rollsData">搜索</el-button>
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
        prop="roleNum"
        label="创角数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="rollNum"
        label="滚服创建数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="rollPercent"
        label="滚服创建占比"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="payNum"
        label="充值人数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="rollPayNum"
        label="滚服充值人数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="rollPayPercent"
        label="滚服充值人数占比"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="payMon"
        label="充值金额"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="rollPayMon"
        label="滚服充值金额"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="rollMonPercent"
        label="滚服充值金额占比"
        width="auto">
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
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
  rollsData() {
    
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