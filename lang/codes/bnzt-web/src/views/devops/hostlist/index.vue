<template>
  <div>
    <el-button type="primary" size="small" icon="el-icon-s-data" style="margin-left:20px;margin-top:20px" @click="getHostData">主机资源</el-button>
    <el-table 
    :data="hostData" 
    v-loading="listLoading" border strip 
    ref="multipleTable" 
    tooltip-effect="dark"
    style="width:100%; margin:20px">
      <el-table-column align="center" label="主机IP" prop="ip"></el-table-column>
      <el-table-column align="center" label="cpu使用率" prop="cpu"></el-table-column>
      <el-table-column align="center" label="内存使用率" prop="mem"></el-table-column>
      <el-table-column align="center" label="磁盘使用率" prop="disk"></el-table-column>
      <el-table-column align="center" label="主机负载" prop="load"></el-table-column>
      <el-table-column align="center" label="网络连接数量" prop="netnum"></el-table-column>
      <el-table-column align="center" label="开服数量" prop="num"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import { ZoneList, GetHostData } from "@/api/zone";
export default {
  data() {
    return {
      hostData: [],
      listLoading: false,
      ips: []
    }
  },
  created() {
    this.zoneList()
  },
  methods: {
    zoneList() {
      ZoneList().then((response) => {
        // console.log(response.data)
        response.data.forEach(v => {
          this.ips.push(v.Ip)
        })
        this.ips = Array.from(new Set(this.ips))
        // console.log(this.ips)
      })
    },
    getHostData() {
      this.listLoading = true
      const data = { ips: this.ips }
      this.hostData = []
      GetHostData(data).then((response) => {
        // console.log(response.data)
        response.data.forEach(v => {
          this.hostData.push({
            ip: v.Ip,
            cpu: v.C.PerPercent[0].toFixed(2),
            mem: v.M.Percent.toFixed(2),
            disk: v.D.Percent.toFixed(2),
            load: v.L.L5,
            netnum: v.N.IoConn.length,
            num: v.Num
          })
        })
        this.listLoading = false
      })
    }
  }
}
</script>

<style>

</style>