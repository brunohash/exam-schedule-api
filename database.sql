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

-- Tabela de Tipos Exames
CREATE TABLE IF NOT EXISTS type_exams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL
);

-- Inserção de Tipos de Exames
INSERT INTO type_exams (name, description) VALUES ('Urina', 'Urina');
INSERT INTO type_exams (name, description) VALUES ('Hemograma', 'Hemograma');
INSERT INTO type_exams (name, description) VALUES ('Fezes', 'Fezes');
INSERT INTO type_exams (name, description) VALUES ('Glicemia', 'Glicemia');
INSERT INTO type_exams (name, description) VALUES ('Colesterol', 'Colesterol');

-- Agendas
CREATE TABLE IF NOT EXISTS schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    time TIME NOT NULL,
    status VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    type_exams INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (type_exams) REFERENCES type_exams(id)
);

-- Tabela de Exames
CREATE TABLE IF NOT EXISTS exams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    type_exams INT NOT NULL,
    exam VARCHAR(255) NOT NULL,
    result VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    schedule_id INT NOT NULL,
    FOREIGN KEY (schedule_id) REFERENCES schedules(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (type_exams) REFERENCES type_exams(id) 
);