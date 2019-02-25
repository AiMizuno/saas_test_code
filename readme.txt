config.json
	系统用到的MySQL数据库的相关信息，包括地址，端口，账号，密码等

config.py
	用于读取配置信息

connector.py
	用于连接数据库的类

private_method.py
	封装了数据库操作的函数
		db_template(sql) 执行SQL语句

		db_template_return(sql) 执行带返回结果的SQL语句

		get_tablenum(tenantId) 获取当前租户表的数量

		get_tableID(tenantId, tableName) 获取特定表的ID

		get_fieldnum(tenantId, tableID) 获取特定表列的数量

		get_fieldID(tenantId, tableID, FieldName) 获取特定列的ID

		primary_check(tenantId, tableID, FieldName) 判断是否为主键

base_method.py
	提供Saas数据库的基本操作的接口
		create_table(tenantId, tableName, column) 创建一个表，其中column包括 数据类型，列名字，表ID，列的编号，是否索引

		insert_data(tenantId, tableName, columns, values) 向指定表插入一条数据

		delete_data(tenantId, tableName, columns, conditions, condition_num) 删除数据，其中columns和condition分别为列和条件的list，condition_num为list的长度

		select_data_all(tenantId, tableName)全表查询

		select_data_condition(tenantId, tableName, columns, num_of_columns, conditions_columns, conditions_operator, conditions, condition_num) 条件查询（columns=["*"]为查询所有列）

		update(tenantId, tableName, columns, values, num_of_columns, conditions_columns, conditions_operator, conditions, condition_num)更新表
saas_method.py
	提供Saas数据库的基本操作的接口
		add_field(tenantId, tableName, column_name, column_type, is_index) 为特定表增加一列
		
		delete_field(tenantId, tableName, fieldName) 为特定表删除一列

		delete_table(tenantId,tableName) 删除一个表

data_generator.py
	用于随机生成数据
		genrate_data(number) 为每个表插入若干条元组

demo.py
	创建测试用的租户以及数据，其中租户1为登山队；2为书法协会；3为中大职协

Transaction.py
	租户的一些事务，数字开头的方法代表租户特有事物

使用说明
	1.使用前修改config.json里面的配置
	2.使用时只需要引用base_method.py和saas_method.py即可
	3.接口表达能力有限，对于复杂操作需要进行二次处理
	4.这是一条测试信息