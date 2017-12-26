from connector import Connector


def db_template(sql):
    try:
        conn = Connector()
        conn.connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print('load sql')
        print('e\t' + str(e))
    finally:
        conn.close()


def db_template_return(sql):
    rows = []
    try:
        conn = Connector()
        conn.connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
    except Exception as e:
        print('load sql')
        print('e\t' + str(e))
    finally:
        conn.close()
        return rows


def get_tablenum(tenantId):
    count = 0
    sql = "select count(*) from saas_table where tenantId = " + str(tenantId)
    rows = db_template_return(sql)
    for row in rows:
            if row[0] is not None:
                count = row[0]
    return count 


def get_fieldnum(tenantId, tableID):
    count = 0
    sql = "select max(fieldNum) from saas_field where tenantId = " + str(tenantId) + " and tableID=" + tableID
    rows = db_template_return(sql)
    for row in rows:
            if row[0] is not None:
                count = row[0]
    return count 


def get_tableID(tenantId, tableName):
    ID = "Not Found"
    sql = "select tableID from saas_table where tenantId = " + str(tenantId) + " And tableName = \'" + str(tableName) + "\'"
    rows = db_template_return(sql)
    for row in rows:
            ID = row[0]
    return ID


def get_fieldID(tenantId, tableID, FieldName): #大小写
    Num = "Not Found"
    sql = "select fieldNum from saas_field where tenantId = " + str(tenantId) + " and tableId=" + str(tableID) + " and fieldName=\'" + str(FieldName) + "\'"
    rows = db_template_return(sql)
    for row in rows:
            Num = row[0]
    return Num


def primary_check(tenantId, tableID, FieldName): #大小写
    ans = False
    sql = "select isIndexed from saas_field where tenantId = " + str(tenantId) + " and tableId=" + str(tableID) + " and fieldName=\'" + str(FieldName) + "\'"
    rows = db_template_return(sql)
    for row in rows:
        ans = row[0]
    return ans