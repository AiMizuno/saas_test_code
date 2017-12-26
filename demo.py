from base_method import *
from saas_method import *
from create_saas_db import *
from data_generator import *

field_sql = """
    INSERT INTO saas_field( dataType, fieldName, tableId, fieldNum, tenantId, isIndexed)
    VALUES ( '%s', '%s', %d, %d, %d, %s);
"""

if __name__ == '__main__':
    print("创建数据库...")
    create_saas_db()
    print("创建数据表完成。")
    print("添加租户...")
    print("---------登山队---------")
    print("创建成员表")
    tenantID = 1
    tableName = "member"
    column = [("ID", "int", True), ("姓名", "varchar", False), ("学号", "varchar", False), ("性别", "varchar", False)
              , ("职位", "varchar", False), ("校区", "varchar", False), ("年级院系专业", "varchar", False),
              ("家庭所在地", "varchar", False), ("身高", "varchar", False),
              ("QQ", "varchar", False), ("邮箱", "varchar", False), ("手机号码", "varchar", False),
              ("紧急联系人姓名", "varchar", False), ("与紧急联系人关系", "varchar", False), ("紧急联系人电话", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建活动表")
    tableName = "activity"
    column = [("ID", "int", True), ("活动名称", "varchar", False), ("活动负责人", "varchar", False), ("时间", "varchar", False),
              ("地点", "varchar", False), ("参与人", "varchar", False), ("活动描述", "varchar", False),
              ("活动流程1", "varchar", False), ("活动流程2", "varchar", False), ("活动流程3", "varchar", False),
              ("活动流程4", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建部门表")
    tableName = "department"
    column = [("ID", "int", True), ("部门名称", "varchar", False), ("部门描述", "varchar", False), ("上级部门", "varchar", False),
              ("下级子部门", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建登山设备表")
    tableName = "facility"
    column = [("ID", "int", True), ("设备名称", "varchar", False), ("设备负责人", "varchar", False), ("购入时间", "varchar", False),
              ("价格", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("登山队创建完成！")

    print("---------书法协会---------")
    tenantID = 2

    print("创建成员表")
    tableName = "member"
    column = [("ID", "int", True), ("姓名", "varchar", False), ("性别", "varchar", False), ("年级院系专业", "varchar", False),
              ("手机号码", "varchar", False), ("邮箱", "varchar", False), ("QQ", "varchar", False),
              ("所属部门", "varchar", False), ("职位", "varchar", False), ("教授类别", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建会员表")
    tableName = "participant"
    column = [("ID", "int", True), ("姓名", "varchar", False), ("性别", "varchar", False), ("年级院系专业", "varchar", False),
              ("手机号码", "varchar", False), ("邮箱", "varchar", False), ("QQ", "varchar", False),
              ("所属老师", "varchar", False), ("所学技能", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建艺术品表")
    tableName = "piece"
    column = [("ID", "int", True), ("名称", "varchar", False), ("作者", "varchar", False), ("收入日期", "varchar", False),
              ("创作日期", "varchar", False), ("捐赠人", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建活动表")
    tableName = "activity"
    column = [("ID", "int", True), ("活动名称", "varchar", False), ("活动负责人", "varchar", False), ("时间", "varchar", False),
              ("地点", "varchar", False), ("参与人", "varchar", False), ("活动描述", "varchar", False),
              ("活动流程1", "varchar", False), ("活动流程2", "varchar", False), ("活动流程3", "varchar", False),
              ("活动流程4", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("书法协会创建完成！")

    print("---------中大职协---------")
    tenantID = 3
    tableName = "member"
    print("创建成员表")
    column = [("ID", "int", True), ("姓名", "varchar", False),  ("职位", "varchar", False),
              ("性别", "varchar", False), ("年级院系专业", "varchar", False), ("学号", "varchar", False),
              ("身高", "int", False), ("QQ", "varchar", False), ("邮箱", "varchar", False), ("手机号码", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建活动表")
    tableName = "activity"
    column = [("ID", "int", True), ("活动名称", "varchar", False), ("活动负责人", "varchar", False), ("时间", "varchar", False),
              ("地点", "varchar", False), ("参与人", "varchar", False), ("活动描述", "varchar", False),
              ("活动流程1", "varchar", False), ("活动流程2", "varchar", False), ("活动流程3", "varchar", False),
              ("活动流程4", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("创建实习登记表")
    tableName = "practice"
    column = [("ID", "int", True), ("名字", "varchar", False), ("实习单位", "varchar", False), ("实习时间", "varchar", False)]
    create_table(tenantID, tableName, column)

    print("中大职协创建完成！")
    print("添加租户完成.")
    genrate_data(1000)
