<template>
  <el-menu
    router
    :default-active="$route.path"
    class="sidebar-menu"
    :collapse="isCollapsed"
    :collapse-transition="false"
  >
    <div v-for="route in routes" :key="route.path">
      <el-sub-menu v-if="route.children && route.children.length > 0" :index="route.path">
        <template #title>
          <el-icon><component :is="route.meta.icon" /></el-icon>
          <span>{{ route.meta.title }}</span>
        </template>
        <el-menu-item v-for="child in route.children" :key="child.path" :index="`${route.path}/${child.path}`">
          <el-icon><component :is="child.meta.icon" /></el-icon>
          <span>{{ child.meta.title }}</span>
        </el-menu-item>
      </el-sub-menu>
      <el-menu-item v-else :index="route.path">
        <el-icon><component :is="route.meta.icon" /></el-icon>
        <span>{{ route.meta.title }}</span>
      </el-menu-item>
    </div>
  </el-menu>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  isCollapsed: {
    type: Boolean,
    default: false
  }
})

const router = useRouter()
const routes = computed(() => {
  const mainRoute = router.options.routes.find(route => route.path === '/')
  return mainRoute ? mainRoute.children : []
})
</script>

<style scoped>
.sidebar-menu {
  height: 100%;
  border-right: none;
}

.sidebar-menu:not(.el-menu-collapse) {
  width: 200px;
}

.el-menu-collapse {
  width: 64px;
}

.el-menu-item [class^="el-icon-"] {
  font-size: 18px;
}

.el-menu-item span,
.el-sub-menu-title span {
  margin-left: 10px;
}
</style>