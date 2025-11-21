// 配置类
package com.laazua.lib


class Properties {
    private static Properties properties = new Properties()
    private static boolean loaded = false
    
    // 静态初始化块
    static {
        // 可以在这里加载默认配置
        loadDefault()
    }
    
    private static void loadDefault() {
        // 设置一些默认值
        properties.setProperty('app.name', 'MyApp')
        properties.setProperty('app.version', '1.0.0')
        properties.setProperty('server.port', '8080')
    }
    
    // 从文件加载配置（静态方法）
    static void loadFromFile(String filename) {
        try {
            File file = new File(filename)
            if (!file.exists()) {
                throw new FileNotFoundException("配置文件不存在: ${filename}")
            }
            
            file.withInputStream { stream ->
                properties.load(stream)
            }
            loaded = true
            println "成功加载配置文件: ${filename}"
        } catch (Exception e) {
            println "加载配置文件失败: ${e.message}"
            throw e
        }
    }
    
    // 获取配置值（静态方法）
    static String get(String key, String defaultValue = null) {
        return properties.getProperty(key, defaultValue)
    }
    
    // 获取所有配置键（静态方法）
    static Set<String> getKeys() {
        return properties.stringPropertyNames()
    }
    
    // 检查键是否存在（静态方法）
    static boolean containsKey(String key) {
        return properties.containsKey(key)
    }
    
    // 设置配置值（静态方法）
    static void set(String key, String value) {
        properties.setProperty(key, value)
    }
    
    // 检查是否已加载配置文件
    static boolean isLoaded() {
        return loaded
    }
}

// 使用示例 - 直接通过类名调用
// PropertiesConfigLoader.loadFromFile('config.properties')

// println "应用名称: ${PropertiesConfigLoader.get('app.name')}"
// println "服务器端口: ${PropertiesConfigLoader.get('server.port', '8080')}"
// println "是否已加载: ${PropertiesConfigLoader.isLoaded()}"

// // 遍历所有配置
// PropertiesConfigLoader.keys.each { key ->
//     println "${key} = ${PropertiesConfigLoader.get(key)}"
// }
