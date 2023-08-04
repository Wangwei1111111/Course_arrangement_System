/*
 Navicat Premium Data Transfer

 Source Server         : MariaDB_local
 Source Server Type    : MariaDB
 Source Server Version : 100424
 Source Host           : localhost:3306
 Source Schema         : course-arrangement system

 Target Server Type    : MariaDB
 Target Server Version : 100424
 File Encoding         : 65001

 Date: 04/08/2023 16:29:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for password
-- ----------------------------
DROP TABLE IF EXISTS `password`;
CREATE TABLE `password`  (
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of password
-- ----------------------------
INSERT INTO `password` VALUES ('123456');

-- ----------------------------
-- Table structure for schedule
-- ----------------------------
DROP TABLE IF EXISTS `schedule`;
CREATE TABLE `schedule`  (
  `stu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacher_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date` datetime(0) NOT NULL,
  `class_num` int(11) NOT NULL,
  `grade` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` double NOT NULL,
  `text` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of schedule
-- ----------------------------
INSERT INTO `schedule` VALUES ('戈钊', '晓晴', '2023-07-18 00:00:00', 0, '0', 2, NULL);
INSERT INTO `schedule` VALUES ('玉轩', '沈琳琳', '2023-07-18 00:00:00', 4, '初一', 2, NULL);
INSERT INTO `schedule` VALUES ('玉轩', '沈琳琳', '2023-07-18 00:00:00', 5, '初一', 2, NULL);
INSERT INTO `schedule` VALUES ('紫琦', '郁', '2023-07-18 00:00:00', 5, '0', 2, NULL);

-- ----------------------------
-- Table structure for schedule_final
-- ----------------------------
DROP TABLE IF EXISTS `schedule_final`;
CREATE TABLE `schedule_final`  (
  `stu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `teacher_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `date` datetime(0) NULL DEFAULT NULL,
  `class_num` int(64) NULL DEFAULT NULL,
  `grade` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` double NULL DEFAULT NULL,
  `text` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of schedule_final
-- ----------------------------
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-03 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-03 00:00:00', 0, '8', 2, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-03 00:00:00', 0, '9', 2, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-03 00:00:00', 0, '7', 1.5, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-09 00:00:00', 0, '7', 1.5, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-09 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-09 00:00:00', 0, '初二', NULL, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-09 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-10 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('黄心', '郁', '2023-07-10 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('黄心', '郁', '2023-07-10 00:00:00', 0, '初一', NULL, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-10 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-10 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('黄心', '郁', '2023-07-10 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('睿哲', '段', '2023-07-14 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('黄心', '郁', '2023-07-14 00:00:00', 0, '7', 2, NULL);
INSERT INTO `schedule_final` VALUES ('玉轩', '传廷', '2023-07-14 00:00:00', 1, '7', 1.5, '不');
INSERT INTO `schedule_final` VALUES ('玉轩', '传廷', '2023-07-13 20:17:14', 1, '7', 1.5, '不');
INSERT INTO `schedule_final` VALUES ('玉轩', '传廷', '2023-07-13 20:20:26', 1, '7', 1.5, '不');
INSERT INTO `schedule_final` VALUES ('玉轩', '传廷', '2023-07-14 00:00:00', 0, '初一', 2, NULL);

-- ----------------------------
-- Table structure for schedule_mirror
-- ----------------------------
DROP TABLE IF EXISTS `schedule_mirror`;
CREATE TABLE `schedule_mirror`  (
  `stu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `teacher_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `date` datetime(0) NULL DEFAULT NULL,
  `class_num` int(11) NULL DEFAULT NULL,
  `grade` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` double NULL DEFAULT NULL,
  `text` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of schedule_mirror
-- ----------------------------
INSERT INTO `schedule_mirror` VALUES ('黄心', '郁', '2023-07-14 00:00:00', 0, '2', 2, 'None');
INSERT INTO `schedule_mirror` VALUES ('容俞', '隋欣', '2023-07-14 00:00:00', 0, '2', 2, 'None');

-- ----------------------------
-- Table structure for specific_time
-- ----------------------------
DROP TABLE IF EXISTS `specific_time`;
CREATE TABLE `specific_time`  (
  `stu_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `class_num` int(11) NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of specific_time
-- ----------------------------

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `grade` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sum` int(11) NULL DEFAULT NULL,
  `paid` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '睿哲', '0', '0', 0, 0);
INSERT INTO `student` VALUES (2, '保烨', '0', '0', 0, 0);
INSERT INTO `student` VALUES (3, '殿朝', '0', '0', 0, 0);
INSERT INTO `student` VALUES (4, '李淼', '0', '0', 0, 0);
INSERT INTO `student` VALUES (5, '杨雯雯', '0', '0', 0, 0);
INSERT INTO `student` VALUES (6, '玉轩', '初一', '0', 2, 0);
INSERT INTO `student` VALUES (7, '紫琦', '0', '0', 0, 0);
INSERT INTO `student` VALUES (8, '容俞', '0', '0', 0, 0);
INSERT INTO `student` VALUES (9, '董静', '0', '0', 0, 0);
INSERT INTO `student` VALUES (10, '中乔', '0', '0', 0, 0);
INSERT INTO `student` VALUES (11, '戈钊', '0', '0', 0, 0);
INSERT INTO `student` VALUES (12, '春奥', '0', '0', 0, 0);
INSERT INTO `student` VALUES (13, '富甲', '0', '0', 0, 0);
INSERT INTO `student` VALUES (14, '庆晓', '0', '0', 0, 0);
INSERT INTO `student` VALUES (15, '恒英', '0', '0', 0, 0);
INSERT INTO `student` VALUES (16, '力家', '0', '0', 0, 0);
INSERT INTO `student` VALUES (17, '子涵', '0', '0', 0, 0);
INSERT INTO `student` VALUES (18, '育良', '0', '0', 0, 0);
INSERT INTO `student` VALUES (19, '美娜', '0', '0', 0, 0);
INSERT INTO `student` VALUES (20, '思蒙', '0', '0', 0, 0);
INSERT INTO `student` VALUES (21, '慧敏', '0', '0', 0, 0);
INSERT INTO `student` VALUES (22, '王青', '0', '0', 0, 0);
INSERT INTO `student` VALUES (23, '姿琪', '0', '0', 0, 0);
INSERT INTO `student` VALUES (24, '梦宣', '0', '0', 0, 0);
INSERT INTO `student` VALUES (25, '传聪', '0', '0', 0, 0);
INSERT INTO `student` VALUES (26, '芳阁', '0', '0', 0, 0);
INSERT INTO `student` VALUES (27, '黄心', '0', '0', 0, 0);
INSERT INTO `student` VALUES (28, '彭真', '0', '0', 0, 0);

-- ----------------------------
-- Table structure for student_his
-- ----------------------------
DROP TABLE IF EXISTS `student_his`;
CREATE TABLE `student_his`  (
  `stu_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `subject` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_his
-- ----------------------------
INSERT INTO `student_his` VALUES (6, 11, '语文');
INSERT INTO `student_his` VALUES (7, 16, '语文');
INSERT INTO `student_his` VALUES (11, 21, '化学');

-- ----------------------------
-- Table structure for student_teacher_subject
-- ----------------------------
DROP TABLE IF EXISTS `student_teacher_subject`;
CREATE TABLE `student_teacher_subject`  (
  `stu_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `subject` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_teacher_subject
-- ----------------------------
INSERT INTO `student_teacher_subject` VALUES (6, 11, '语文');
INSERT INTO `student_teacher_subject` VALUES (6, 4, '语文');
INSERT INTO `student_teacher_subject` VALUES (6, 7, '语文');
INSERT INTO `student_teacher_subject` VALUES (6, 14, '语文');
INSERT INTO `student_teacher_subject` VALUES (6, 1, '语文');
INSERT INTO `student_teacher_subject` VALUES (7, 16, '语文');
INSERT INTO `student_teacher_subject` VALUES (7, 6, '化学');
INSERT INTO `student_teacher_subject` VALUES (10, 11, '化学');
INSERT INTO `student_teacher_subject` VALUES (10, 14, '化学');
INSERT INTO `student_teacher_subject` VALUES (10, 19, '化学');
INSERT INTO `student_teacher_subject` VALUES (10, 2, '化学');
INSERT INTO `student_teacher_subject` VALUES (11, 21, '化学');
INSERT INTO `student_teacher_subject` VALUES (11, 13, '化学');
INSERT INTO `student_teacher_subject` VALUES (11, 1, '化学');
INSERT INTO `student_teacher_subject` VALUES (11, 7, '化学');
INSERT INTO `student_teacher_subject` VALUES (12, 16, '化学');
INSERT INTO `student_teacher_subject` VALUES (12, 22, '英语');
INSERT INTO `student_teacher_subject` VALUES (12, 5, '化学');
INSERT INTO `student_teacher_subject` VALUES (12, 19, '物理');
INSERT INTO `student_teacher_subject` VALUES (13, 13, '物理');
INSERT INTO `student_teacher_subject` VALUES (1, 20, '数学');
INSERT INTO `student_teacher_subject` VALUES (1, 13, '物理');
INSERT INTO `student_teacher_subject` VALUES (1, 2, '语文');
INSERT INTO `student_teacher_subject` VALUES (1, 7, '英语');
INSERT INTO `student_teacher_subject` VALUES (17, 1, '物理');
INSERT INTO `student_teacher_subject` VALUES (17, 6, '物理');
INSERT INTO `student_teacher_subject` VALUES (17, 17, '数学');
INSERT INTO `student_teacher_subject` VALUES (17, 12, '物理');
INSERT INTO `student_teacher_subject` VALUES (18, 13, '数学');
INSERT INTO `student_teacher_subject` VALUES (18, 20, '数学');
INSERT INTO `student_teacher_subject` VALUES (18, 6, '数学');
INSERT INTO `student_teacher_subject` VALUES (18, 23, '数学');
INSERT INTO `student_teacher_subject` VALUES (19, 10, '物理');
INSERT INTO `student_teacher_subject` VALUES (19, 11, '物理');
INSERT INTO `student_teacher_subject` VALUES (19, 7, '物理');
INSERT INTO `student_teacher_subject` VALUES (19, 14, '物理');
INSERT INTO `student_teacher_subject` VALUES (26, 6, '化学');
INSERT INTO `student_teacher_subject` VALUES (26, 24, '化学');
INSERT INTO `student_teacher_subject` VALUES (26, 2, '化学');
INSERT INTO `student_teacher_subject` VALUES (26, 19, '化学');
INSERT INTO `student_teacher_subject` VALUES (22, 20, '数学');
INSERT INTO `student_teacher_subject` VALUES (22, 25, '数学');
INSERT INTO `student_teacher_subject` VALUES (22, 13, '数学');
INSERT INTO `student_teacher_subject` VALUES (22, 23, '数学');
INSERT INTO `student_teacher_subject` VALUES (24, 6, '化学');
INSERT INTO `student_teacher_subject` VALUES (24, 7, '化学');
INSERT INTO `student_teacher_subject` VALUES (24, 21, '化学');
INSERT INTO `student_teacher_subject` VALUES (24, 2, '语文');
INSERT INTO `student_teacher_subject` VALUES (23, 16, '数学');
INSERT INTO `student_teacher_subject` VALUES (8, 22, '英语');
INSERT INTO `student_teacher_subject` VALUES (8, 5, '化学');
INSERT INTO `student_teacher_subject` VALUES (27, 16, '化学');
INSERT INTO `student_teacher_subject` VALUES (27, 12, '化学');
INSERT INTO `student_teacher_subject` VALUES (9, 20, '物理');
INSERT INTO `student_teacher_subject` VALUES (9, 25, '物理');
INSERT INTO `student_teacher_subject` VALUES (9, 6, '物理');

-- ----------------------------
-- Table structure for student_twice
-- ----------------------------
DROP TABLE IF EXISTS `student_twice`;
CREATE TABLE `student_twice`  (
  `stu_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `subject` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_twice
-- ----------------------------
INSERT INTO `student_twice` VALUES (6, 11, '语文');

-- ----------------------------
-- Table structure for student_unavailable_periods
-- ----------------------------
DROP TABLE IF EXISTS `student_unavailable_periods`;
CREATE TABLE `student_unavailable_periods`  (
  `stu_id` int(11) NOT NULL,
  `class_num` int(11) NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_unavailable_periods
-- ----------------------------
INSERT INTO `student_unavailable_periods` VALUES (7, 0);
INSERT INTO `student_unavailable_periods` VALUES (7, 2);
INSERT INTO `student_unavailable_periods` VALUES (7, 3);
INSERT INTO `student_unavailable_periods` VALUES (4, 0);
INSERT INTO `student_unavailable_periods` VALUES (4, 2);
INSERT INTO `student_unavailable_periods` VALUES (4, 5);
INSERT INTO `student_unavailable_periods` VALUES (10, 2);
INSERT INTO `student_unavailable_periods` VALUES (10, 5);
INSERT INTO `student_unavailable_periods` VALUES (13, 0);
INSERT INTO `student_unavailable_periods` VALUES (13, 1);
INSERT INTO `student_unavailable_periods` VALUES (13, 2);
INSERT INTO `student_unavailable_periods` VALUES (13, 3);
INSERT INTO `student_unavailable_periods` VALUES (13, 4);
INSERT INTO `student_unavailable_periods` VALUES (23, 0);
INSERT INTO `student_unavailable_periods` VALUES (23, 1);
INSERT INTO `student_unavailable_periods` VALUES (23, 2);
INSERT INTO `student_unavailable_periods` VALUES (23, 3);
INSERT INTO `student_unavailable_periods` VALUES (1, 5);
INSERT INTO `student_unavailable_periods` VALUES (8, 1);
INSERT INTO `student_unavailable_periods` VALUES (8, 3);
INSERT INTO `student_unavailable_periods` VALUES (8, 4);
INSERT INTO `student_unavailable_periods` VALUES (8, 5);
INSERT INTO `student_unavailable_periods` VALUES (19, 0);
INSERT INTO `student_unavailable_periods` VALUES (19, 3);
INSERT INTO `student_unavailable_periods` VALUES (11, 2);
INSERT INTO `student_unavailable_periods` VALUES (11, 5);
INSERT INTO `student_unavailable_periods` VALUES (12, 2);
INSERT INTO `student_unavailable_periods` VALUES (12, 5);
INSERT INTO `student_unavailable_periods` VALUES (17, 2);
INSERT INTO `student_unavailable_periods` VALUES (18, 2);
INSERT INTO `student_unavailable_periods` VALUES (16, 2);
INSERT INTO `student_unavailable_periods` VALUES (16, 5);
INSERT INTO `student_unavailable_periods` VALUES (22, 2);
INSERT INTO `student_unavailable_periods` VALUES (24, 2);
INSERT INTO `student_unavailable_periods` VALUES (25, 0);
INSERT INTO `student_unavailable_periods` VALUES (25, 1);
INSERT INTO `student_unavailable_periods` VALUES (25, 2);
INSERT INTO `student_unavailable_periods` VALUES (25, 3);
INSERT INTO `student_unavailable_periods` VALUES (25, 4);

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `day_sum` int(11) NULL DEFAULT NULL,
  `sum` int(11) NULL DEFAULT NULL,
  `punish` int(11) NULL DEFAULT 10,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES (1, '传廷', '0', 0, 2, 10);
INSERT INTO `teacher` VALUES (2, '沈佳佳', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (3, '文琦', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (4, '贵强', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (5, '保发', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (6, '杜婷婷', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (7, '段', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (8, '王宇', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (9, '顾立', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (10, '延蒙', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (11, '沈琳琳', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (12, '于', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (13, '李战胜', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (14, '张书冬', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (15, '王炜', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (16, '郁', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (17, '马坤（高中）', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (18, '刘佳佳', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (19, '常', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (20, '志硕', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (21, '晓晴', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (22, '隋欣', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (23, '张娜', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (24, '崔', '0', 0, 0, 10);
INSERT INTO `teacher` VALUES (25, '赵会', '0', 0, 0, 10);

-- ----------------------------
-- Table structure for teacher_unavailable_periods
-- ----------------------------
DROP TABLE IF EXISTS `teacher_unavailable_periods`;
CREATE TABLE `teacher_unavailable_periods`  (
  `teacher_id` int(11) NOT NULL,
  `class_num` int(11) NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher_unavailable_periods
-- ----------------------------
INSERT INTO `teacher_unavailable_periods` VALUES (2, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (4, 0);
INSERT INTO `teacher_unavailable_periods` VALUES (4, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (4, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (4, 4);
INSERT INTO `teacher_unavailable_periods` VALUES (7, 5);
INSERT INTO `teacher_unavailable_periods` VALUES (12, 0);
INSERT INTO `teacher_unavailable_periods` VALUES (12, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (12, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (12, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (17, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (17, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (17, 4);
INSERT INTO `teacher_unavailable_periods` VALUES (17, 5);
INSERT INTO `teacher_unavailable_periods` VALUES (23, 0);
INSERT INTO `teacher_unavailable_periods` VALUES (23, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (23, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (23, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (23, 4);
INSERT INTO `teacher_unavailable_periods` VALUES (1, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (1, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (1, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (1, 4);
INSERT INTO `teacher_unavailable_periods` VALUES (8, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (8, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (8, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (8, 4);
INSERT INTO `teacher_unavailable_periods` VALUES (8, 5);
INSERT INTO `teacher_unavailable_periods` VALUES (19, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (3, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (5, 0);
INSERT INTO `teacher_unavailable_periods` VALUES (5, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (5, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (5, 5);
INSERT INTO `teacher_unavailable_periods` VALUES (6, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (10, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (11, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (14, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (15, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (16, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (13, 5);
INSERT INTO `teacher_unavailable_periods` VALUES (18, 0);
INSERT INTO `teacher_unavailable_periods` VALUES (18, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (18, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (18, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (18, 4);
INSERT INTO `teacher_unavailable_periods` VALUES (21, 1);
INSERT INTO `teacher_unavailable_periods` VALUES (21, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (21, 3);
INSERT INTO `teacher_unavailable_periods` VALUES (21, 4);
INSERT INTO `teacher_unavailable_periods` VALUES (20, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (22, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (24, 2);
INSERT INTO `teacher_unavailable_periods` VALUES (25, 2);

SET FOREIGN_KEY_CHECKS = 1;
