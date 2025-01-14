# Implementación de una Base de Datos Contenerizada para una Casa/Sitio de Apuestas

# Descripción del Proyecto
Este proyecto consiste en el diseño, desarrollo e implementación de una solución de base de datos contenerizada utilizando Docker para una casa/sitio de apuestas. Se centra en garantizar la escalabilidad, portabilidad y seguridad, integrando un modelo de administración basada en roles (RBA) para mitigar riesgos asociados con la gestión de privilegios.

# Tabla de Contenidos
1. Introducción
2. Alcance
3. Justificación
4. Estructura del Proyecto
5. Tecnologías Utilizadas
6. Requisitos
7. Instrucciones de Instalación
8. Autores

# Introducción
En la actualidad, la contenerización se ha convertido en una práctica estándar para el desarrollo de sistemas escalables y eficientes. Este proyecto aborda las necesidades de las casas de apuestas, donde se manejan datos sensibles como transacciones financieras, utilizando Docker para contenerización y un enfoque RBA para seguridad granular.

# Alcance
Despliegue inicial: Configuración y validación funcional de la base de datos contenerizada.
Análisis de riesgos: Identificación de riesgos de seguridad relacionados con privilegios.
Solución basada en RBA: Diseño, implementación y validación de roles de acceso.
Documentación: Registro de procesos técnicos y resultados obtenidos.

# Justificación
La industria de las apuestas depende de sistemas robustos que protejan información sensible y garanticen disponibilidad. Este proyecto busca abordar estas necesidades mediante una solución segura y replicable, enfocada en minimizar riesgos y mejorar la eficiencia operativa.

# Estructura del Proyecto
El proyecto se divide en las siguientes fases:

Planificación: Definición de cronograma, roles y responsabilidades.
Configuración de Seguridad RBA: Creación y asignación de roles para controlar privilegios.
Configuración del Entorno Contenerizado: Despliegue y configuración de un servidor Ubuntu y Docker.
Despliegue Inicial de la Base de Datos: Implementación de almacenamiento persistente y conexiones seguras.
Ajustes y Validación: Pruebas de seguridad y funcionalidad.

# Tecnologías Utilizadas
Docker: Para la contenerización.
Ubuntu Server 24.04: Como sistema operativo base.
MySQL: Motor de base de datos.
MySQL Workbench: Herramienta gráfica de gestión.

# Requisitos
Sistema operativo con soporte para Docker (Linux recomendado).
Instalación de Docker y Docker Compose.
Herramienta de gestión gráfica como MySQL Workbench.
Conocimientos básicos de bases de datos y administración de servidores.

# Instrucciones de Instalación
1. Clona este repositorio:
git clone https://github.com/vchimboUDLA/Proyecto-Integrador-BD.git
cd Proyecto-Integrador-BD

2. Configura el servidor Ubuntu:
Actualiza los paquetes: sudo apt update && sudo apt upgrade -y
Instala Docker: sudo apt install docker.io -y
Configura el contenedor MySQL: docker run --name casinodb-container -e MYSQL_ROOT_PASSWORD=casino -d -p 3307:3306 -v /path/to/data:/var/lib/mysql mysql:latest

3. Configura roles de acceso con RBA en MySQL.
4. Realiza pruebas de conexión utilizando MySQL Workbench.

# Autores
- José Sánchez
- Jorge Lagla
- Verónica Chimbo

# Año
2025
