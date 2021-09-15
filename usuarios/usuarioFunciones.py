import usuarios.usuarioModel as usuarioModelo

def buscar(email):
    buscando = usuarioModelo.Usuario.buscar(email)
    return buscando


def RegistrarUsuario():
    print('\n-----Formulario de Registro --------')
    nombre = input('Escribe tu nombre:   ')
    apellidos = input('Escribe tus apellidos:   ')
    email = input('Escribe tu email:   ')
    password = input('Escribe tu contraseña:   ')

    buscando = buscar(email)
    
    if len(buscando)!=0:
        return '¡Up! ya exste un usuario con este email'
    else:
        try:
            usuario = usuarioModelo.Usuario(nombre,apellidos,email,password)
            guardar = usuario.guardar()
            return guardar
        except:
            return 'Error al registrar usuario en la bd'

def Login():
    print('\n-   Formulario de Login')
    email = input('Escribe tu Email:   ')
    password = input('Escribe tu Contraseña:   ')
    
    buscando = buscar(email)

    if len(buscando)==0:
        return ' Este usuario no existe '
    else:
        passwordBD = buscando[0][4]
        if passwordBD!=password:
            return ['La Contraseña es incorrecta','']
        else:
            return [True,buscando[0][1],buscando[0][0]]
