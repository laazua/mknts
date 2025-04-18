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
      end-placeholder="结束日期">
    </el-date-picker>
    <el-input v-model="zone" size="small" placeholder="区服" style="width: 120px; margin-left: 10px"></el-input>
    <el-button type="primary" size="small" icon="el-icon-search" style="margin-left: 10px" @click="recharank">搜索</el-button>
    <el-table
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
      <el-table-column prop="id" label="区服ID" width="auto"> </el-table-column>
      <el-table-column prop="uid" label="玩家ID" width="auto"></el-table-column>
      <el-table-column prop="chargeNum" label="充值次数" width="auto"></el-table-column>
      <el-table-column prop="chargeSum" label="充值金额" width="auto"></el-table-column>
      <el-table-column prop="chargeTime" label="最后充值时间" width="auto"></el-table-column>
    </el-table>
    <!-- 分页
    <el-pagination
    style="margin-top: 10px"
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
    :current-page="page.num"
    :page-sizes="[10, 15, 20, 50, 100]"
    :page-size="page.size"
    layout="total, sizes, prev, pager, next, jumper"
    :total="total">
    </el-pagination> -->
  </div>
</template>

<script>
import { Recharank } from "@/api/operation";
export default {
  data() {
    return {
      value: "",
      tableData: [],
      zone: "",
      listLoading: false,
    };
  },
  methods: {
    handleClose(done) {
      done();
    },
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex % 2 === 1) {
        return "warning-row";
      } else if (rowIndex % 2 === 0) {
        return "success-row";
      }
      return "";
    },
    handleSizeChange(newSize) {
      this.page.size = newSize;
      this.recharank();
    },
    handleCurrentChange(newPage) {
      this.page.num = newPage;
      this.recharank();
    },
    recharank() {
      const data = {
        stime: this.value[0],
        etime: this.value[1],
        zone: this.zone,
      };
      this.listLoading = true;
      Recharank(data).then((response) => {
        // console.log(data)
        // console.log(response.data.aggregations.payNum.buckets)
        if (response.code === 200 && response.data.aggregations.payNum.buckets !== 0) {
          this.tableData = []
          response.data.aggregations.payNum.buckets.forEach((v) => {
            this.tableData.push({
              id: this.zone,
              uid: v.key,
              chargeNum: v.doc_count,
              chargeSum: v.paySum.value,
              chargeTime: v.time.value_as_string,
            });
          });
          this.total = response.data.hits.total.value
          this.listLoading = false
        }
      });
    },
  },
};
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