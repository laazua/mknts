/*
 Navicat Premium Data Transfer

 Source Server         : my-host
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : 101.132.245.153:3306
 Source Schema         : msbn

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 09/02/2022 13:54:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for permisson
-- ----------------------------
DROP TABLE IF EXISTS `permisson`;
CREATE TABLE `permisson`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `desc` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `namepath` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mainmenu` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `subdesc` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `subpath` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_permisson_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permisson
-- ----------------------------
INSERT INTO `permisson` VALUES (1, '2022-02-08 22:09:12.820', '2022-02-08 22:09:12.820', NULL, '用户管理', '/user', 'user', 'userList', '/userlist');
INSERT INTO `permisson` VALUES (2, '2022-02-08 22:10:09.550', '2022-02-08 22:10:09.550', NULL, '用户管理', '/user', 'user', 'roleList', '/rolelist');
INSERT INTO `permisson` VALUES (3, '2022-02-08 22:10:30.487', '2022-02-08 22:10:30.487', NULL, '用户管理', '/user', 'user', 'permissList', '/permisslist');
INSERT INTO `permisson` VALUES (4, '2022-02-08 22:11:55.341', '2022-02-08 22:11:55.341', NULL, '运营管理', '/operation', 'operation', 'rechargeRank', '/rechargeRank');
INSERT INTO `permisson` VALUES (5, '2022-02-08 22:12:07.290', '2022-02-08 22:12:07.290', NULL, '运营管理', '/operation', 'operation', 'gradeDistribute', '/gradedistribute');
INSERT INTO `permisson` VALUES (6, '2022-02-08 22:12:15.630', '2022-02-08 22:12:15.630', NULL, '运营管理', '/operation', 'operation', 'loginOnline', '/loginonline');
INSERT INTO `permisson` VALUES (7, '2022-02-08 22:12:26.972', '2022-02-08 22:12:26.972', NULL, '运营管理', '/operation', 'operation', 'rollData', '/rolldata');
INSERT INTO `permisson` VALUES (8, '2022-02-08 22:12:42.806', '2022-02-08 22:12:42.806', NULL, '运营管理', '/operation', 'operation', 'retaineData', '/retainedata');
INSERT INTO `permisson` VALUES (9, '2022-02-08 22:12:56.510', '2022-02-08 22:12:56.510', NULL, '运营管理', '/operation', 'operation', 'livData', '/livdata');
INSERT INTO `permisson` VALUES (10, '2022-02-08 22:13:06.131', '2022-02-08 22:13:06.131', NULL, '运营管理', '/operation', 'operation', 'firstChargeLev', '/firstchargeLev');
INSERT INTO `permisson` VALUES (11, '2022-02-08 22:13:16.228', '2022-02-08 22:13:16.228', NULL, '运营管理', '/operation', 'operation', 'dataQuery', '/dataquery');
INSERT INTO `permisson` VALUES (12, '2022-02-08 22:13:25.401', '2022-02-08 22:13:25.401', NULL, '运营管理', '/operation', 'operation', 'vipLevel', '/viplevel');
INSERT INTO `permisson` VALUES (13, '2022-02-08 22:13:55.581', '2022-02-08 22:13:55.581', NULL, '玩家相关', '/player', 'player', 'orderTrack', '/ordertrack');
INSERT INTO `permisson` VALUES (14, '2022-02-08 22:14:02.394', '2022-02-08 22:14:02.394', NULL, '玩家相关', '/player', 'player', 'currenQuery', '/currenquery');
INSERT INTO `permisson` VALUES (15, '2022-02-08 22:14:25.820', '2022-02-08 22:14:25.820', NULL, '玩家相关', '/player', 'player', 'roleQuery', '/rolequery');
INSERT INTO `permisson` VALUES (16, '2022-02-08 22:14:39.180', '2022-02-08 22:14:39.180', NULL, '玩家相关', '/player', 'player', 'logQuery', '/logquery');
INSERT INTO `permisson` VALUES (17, '2022-02-08 22:14:53.574', '2022-02-08 22:14:53.574', NULL, '玩家相关', '/player', 'player', 'detailsMsg', '/detailsmsg');
INSERT INTO `permisson` VALUES (18, '2022-02-08 22:15:21.313', '2022-02-08 22:15:21.313', NULL, 'GM工具', '/gmtools', 'gmtools', 'awardRecord', '/awardrecord');
INSERT INTO `permisson` VALUES (19, '2022-02-08 22:15:33.578', '2022-02-08 22:15:33.578', NULL, 'GM工具', '/gmtools', 'gmtools', 'announQuery', '/announquery');
INSERT INTO `permisson` VALUES (20, '2022-02-08 22:15:48.022', '2022-02-08 22:15:48.022', NULL, 'GM工具', '/gmtools', 'gmtools', 'zoneAnnoun', '/zoneannoun');
INSERT INTO `permisson` VALUES (21, '2022-02-08 22:15:58.512', '2022-02-08 22:15:58.512', NULL, 'GM工具', '/gmtools', 'gmtools', 'zoneRewards', '/zonerewards');
INSERT INTO `permisson` VALUES (22, '2022-02-08 22:16:10.326', '2022-02-08 22:16:10.326', NULL, 'GM工具', '/gmtools', 'gmtools', 'homePage', '/homepage');
INSERT INTO `permisson` VALUES (23, '2022-02-08 22:16:35.584', '2022-02-08 22:16:35.584', NULL, 'GM工具', '/gmtools', 'gmtools', 'playerAward', '/playeraward');
INSERT INTO `permisson` VALUES (24, '2022-02-08 22:17:00.561', '2022-02-08 22:17:00.561', NULL, '礼包管理', '/gifts', 'gifts', 'activeList', '/activelist');
INSERT INTO `permisson` VALUES (25, '2022-02-08 22:17:49.125', '2022-02-08 22:17:49.125', NULL, '礼包管理', '/gifts', 'gifts', 'activeData', '/activedata');
INSERT INTO `permisson` VALUES (26, '2022-02-08 22:18:01.256', '2022-02-08 22:18:01.256', NULL, '礼包管理', '/gifts', 'gifts', 'configPackage', '/configpackage');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `desc` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_role_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, '2022-02-08 23:07:59.558', '2022-02-08 23:13:19.581', NULL, 'admin', '管理员');
INSERT INTO `role` VALUES (2, '2022-02-08 23:08:13.911', '2022-02-08 23:08:13.911', NULL, 'customer', '客服');
INSERT INTO `role` VALUES (3, '2022-02-08 23:08:26.206', '2022-02-08 23:08:26.206', NULL, 'partner', '合作方');

-- ----------------------------
-- Table structure for rolepermisson
-- ----------------------------
DROP TABLE IF EXISTS `rolepermisson`;
CREATE TABLE `rolepermisson`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `rolename` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mainmenu` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_rolepermisson_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rolepermisson
-- ----------------------------
INSERT INTO `rolepermisson` VALUES (1, '2022-02-08 23:18:58.888', '2022-02-08 23:18:58.888', NULL, 'admin', 'user');
INSERT INTO `rolepermisson` VALUES (2, '2022-02-08 23:19:29.755', '2022-02-08 23:19:29.755', NULL, 'admin', 'operation');
INSERT INTO `rolepermisson` VALUES (3, '2022-02-08 23:19:37.313', '2022-02-08 23:19:37.313', NULL, 'admin', 'player');
INSERT INTO `rolepermisson` VALUES (4, '2022-02-08 23:19:44.749', '2022-02-08 23:19:44.749', NULL, 'admin', 'gmtools');
INSERT INTO `rolepermisson` VALUES (5, '2022-02-08 23:19:53.099', '2022-02-08 23:19:53.099', NULL, 'admin', 'gifts');
INSERT INTO `rolepermisson` VALUES (6, '2022-02-08 23:21:40.634', '2022-02-08 23:21:40.634', NULL, 'partner', 'operation');
INSERT INTO `rolepermisson` VALUES (7, '2022-02-08 23:21:46.663', '2022-02-08 23:21:46.663', NULL, 'partner', 'player');
INSERT INTO `rolepermisson` VALUES (8, '2022-02-08 23:22:27.085', '2022-02-08 23:22:27.085', NULL, 'customer', 'player');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `hspass` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `rolename` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `idx_user_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '2022-02-08 22:30:40.736', '2022-02-08 22:37:51.133', NULL, 'admin', '$2a$04$2hR6u3ggI21uU5tOIn3dEOzDXq9sRC.o3s2g0yl.US7qqWHtELr3a', 'admin');
INSERT INTO `user` VALUES (2, '2022-02-08 22:31:23.960', '2022-02-08 22:37:22.002', NULL, 'zhangsan', '$2a$04$ofdR5xwxWKdxwL89IkUmFeBKguvRmHKuRIzVsJ3FX2abZ58KNgu/y', 'customer');
INSERT INTO `user` VALUES (3, '2022-02-08 22:31:35.821', '2022-02-08 22:38:06.841', NULL, 'lisi', '$2a$04$qeCOZw1N8zz1VdaHoZbrw.I14TISYg6voNMcir2xtK4kCdhGKSrp2', 'partner');

-- ----------------------------
-- Table structure for userole
-- ----------------------------
DROP TABLE IF EXISTS `userole`;
CREATE TABLE `userole`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) NULL DEFAULT NULL,
  `updated_at` datetime(3) NULL DEFAULT NULL,
  `deleted_at` datetime(3) NULL DEFAULT NULL,
  `userid` bigint UNSIGNED NOT NULL,
  `roleid` bigint UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_userole_deleted_at`(`deleted_at`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of userole
-- ----------------------------
INSERT INTO `userole` VALUES (1, '2022-02-08 21:32:17.000', '2022-02-08 21:32:17.000', NULL, 1, 2);
INSERT INTO `userole` VALUES (2, '2022-02-08 21:34:08.551', '2022-02-08 21:34:08.551', NULL, 3, 1);
INSERT INTO `userole` VALUES (3, '2022-02-08 22:33:54.093', '2022-02-08 22:33:54.093', NULL, 3, 0);
INSERT INTO `userole` VALUES (4, '2022-02-08 22:34:04.276', '2022-02-08 22:34:04.276', NULL, 1, 0);
INSERT INTO `userole` VALUES (5, '2022-02-08 22:34:43.050', '2022-02-08 22:34:43.050', NULL, 0, 0);

SET FOREIGN_KEY_CHECKS = 1;
