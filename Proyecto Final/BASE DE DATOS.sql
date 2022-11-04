drop database cambioclimatico;
CREATE DATABASE CambioClimatico;

USE CambioClimatico;

CREATE TABLE REGISTRO(
Id INT auto_increment,
Nombre VARCHAR(50),
Correo VARCHAR(50),
Contraseña VARCHAR(50)
);

SELECT * FROM REGISTRO;

CREATE TABLE IMAGENES(
Id_imagen INT,
Nombre VARCHAR(50),
Direccion VARCHAR(50),
Tamaño VARCHAR(50)
);

CREATE TABLE DATOS(
Id_fotos INT,
Nombre VARCHAR(50),
Informacion VARCHAR(50),
Titulo VARCHAR(50)
);


SELECT * FROM IMAGENES;
SELECT * FROM DATOS;
