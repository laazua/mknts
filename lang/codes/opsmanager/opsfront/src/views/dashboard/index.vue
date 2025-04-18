<template>
  <div class="dashboard-container">
    <el-card class="box-card" shadow="hover">
      <div>
        Hello, {{ name }}. 欢迎使用运维系统!<br>
        <!--
        <br>
        城市: {{ city }} <br>
        <br>
        天气: {{ weather }} <br> 
        <br>
        -->
        <br>
        时间: {{ year }} {{ weekday }} {{ day }}
      </div>
    </el-card>
    <div class="desc">
      <h3>WEB系统工具说明</h3>
      <p style="white-space: pre;">
        1. 除去首页, 共有4个页面,分别为: 用户,日志,区服,主机. <br>
        2. 权限共有两个分别为: root, yunwei; 当用户获得yunwei权限时,其只能操作区服和主机页面; 
           当用户同时拥有root, yunwei权限时,其可以操作所有页面. <br>
        3. 用户页面是可以对系统人员进行增减. <br>
        4. 日志页面可以查询用户执行了哪些关键操作. <br>
        5. 区服页面可以管理区服,进行更新,启停,状态检查操作等. <br>
        6. 主机页面可以查询主机资源使用情况.
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import dayjs from 'dayjs'
import axios from 'axios'

export default {
  name: 'Dashboard',
  data() {
    return {
      city: null,
      weather: null,
      timer: null,
      day: null,
      year: null,
      // week: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      week: ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'],
      weekday: null
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  mounted() {
    this.timer = setInterval(() => {
      const date = dayjs(new Date())
      this.day = date.format('HH:mm:ss')
      this.year = date.format('YYYY-MM-DD')
      this.weekday = date.format(this.week[date.day()])
    }, 10)
    // this.getWeather()
  },
  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer)
    }
  },
  methods: {
    getWeather() {
      axios.get('https://www.tianqiapi.com/api/', {
        params: {
          appid: '86151531',
          appsecret: 'k5b1bDYM',
          city: '成都'
        }
      }).then(res => {
        console.log(res)
        this.city = res.data.country + ' ' + res.data.city
        const weath = res.data.data[0]
        this.weather = weath.wea + ' ' + weath.tem + ' ' + weath.air_level
      }).catch(err => {
        console.log(err)
      })
    }
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
// .el-card {
//   margin: 0 auto;
//   margin-top: 180px;
//   box-sizing: content-box;
//   width: 20%;
//   border: solid rgb(197, 196, 196) 1px;
//   padding: 2px;
//   background-color: rgb(255, 255, 255);
//   font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
// }
.el-card {
  width: 20%;
  margin-left: 40%;
}
.desc {
  margin-top: 20px;
  margin-left: 10%;
  white-space: pre;
  .p{
    text-indent: 2em;
  }
}
</style>
