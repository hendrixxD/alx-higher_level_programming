-- create database
CREATE DATABASE hbtn_0d_usa
-- use db created above
USE hbtn_0d_usa
-- create table states
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
