# ProyectoFinal
Api Crud realizado en Python Flask, como proyecto final del modulo 3 de Full Stack

    "developer": "Javier Omar Poquechoque Foronda",
    
    "email": "xavipoquefor@gmail.com",
    
    "nameSystem ": "api-users",
    
    "version": "0.0.1"
    
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

- Clonar el repositorio con "git clon https://github.com/javitopoque/ProyectoFinal.git"
- Para correr los APIs ejecutar desde la carpeta contenedora: "source venv/bin/activate" y luego ""python app.py
- Para acceder a los End Points se puede utilizar Postman:
    • Para crear un usuario POST ‘/usuarios’
        http://localhost:5000/usuarios
        Captura de pantalla
        ![1](https://github.com/javitopoque/ProyectoFinal/assets/113144412/66c1cb0e-d20a-467d-852b-ade62ad02578)

    • Para listar a todos lo usuarios: GET ‘/usuarios’ 
        http://localhost:5000/usuarios
        Captura de pantalla
        ![2](https://github.com/javitopoque/ProyectoFinal/assets/113144412/c9c8ba6c-853f-428a-b07e-747bde5e9cbd)
        
    • Para listar unsuario en especifico GET ‘/usuarios/:id_usuario’
        http://localhost:5000/usuarios/55
        Captura de pantalla
        ![4](https://github.com/javitopoque/ProyectoFinal/assets/113144412/05e86dcb-1be9-42f0-a4b3-672be893e1c5)

    • Para actualizar los datos de un usuario: PUT ‘/usuarios/:id_usuario’
        http://localhost:5000/usuarios/49
        Captura de pantalla
        ![5](https://github.com/javitopoque/ProyectoFinal/assets/113144412/92759313-756a-447f-8e06-8c18bc53fb64)

    • Para eliminar a un usuario: DELETE ‘usuarios/:id_usuario’
        http://localhost:5000/usuarios/53
        Captura de pantalla
        ![6](https://github.com/javitopoque/ProyectoFinal/assets/113144412/2773bbc4-9013-4b60-9fe1-a593fab39843)

    • Para mostrar el promedio de edades de los usuarios: GET ‘/usuarios/promedio-edad’
        http://localhost:5000/usuarios/promedio-edad
        Captura de pantalla
        ![8](https://github.com/javitopoque/ProyectoFinal/assets/113144412/ce4ebc16-5a68-4127-a1ce-6b82db667633)

    • Para mostrar la version del api rest: GET ‘/estado’
        http://localhost:5000/estado
        Captura de pantalla
        ![9](https://github.com/javitopoque/ProyectoFinal/assets/113144412/7cfb2ec8-2c68-4f2b-aaa1-5bd005fdc6fc)
