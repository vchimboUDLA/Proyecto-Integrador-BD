-- Seleccionar la base de datos casinodb
USE casinodb;

-- Desactivar las verificaciones de claves foráneas
SET FOREIGN_KEY_CHECKS = 0;

-- Eliminar datos de las tablas en el orden adecuado
DELETE FROM Transaccion;
DELETE FROM Apuesta;
DELETE FROM Cuota;
DELETE FROM Evento_Participante;
DELETE FROM Evento;
DELETE FROM Participante;
DELETE FROM Usuario;
DELETE FROM Mercados_Apuesta;
DELETE FROM Deporte;

-- Activar nuevamente las verificaciones de claves foráneas
SET FOREIGN_KEY_CHECKS = 1;
