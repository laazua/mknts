// 项目类型

// vars/PipelineItem.groovy
class PipelineItem {
    // 定义全局字典
    private static final Map GLOBAL_CONFIG = [
        'api': [
            'timeout': 30,
            'node': 'master'
        ],
        'web': [
            'environment': 'production',
            'rollback': true
        ],
    ]
    
    def call() {
        return GLOBAL_CONFIG
    }
    
    // 静态方法直接获取配置
    static Map getGlobalConfig() {
        return GLOBAL_CONFIG
    }
    
    // 获取特定配置项
    static def getConfig(String key) {
        return GLOBAL_CONFIG.get(key)
    }
    
    // 检查键是否存在
    static boolean containsKey(String key) {
        return GLOBAL_CONFIG.containsKey(key)
    }
    
    // 安全获取值，如果键不存在返回null
    static def getSafe(String key) {
        return GLOBAL_CONFIG.get(key)
    }
    
    // 安全获取值，带默认值
    static def getSafe(String key, defaultValue) {
        return GLOBAL_CONFIG.get(key) ?: defaultValue
    }
    
    // 检查并获取值，如果存在返回值，不存在返回null
    static def getIfExists(String key) {
        return containsKey(key) ? getConfig(key) : null
    }
    
    // 检查并获取值，带自定义不存在时的处理
    static def getIfExists(String key, Closure notFoundHandler) {
        if (containsKey(key)) {
            return getConfig(key)
        } else {
            return notFoundHandler.call(key)
        }
    }
}