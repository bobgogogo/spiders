/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50715
 Source Host           : localhost
 Source Database       : spider

 Target Server Type    : MySQL
 Target Server Version : 50715
 File Encoding         : utf-8

 Date: 08/29/2018 17:24:40 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `ip_proxy_pool`
-- ----------------------------
DROP TABLE IF EXISTS `ip_proxy_pool`;
CREATE TABLE `ip_proxy_pool` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) NOT NULL DEFAULT '',
  `port` int(10) NOT NULL DEFAULT '80',
  `create_time` float(16,6) NOT NULL DEFAULT '0.000000',
  `update_time` float(16,6) NOT NULL DEFAULT '0.000000',
  `http_type` varchar(8) NOT NULL DEFAULT '',
  `speed` varchar(8) NOT NULL DEFAULT '0.0000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=701 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
