import flask
from flask import request, jsonify
from record_methods import create_record, read_record, update_record, delete_record
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/job', methods=['GET','POST', 'PUT', 'DELETE'])
def job_methods():
	form = request.form
	if request.method == 'GET':
		error, result = read_record('job', form)
	elif request.method == 'POST':
		error, result = create_record('job', form)
	elif request.method == 'PUT':
		error, result = update_record('job', form)
	elif request.method == 'DELETE':
		error, result = delete_record('job', form)
	else:
		return 'Unsuppoerted method'
	
	if error:
		return result;
	return jsonify(result)
	

@app.route('/company', methods=['GET','POST', 'PUT', 'DELETE'])
def company_methods():
	form = request.form
	if request.method == 'GET':
		error, result = read_record('company', form)
	elif request.method == 'POST':
		error, result = create_record('company', form)
	elif request.method == 'PUT':
		error, result = update_record('company', form)
	elif request.method == 'DELETE':
		error, result = delete_record('company', form)
	else:
		return 'Unsuppoerted method'
	
	if error:
		return result;
	return jsonify(result)


@app.route('/recruiter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def recruiter_methods():
	form = request.form
	if request.method == 'GET':
		error, result = read_record('recruiter', form)
	elif request.method == 'POST':
		error, result = create_record('recruiter', form)
	elif request.method == 'PUT':
		error, result = update_record('recruiter', form)
	elif request.method == 'DELETE':
		error, result = delete_record('recruiter', form)
	else:
		return 'Unsuppoerted method'
	
	if error:
		return result;
	return jsonify(result)





app.run()