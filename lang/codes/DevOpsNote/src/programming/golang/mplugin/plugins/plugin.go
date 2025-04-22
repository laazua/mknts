package main

import "fmt"

// 插件必须导出名为 Plugin 的变量
type PluginImpl struct{}

func (p *PluginImpl) Execute(args ...string) error {
	fmt.Println("Plugin Execute:", args)
	return nil
}

// 导出插件实例
var Plugin PluginImpl

