from bd import obtener_conexion

def getting_report(id):
    connection = obtener_conexion()
    request = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `expediente` WHERE idsolicitud = %s;", (id,))
        request = cursor.fetchall()
    connection.close()
    return request


def eliminar_reporte(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE idsolicitud = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_reporte():
    conexion = obtener_conexion()
    reporte = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM `expediente`")
        reporte = cursor.fetchall()
    conexion.close()
    return reporte

def obtener_respaldo():
    conexion = obtener_conexion()
    respaldo = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM `respaldo`")
        respaldo = cursor.fetchall()
    conexion.close()
    return respaldo

def obtener_solicitud():
    conexion = obtener_conexion()
    solicitud = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT solicitud FROM `expediente`")
        solicitud = cursor.fetchall()
    conexion.close()
    return solicitud

def obtener_acreditacion():
    conexion = obtener_conexion()
    acreditacion = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT acreditacion FROM `expediente`")
        acreditacion = cursor.fetchall()
    conexion.close()
    return acreditacion

def obtener_acta():
    conexion = obtener_conexion()
    acta = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT acta_constitutiva FROM `expediente`")
        acta = cursor.fetchall()
    conexion.close()
    return acta

def obtener_identificacion():
    conexion = obtener_conexion()
    identificacion= []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT identificacion FROM `expediente`")
        identificacion = cursor.fetchall()
    conexion.close()
    return identificacion

def obtener_ubicacion():
    conexion = obtener_conexion()
    ubicacion = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT ubicacion FROM `expediente`")
        ubicacion = cursor.fetchall()
    conexion.close()
    return ubicacion

def obtener_plano():
    conexion = obtener_conexion()
    plano = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT plano FROM `expediente`")
        plano = cursor.fetchall()
    conexion.close()
    return plano

def obtener_carta():
    conexion = obtener_conexion()
    carta = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT carta_poder FROM `expediente`")
        carta = cursor.fetchall()
    conexion.close
    return carta

def obtener_descripcion():
    conexion = obtener_conexion()
    descripcion = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT descripcion FROM `expediente`")
        descripcion = cursor.fetchall()
    conexion.close
    return descripcion

def obtener_estatus():
    conexion = obtener_conexion()
    estatus = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT estatus FROM `expediente`")
        estatus = cursor.fetchall()
    conexion.close
    return estatus

def eliminar_solicitud(solicitud):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE solicitud = %s", (solicitud,))
    conexion.commit()
    conexion.close()

def eliminar_acreditacion(acreditacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE acreditacion = %s", (acreditacion,))
    conexion.commit()
    conexion.close()

def eliminar_acta(actaconstitutiva):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE acta_constitutiva = %s", (actaconstitutiva,))
    conexion.commit()
    conexion.close()

def eliminar_identificacion(identificacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE identificacion = %s", (identificacion,))
    conexion.commit()
    conexion.close()

def eliminar_ubicacion(ubicacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE ubicacion = %s", (ubicacion,))
    conexion.commit()
    conexion.close()

def eliminar_plano(plano):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE plano = %s", (plano,))
    conexion.commit()
    conexion.close()

def eliminar_carta_poder(cartadepoder):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE carta_poder = %s", (cartadepoder,))
    conexion.commit()
    conexion.close()

def eliminar_descripcion(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE descripcion = %s", (descripcion,))
    conexion.commit()
    conexion.close()

def eliminar_estatus(estatus):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE estatus = %s", (estatus,))
    conexion.commit()
    conexion.close()


def download_pdf_file(estatus):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM `expediente` WHERE estatus = %s", (estatus,))
    row = cursor.fetchall()
    for i in row:
        try:
            with open(i[0], 'wb') as outfile:
                outfile.write(i[1])
                outfile.close()
                print("Filename Saved as: " + i[0])
        except:
            pass
        return
