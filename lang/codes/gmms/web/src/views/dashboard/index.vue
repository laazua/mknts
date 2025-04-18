<template>
  <div class="dashboard-container">
    <div class="ds-item">
      <h3>欢迎来到运维管理平台</h3>
      <h4 class="h4">== 使用说明手册 ==</h4>
      <p class="item">1. 用户管理 </p>
      <p class="des">A. 添加用户</p>
      <p class="des">B. 删除用户</p>
      <p class="des">C. 用户日志查询</p>
      <p class="item">2. 游戏管理 </p>
      <p class="des">A. 游戏开服</p>
      <p class="des">B. 资源更新</p>
      <p class="srcup">a. 先更新资源</p>
      <p class="srcup">b. 再更新区服</p>
      <p class="des">C. 区服管理</p>
      <p class="srcup">a. 区服启动</p>
      <p class="srcup">b. 区服关闭</p>
      <p class="srcup">c. 区服更新</p>
      <p class="srcup">d. 区服检查</p>
      <p class="item">3. 主机管理 </p>
      <p class="des">A. 主机资源状态</p>
    </div>
    <!-- <el-calendar v-model="value"></el-calendar> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      value: new Date()
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.h4 {
  margin-top: 30px;
  margin-left: 20px;
}
.item {
  margin-left: 40px;
}
.des {
  margin-left: 56px;
}
.srcup {
  margin-left: 76px;
}
</style>
