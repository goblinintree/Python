-- init database
drop database if exists myproject;

create database myproject;

use myproject;

grant select, insert, update, delete on myproject.* to 'root'@'localhost' identified by 'root';
