import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from utils import create_clause, update_clause

load_dotenv()
HOST = os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PW = os.getenv('DB_PW')
DB = os.getenv('DB_NAME')


def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PW,
            database=DB,
        )
        print('Successfully connected to DB')
        return 0, connection
    except Error as err:
        return 1, err

    
# def execute_query(query):
#     error, connection = create_server_connection()
#
#     if error:
#         return connection
#
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()  # use this after modifying db
#         return 0, None
#     except Error as err:
#         return 1, err


def create_query(table, data=None):
    """
    insert data into the given table

    :param table: string, name of the table
    :param data: dictionary, default None
    :return error_status, result (query result if succeed else Error message)
    """
    
    if not data:
        return 0, "No change to make"

    error, connection = create_server_connection()

    if error:
        return 1, connection

    cursor = connection.cursor()
    
    sql, vals = create_clause(table, data)
    
    try:
        cursor.execute(sql, vals)
        connection.commit()
        return 0, None
    except Error as err:
        return 1, str(err)


def read_query(table, record_id=None):
    """
    read data of the given id in the given table from DB
    default id is None, meaning return all records
    
    :param table: string, table name
    :param record_id: integer, id of the item, default None
    :return error_status, result (query result if succeed else Error message)
    """
    
    error, connection = create_server_connection()
    
    if error:
        return 1, connection
    
    cursor = connection.cursor()
    result = None
    
    try:
        if not record_id:
            sql = f"SELECT * FROM {table};"
            vals = None
        else:
            sql = f"SELECT * FROM {table} WHERE id = %s;"
            vals = (record_id,)
        
        cursor.execute(sql, vals)
        result = cursor.fetchall()
        return 0, result
    except Error as err:
        return 1, err
    

def update_query(table, record_id=None, data=None):
    """
    overwrite the record of record_id with new data in given table
    
    :param table: string, name of table
    :param record_id: integer, id of the record, default None
    :param data: dictionary, default None
    :return error_status, result (query result if succeed else Error message)
    """
    
    if not record_id and not data:
        return 0, "No change to make"
    
    error, connection = create_server_connection()

    if error:
        return 1, connection

    cursor = connection.cursor()

    sql, vals = update_clause(table, record_id, data)

    try:
        cursor.execute(sql, vals)
        connection.commit()
        return 0, None
    except Error as err:
        return 1, str(err)
        
        
def delete_query(table, record_id):
    """
    delete the certain record form table

    :param table: string, table name
    :param record_id: integer, id of the item
    :return error_status, result (query result if succeed else Error message)
    """
    error, connection = create_server_connection()
    
    if error:
        return 1, connection
    
    cursor = connection.cursor()
    
    sql = f"DELETE FROM {table} WHERE id = %s;"
    vals = (record_id, )
    try:
        cursor.execute(sql, vals)
        connection.commit()
        return 0, None
    except Error as err:
        return 1, str(err)
    


# def insert_company(company):
#     error, connection = create_server_connection()
#
#     if error:
#         return connection
#
#     cursor = connection.cursor()
#
#     sql = """
#     INSERT INTO company (name, about, link, summary, note)
#     VALUES (%s, %s, %s, %s, %s)
#     """
#
#     vals = [(company['name'], company['about'], company['link'], company['summary'], company['note'])]
#
#     try:
#         cursor.executemany(sql, vals)
#         connection.commit()
#         return None
#     except Error as err:
#         return str(err)
#
#
# def insert_recruiter(recruiter):
#     error, connection = create_server_connection()
#
#     if error:
#         return connection
#
#     cursor = connection.cursor()
#
#     sql = """
#     INSERT INTO recruiter (name, email, phone, note, company_id)
#     VALUES (%s, %s, %s, %s, %s)
#     """
#
#     vals = [(recruiter['name'], recruiter['email'], recruiter['phone'], recruiter['note'], recruiter['company_id'])]
#
#     try:
#         cursor.executemany(sql, vals)
#         connection.commit()
#         return None
#     except Error as err:
#         return str(err)