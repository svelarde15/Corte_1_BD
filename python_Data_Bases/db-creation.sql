CREATE DATABASE IF NOT EXISTS customer;

USE customer;

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS compras (
    id_compra INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    fecha DATE NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    
);

CREATE TABLE IF NOT EXISTS detalles_cliente_compra (
    id_cliente INT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    id_compra INT,
    fecha DATE NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    
);
