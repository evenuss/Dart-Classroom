from flask import *
from flask_pymongo import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = "SECRET_KEY"
# app.config["MONGO_URI"] = "mongodb+srv://evenuss:arjuna203@cluster0-sxt0m.gcp.mongodb.net/contoso"
app.config["MONGO_URI"] = "mongodb://localhost:27017/dart_classroom"
mongo = PyMongo(app)


@app.route('/', methods=['GET','POST'])
def login():
	username = request.form.get('username')
	password = request.form.get('password')
	if request.form:
		user = mongo.db.users.count({'username':username,'password':password})
		print(user)
		if user > 0:
			return redirect('/dashboard')
		else:
			return render_template('login.html')
	return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def regUser():
	if request.method == 'POST':
		data = request.form
		username = data['username']
		email = data['email']
		email_verivied_at = datetime.now()
		password = data['password']
		jurusan = data['jurusan']
		kelas = data['kelas']
		if request.form:
			insert = mongo.db.users.insert({
				'_id':3,
				'username':username,
				'email':email,
				'email_verified_at':email_verivied_at,
				'password':password,
				'jurusan':jurusan,
				'kelas':kelas,
				'role':'siswa'
			})
			if insert:
				return render_template('login.html')
		else:
			return 'Error'
	return render_template('register.html')


@app.route('/createclass', methods=['GET','POST'])
def new_class():
	if request.method == 'POST':
		data = request.form
		leader = 1
		name = data['class_name']
		desc = data['class_desc']
		pict = data['class_pict']
		rombel = data['jurusan']
		clas = data['kelas']
		time = datetime.now()
		mongo.db.classroom.insert({
				'_id':1,
				'class_name':name,
				'class_desc':desc,
				'class_pict':pict,
				'jurusan':rombel,
				'kelas':clas,
				'createAt':time,
				'deleteAt':time
			})
			
		return 'Success!'
	return render_template('/createclass.html')

@app.route('/dashboard', methods=['GET','POST'])
def allClass():
	showAll = mongo.db.classroom.find({})
	return render_template('dashboard.html', data=showAll)		


@app.route('/jumlahdata', methods=['GET','POST'])
def jml():
	data = mongo.db.users.count({'role':'siswa'})
	print(data)
	return data
# @app.route('/', methods=['GET','POST'])
# def regUser():
# 	if 
if __name__ == '__main__':
    app.run(debug=True)
