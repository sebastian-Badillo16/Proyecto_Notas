import notas.notasModel as notaModelo

def buscar(titulo):
    buscando = notaModelo.Nota.buscar(titulo)
    return buscando

def Registrar(idUser):
    print('\n-------Datos de la nota---------')
    titulo = input('Titulo de la nota:  ')
    descripcion = input('Descripcion:  ')

    buscando = buscar(titulo)
    if len(buscando)!=0:
        return '¡Up! ya exste un nota con este titulo'
    else:
        try:
            nota = notaModelo.Nota(idUser,titulo,descripcion)
            guardar = nota.guardar()
            return guardar
        except:
           return 'Error al registrar nota en la bd' 


def mostrarTodas():
    print('\n------- Notas registradas---------')
    buscando = notaModelo.Nota.buscarTodo()
    return buscando

def EliminarNota(titulo):
    buscando = buscar(titulo)
    if len(buscando)==0:
        print("¡Mmm..! Esa nonta no existe" )
    else:
        try:
            eliminar = notaModelo.Nota.Eliminar(titulo)
            return eliminar
        except:
            return 'Error al eliminar la nota en la bd'
