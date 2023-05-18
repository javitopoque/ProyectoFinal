# ProyectoFinal
Api Crud realizado en Python Flask, como proyecto final del modulo 3 de Full Stack

PASOS A SEGUIR
- Crear Base de Datos "proyecto_final"
- Ejecutar Script para crear la tabla y tuplas
    
    --Crear tabla usuario

    CREATE TABLE usuario (
      id serial4 NOT NULL,
      cedula_identidad varchar(15) NOT NULL,  --tipo texto ya que el carnet puede tener complemento
      nombre varchar(30) NOT NULL,
      primer_apellido varchar(30) NOT NULL,
      segundo_apellido varchar(30) NOT NULL,
      fecha_nacimiento date NOT null DEFAULT CURRENT_DATE,
      CONSTRAINT usuario_pk PRIMARY KEY (id)
    );
    CREATE UNIQUE INDEX pk_usuario ON usuario USING btree (id);


      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('5493424', 'javier', 'poque', 'foronda', '1985/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('123456', 'jorge', 'perez', 'alfer', '1999/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('65487989', 'juan', 'tevez', 'olguin', '1985/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('324589', 'elver', 'lopez', 'albarado', '1977/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('741285', 'cesar', 'aguilar', 'reynods', '2003/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('965874', 'elvis', 'urzagaste', 'borquez', '1966/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('528743', 'laura', 'andrade', 'toro', '1988/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('6654228', 'pepe', 'arduz', 'filon', '1948/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('9512357', 'gabril', 'vilar', 'busch', '1955/10/01');

      --Insertar usuarios por defecto
      INSERT INTO usuario
      ( cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
      VALUES('8547632', 'lorena', 'torrez', 'almendras', '1999/10/01');

- 
