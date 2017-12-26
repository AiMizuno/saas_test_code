from base_method import *
from private_method import *
import random


def random_string():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt


def generate_template(tenantid, tableid, columns, values):
    for j in range(1, len(columns)):
        values.append(random_string())
    # insert_data(tenantid, tablename, columns, values)
    sql = "insert into saas_data (tableID, tenantId,"
    for i in range(0, len(columns)):
        sql += "value" + str(i) + ","
    sql = sql[:-1]
    sql += ") values (" + str(tableid) + "," + str(tenantid) + ","
    for i in values:
        sql += "\'" + str(i) + "\',"
    sql = sql[:-1]
    sql += ")"
    db_template(sql)

    sql = "select Id from saas_data where tenantId= " + str(tenantid) + " and tableID= " + str(tableid) \
          + " and value" + str(0) + "= \'" + str(values[0]) + "\'"
    id = db_template_return(sql)
    sql = "insert into public.saas_index ( \"tenantId\", \"tableId\" , \"fieldNum\", \"recordId\", \"stringValue\") values("
    sql += str(tenantid) + " , " + str(tableid) + " ," + str(0) + " , " + str(
        id[0][0]) + " , \'" + str(values[0]) + "\');"
    db_template(sql)


def genrate_data(number):
    print("开始插入数据。。。")
    for i in range(1, number+1):
        columns = ["ID", "姓名", "学号", "性别", "职位", "校区", "年级院系专业", "家庭所在地", "身高", "QQ", "邮箱",
                   "手机号码", "紧急联系人姓名", "与紧急联系人关系", "紧急联系人电话"]
        generate_template(1, 1, columns, [i])

        columns = ["ID", "活动名称", "活动负责人", "时间", "地点", "参与人", "活动描述", "活动流程1", "活动流程2", "活动流程3",
                   "活动流程4"]
        generate_template(1, 2, columns, [i])

        columns = ["ID", "部门名称", "部门描述", "上级部门", "下级子部门"]
        generate_template(1, 3, columns, [i])

        columns = ["ID", "设备名称", "设备负责人", "购入时间", "价格"]
        generate_template(1, 4, columns, [i])

        columns = ["ID", "姓名", "性别", "年级院系专业", "手机号码", "邮箱", "QQ", "所属部门", "职位", "教授类别"]
        generate_template(2, 5, columns, [i])

        columns = ["ID", "姓名", "性别", "年级院系专业", "手机号码", "邮箱", "QQ", "所属老师", "所学技能"]
        generate_template(2, 6, columns, [i])

        columns = ["ID", "名称", "作者", "收入日期", "创作日期", "捐赠人"]
        generate_template(2, 7, columns, [i])

        columns = ["ID", "活动名称", "活动负责人", "时间", "地点", "参与人", "活动描述", "活动流程1", "活动流程2", "活动流程3",
                   "活动流程4"]
        generate_template(2, 8, columns, [i])

        columns = ["ID", "姓名", "职位", "性别", "年级院系专业", "学号", "身高", "QQ", "邮箱", "手机号码"]
        generate_template(3, 9, columns, [i])

        columns = ["ID", "活动名称", "活动负责人", "时间", "地点", "参与人", "活动描述", "活动流程1", "活动流程2", "活动流程3",
                   "活动流程4"]
        generate_template(3, 10, columns, [i])

        columns = ["ID", "名字", "实习单位", "实习时间"]
        generate_template(3, 11, columns, [i])
    print("插入完成")
