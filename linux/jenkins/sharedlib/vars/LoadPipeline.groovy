import com.laazua.lib.Properties


// 脚本入口
def call(String name) {
  pipeline {
    agent any
    options {
      skipDefaultCheckout()  //删除隐式checkout scm语句
      disableConcurrentBuilds() //禁止并行
      timeout(time: 1, unit: 'HOURS')  //流水线超时设置1小时
    }

    stages {
      stage("开始加载流水线") {
        steps{
          script{
              // 根据 name 来判断项目属于哪一类项目进而执行什么类型的流水线
              switch(name) {
                case PiplineItem.containsKey(name):
                  //
              }
            }
          }
        }
    }

    post {
      success{
        script{
          // 发送通知消息
        }
      }
      failure{
        script{
          // 发送通知消息
        }
      }
      aborted {
        script {
          // 发送通知消息
        }
      }
    }
  }
}

return this