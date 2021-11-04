from db import create_query, read_query, update_query, delete_query
from datetime import date
from utils import get_data


def create_record(table, form):
	"""
	create a record in the given table

	:param table: string, name of the table
	:param form:  Immutablemultidict, form-data by flask.request
	:return: None or Error message
	"""
	# get form key, value pair only if value is not empty else use NULL
	data = get_data(form)
	data['added_at'] = date.today()
	return create_query(table, data)


def read_record(table, form):
	"""
	read a record or all records from the given table

	:param table: string, name of the table
	:param form:  Immutablemultidict, form-data by flask.request
	:return: None or Error message
	"""
	
	record_id = form.get('id')
	return read_query(table, record_id)


def update_record(table, form):
	"""
	update a record in the given table

	:param table: string, name of the table
	:param form:  Immutablemultidict, form-data by flask.request
	:return: None or Error message
	"""
	data = get_data(form)
	record_id = data.pop('id')
	return update_query(table, record_id, data)


def delete_record(table, form):
	"""
	delete a record from the given table

	:param table: string, name of the table
	:param form: Immutablemultidict, form-data by flask.request
	:return: None or Error message
	"""
	record_id = form.get('id')
	return delete_query(table, record_id)