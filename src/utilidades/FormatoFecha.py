import datetime

class FormatoFecha():
    
    @classmethod
    def convertir_fecha(self, fecha):
        return datetime.datetime.strftime(fecha, '%d/%m/%Y')
