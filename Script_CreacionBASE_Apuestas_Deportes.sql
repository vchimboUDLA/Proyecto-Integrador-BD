CREATE DATABASE IF NOT EXISTS casinodb;
USE casinodb;

-- Creación de la tabla Deporte
CREATE TABLE Deporte (
    deporte_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_deporte VARCHAR(100) NOT NULL
);

-- Creación de la tabla Usuario
CREATE TABLE Usuario (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo_elec VARCHAR(100) NOT NULL UNIQUE,
    contrasenia VARCHAR(255) NOT NULL,
    fecha_registro DATE NOT NULL,
    saldo DECIMAL(10, 2) NOT NULL DEFAULT 0.00 -- valor no nulo que si no especifica valor por defecto es 0. 
);

-- Creación de la tabla Participante
CREATE TABLE Participante (
    participante_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_participante VARCHAR(100) NOT NULL,
    tipo ENUM('individual', 'equipo') NOT NULL
);

-- Creación de la tabla Evento
CREATE TABLE Evento (
    evento_id INT AUTO_INCREMENT PRIMARY KEY,
    deporte_id INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    estado ENUM('programado', 'en_progreso', 'finalizado') NOT NULL,
    FOREIGN KEY (deporte_id) REFERENCES Deporte(deporte_id)
);


-- Creación de la tabla Evento_Participante
CREATE TABLE Evento_Participante ( -- tabla de union N a M
    evento_id INT NOT NULL,
    participante_id INT NOT NULL,
    PRIMARY KEY (evento_id, participante_id), -- primary key compuesta
    FOREIGN KEY (evento_id) REFERENCES Evento(evento_id),
    FOREIGN KEY (participante_id) REFERENCES Participante(participante_id)
);

-- Creación de la tabla Mercados_Apuesta, el tipo de apuesta a. Resultado de Partido, Cantidad de goles, etc...
CREATE TABLE Mercados_Apuesta (
    mercado_id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL
);

-- Creación de la tabla Cuota , almacena las ganancias de apuesta de los eventos deportivos. Equipo A: 1.80, Empate: 3.50, Equipo B: 1.50 
CREATE TABLE Cuota (
    cuota_id INT AUTO_INCREMENT PRIMARY KEY,
    evento_id INT NOT NULL,
    mercado_id INT NOT NULL,
    valor_cuota DECIMAL(5, 2) NOT NULL, -- 1.50
    descripcion VARCHAR(255) NOT NULL, -- Ejem: Gana equipo A
    FOREIGN KEY (evento_id) REFERENCES Evento(evento_id),
    FOREIGN KEY (mercado_id) REFERENCES Mercados_Apuesta(mercado_id)
);

-- Creación de la tabla Apuesta
CREATE TABLE Apuesta (
    apuesta_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    evento_id INT NOT NULL,
    tipo_apuesta VARCHAR(100) NOT NULL,
    cuota DECIMAL(5, 2) NOT NULL,
    monto_apostado DECIMAL(10, 2) NOT NULL,
    fecha_hora_apuesta DATETIME NOT NULL,
    estado_apuesta ENUM('pendiente', 'ganada', 'perdida') NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (evento_id) REFERENCES Evento(evento_id)
);

-- Creación de la tabla Transaccion, depositos y retiros afectan al saldo que tiene el usuario para jugar. 
CREATE TABLE Transaccion (
    transaccion_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    tipo_transaccion ENUM('deposito', 'retiro') NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id)
);
