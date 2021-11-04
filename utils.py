from flask import request


def get_data(form):
	"""
	Convert flask form data to dictionary type with replacing empty values to None (i.e. NULL in db)
	
	:param form: Immutablemultidict, form-data by flask.request
	:return: dict of db_key:db_val
	"""
	
	form = request.form.to_dict(flat=False)
	data = {k: (v[0] if v[0] else None) for k, v in form.items()}
	
	return data


def create_clause(table, data):
	"""
	forming create query
	
	:param table: string, name of the table
	:param data: dictionary, actual data
	:return: tuple of sql and vals for cursor.execute()
	"""
	
	keys = []
	vals = []
	placeholders = ""
	
	for k, v in data.items():
		keys.append(k)
		vals.append(v)
		placeholders += ", %s"
	
	keys = ", ".join(keys)
	vals = tuple(vals)

	sql = f"INSERT INTO {table} ({keys}) VALUES ({placeholders[2:]});"
	
	return sql, vals
	
	
def update_clause(table, record_id, data):
	"""
	forming update query
	
	:param table: string, name of the table
	:param record_id: integer, the row needs to be updated by id
	:param data: dictionary, actual data
	:return: tuple of sql and vals for cursor.execute()
	"""
	clause = ""
	vals = []
	
	for k, v in data.items():
		clause += f', {k} = %s'
		vals.append(v)
	
	sql = f"UPDATE {table} SET {clause[2:]} WHERE id = {record_id};"
	
	return sql, vals

