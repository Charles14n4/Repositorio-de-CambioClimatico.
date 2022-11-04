from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from config import config


app = Flask (__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345678"
app.config["MYSQL_DB"] = "CambioClimatico"
mysql = MySQL(app)

app.secret_key = "gaysumusreverentes"

@app.route("/")
def bienvenido():
    return render_template('bienvenido.html')

@app.route("/home")
def Index():
    return render_template('index.html')


# ESTAS RUTAS LAS PUEDEN EDITAR
@app.route("/indexpa")
def Indexpa():
    return render_template('indexpa.html')

@app.route("/imagenes")
def Imagenes():
    return render_template('imagenes.html')
# HASTA AQUI Y PUEDEN AGREGAR OTRAS TAMBIEN
@app.route("/somos")
def somos():
    return render_template('somos.html')


# ESTA ES LA CONEXION (No la vayan a editar)
@app.route("/cambioclimatico", methods=['POST'])
def add_contact():
     if request.method == 'POST':
        Nombre = request.form["Nombre"]
        Correo = request.form["Correo"]
        Contraseña = request.form["Contraseña"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO REGISTRO (Nombre, Correo, Contraseña) VALUES (%s, %s, %s)",
        (Nombre, Correo, Contraseña))
        mysql.connection.commit()
        return redirect(url_for("Indexpa")) # Este si lo pueden cambiar

if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run(port = 3000, debug = True)