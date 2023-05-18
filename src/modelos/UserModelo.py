from basededatos.db import get_connection
from modelos.entidades.User import  User

class UserModelo():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM usuario ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    users.append(user.to_JSON())
                
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM usuario WHERE id = %s", (id,))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    user=user.to_JSON()
                
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()
          
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
                                VALUES(%s, %s, %s, %s, %s)""", (user.cedula_identidad, user.nombre, user.primer_apellido, user.segundo_apellido, user.fecha_nacimiento))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()
          
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuario SET cedula_identidad = %s, nombre = %s, primer_apellido = %s, segundo_apellido = %s, fecha_nacimiento = %s
                                WHERE id = %s""", (user.cedula_identidad, user.nombre, user.primer_apellido, user.segundo_apellido, user.fecha_nacimiento, user.id))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()
          
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuario WHERE id = %s", (user.id,))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_promedio(self):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT AVG(EXTRACT(YEAR FROM AGE(NOW(), fecha_nacimiento))) AS promedio_edades FROM usuario u ;")
                
                resultset = cursor.fetchall()
                prom = resultset[0]
            connection.close()
            return prom
        except Exception as ex:
            raise Exception(ex)
