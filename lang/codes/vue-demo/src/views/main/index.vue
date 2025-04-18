<template>
  <el-container style="height: 100%">
    <el-aside width="auto">
      <comm-aside></comm-aside>
    </el-aside>
    <el-container>
      <el-header>
        <comm-header></comm-header>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import CommAside from '../../components/CommAside.vue'
import CommHeader from '../../components/commHeader.vue'
export default {
  components: {
    CommAside,
    CommHeader
  },
  data() {
    return {}
  }
}
</script>

<style lang='less' scoped>
.el-header {
  background: #333;
}
.le-aside {
  background: #333;
}
.el-main {
  padding-top: 0;
}
</style>