from flask import Flask

#para cambiar puerto y sea compatible con otros 
#from flask_cors import CORS

from config import config

#Importar rutas
from rutas import User

app=Flask(__name__)

#para cambiar puerto y sea compatible con otros 
#CORS(app, resources={"*": {"origin": "http://localhost:3000"}})

def page_not_found(error):
    return "<h1> Pagina no encontrada</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])


# Blueprints
app.register_blueprint(User.main, url_prefix='/')

#captura de error de pagina
app.register_error_handler(404, page_not_found)
app.run()
    
    
     