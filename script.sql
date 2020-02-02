create database autonomo2DB;
use autonomo2DB;

create table personas(
	idPersona INT PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(50),
    apellido varchar(50),
    edad int,
    fecha_nacimiento date
);

insert into personas(nombre,apellido,edad,fecha_nacimiento)
values("Milton","Garcia Cox","20",date("1998-11-16"));

insert into personas(nombre,apellido,edad,fecha_nacimiento)
values("Maria","Meza","19",date("1999-05-14"));

select *
from personas;