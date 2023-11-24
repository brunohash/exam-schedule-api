-- Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS global_solutions
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE global_solutions;

-- Tabela de Tipos de Usuários
CREATE TABLE IF NOT EXISTS type_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL
);

-- Inserção de Tipos de Usuários
INSERT INTO type_users (name, description) VALUES ('Administrador', 'Administrador do Sistema');
INSERT INTO type_users (name, description) VALUES ('Enfermeiro', 'Enfermeiro');
INSERT INTO type_users (name, description) VALUES ('Paciente', 'Paciente');

-- Tabela de Usuários
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    age INT,
    birthdate DATE,
    street VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip VARCHAR(10),
    phone VARCHAR(15),
    password VARCHAR(255) NOT NULL,
    type_id INT NOT NULL,
    FOREIGN KEY (type_id) REFERENCES type_users(id)
);
