/*
 Navicat Premium Data Transfer

 Source Server         : benchmarksql
 Source Server Type    : PostgreSQL
 Source Server Version : 90606
 Source Host           : localhost:5432
 Source Catalog        : postgres
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90606
 File Encoding         : 65001

 Date: 01/12/2017 16:27:42
*/


-- ----------------------------
-- Table structure for saas_index
-- ----------------------------
DROP TABLE IF EXISTS "public"."saas_index";
CREATE TABLE "public"."saas_index" (
  "tenantId" int4 NOT NULL,
  "tableId" int4 NOT NULL,
  "fieldNum" int4 NOT NULL,
  "recordId" int4,
  "stringValue" varchar(100) COLLATE "pg_catalog"."default",
  "numValue" numeric(100),
  "dateValue" timestamp(6),
  "jointValue" varchar(100) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Primary Key structure for table saas_index
-- ----------------------------
ALTER TABLE "public"."saas_index" ADD CONSTRAINT "saas_index_pkey" PRIMARY KEY ("tenantId", "tableId", "fieldNum");
