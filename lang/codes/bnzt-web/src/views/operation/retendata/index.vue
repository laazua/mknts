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
    <el-button type="primary" size="small" icon="el-icon-search" style="margin-left:10px" @click="retenData">搜索</el-button>
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
        prop="newNum"
        label="新增账号登陆数"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="countDau"
        label="账号DAU"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="oldCount"
        label="老用户"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="towDay"
        label="2日"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="threeDay"
        label="3日"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="fiveDay"
        label="5日"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="seveDay"
        label="7日"
        width="auto">
    </el-table-column>
    <el-table-column
        prop="fiftyDay"
        label="15日"
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
  retenData() {
    
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