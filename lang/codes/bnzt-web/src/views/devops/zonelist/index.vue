<template>
  <div class="parent-box">
    <el-button type="primary" size="small" icon="el-icon-plus" @click="dialogZoneVisible = true">添加区服</el-button>
    <el-button type="primary" size="small" icon="el-icon-s-tools" style="margin-left: 50px" @click="manZone">执行操作</el-button>
    <el-select
    v-model="vtarget"
    size="small"
    style="margin-left: 10px; width: 120px"
    clearable
    placeholder="选择操作">
      <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.label"></el-option>
    </el-select>
    <el-dialog
    title="添加区服"
    :visible.sync="dialogZoneVisible"
    width="30%"
    :before-close="handleClose">
      <el-form>
        <el-form-item label="区服地址" label-width="auto">
          <el-input v-model="zoneForm.ip" autocomplete="off" placeholder="开服ip"></el-input>
        </el-form-item>
        <el-form-item label="区服名称" label-width="auto">
          <el-input v-model="zoneForm.channame" autocomplete="off" placeholder="区服名称"></el-input>
        </el-form-item>
        <el-form-item label="区服ID" label-width="auto">
          <el-input v-model="zoneForm.zone" autocomplete="off" placeholder="区服ID"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="small" @click="dialogZoneVisible = false">取 消</el-button>
        <el-button type="primary" size="small" @click="openZone">确 定</el-button>
      </span>
    </el-dialog>
    <el-table
    v-loading="loading"
    ref="multipleTable"
    :data="tableData"
    :key="ishow"
    tooltip-effect="dark"
    style="width: 100%; margin-top: 20px"
    @selection-change="handleSelectionChange"
    :row-class-name="tableRowClassName">
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column prop="zone" label="区服ID" width="auto"> </el-table-column>
      <el-table-column prop="channame" label="区服名称" width="auto"></el-table-column>
      <el-table-column prop="ip" label="区服IP" width="auto"> </el-table-column>
      <!-- <el-table-column prop="combine" label="合服标记" width="auto"></el-table-column> -->
      <el-table-column prop="state" label="结果状态" width="auto"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import { ZoneList, AddZone, ManZone } from "@/api/zone";
export default {
  data() {
    return {
      ishow: true,
      tableData: [],
      vtarget: "",
      dialogZoneVisible: false,
      zoneForm: {
        ip: "",
        channame: "",
        zone: null,
        target: "Open"
      },
      multipleSelection: [],
      options: [
        {
          value: "选项1",
          label: "Start",
        },
        {
          value: "选项2",
          label: "Stop",
        },
        {
          value: "选项3",
          label: "Check",
        },
        {
          value: "选项4",
          label: "UpdateCon",
        },
        {
          value: "选项5",
          label: "UpdateBin",
        },
        {
          value: "选项6",
          label: "Reload"
        }
      ],
      loading: false
    }
  },
  created() {
    this.zoneList()
  },
  methods: {
    handleClose(done) {
      done();
    },
    tableRowClassName(row, rowIndex) {
      if (rowIndex % 2 === 1) {
        return "warning-row"
      } else if (rowIndex % 2 === 0) {
        return "success-row"
      }
      return ""
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row)
        });
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val
    },
    zoneList() {
      ZoneList().then((response) => {
        // console.log(response.data)
        response.data.forEach(v => {
          this.tableData.push({
            zone: v.Zone,
            channame: v.ChanName,
            ip: v.Ip,
            state: ''
          })
        })
      });
    },
    openZone() {
      this.$confirm("是否添加区服" + this.zoneForm.channame + ':' + this.zoneForm.zone, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        AddZone(this.zoneForm).then((response) => {
          if (response.code === 200) {
            this.$message({
              message: "添加区服: " + this.zoneForm.channame + ':' + this.zoneForm.zone + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: "添加区服: " + this.zoneForm.channame + ':' + this.zoneForm.zone + " 失败!",
              type: "warning",
            });
          }
          this.dialogZoneVisible = false
        });
      });
    },
    manZone() {
      this.multipleSelection.forEach(v => {
        v['target'] = this.vtarget
        delete v['combine']
        delete v['state']
      })
      this.$confirm("所选区服是否执行: " + this.vtarget, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        const data = {"zones": this.multipleSelection}
        this.loading = true
        ManZone(data).then((response) => {
          // console.log(response)
          if (response.code === 200) {
            response.data.forEach(x => {
              this.tableData.forEach(y => {
                if (x.ChanName === y.channame && x.Zone === y.zone) {
                  y.state = x.Msg
                }
              })
            })
            this.loading = false
            this.ishow = !this.ishow
          } else {
            console.log(response.message)
          }
        })
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
