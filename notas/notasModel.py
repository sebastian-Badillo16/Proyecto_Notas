import database.config as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self,usuario_id,titulo,descripcion):
        self.usuario_id = usuario_id
        self.titulo =titulo
        self.descripcion=descripcion 

    def buscar(titulo):
        sql = f'SELECT * FROM notas WHERE titulo="{titulo}"'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def guardar(self):
        sql='INSERT INTO notas VALUE (null,%s,%s,%s,now())'
        nota = (self.usuario_id,self.titulo,self.descripcion)
        cursor.execute(sql,nota)
        database.commit()
        return f'La nota {self.titulo} se a guardado con exito'

    def buscarTodo():
        sql = 'SELECT * FROM notas'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def Eliminar(titulo):
        sql = f'DELETE FROM notas WHERE titulo="{titulo}"'
        cursor.execute(sql)
        database.commit()
        return f'la nota {titulo} se elimino con exito'
