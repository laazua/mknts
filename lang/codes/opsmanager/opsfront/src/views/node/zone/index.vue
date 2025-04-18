<template>
  <div class="parent-box">
    <el-button type="primary" size="mini" icon="el-icon-plus" @click="dialogZoneVisible = true">添加区服</el-button>
    <el-button type="primary" size="mini" icon="el-icon-s-tools" style="margin-left: 50px" @click="manZone">执行操作</el-button>
    <el-select
    v-model="vtarget"
    size="small"
    style="margin-left: 10px; width: 120px"
    clearable
    placeholder="选择操作">
      <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.label"></el-option>
    </el-select>
    <el-input v-model="svnversion" autocomplete="off" placeholder="更新配置时,svn配置版本号" size="small" style="width:210px;margin-left:10px"></el-input>
    <el-button type="primary" size="mini" icon="el-icon-refresh-right" style="margin-left:100px" @click="getTaskRes">获取结果</el-button>
    <el-dialog
    title="添加区服"
    :visible.sync="dialogZoneVisible"
    width="30%"
    :before-close="handleClose">
      <el-form v-loading="loading">
        <el-form-item label="区服地址" label-width="auto">
          <el-input v-model="zoneForm.zone[0].ip" autocomplete="off" placeholder="开服ip"></el-input>
        </el-form-item>
        <el-form-item label="区服名称" label-width="auto">
          <el-input v-model="zoneForm.zone[0].name" autocomplete="off" placeholder="区服名称"></el-input>
        </el-form-item>
        <el-form-item label="区服ID" label-width="auto">
          <el-input v-model="zoneForm.zone[0].number" autocomplete="off" placeholder="区服ID"></el-input>
        </el-form-item>
        <el-form-item label="svn配置版本号" label-width="auto">
           <el-input v-model="zoneForm.zone[0].svnversion" autocomplete="off" placeholder="svn配置版本号"></el-input>
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
    size="mini"
    :cell-style="{ textAlign: 'center' }"
    :header-cell-style="{ textAlign: 'center' }"
    :data="tableData"
    stripe
    :key="ishow"
    tooltip-effect="dark"
    style="width: 100%; margin-top: 20px;"
    @selection-change="handleSelectionChange"
    :row-class-name="tableRowClassName">
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column prop="number" label="区服ID" width="auto"> </el-table-column>
      <el-table-column prop="name" label="区服名称" width="auto"></el-table-column>
      <el-table-column prop="ip" label="区服IP" width="auto"> </el-table-column>
      <!-- <el-table-column prop="combine" label="合服标记" width="auto"></el-table-column> -->
      <el-table-column prop="state" label="结果状态" width="auto"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import { ZoneList, ManZone, GetTasks } from "@/api/zone";
export default {
  data() {
    return {
      ishow: true,
      tableData: [],
      vtarget: "",
      dialogZoneVisible: false,
      svnversion: "",
      zoneForm: {
        zone: [{ip: "", name: "", number: "", target: "addition", svnversion: this.svnversion}],
      },
      multipleSelection: [],
      options: [
        {
          value: "选项2",
          label: "updatebin",
        },
        {
          value: "选项3",
          label: "updatecon",
        },
        {
          value: "选项4",
          label: "start",
        },
        {
          value: "选项5",
          label: "check",
        },
        {
          value: "选项6",
          label: "stop",
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
        console.log(response.data)
        response.data.forEach(v => {
          this.tableData.push({
            number: v.number,
            name: v.name,
            ip: v.ip,
            state: ''
          })
        })
      });
    },
    openZone() {
      this.$confirm("是否添加区服" + this.zoneForm.zone[0].name + ':' + this.zoneForm.zone[0].number, "提示", {
        confirmButtonText: "是",
        cancelButtonText: "否",
        type: "warning",
      }).then(() => {
        // console.log(this.zoneForm)
        this.loading = true
        ManZone(this.zoneForm).then((response) => {
          if (response.code === 20000) {
            this.$message({
              message: "添加区服: " + this.zoneForm.zone[0].name + ':' + this.zoneForm.zone[0].number + " 成功!",
              type: "success",
            });
          } else {
            this.$message({
              message: "添加区服: " + this.zoneForm.zone[0].name + ':' + this.zoneForm.zone[0].number + " 失败!",
              type: "warning",
            });
          }
          this.loading = false
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
        const data = {"zone": this.multipleSelection, "target": this.vtarget}
        console.log("xxxxxxxxxxxxxx", data)
        this.loading = true
        // console.log(data)
        ManZone(data).then((response) => {
          // console.log(response.data)
          // console.log(this.tableData)
          if (response.code === 20000) {
            // response.data.forEach(x => {
            //   this.tableData.forEach(y => {
            //     if (x.name === y.name && x.number === y.number) {
            //       y.state = x.msg
            //     }
            //   })
            // })
            console.log("xxxx", response.data)
            this.loading = false
            this.ishow = !this.ishow
          } else {
            console.log(response.msg)
          }
        })
      })
    },
    getTaskRes() {
      console.log("aaaaaaaaaaaa")
      GetTasks().then((response) => {
        if (response.code === 20000) {
          response.data.forEach(x => {
            this.tableData.forEach(y => {
              if (x.name === y.name && x.number === y.number) {
                y.state = x.result
              }
            })
          })
        }
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