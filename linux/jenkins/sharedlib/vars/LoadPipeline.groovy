

// 加载bash/python脚本
def loadScript(name) {
    writeFile file: name, text: libraryResource("scripts/${name}")
}

// 脚本入口
def call(String name) {
  //加载默认配置
  def cfg_text = libraryResource("config.yaml")
  def cfg = readYaml text: cfg_text

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
                case 'app.name':
                  // 执行脚本前加载脚本
                  loadScript("request.py")
                  loadScript("build.sh")
                  // 执行脚本
                  sh """
                      chmod +x build.sh
                      export PYTHONPATH=${cfg.python.vendor}
                      python3 request.py
                      ./build.sh
                  """
                default:
                  println "123"
              }
            }
          }
        }
    }

    post {
      success{
        script{
          // 发送通知消息
          sh """
            echo "success"
          """
        }
      }
      failure{
        script{
          // 发送通知消息
           sh """
            echo "failure"
          """
        }
      }
      aborted {
        script {
          // 发送通知消息
          sh """
            echo "aborted"
          """
        }
      }
    }
  }
}

return this