from flask import Flask, render_template

app = Flask(__name__)


app_name = "My Application Name is: life core with female"

#1 App Route di flask "hello word"
@app.route("/")
def hello_world():
    return f"<p>Bonjour, j m'appelle Popo, comment ca va? {app_name} </p>"


#2 App Route di flask
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Welcome to Flask's application </p>"


#3 App Route dengan HTML 
@app.route("/about/")
def about():
    return render_template('about_without_bostrapp.html')

#4 App Route dengan HTML with bostrapp
@app.route("/about-bostrapp/")
def about_bostrapp():
    return render_template('about.html')


#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(nama_mahasiswa):
    return "nama anda adalah {}".format(nama_mahasiswa)

#6 App Route ID
@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

#7 App Route Variabel Global
@app.route('/variabel-global/')
def variabel_global():
    return f"Selamat datang {app_name}"

#8 App Route Dictionary Variabel
@app.route('/data')
def data():
    user = {"name": "Pipi", "age": 20, "city": "IKN"}
    return render_template('data.html', user=user)

if __name__ == "__main__":
    app.run()
