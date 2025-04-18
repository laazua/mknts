<template>
  <div class="item-cd">
    <el-button type="primary" size="mini" icon="el-icon-s-data" style="margin-left:10px;margin-top:20px" @click="getHostResource">主机资源</el-button>
    <el-row :gutter="20">
    <el-col :span="6" v-for="item in hostData">
      <el-card>
        <el-row :gutter="20">
          <el-col :span="24">
            <div class="item-ip">IP: {{item.ip}}</div>
          </el-col>
          <el-col :span="12">
            <el-progress width=80 stroke-width=2 style="margin-left:25px" type="dashboard" color="red" :percentage="item.node.cpu"></el-progress>
          </el-col>
          
          <el-col :span="12">
            <el-progress width=80 stroke-width=2 type="dashboard" color="green" :percentage="item.node.mem">mem</el-progress>
          </el-col>
       
          <el-col>
            <a style="margin-left:50px">cpu</a>
            <a style="margin-left:96px">disk</a>
          </el-col>
        
          <el-col :span="12">
            <el-progress width=80 stroke-width=2 style="margin-left:25px" type="dashboard" color="blue" :percentage="item.node.disk">disk</el-progress>
          </el-col>
          
          <el-col :span="12">
            <el-progress width=80 stroke-width=2 type="dashboard" :percentage="item.node.load">load</el-progress>
          </el-col>
        
          <el-col :span="12">
            <a style="margin-left:50px">mem</a>
            <a style="margin-left:90px">load</a>
          </el-col>
        
        </el-row>
      </el-card>
    </el-col>
  </el-row>
  </div>
</template>

<script>
import { GetHostResource } from '@/api/host'

export default {
  data() {
    return {
      hostData: [],
      loading: false
    }
  },
  methods: {
    getHostResource() {
      GetHostResource().then(res => {
        this.hostData = res.data
        console.log(this.hostData)
      }).catch(err => {
        console.log(err)
      })
    }
  },
}

</script>

<style lang="scss" scoped>
.item-cd {
  width: 80%;
  margin-top: 18px;
  margin-left: 180px;
  .el-card {
    width: 100%;
  }
  .item-ip{
    margin-left: 62px;
  }
}
</style>