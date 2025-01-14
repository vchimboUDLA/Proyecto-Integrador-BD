-- EJECUTAR ESTOS COMANDOS 1 a 1

-- GENERAR EL ROL DE LECTURA
CREATE ROLE 'rol_lectura' ; 
GRANT SELECT ON casinodb.* TO 'rol_lectura';

-- GENERAR EL ROL DE ADMINISTRADOR
CREATE ROLE 'rol_admin' ; 
GRANT SELECT, INSERT, UPDATE, DELETE ON casinodb.* TO 'rol_admin';

-- CREAR UN USUARIO Y DARLE EL ROL DE LECTURA
CREATE USER 'usuario_lectura_Jose'@'%' IDENTIFIED BY 'lectura';
GRANT 'rol_lectura' TO 'usuario_lectura_Jose'@'%';

-- CREAR UN USUARIO Y DARLE EL ROL DE ADMINISTRADOR
CREATE USER 'usuario_admin_Veronica'@'%' IDENTIFIED BY 'admin';
GRANT 'rol_admin' TO 'usuario_admin_Veronica'@'%';