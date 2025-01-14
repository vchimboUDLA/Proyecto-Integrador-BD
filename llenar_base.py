from faker import Faker
import random
import mysql.connector

# Inicializar Faker
fake = Faker()

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # Reemplaza con tu contraseña
    database="casinodb"
)
cursor = conn.cursor()

# Cantidades de datos a generar
n_deportes = 5
n_usuarios = 20
n_participantes = 30
n_eventos = 10
n_mercados_apuesta = 5
n_cuotas_por_evento = 3
n_apuestas = 50
n_transacciones = 40

# Funciones para insertar datos en las tablas
def insert_deportes():
    for i in range(n_deportes):
        nombre_deporte = fake.word()
        cursor.execute("SELECT COUNT(*) FROM Deporte WHERE nombre_deporte = %s", (nombre_deporte,))
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO Deporte (nombre_deporte) VALUES (%s)", (nombre_deporte,))

def insert_usuarios():
    for i in range(n_usuarios):
        nombre = fake.first_name()
        apellido = fake.last_name()
        correo_elec = fake.email()
        contrasenia = fake.password()
        fecha_registro = fake.date_this_decade()
        saldo = round(random.uniform(50, 500), 2)
        cursor.execute("SELECT COUNT(*) FROM Usuario WHERE correo_elec = %s", (correo_elec,))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO Usuario (nombre, apellido, correo_elec, contrasenia, fecha_registro, saldo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nombre, apellido, correo_elec, contrasenia, fecha_registro, saldo))

def insert_participantes():
    for i in range(n_participantes):
        nombre_participante = fake.company()
        tipo = random.choice(["individual", "equipo"])  # Valores válidos
        cursor.execute("SELECT COUNT(*) FROM Participante WHERE nombre_participante = %s AND tipo = %s", (nombre_participante, tipo))
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO Participante (nombre_participante, tipo) VALUES (%s, %s)", (nombre_participante, tipo))


def insert_eventos():
    cursor.execute("SELECT deporte_id FROM Deporte")
    deportes = [row[0] for row in cursor.fetchall()]
    for i in range(n_eventos):
        deporte_id = random.choice(deportes)
        fecha_hora = fake.date_time_this_year()
        estado = random.choice(["programado", "en_progreso", "finalizado"])  # Valores válidos
        cursor.execute("""
            SELECT COUNT(*) FROM Evento WHERE deporte_id = %s AND fecha_hora = %s
        """, (deporte_id, fecha_hora))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO Evento (deporte_id, fecha_hora, estado)
                VALUES (%s, %s, %s)
            """, (deporte_id, fecha_hora, estado))


def insert_evento_participantes():
    cursor.execute("SELECT evento_id FROM Evento")
    eventos = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT participante_id FROM Participante")
    participantes = [row[0] for row in cursor.fetchall()]
    for i in range(n_eventos * 2):
        evento_id = random.choice(eventos)
        participante_id = random.choice(participantes)
        cursor.execute("""
            SELECT COUNT(*) FROM Evento_Participante WHERE evento_id = %s AND participante_id = %s
        """, (evento_id, participante_id))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO Evento_Participante (evento_id, participante_id)
                VALUES (%s, %s)
            """, (evento_id, participante_id))

def insert_mercados_apuesta():
    for i in range(n_mercados_apuesta):
        descripcion = f"Mercado {i + 1}"
        cursor.execute("SELECT COUNT(*) FROM Mercados_Apuesta WHERE descripcion = %s", (descripcion,))
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO Mercados_Apuesta (descripcion) VALUES (%s)", (descripcion,))

def insert_cuotas():
    cursor.execute("SELECT evento_id FROM Evento")
    eventos = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT mercado_id FROM Mercados_Apuesta")
    mercados = [row[0] for row in cursor.fetchall()]
    for i in range(n_eventos * n_cuotas_por_evento):
        evento_id = random.choice(eventos)
        mercado_id = random.choice(mercados)
        valor_cuota = round(random.uniform(1.5, 5.0), 2)
        descripcion = f"Resultado {fake.word()}"
        cursor.execute("""
            SELECT COUNT(*) FROM Cuota WHERE evento_id = %s AND mercado_id = %s AND descripcion = %s
        """, (evento_id, mercado_id, descripcion))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO Cuota (evento_id, mercado_id, valor_cuota, descripcion)
                VALUES (%s, %s, %s, %s)
            """, (evento_id, mercado_id, valor_cuota, descripcion))

def insert_apuestas():
    cursor.execute("SELECT usuario_id FROM Usuario")
    usuarios = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT evento_id FROM Evento")
    eventos = [row[0] for row in cursor.fetchall()]
    for i in range(n_apuestas):
        usuario_id = random.choice(usuarios)
        evento_id = random.choice(eventos)
        tipo_apuesta = f"Apuesta {i + 1}"
        cuota = round(random.uniform(1.5, 5.0), 2)
        monto_apostado = round(random.uniform(10, 100), 2)
        fecha_hora_apuesta = fake.date_time_this_year()
        estado_apuesta = random.choice(["pendiente", "ganada", "perdida"])  # Valores válidos
        cursor.execute("""
            SELECT COUNT(*) FROM Apuesta WHERE usuario_id = %s AND evento_id = %s AND tipo_apuesta = %s
        """, (usuario_id, evento_id, tipo_apuesta))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO Apuesta (usuario_id, evento_id, tipo_apuesta, cuota, monto_apostado, fecha_hora_apuesta, estado_apuesta)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (usuario_id, evento_id, tipo_apuesta, cuota, monto_apostado, fecha_hora_apuesta, estado_apuesta))


def insert_transacciones():
    cursor.execute("SELECT usuario_id FROM Usuario")
    usuarios = [row[0] for row in cursor.fetchall()]
    for i in range(n_transacciones):
        usuario_id = random.choice(usuarios)
        tipo_transaccion = random.choice(["deposito", "retiro"])  # Valores válidos
        monto = round(random.uniform(10, 200), 2)
        fecha_hora = fake.date_time_this_year()
        cursor.execute("""
            SELECT COUNT(*) FROM Transaccion WHERE usuario_id = %s AND tipo_transaccion = %s AND fecha_hora = %s
        """, (usuario_id, tipo_transaccion, fecha_hora))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO Transaccion (usuario_id, tipo_transaccion, monto, fecha_hora)
                VALUES (%s, %s, %s, %s)
            """, (usuario_id, tipo_transaccion, monto, fecha_hora))


# Ejecutar las inserciones
def main():
    insert_deportes()
    insert_usuarios()
    insert_participantes()
    insert_eventos()
    insert_evento_participantes()
    insert_mercados_apuesta()
    insert_cuotas()
    insert_apuestas()
    insert_transacciones()
    conn.commit()
    print("Datos insertados correctamente en la base de datos.")

if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()
