config.json
	ϵͳ�õ���MySQL���ݿ�������Ϣ��������ַ���˿ڣ��˺ţ������

config.py
	���ڶ�ȡ������Ϣ

connector.py
	�����������ݿ����

private_method.py
	��װ�����ݿ�����ĺ���
		db_template(sql) ִ��SQL���

		db_template_return(sql) ִ�д����ؽ����SQL���

		get_tablenum(tenantId) ��ȡ��ǰ�⻧�������

		get_tableID(tenantId, tableName) ��ȡ�ض����ID

		get_fieldnum(tenantId, tableID) ��ȡ�ض����е�����

		get_fieldID(tenantId, tableID, FieldName) ��ȡ�ض��е�ID

		primary_check(tenantId, tableID, FieldName) �ж��Ƿ�Ϊ����

base_method.py
	�ṩSaas���ݿ�Ļ��������Ľӿ�
		create_table(tenantId, tableName, column) ����һ��������column���� �������ͣ������֣���ID���еı�ţ��Ƿ�����

		insert_data(tenantId, tableName, columns, values) ��ָ�������һ������

		delete_data(tenantId, tableName, columns, conditions, condition_num) ɾ�����ݣ�����columns��condition�ֱ�Ϊ�к�������list��condition_numΪlist�ĳ���

		select_data_all(tenantId, tableName)ȫ���ѯ

		select_data_condition(tenantId, tableName, columns, num_of_columns, conditions_columns, conditions_operator, conditions, condition_num) ������ѯ��columns=["*"]Ϊ��ѯ�����У�

		update(tenantId, tableName, columns, values, num_of_columns, conditions_columns, conditions_operator, conditions, condition_num)���±�
saas_method.py
	�ṩSaas���ݿ�Ļ��������Ľӿ�
		add_field(tenantId, tableName, column_name, column_type, is_index) Ϊ�ض�������һ��
		
		delete_field(tenantId, tableName, fieldName) Ϊ�ض���ɾ��һ��

		delete_table(tenantId,tableName) ɾ��һ����

data_generator.py
	���������������
		genrate_data(number) Ϊÿ�������������Ԫ��

demo.py
	���������õ��⻧�Լ����ݣ������⻧1Ϊ��ɽ�ӣ�2Ϊ�鷨Э�᣻3Ϊ�д�ְЭ

Transaction.py
	�⻧��һЩ�������ֿ�ͷ�ķ��������⻧��������

ʹ��˵��
	1.ʹ��ǰ�޸�config.json���������
	2.ʹ��ʱֻ��Ҫ����base_method.py��saas_method.py����
	3.�ӿڱ���������ޣ����ڸ��Ӳ�����Ҫ���ж��δ���