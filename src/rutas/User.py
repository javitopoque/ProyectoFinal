from flask import Blueprint, jsonify, request

#generar codigo unico
#import uuid

#Modelo
from modelos.UserModelo import UserModelo

#Entidades
from modelos.entidades.User import User

main = Blueprint('user_blueprint', __name__)


@main.route('/usuarios/' , methods=['GET'])
def get_users():
    try:
        users = UserModelo.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/usuarios/<id>' , methods=['GET'])
def get_user(id):
    try:
        user = UserModelo.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/usuarios', methods=['POST'])
def add_user():
    try:
        cedula_identidad = request.json['cedula_identidad']
        nombre = request.json['nombre']
        primer_apellido = request.json['primer_apellido']
        segundo_apellido = request.json['segundo_apellido']
        fecha_nacimiento = request.json["fecha_nacimiento"]
        user = User(None, cedula_identidad,nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
        affected_rows = UserModelo.add_user(user)
        if affected_rows == 1:
            return jsonify(user.cedula_identidad)
        else:
            return jsonify({'message', "Error al insertar"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/usuarios/<id>', methods=['PUT'])
def update_user(id):
    try:
        cedula_identidad = request.json['cedula_identidad']
        nombre = request.json['nombre']
        primer_apellido = request.json['primer_apellido']
        segundo_apellido = request.json['segundo_apellido']
        fecha_nacimiento = request.json["fecha_nacimiento"]
        user = User(id, cedula_identidad,nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
        print(id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
        affected_rows = UserModelo.update_user(user)
        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message', "no se actualizo usuario"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/usuarios/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User(id)

        affected_rows = UserModelo.delete_user(user)
        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message', "Usuario no borrado, no existe en base de datos"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/usuarios/promedio-edad')
def get_promedio():
    try:
        promedio = UserModelo.get_promedio()
        return jsonify({'promedioEdad: ': str(promedio[0])})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/estado')
def get_estado():
    try:
        nameSystem = 'api-users' 
        version = '0.0.1'
        developer = 'Javier Omar Poquechoque Foronda'
        email = 'xavipoquefor@gmail.com'
        return jsonify({'nameSystem ': nameSystem, 'version': version, 'developer': developer, 'email': email})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 404
