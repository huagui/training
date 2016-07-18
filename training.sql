/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50617
Source Host           : localhost:3306
Source Database       : training

Target Server Type    : MYSQL
Target Server Version : 50617
File Encoding         : 65001

Date: 2016-06-12 21:13:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `detail` varchar(100) DEFAULT '',
  `parent_id` int(11) NOT NULL DEFAULT '0' COMMENT '父类id，0则为顶级分类',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', 'PHP', '', '0');
INSERT INTO `category` VALUES ('2', 'HTML', '', '0');

-- ----------------------------
-- Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cate_id` int(11) NOT NULL COMMENT '分类id',
  `name` varchar(30) NOT NULL COMMENT '班级名称。unique',
  `detail` text,
  `target` text COMMENT '培训对象',
  `basis` text COMMENT '基础要求',
  `project` text COMMENT '实战项目',
  `goal` text COMMENT '实战后成果。',
  `plan` text COMMENT '时间规划',
  `charge` int(11) NOT NULL DEFAULT '0' COMMENT '培训费用',
  `idea` text COMMENT '理念',
  `practice_plan` text COMMENT '实战规划,用于学员版的实战规划',
  `teaching_demand` text COMMENT '任教要求，用于教练版的加入班级',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `cate_id` (`cate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('1', '1', 'PHP初级', 'chujiban', 'fish man', 'nothing', 'some projects', 'learning php grammar', 'two weeks', '0', 'simple and fast', '1.a 2.b 3.c', 'a master');
INSERT INTO `class` VALUES ('2', '1', 'PHP中级', '', null, null, null, null, null, '0', null, null, null);
INSERT INTO `class` VALUES ('3', '2', 'HTML初级', '', null, null, null, null, null, '0', null, null, null);
INSERT INTO `class` VALUES ('4', '2', 'HTML中级', '', null, null, null, null, null, '0', null, null, null);

-- ----------------------------
-- Table structure for `comment`
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `student_id` int(11) NOT NULL,
  `trainer_id` int(11) NOT NULL,
  `publish_time` datetime NOT NULL,
  `class_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='记录学员对教练的评论';

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('1', 'good', '1', '1', '2016-06-12 20:25:05', '0');
INSERT INTO `comment` VALUES ('2', 'aaa', '1', '1', '2016-06-12 20:58:25', '1');
INSERT INTO `comment` VALUES ('3', 'aaa', '1', '1', '2016-06-12 21:12:28', '1');

-- ----------------------------
-- Table structure for `history`
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `finish_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '任务完成状态标记： 1：进行中，2：学员提交，等待教练评分，3：已完成',
  `class_id` int(11) NOT NULL,
  `point` tinyint(3) NOT NULL DEFAULT '0' COMMENT '任务得分',
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`,`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of history
-- ----------------------------
INSERT INTO `history` VALUES ('44', '2', '2', '2016-05-21 16:15:07', '3', '2', '99');
INSERT INTO `history` VALUES ('50', '3', '2', '0000-00-00 00:00:00', '1', '2', '0');

-- ----------------------------
-- Table structure for `message`
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relation_id` int(11) NOT NULL,
  `from_stu` tinyint(1) NOT NULL COMMENT '1为学员发送的留言，0为教练发送的留言',
  `publish_time` datetime NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('9', '48', '1', '2016-05-23 16:17:30', '啊啊');
INSERT INTO `message` VALUES ('10', '48', '0', '2016-05-23 16:18:14', '啊啊');
INSERT INTO `message` VALUES ('11', '48', '1', '2016-05-23 16:47:59', '');
INSERT INTO `message` VALUES ('12', '48', '0', '2016-05-12 16:48:03', '');
INSERT INTO `message` VALUES ('13', '48', '1', '2016-05-23 16:59:46', '啊啊');

-- ----------------------------
-- Table structure for `notification`
-- ----------------------------
DROP TABLE IF EXISTS `notification`;
CREATE TABLE `notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_type` tinyint(1) NOT NULL COMMENT '1为学员，2为教练, 3为指导申请',
  `target_id` int(11) NOT NULL COMMENT '目标id',
  `content` varchar(255) NOT NULL,
  `is_handled` tinyint(1) DEFAULT '0' COMMENT '1代表通知已处理',
  `relation_id` int(11) NOT NULL DEFAULT '0' COMMENT '通知为学员申请时用到、',
  `msg_type` tinyint(2) NOT NULL DEFAULT '0' COMMENT '通知类型、 1为 学员申请, 2为 学员提交任务, 3为学员申请回复, 4为指导申请,5为指导通知(目标是教练)，6指导确认通知(目标是学员)',
  `agreement` tinyint(1) DEFAULT NULL COMMENT '是否同意',
  PRIMARY KEY (`id`),
  UNIQUE KEY `relation_id` (`relation_id`,`msg_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of notification
-- ----------------------------

-- ----------------------------
-- Table structure for `question`
-- ----------------------------
DROP TABLE IF EXISTS `question`;
CREATE TABLE `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relation_id` int(11) NOT NULL DEFAULT '0',
  `stu_name` varchar(30) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `qq` int(11) DEFAULT NULL,
  `content` text COMMENT '指导的具体问题',
  `publish_time` datetime NOT NULL COMMENT '申请时间',
  `flower_num` int(11) NOT NULL DEFAULT '10' COMMENT '给教练的鲜花数目,单位：支  最少10支',
  `trainer_verify` tinyint(1) NOT NULL DEFAULT '0' COMMENT '教练确认标志',
  PRIMARY KEY (`id`),
  UNIQUE KEY `relation_id` (`relation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='学员申请指导时相关信息的记录表';

-- ----------------------------
-- Records of question
-- ----------------------------

-- ----------------------------
-- Table structure for `relation`
-- ----------------------------
DROP TABLE IF EXISTS `relation`;
CREATE TABLE `relation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trainer_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `status` int(1) NOT NULL DEFAULT '0' COMMENT '状态标记 0：学生申请了该教练  1:教练接受该学员',
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_id` (`student_id`,`class_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of relation
-- ----------------------------
INSERT INTO `relation` VALUES ('1', '1', '1', '1', '1');

-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(22) NOT NULL,
  `password` varchar(22) NOT NULL,
  `phone` varchar(11) DEFAULT '',
  `about` varchar(100) DEFAULT '',
  `nickname` varchar(20) NOT NULL,
  `qq` int(11) NOT NULL,
  `true_name` varchar(30) NOT NULL COMMENT '真实姓名',
  `flower_num` int(11) NOT NULL DEFAULT '200' COMMENT '鲜花数目，单位：支',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', 'hg', 'a', '12', 'iiiiasasi', 'hah', '0', '', '181');
INSERT INTO `student` VALUES ('2', 'test', 'a', '1231', 'fdaf', '特殊', '0', '', '200');
INSERT INTO `student` VALUES ('8', 'test3', 'a', '1324135', 'iamss', '结果', '0', '', '200');
INSERT INTO `student` VALUES ('9', 'a', 'a', 'a', 'a', '格源', '0', '', '0');
INSERT INTO `student` VALUES ('10', 'geyuan', 'a', '123456', 'a', '格源', '0', '', '0');
INSERT INTO `student` VALUES ('12', 'aaa', 'a', '123456', '哈哈的简介', '哈哈', '0', '', '0');
INSERT INTO `student` VALUES ('13', 'huagui', 'a', '453789', '华贵的简介', '华贵', '0', '', '0');
INSERT INTO `student` VALUES ('14', 'caike', 'a', '123789', '才可的简', '才可', '0', '', '0');
INSERT INTO `student` VALUES ('15', 'z', 'z', '12589637', '帅气的简介', '^0^', '0', '', '0');
INSERT INTO `student` VALUES ('16', 'asd', 'a', '12589760', '(*°ω°*)ﾉ\"非战斗人员请撤离！！', '0.0', '0', '', '0');
INSERT INTO `student` VALUES ('17', 'bbb', 'a', '1284066', 'ʕ•̫͡•ʔ族', '(｡☉౪ ⊙｡)bb', '0', '', '0');
INSERT INTO `student` VALUES ('18', 'ccc', 'a', ' o((*^▽^*))', '(๑•ૅㅁ•๑)ヾ(≧∪≦*)ノ〃', '(｡•ˇ‸ˇ•｡)', '0', '', '0');
INSERT INTO `student` VALUES ('19', 'tang_yu', 'ty6055222', '15766489901', '你好', 'tang\'yu', '0', '', '0');
INSERT INTO `student` VALUES ('20', '唐富', 'tf6055222', '18666809698', '姓名：唐富  性别：男', 'TF', '0', '', '0');
INSERT INTO `student` VALUES ('21', 'ty', '123456', '15766489901', '9', 'ty', '0', '', '0');
INSERT INTO `student` VALUES ('22', 'dd', 'a', '762762264', 'dd的简介', 'dd', '0', '', '0');
INSERT INTO `student` VALUES ('23', 'mm', 'a', '1558755', 'mm的简介', 'mm', '0', '', '0');
INSERT INTO `student` VALUES ('24', 'ee', 'a', '185657', 'ee的简介  ', 'ee', '0', '', '0');
INSERT INTO `student` VALUES ('25', '11', 'a', '1', '000', '0', '0', '', '0');
INSERT INTO `student` VALUES ('26', '22', 'a', '11', '111', '111', '0', '', '0');
INSERT INTO `student` VALUES ('27', 'test11', 'abc', '110', '哈哈', '测试', '0', '', '0');

-- ----------------------------
-- Table structure for `task`
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '项目名称',
  `content` text NOT NULL COMMENT '项目要求',
  `cost` int(3) NOT NULL DEFAULT '0' COMMENT '任务所需天数,单位：天',
  `class_id` int(11) NOT NULL DEFAULT '0' COMMENT '班级id',
  `num` int(11) NOT NULL COMMENT '任务序号,自动分发任务的序列号，从1开始',
  `materials` text NOT NULL COMMENT '项目相关资料',
  `guide` text NOT NULL COMMENT '项目指导',
  `guide_num` tinyint(3) NOT NULL DEFAULT '0' COMMENT '答疑和指导次数',
  `required_hour` int(11) NOT NULL DEFAULT '0' COMMENT '所需时间,完成任务实际工作的时间，单位：小时',
  `free_guide_mun` tinyint(3) NOT NULL COMMENT '免费指导次数，超过需要付费',
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`) USING BTREE,
  KEY `class_id` (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of task
-- ----------------------------
INSERT INTO `task` VALUES ('1', 'task1', 'aaa', '0', '2', '1', '', '', '0', '0', '0');
INSERT INTO `task` VALUES ('2', 'task2', 'bbbb', '5', '2', '2', 'www.baidu.com', 'just code', '1', '10', '0');
INSERT INTO `task` VALUES ('3', 'task3', 'cccc', '1', '2', '3', '', '', '0', '0', '0');
INSERT INTO `task` VALUES ('4', 'task4', 'create an app', '1', '2', '4', '', '', '0', '0', '0');
INSERT INTO `task` VALUES ('5', 'task5', 'ddddd', '2', '2', '5', '', '', '0', '0', '0');
INSERT INTO `task` VALUES ('6', 'task6', 'eeeee', '1', '2', '6', '', '', '0', '0', '0');

-- ----------------------------
-- Table structure for `trainer`
-- ----------------------------
DROP TABLE IF EXISTS `trainer`;
CREATE TABLE `trainer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(22) NOT NULL,
  `password` varchar(22) NOT NULL,
  `phone` varchar(11) DEFAULT '',
  `about` varchar(100) DEFAULT '',
  `nickname` varchar(20) NOT NULL,
  `class_id` int(11) NOT NULL DEFAULT '0' COMMENT '班级id',
  `qq` int(11) NOT NULL,
  `true_name` varchar(30) NOT NULL COMMENT '真实姓名',
  `flower_num` int(11) DEFAULT '200' COMMENT '鲜花数目 单位：支',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of trainer
-- ----------------------------
INSERT INTO `trainer` VALUES ('1', 'tom', 'a', '1234770123', 'tom!!!!', '雷', '2', '0', '', '220');
INSERT INTO `trainer` VALUES ('2', 'test', 'a', '1324135', 'adfadsf', '教练1', '10', '0', '', '200');
INSERT INTO `trainer` VALUES ('3', 'g', 'a', '159357', '帅气的格源教练', '教练_格源', '6', '0', '', '200');
INSERT INTO `trainer` VALUES ('7', 't', 't', '15698758', 'test教师的简介', 'test', '2', '0', '', '200');
INSERT INTO `trainer` VALUES ('8', 'tangyu', '123456', '15766489901', '哈哈', 'tang\'yu', '2', '0', '', '200');
INSERT INTO `trainer` VALUES ('9', 'tangfu', 'tf6055222', '18666809698', '现居住地：广东省茂名市', 'tangfu', '8', '0', '', '200');
INSERT INTO `trainer` VALUES ('10', 'tang', '123456', '15766489901', '9', 'tang', '10', '0', '', '200');
INSERT INTO `trainer` VALUES ('11', '123', '123', '123', '123', '123', '0', '0', '', '200');
INSERT INTO `trainer` VALUES ('12', '帅哥', '123456', '18300070738', 'mhhg', '太帅', '0', '0', '', '200');
INSERT INTO `trainer` VALUES ('13', 'peter', '123456', '12345678910', '帅', '麦涌', '28', '0', '', '200');
