-------------------------------------------------------
-- Tabla ESTADO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inmobiliaria`.`estado` values (1,'DISPONIBLE');
insert into `db_inmobiliaria`.`estado` values (2,'NO DISPONIBLE');

-------------------------------------------------------
-- Tabla OPERATORIA COMERCIAL - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inmobiliaria`.`operatoriacomercial` values (1,'VENTA');
insert into `db_inmobiliaria`.`operatoriacomercial` values (2,'ALQUILER');

-------------------------------------------------------
-- Tabla PROPIETARIO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inmobiliaria`.`propietario` values (1,'Emilio Vera','Cordoba','3513370557');
insert into `db_inmobiliaria`.`propietario` values (2,'Pedro ROJO ','Carlos paz','33134567');
insert into `db_inmobiliaria`.`propietario` values (3,'Juan narvaez','Santa Cruz','33134568');
insert into `db_inmobiliaria`.`propietario` values (4,'Mavi Schaffre','Tierra del fuego','33134569');

-------------------------------------------------------
-- Tabla TIPO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inmobiliaria`.`tipo` values (1,'LOCAL COMERCIAL');
insert into `db_inmobiliaria`.`tipo` values (2,'DEPARTAMENTO ');
insert into `db_inmobiliaria`.`tipo` values (3,'CASA ');
insert into `db_inmobiliaria`.`tipo` values (4,'CABAÑA');
insert into `db_inmobiliaria`.`tipo` values (5,'MONOAMBIENTE');

-------------------------------------------------------
-- Tabla PROPIEDAD - INSERTANDO DATOS 
-------------------------------------------------------

insert into `db_inmobiliaria`.`propiedad`  values ('1', '5', '1', '2', '1', 'marcelo t de alvear 8855', 'CORDOBA', 'CORDOBA');
insert into `db_inmobiliaria`.`propiedad`  values ('2', '4', '2', '2', '2', 'San Martin 203', 'CORDOBA', 'Cordoba');
insert into `db_inmobiliaria`.`propiedad`  values ('3', '5', '2', '1', '1', 'Mariano moreno 1067', 'CORDOBA', 'CORDOBA');
insert into `db_inmobiliaria`.`propiedad`  values ('4', '4', '1', '1', '2', 'Av 9 de Julio 1757', 'Capital', 'Buenos Aires');
insert into `db_inmobiliaria`.`propiedad`  values ('5', '5', '2', '1', '3', 'RAv. Velez Sarsifield 4555', 'Formosa', 'Formosa');
