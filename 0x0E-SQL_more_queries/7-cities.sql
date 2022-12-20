-- create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the created db above
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, PRIMARY KEY(id), name VARCHAR(256));
