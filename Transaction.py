from base_method import *
import random


def random_string():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt


def add_member(tenantid):  # 获取成员的最大ID并且加入一个新成员
    rows = select_data_condition(tenantid, "member", ["id"], 1, [], [], [], 0)
    max_id = 0
    for row in rows:
        if row[0] > max_id:
            max_id = row[0]
    max_id += 1
    insert_data(tenantid, "member", ["id", "姓名"], [max_id, random_string()])


def delete_member(tenantid, id):  # 删除特定ID的成员
    delete_data(tenantid, "member", ["id"], id, 1)


def update_member(tenantid, id, name):  # 更新特定成员的名字
    update(tenantid, "member", ["姓名"], name, 1, ["id"], ["="], [id], 1)


def get_all_member(tenantid):  # 获取所有成员
    select_data_all(tenantid, "member")


def _1_new_activity():  # 创建登山队的活动
    column = ["ID", "活动名称", "活动负责人", "时间", "地点", "参与人", "活动描述", "活动流程1", "活动流程2", "活动流程3",
              "活动流程4"]
    rows = select_data_condition(1, "activity", ["id"], 1, [], [], [], 0)
    max_id = 0
    for row in rows:
        if row[0] > max_id:
            max_id = row[0]
    max_id += 1
    value = [max_id]
    for i in range(1, len(column)):
        value.append(random_string())
    insert_data(1, "activity", column, value)


def _1_modify_department(name, description):  # 获取指定部门并修改其描述
    id = select_data_condition(1, "department", ["id"], 1, ["部门名字"], ["="], [name], 1)
    update(1, "department", ["部门描述"], [description], 1, ["id"], ["="], [id], 1)


def _1_get_facility(name):  # 获取特定名字的设备信息
    return select_data_condition(1, "facility", ["*"], 1, ["设备名称"], ["="], [name], 1)


def _2_create_participant(number):  # 招募若干个新成员
    rows = select_data_condition(2, "participant", ["id"], 1, [], [], [], 0)
    max_id = 0
    for row in rows:
        if row[0] > max_id:
            max_id = row[0]
    max_id += 1
    for i in range(max_id, max_id+number+1):
        column = ["ID", "姓名", "性别", "年级院系专业", "手机号码", "邮箱", "QQ", "所属老师", "所学技能"]
        value = [i]
        for j in range(1, len(column)):
            value.append(random_string())
        insert_data(2, "participant", column, value)


def _2_add_piece(name):  # 删除指定名字的收藏品
    delete_data(1, "piece", ["名称"], name, 1)


def _2_get_piece(name):  # 获取指定作者的作品
    select_data_condition(1, "piece", ["*"], 1, ["作者"], ["="], [name], 1)


def _3_new_activity():  # 创建职协的活动
    column = ["ID", "活动名称", "活动负责人", "时间", "地点", "参与人", "活动描述", "活动流程1", "活动流程2", "活动流程3", "活动流程4"]
    rows = select_data_condition(3, "activity", ["id"], 1, [], [], [], 0)
    max_id = 0
    for row in rows:
        if row[0] > max_id:
            max_id = row[0]
    max_id += 1
    value = [max_id]
    for i in range(1, len(column)):
        value.append(random_string())
    insert_data(3, "activity", column, value)


def _3_new_paritce():  # 录入新的实习信息
    column = ["ID", "名字", "实习单位", "实习时间"]
    rows = select_data_condition(3, "practice", ["id"], 1, [], [], [], 0)
    max_id = 0
    for row in rows:
        if row[0] > max_id:
            max_id = row[0]
    max_id += 1
    value = [max_id]
    for i in range(1, len(column)):
        value.append(random_string())
    insert_data(3, "practice", column, value)
