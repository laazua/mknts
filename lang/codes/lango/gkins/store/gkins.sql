-- 创建数据库: gkins
CREATE DATABASE IF NOT EXISTS gkins;

-- 切换数据库: gkins
USE gkins;

-- 创建用户表：user
CREATE TABLE IF NOT EXISTS `gk_user` (
    id INT AUTO_INCREMENT PRIMARY KEY,    -- 自增的 id 字段,作为主键
    name VARCHAR(100) NOT NULL,           -- 用户名字段,不允许为空
    email VARCHAR(100) NOT NULL UNIQUE,   -- 邮箱字段,不允许为空且唯一
    password VARCHAR(255) NOT NULL,       -- 密码字段,不允许为空
    role VARCHAR(100) DEFAULT NULL,           -- 角色字段[超级用户,普通用户]
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 创建时间,默认为当前时间
    deleted_at TIMESTAMP NULL,            -- 删除时间,默认为 NULL
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- 更新时间.默认为当前时间,并在每次更新时自动更新
);

-- 创建任务表: task
CREATE TABLE IF NOT EXISTS `gk_task` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    template JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 新增管理员信息:
INSERT INTO `gk_user` (name, email, password)
VALUES ('admin', 'admin@gkins.com', '$jZae727K08KaOmKSgOaGzww_XVqGr_PKEgIMkjrcbJI=');