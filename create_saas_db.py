#! /usr/bin/env python   
# -*- coding: utf-8 -*-  

import sys
sys.path.append('../utils/')
sys.path.append('./utils/')

from connector import Connector

Table_sql = """
    DROP TABLE IF EXISTS saas_table;
    CREATE TABLE saas_table(
        tableId serial PRIMARY KEY ,
        tableName VARCHAR(50),
        tenantId INTEGER
    );
"""

Field_sql = """
    DROP TABLE IF EXISTS saas_field;
    CREATE TABLE saas_field(
        fieldId serial PRIMARY KEY,
        dataType VARCHAR(50),
        fieldName VARCHAR(50),
        tableId INTEGER,
        fieldNum INTEGER,
        tenantId INTEGER,
        isIndexed BOOL
    );
"""

Data_sql = """
    DROP TABLE IF EXISTS saas_data;
    CREATE TABLE saas_data(
        Id serial,
        tableId INTEGER,
        tenantId INTEGER,
        naturalName VARCHAR(100),"""

for i in range(0, 50):
    Data_sql += """
        value%d TEXT,""" % i
Data_sql += """
        PRIMARY KEY(Id)
    );"""

Index_sql = """
DROP TABLE IF EXISTS "public"."saas_index";
CREATE TABLE "public"."saas_index" (
  "tenantId" int4 NOT NULL,
  "tableId" int4 NOT NULL,
  "fieldNum" int4 NOT NULL,
  "recordId" int4 NOT NULL,
  "stringValue" varchar(100) COLLATE "pg_catalog"."default",
  "numValue" numeric(100),
  "dateValue" timestamp(6),
  "jointValue" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."saas_index" ADD CONSTRAINT "saas_index_pkey" PRIMARY KEY ("tenantId", "tableId", "fieldNum", "recordId");"""

def create_saas_db():
    conn = Connector()
    conn.connect()

    conn.execute(Table_sql)
    conn.execute(Field_sql)
    conn.execute(Data_sql)
    conn.execute(Index_sql)

    conn.close()

    print("创建universal table成功!")