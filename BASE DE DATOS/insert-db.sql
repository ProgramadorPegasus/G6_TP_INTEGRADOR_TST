-------------------------------------------------------
-- Tabla ESTADO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `bd_inmobiliaria`.`estado` values (1,'DISPONIBLE');
insert into `bd_inmobiliaria`.`estado` values (2,'NO DISPONIBLE');

-------------------------------------------------------
-- Tabla OPERATORIA COMERCIAL - INSERTANDO DATOS 
-------------------------------------------------------
insert into `bd_inmobiliaria`.`operatoriacomercial` values (1,'VENTA');
insert into `bd_inmobiliaria`.`operatoriacomercial` values (2,'ALQUILER');

-------------------------------------------------------
-- Tabla PROPIETARIO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `bd_inmobiliaria`.`propietario` values (1,'Emilio Vera','Cordoba','3513370557');
insert into `bd_inmobiliaria`.`propietario` values (2,'Pedro ROJO ','Carlos paz','33134567');
insert into `bd_inmobiliaria`.`propietario` values (3,'Juan narvaez','Santa Cruz','33134568');
insert into `bd_inmobiliaria`.`propietario` values (4,'Mavi Schaffre','Tierra del fuego','33134569');

-------------------------------------------------------
-- Tabla TIPO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `bd_inmobiliaria`.`tipo` values (1,'LOCAL COMERCIAL');
insert into `bd_inmobiliaria`.`tipo` values (2,'DEPARTAMENTO ');
insert into `bd_inmobiliaria`.`tipo` values (3,'CASA ');
insert into `bd_inmobiliariab`.`tipo` values (4,'CABAÑA');
insert into `ibd_inmobiliaria`.`tipo` values (5,'MONOAMBIENTE');
insert into `bd_inmobiliaria`.`tipo` values (6,'DOS AMBIENTES ');
insert into `bd_inmobiliariab`.`tipo` values (7,'QUINCHO ');
insert into `bd_inmobiliaria`.`tipo` values (8,'CAMPO ');
insert into `bd_inmobiliaria`.`tipo` values (9,' ESCUELA');
insert into `bd_inmobiliaria`.`tipo` values (10,'JARDIN');

-------------------------------------------------------
-- Tabla PROPIEDAD - INSERTANDO DATOS 
-------------------------------------------------------

insert into `bd_inmobiliaria`.`propiedad`  values ('1', '5', '1', '2', '1', 'marcelo t de alvear 8855', 'CORDOBA', 'CORDOBA');
insert into `bd_inmobiliaria`.`propiedad`  values ('2', '4', '2', '2', '2', 'San Martin 203', 'CORDOBA', 'Cordoba');
insert into `bd_inmobiliaria`.`propiedad`  values ('3', '5', '2', '1', '1', 'Mariano moreno 1067', 'CORDOBA', 'CORDOBA');
insert into `bd_inmobiliaria`.`propiedad`  values ('4', '4', '1', '1', '2', 'Av 9 de Julio 1757', 'Capital', 'Buenos Aires');
insert into `bd_inmobiliaria`.`propiedad`  values ('5', '5', '2', '1', '3', 'RAv. Velez Sarsifield 4555', 'Formosa', 'Formosa');
insert into `bd_inmobiliaria`.`propiedad`  values ('6', '5', '1', '2', '3', 'Tucuman 990', 'Santa Fe', 'Santa Fe');
insert into `bd_inmobiliaria`.`propiedad`  values ('7', '5', '2', '2', '1', 'Tanti 123', 'CORDOBA', 'CORDOBA');
insert into `bd_inmobiliaria`.`propiedad`  values ('8', '2', '2', '1', '1', 'Tafi  333 ', 'Salta', 'Salta')
