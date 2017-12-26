from private_method import *

table_sql = """
    INSERT INTO saas_table(tableName, tenantId)
    VALUES ('%s', %d);
"""

field_sql = """
    INSERT INTO saas_field( dataType, fieldName, tableId, fieldNum, tenantId, isIndexed)
    VALUES ( '%s', '%s', %d, %d, %d, %s);
"""

# dataType, fieldName, tableId, fieldNum, tenantId, isIndexed


def create_table(tenantId, tableName, column):
    table_para = (tableName, tenantId)
    sql = table_sql % table_para   # 创建表
    field_num = 0
    db_template(sql)
    count = get_tableID(tenantId, tableName)
    sql = ""
    for i in column:  # 创建列
        tmp = (i[1], i[0], count, field_num, tenantId, i[2])
        sql += (field_sql % tmp)
        field_num += 1
    db_template(sql)


def insert_data(tenantId, tableName, columns, values):
    tableID = get_tableID(tenantId, tableName)
    sql = "insert into saas_data (tableID, tenantId,"
    cnt = 0
    for i in columns: 
        num = get_fieldID(tenantId, tableID, i)
        sql += "value" + str(num) + ","
        cnt += 1
    sql = sql[:-1]
    sql += ") values (" + str(tableID) + "," + str(tenantId) + ","
    for i in values: 
        sql += "\'" + str(i) + "\',"
    sql = sql[:-1]
    sql += ")"
    db_template(sql)
    sql = "select fieldNum,fieldName from saas_field where tenantId= " + str(tenantId) + " and tableID= " + str(tableID) + " and isIndexed= True"
    field_rows = db_template_return(sql)
    for i in range(0,cnt):
        for row in field_rows:
            if columns[i] == row[1]:
                cnt = get_fieldID(tenantId,tableID, columns[i])
                sql = "select Id from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID) \
                      + " and value" + str(cnt) + "= \'" + str(values[i]) + "\'"
                id = db_template_return(sql)
                sql = "insert into public.saas_index ( \"tenantId\", \"tableId\" , \"fieldNum\", \"recordId\", \"stringValue\") values("
                sql += str(tenantId) + " , " + str(tableID) + " ," + str(row[0]) + " , " + str(id[0][0]) + " , \'" + str(values[i]) + "\');"
                db_template(sql)


def delete_data(tenantId, tableName, columns, conditions, condition_num):
    tableID = get_tableID(tenantId, tableName)
    sql = "select Id from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    for i in range(0, condition_num):
        num = get_fieldID(tenantId, tableID, columns[i])
        sql += " and value" + str(num) + " =\'" + str(conditions[i]) + "\'"
    rows = db_template_return(sql)
    for row in rows:
         sql = "delete from saas_index where recordId= " + row[0]
         db_template(sql)

    sql = "delete from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    for i in range(0,condition_num):
        num = get_fieldID(tenantId, tableID, columns[i])
        sql += " and value" + str(num) + " =\'" + str(conditions[i]) + "\'"
    db_template(sql)


def select_data_all(tenantId, tableName):
    tableID = get_tableID(tenantId, tableName)
    rows = []

    sql = "select fieldNum from saas_field where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    field_rows = db_template_return(sql)

    sql = "select "
    for i in field_rows:
        sql += " value" + str(i[0]) + ","
    sql = sql[:-1]
    sql += " from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    rows = db_template_return(sql)
    return rows


def select_data_condition(tenantId, tableName, columns, num_of_columns, conditions_columns, conditions_operators, conditions, condition_num):
    tableID = get_tableID(tenantId, tableName)
    rows = []
    sql = "select "
    for i in range(num_of_columns):
        if columns[i] == "*":
            sql += "*"
        else:
            num = get_fieldID(tenantId, tableID, columns[i])
            sql += " value" + str(num) + " ,"
    sql = sql[:-1]
    sql += " from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    for i in range(0, condition_num):
        num = get_fieldID(tenantId, tableID, conditions_columns[i])
        pri = primary_check(tenantId, tableID, conditions_columns[i])
        if pri is True:
            sql += " and Id in ( select \"recordId\" from saas_index where \"stringValue\"" + conditions_operators[i] + " \'" + str(conditions[i]) + "\') "
        else:
            sql += " and value" + str(num) + conditions_operators[i] + "\'" + str(conditions[i]) + "\'"
    rows = db_template_return(sql)
    return rows


def update(tenantId, tableName, columns, values, num_of_columns, conditions_columns, conditions_operators, conditions, condition_num):
    tableID = get_tableID(tenantId, tableName)
    sql = "update saas_data set"
    for i in range(num_of_columns):
        num = get_fieldID(tenantId,tableID,columns[i])
        sql += " value" + str(num) + " = \'" + str(values[i]) + "\',"
    sql = sql[:-1]
    sql += "where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    for i in range(0, condition_num):
        num = get_fieldID(tenantId, tableID, conditions_columns[i])
        pri = primary_check(tenantId, tableID, conditions_columns[i])
        if pri is True:
            sql += " and Id in ( select \"recordId\" from saas_index where \"stringValue\"" + conditions_operators[
                i] + " \'" + str(conditions[i]) + "\') "
        else:
            sql += " and value" + str(num) + conditions_operators[i] + "\'" + str(conditions[i]) + "\'"
    db_template(sql)
