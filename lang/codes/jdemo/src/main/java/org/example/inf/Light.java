package org.example.inf;

// 接口: 本质协议约束
// 不允许存在变量, 只能是方法的集合
public interface Light {
    public void on();
    public void off();
    public String getStatus();
}
