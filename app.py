from unicodedata import name
from flask import Flask, redirect, render_template, request, session, url_for
import mysql.connector
import base64
import controlador
from datetime import timedelta
from functools import wraps


conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="ayuntamiento")
cursor= conn.cursor()

app = Flask(__name__)
app.secret_key="secret key"


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username_admin' in session:
            return f(*args, **kwargs)
        else:
            return render_template('access-denied.html')
    return wrap


def capturist_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username_capturist' in session:
            return f(*args, **kwargs)
        else:
            return render_template('access-denied.html')
    return wrap


def guest_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username_guest' in session:
            return f(*args, **kwargs)
        else:
            return render_template('access-denied.html')
    return wrap

@app.route('/')
@app.route('/inicio')
def index():
    return render_template("inicio.html")


@app.route('/adminhome')
@admin_required
def home():
    return render_template('admin_home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor.execute('SELECT user, password, idprivilegios from usuario where user=%s and password=%s and idprivilegios=1', (username,password))
        record = cursor.fetchone()
        if record:
            session['username_admin'] = username
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=120)
            return redirect(url_for('home'))
        else:
            msg="Incorrect"

    return render_template('login.html', msg=msg)


@app.route('/loginCapturista')
def loginCapturista():
    return render_template('login_capturista.html')


@app.route('/capturista')
@capturist_required
def capturista():
    return render_template('capturista_home.html')

@app.route('/loginC', methods=['GET','POST'])
def loginC():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor.execute('SELECT user, password, idprivilegios from usuario where user=%s and password=%s and idprivilegios=2', (username,password))        
        record = cursor.fetchone()
        if record:
            session['username_capturist'] = username
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=120)
            return redirect(url_for('capturista'))
        else:
            msg="Incorrect"

    return render_template('login_capturista.html', msg=msg)

@app.route('/loginvisitante')
def loginvisitante():
    return render_template('login_visitante.html')


@app.route('/visitante')
@guest_required
def visitante():
    return render_template('visitante.html')

@app.route('/loginV', methods=['GET','POST'])
def loginV():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor.execute('SELECT user, password, idprivilegios from usuario where user=%s and password=%s and idprivilegios=3', (username,password))        
        record = cursor.fetchone()
        if record:
            session['username_guest'] = username
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=120)
            return redirect(url_for('visitante'))
        else:
            msg="Incorrect"

    return render_template('login_visitante.html', msg=msg)


@app.route('/reportesV')
@guest_required
def reportesV():
    reportes = controlador.obtener_reporte()
    return render_template('reportes_visitante.html', reportes=reportes)


@app.route('/formularioCapturista')
@capturist_required
def formularioCapturista():
    return render_template('formularioCapturista.html')


@app.route('/formularioAdministrador')
@admin_required
def formularioAdministrador():
    return render_template('formularioAdministrador.html')

@app.route('/deleted_reports')
@admin_required
def deleted_reports():
    respaldos = controlador.obtener_respaldo()
    return render_template('view_deleted_reports.html', respaldos = respaldos)

@app.route('/reportesA')
@admin_required
def reportesA():
    reportes = controlador.obtener_reporte()
    return render_template('reportes_administrador.html', reportes=reportes)

@app.route('/captura', methods=['POST'])
def captura():
    if request.method == 'POST':
        if not request.files.get('cartadepoder'):
            file = request.files['solicitud']
            file1 =request.files['acreditacion']
            file2 =request.files['actaconstitutiva']
            file3 =request.files['identificacion']
            file4 =request.files['ubicacion']
            file5 =request.files['plano']
            
            blob = base64.b64encode(file.read())
            blob1 = base64.b64encode(file1.read())
            blob2 = base64.b64encode(file2.read())
            blob3 = base64.b64encode(file3.read())
            blob4 = base64.b64encode(file4.read())
            blob5 = base64.b64encode(file5.read())
            
            id = request.form['id']
            descripcion = request.form['descripcion']
            estatus = request.form['estatus']

            query='INSERT INTO `expediente` (`idsolicitud`,`solicitud`,`acreditacion`,`acta_constitutiva`,`identificacion`,`ubicacion`,`plano`,`descripcion`,`estatus`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           
            if blob:
                cursor.execute(query,(id,blob,blob1,blob2,blob3,blob4,blob5,descripcion,estatus))
                conn.commit()
            return redirect(url_for('capturista'))

        else:
            file = request.files['solicitud']
            file1 =request.files['acreditacion']
            file2 =request.files['actaconstitutiva']
            file3 =request.files['identificacion']
            file4 =request.files['ubicacion']
            file5 =request.files['plano']
            file6 =request.files['cartadepoder']
            blob = base64.b64encode(file.read())
            blob1 = base64.b64encode(file1.read())
            blob2 = base64.b64encode(file2.read())
            blob3 = base64.b64encode(file3.read())
            blob4 = base64.b64encode(file4.read())
            blob5 = base64.b64encode(file5.read())
            blob6 = base64.b64encode(file6.read())
            id = request.form['id']
            descripcion = request.form['descripcion']
            estatus = request.form['estatus']

            query='INSERT INTO `expediente` (`idsolicitud`,`solicitud`,`acreditacion`,`acta_constitutiva`,`identificacion`,`ubicacion`,`plano`,`carta_poder`,`descripcion`,`estatus`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           
            if blob:
                cursor.execute(query,(id,blob,blob1,blob2,blob3,blob4,blob5,blob6,descripcion,estatus))
                conn.commit()
                return redirect(url_for('capturista'))
            else:
                return '<h1> Fallo </h1>'


@app.route('/capturaA', methods=['POST'])
def capturaA():
    if request.method == 'POST':
        if not request.files.get('cartadepoder'):
            file = request.files['solicitud']
            file1 =request.files['acreditacion']
            file2 =request.files['actaconstitutiva']
            file3 =request.files['identificacion']
            file4 =request.files['ubicacion']
            file5 =request.files['plano']
            
            blob = base64.b64encode(file.read())
            blob1 = base64.b64encode(file1.read())
            blob2 = base64.b64encode(file2.read())
            blob3 = base64.b64encode(file3.read())
            blob4 = base64.b64encode(file4.read())
            blob5 = base64.b64encode(file5.read())
            
            id = request.form['id']
            descripcion = request.form['descripcion']
            estatus = request.form['estatus']

            query='INSERT INTO `expediente` (`idsolicitud`,`solicitud`,`acreditacion`,`acta_constitutiva`,`identificacion`,`ubicacion`,`plano`,`descripcion`,`estatus`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           
            if blob:
                cursor.execute(query,(id,blob,blob1,blob2,blob3,blob4,blob5,descripcion,estatus))
                conn.commit()
            return redirect(url_for('home'))

        else:
            file = request.files['solicitud']
            file1 =request.files['acreditacion']
            file2 =request.files['actaconstitutiva']
            file3 =request.files['identificacion']
            file4 =request.files['ubicacion']
            file5 =request.files['plano']
            file6 =request.files['cartadepoder']
            blob = base64.b64encode(file.read())
            blob1 = base64.b64encode(file1.read())
            blob2 = base64.b64encode(file2.read())
            blob3 = base64.b64encode(file3.read())
            blob4 = base64.b64encode(file4.read())
            blob5 = base64.b64encode(file5.read())
            blob6 = base64.b64encode(file6.read())
            id = request.form['id']
            descripcion = request.form['descripcion']
            estatus = request.form['estatus']

            query='INSERT INTO `expediente` (`idsolicitud`,`solicitud`,`acreditacion`,`acta_constitutiva`,`identificacion`,`ubicacion`,`plano`,`carta_poder`,`descripcion`,`estatus`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           
            if blob:
                cursor.execute(query,(id,blob,blob1,blob2,blob3,blob4,blob5,blob6,descripcion,estatus))
                conn.commit()
                return redirect(url_for('home'))
            else:
                return '<h1> Fallo </h1>'


@app.route('/reportes')
def reportes():
    reportes = controlador.obtener_reporte()
    return render_template('reportes.html', reportes=reportes)

@app.route('/editar')
def editar_reporte():
    reportes = controlador.obtener_reporte()
    return render_template('editar_reporte.html', reportes=reportes)

@app.route('/edit_reporte/<int:id>')
def edit_reporte(id):
    reportes = controlador.getting_report(id)
    return render_template('editing_report.html', reportes=reportes)



@app.route('/editando_reporte', methods=['POST'])
def editing_report_admin():
    if request.method == 'POST':
        if not request.files.get('solicitud') \
        and not request.files.get('acreditacion')\
        and not request.files.get('acta_constitutiva') \
        and not request.files.get('identificacion') \
        and not request.files.get('ubicacion') \
        and not request.files.get('plano') \
        and not request.files.get('carta_poder'):
            #UPDATE ONLY ID/FOLIO
            new_id = request.form['id']
            real_id = request.form['real_id']
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            data = (new_id, description, status, real_id)
            cursor.execute(query,data)
            conn.commit()
            return redirect(url_for('editar_reporte'))
        elif not request.files.get('acreditacion')\
        and not request.files.get('acta_constitutiva') \
        and not request.files.get('identificacion') \
        and not request.files.get('ubicacion') \
        and not request.files.get('plano') \
        and not request.files.get('carta_poder'):
            #UPDATE ONLY SOLICITUD
            new_id = request.form['id']
            real_id = request.form['real_id']
            file = request.files['solicitud']
            blob = base64.b64encode(file.read())
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, solicitud=%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            if blob:
                cursor.execute(query,(new_id,blob,description,status, real_id))
                conn.commit()
                return redirect(url_for('editar_reporte'))

        elif not request.files.get('solicitud')\
        and not request.files.get('acta_constitutiva') \
        and not request.files.get('identificacion') \
        and not request.files.get('ubicacion') \
        and not request.files.get('plano') \
        and not request.files.get('carta_poder'):
            #UPDATE ONLY ACREDITACION
            new_id = request.form['id']
            real_id = request.form['real_id']
            file = request.files['acreditacion']
            blob = base64.b64encode(file.read())
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, acreditacion=%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            if blob:
                cursor.execute(query,(new_id,blob,description,status, real_id))
                conn.commit()
                return redirect(url_for('editar_reporte'))

        elif not request.files.get('solicitud')\
        and not request.files.get('acreditacion') \
        and not request.files.get('identificacion') \
        and not request.files.get('ubicacion') \
        and not request.files.get('plano') \
        and not request.files.get('carta_poder'):
            #UPDATE ONLY ACTA CONSTITUTIVA
            new_id = request.form['id']
            real_id = request.form['real_id']
            file = request.files['acta_constitutiva']
            blob = base64.b64encode(file.read())
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, acta_constitutiva=%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            if blob:
                cursor.execute(query,(new_id,blob,description,status, real_id))
                conn.commit()
                return redirect(url_for('editar_reporte'))

        elif not request.files.get('solicitud')\
        and not request.files.get('acreditacion') \
        and not request.files.get('acta_constitutiva') \
        and not request.files.get('ubicacion') \
        and not request.files.get('plano') \
        and not request.files.get('carta_poder'):
            #UPDATE ONLY IDENTIFICACION
            new_id = request.form['id']
            real_id = request.form['real_id']
            file = request.files['identificacion']
            blob = base64.b64encode(file.read())
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, identificacion=%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            if blob:
                cursor.execute(query,(new_id,blob,description,status, real_id))
                conn.commit()
                return redirect(url_for('editar_reporte'))    

        elif not request.files.get('solicitud')\
        and not request.files.get('acreditacion') \
        and not request.files.get('acta_constitutiva') \
        and not request.files.get('identificacion') \
        and not request.files.get('plano') \
        and not request.files.get('carta_poder'):
            #UPDATE ONLY IDENTIFICACION
            new_id = request.form['id']
            real_id = request.form['real_id']
            file = request.files['ubicacion']
            blob = base64.b64encode(file.read())
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, ubicacion=%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            if blob:
                cursor.execute(query,(new_id,blob,description,status, real_id))
                conn.commit()
                return redirect(url_for('editar_reporte'))

        elif not request.files.get('solicitud')\
        and not request.files.get('acreditacion') \
        and not request.files.get('acta_constitutiva') \
        and not request.files.get('identificacion') \
        and not request.files.get('ubicacion') \
        and not request.files.get('carta_poder'):
            #UPDATE ONLY IDENTIFICACION
            new_id = request.form['id']
            real_id = request.form['real_id']
            file = request.files['plano']
            blob = base64.b64encode(file.read())
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, plano=%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            if blob:
                cursor.execute(query,(new_id,blob,description,status, real_id))
                conn.commit()
                return redirect(url_for('editar_reporte'))

        elif not request.files.get('solicitud')\
        and not request.files.get('acreditacion') \
        and not request.files.get('acta_constitutiva') \
        and not request.files.get('identificacion') \
        and not request.files.get('ubicacion') \
        and not request.files.get('plano'):
            #UPDATE ONLY IDENTIFICACION
            new_id = request.form['id']
            real_id = request.form['real_id']
            file = request.files['carta_poder']
            blob = base64.b64encode(file.read())
            description = request.form['descripcion']
            status = request.form['estatus']
            query="UPDATE expediente SET idsolicitud =%s, carta_poder=%s, descripcion = %s, estatus=%s WHERE idsolicitud = %s"
            if blob:
                cursor.execute(query,(new_id,blob,description,status, real_id))
                conn.commit()
                return redirect(url_for('editar_reporte'))



@app.route('/eliminar')
def eliminar():
    reportes = controlador.obtener_reporte()
    solicitudes = controlador.obtener_solicitud()
    acreditaciones = controlador.obtener_acreditacion()
    actas = controlador.obtener_acta()
    identificaciones = controlador.obtener_identificacion()
    ubicaciones = controlador.obtener_ubicacion()
    planos = controlador.obtener_plano()
    cartas = controlador.obtener_carta()
    descripcion = controlador.obtener_descripcion()
    estatus = controlador.obtener_estatus()
    return render_template('eliminarreporte.html', reportes=reportes, solicitudes=solicitudes, acreditaciones=acreditaciones, actas=actas, identificaciones= identificaciones, ubicaciones=ubicaciones, planos=planos, cartas=cartas, descripcion=descripcion, estatus=estatus)

@app.route("/eliminar_reporte", methods=["POST"])
def eliminar_reporte():
    controlador.eliminar_reporte(request.form["id"])
    return redirect("/eliminar")

@app.route("/eliminar_reporte", methods=["POST"])
def eliminar_solicitud():
    controlador.eliminar_solicitud(request.form["solicitud"])
    return redirect("/eliminar")

@app.route('/eliminar_acreditacion', methods=["POST"])
def eliminar_acreditacion():
    controlador.eliminar_acreditacion(request.form['acreditacion'])
    return redirect("/eliminar")

@app.route('/eliminar_acta', methods=["POST"])
def eliminar_acta():
    controlador.eliminar_acta(request.form['actaconstitutiva'])
    return redirect("/eliminar")

@app.route('/eliminar_identificacion', methods=["POST"])
def eliminar_identificacion():
    controlador.eliminar_identificacion(request.form['identificacion'])
    return redirect("/eliminar")

@app.route('/eliminar_ubicacion', methods=["POST"])
def eliminar_ubicacion():
    controlador.eliminar_ubicacion(request.form['ubicacion'])
    return redirect("/eliminar")

@app.route('/eliminar_plano', methods=["POST"])
def eliminar_plano():
    controlador.eliminar_plano(request.form['plano'])
    return redirect("/eliminar")

@app.route('/eliminar_carta', methods=["POST"])
def eliminar_carta():
    controlador.eliminar_carta_poder(request.form['cartadepoder'])
    return redirect("/eliminar")

@app.route('/eliminar_carta', methods=["POST"])
def eliminar_descripcion():
    controlador.eliminar_carta_poder(request.form['descripcion'])
    return redirect("/eliminar")

@app.route('/eliminar_carta', methods=["POST"])
def eliminar_estatus():
    controlador.eliminar_carta_poder(request.form['estatus'])
    return redirect("/eliminar")


@app.route("/cerrar-sesion-capturista")
def logout_capturist():
    session.pop('username_capturist',None)
    session.permanent = False
    return redirect('/inicio')

@app.route("/cerrar-sesion-admin")
def logout_admin():
    session.pop('username_admin',None)
    session.permanent = False
    return redirect('/inicio')

@app.route("/cerrar-sesion-visitante")
def logout_guest():
    session.pop('username_guest',None)
    session.permanent = False
    return redirect('/inicio')
    

#Handling Errors

#@app.errorhandler(400)
#def handle_bad_request(e):
#    return render_template('error-400.html'), 400

@app.errorhandler(403)
def handle_bad_request(e):
    return render_template('error-403.html'), 403

@app.errorhandler(404)
def not_found(self):
    return render_template('error-404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error-500.html'), 500

@app.errorhandler(405)
def method_not_found(error):
    return render_template('error-405.html'), 405



@app.route('/descargar_pdf')
@capturist_required
def download():
    return

if __name__ == "__main__":
    app.run(debug=True) 
