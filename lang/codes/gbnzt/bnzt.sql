/*
 Navicat Premium Data Transfer

 Source Server         : my-host
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : 101.132.245.153:3306
 Source Schema         : bnzt

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 09/03/2022 18:44:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `permdesc` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `namepath` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `subdesc` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `subpath` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_permission_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permission
-- ----------------------------
INSERT INTO `permission` VALUES (1, '2022-02-27 22:28:34.479', '2022-02-27 22:28:34.479', NULL, 'user', '/user', '用户列表', '/user');
INSERT INTO `permission` VALUES (2, '2022-02-27 22:28:51.353', '2022-02-27 22:28:51.353', NULL, 'user', '/user', '角色列表', '/role');
INSERT INTO `permission` VALUES (3, '2022-02-27 22:29:19.921', '2022-02-27 22:29:19.921', NULL, 'user', '/user', '权限列表', '/perm');
INSERT INTO `permission` VALUES (4, '2022-02-27 22:31:44.067', '2022-02-27 22:31:44.067', NULL, 'operation', '/operation', '充值排行', '/recharank');
INSERT INTO `permission` VALUES (5, '2022-02-27 22:32:15.563', '2022-02-27 22:32:15.563', NULL, 'operation', '/operation', '等级分布', '/gradedist');
INSERT INTO `permission` VALUES (6, '2022-02-27 22:32:29.836', '2022-02-27 22:32:29.836', NULL, 'operation', '/operation', '数据查询', '/countdata');
INSERT INTO `permission` VALUES (7, '2022-02-27 22:32:42.912', '2022-02-27 22:32:42.912', NULL, 'operation', '/operation', '滚服数据', '/rollsdata');
INSERT INTO `permission` VALUES (8, '2022-02-27 22:33:01.121', '2022-02-27 22:33:01.121', NULL, 'operation', '/operation', '留存数据', '/retendata');
INSERT INTO `permission` VALUES (9, '2022-02-27 22:33:16.982', '2022-02-27 22:33:16.982', NULL, 'operation', '/operation', 'VIP等级', '/vipsdata');
INSERT INTO `permission` VALUES (10, '2022-02-27 22:33:33.157', '2022-02-27 22:33:33.157', NULL, 'operation', '/operation', 'LTV数据', '/ltvsdata');
INSERT INTO `permission` VALUES (11, '2022-02-27 22:34:10.779', '2022-02-27 22:34:10.779', NULL, 'player', '/player', '订单查询', '/orderdata');
INSERT INTO `permission` VALUES (12, '2022-02-27 22:34:25.415', '2022-02-27 22:34:25.415', NULL, 'player', '/player', '角色查询', '/roledata');
INSERT INTO `permission` VALUES (13, '2022-02-27 22:34:41.964', '2022-02-27 22:34:41.964', NULL, 'player', '/player', '货币查询', '/currdata');
INSERT INTO `permission` VALUES (14, '2022-03-02 02:54:42.398', '2022-03-02 02:54:42.398', NULL, 'devops', '/devops', '区服列表', '/zonelist');
INSERT INTO `permission` VALUES (15, '2022-03-02 02:56:23.264', '2022-03-02 02:56:23.264', NULL, 'devops', '/devops', '资源更新', '/sourceup');
INSERT INTO `permission` VALUES (16, '2022-03-03 02:40:08.346', '2022-03-03 02:40:08.346', NULL, 'devops', '/devops', '主机状态', '/hostlist');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `rolename` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `roledesc` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mainmenu` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_role_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, '2022-02-21 01:30:20.502', '2022-03-02 03:09:44.296', NULL, 'root', '管理员', 'user');
INSERT INTO `role` VALUES (2, '2022-02-21 01:31:21.862', '2022-02-21 01:31:21.862', NULL, 'root', '管理员', 'player');
INSERT INTO `role` VALUES (4, '2022-02-27 22:41:37.979', '2022-02-27 22:41:37.979', NULL, 'root', '管理员', 'operation');
INSERT INTO `role` VALUES (7, '2022-02-28 21:57:52.564', '2022-02-28 21:57:52.723', NULL, 'partner', '合作方', 'operation');
INSERT INTO `role` VALUES (8, '2022-02-28 23:48:08.906', '2022-02-28 23:48:08.906', NULL, 'customer', '客服', 'player');
INSERT INTO `role` VALUES (9, '2022-03-02 02:57:09.673', '2022-03-02 02:57:09.673', NULL, 'yunwei', '运维', 'devops');
INSERT INTO `role` VALUES (10, '2022-03-02 03:11:22.608', '2022-03-02 03:11:22.608', NULL, 'root', '管理员', 'devops');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `username` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `hspass` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `rolename` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  INDEX `idx_user_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '2022-02-21 01:26:16.124', '2022-02-21 01:26:16.124', NULL, 'admin', '$2a$04$MjYewj7D9gBZXXZ1D34F2uiODwJtx2gBAFtxzpUxE6Vcy0jPF5f3W', 'root');
INSERT INTO `user` VALUES (3, '2022-02-28 02:50:59.684', '2022-02-28 02:50:59.684', NULL, 'zhangsan', '$2a$04$xFXBvqXknRHh1b5mTBvKmutRUvigPS966MA3UyJ/1D1yLAR9W/rfa', 'partner');
INSERT INTO `user` VALUES (4, '2022-02-28 05:54:28.178', '2022-03-02 03:02:40.696', NULL, 'lisi', '$2a$04$D1L3G4uG9Wrod.7VwPTVGuClXac4RDh2Tpx0XavCcDzzlFR9cBE5K', 'yunwei');
INSERT INTO `user` VALUES (7, '2022-02-28 23:35:42.383', '2022-02-28 23:48:50.713', NULL, 'wangwu', '$2a$04$ztM74qSq0jSd82yjSW9DLOr80OsQGJ5G6YgIuPahfLJZVAXQeTxFy', 'customer');

-- ----------------------------
-- Table structure for zone
-- ----------------------------
DROP TABLE IF EXISTS `zone`;
CREATE TABLE `zone`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `ip` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `channame` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `zone` bigint UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_zone_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zone
-- ----------------------------
INSERT INTO `zone` VALUES (1, '2022-03-09 02:11:05.050', '2022-03-09 02:11:05.050', NULL, '172.16.9.128', 'syf_test', 1001);
INSERT INTO `zone` VALUES (2, '2022-03-09 03:30:31.835', '2022-03-09 03:30:31.835', NULL, '172.16.9.128', 'syf_test', 1002);

SET FOREIGN_KEY_CHECKS = 1;
