from flask import Flask, render_template, request, url_for, redirect, flash
from models import db
from models import contacts


app = Flask(__name__)
app.secret_key = '8az43a6he9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/flaskcontacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

@app.route('/')
def index():
	values = contacts.query.all()
	return render_template('index.html', values=values)

@app.route('/add_contact', methods=['POST'])
def add_contact():
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		value = contacts(fullname=fullname, phone=phone, email=email)
		db.session.add(value)
		db.session.commit()
		flash('Contacts Added Successfully')
	return redirect(url_for('index'))
	

@app.route('/edit/<string:id>')
def get_contact(id):
	get_value = contacts.query.filter_by(id=int(id)).first()
	return render_template('edit_contact.html', value=get_value)

@app.route('/update/<string:id>', methods=['POST'])
def update_contact(id):
	if request.method == 'POST':
		update_value = contacts.query.filter_by(id=int(id)).first()
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		update_value.fullname = fullname
		update_value.phone = phone
		update_value.email = email
		db.session.commit()
		flash('Contact Update Successfully')
	return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
	value_del = contacts.query.filter_by(id=int(id)).delete()
	db.session.commit()
	flash('Contact Delete Successfully')
	return redirect(url_for('index'))

if __name__ == '__main__':
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(port=3000, debug=True)