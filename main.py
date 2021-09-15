import usuarios.usuarioModel as modelo
import usuarios.usuarioFunciones as usuarioFunciones
import notas.notasFunciones as notasFunciones
        
def iniciar():
    
    print('----------Bienvenido -----------')
    print('Que deseas hacer?  \n   Crear usuario (registrar) \n   Iniciar sesion (ingresar)')
    opcion=input('Deseo:   ')
    
    if opcion!='registrar' and opcion!='ingresar':
        print('Opcion invalida')
    else:
        if opcion == 'registrar':
            registrarU = usuarioFunciones.RegistrarUsuario()
            print(registrarU)
        else:
            login = usuarioFunciones.Login()
            if login[0] != True:
                
                print(login)
            else:
                idUser = login[2]
                print(f'\n-------Bienvenido Menu de  asistente de notas  ------')
                accion=''
                while accion !='salir':
                    # print('\n   Menu  ')
                    print('   Crear nota (crear) \n   Mostrar Notas (mostrar) \n   Eliminar nota (eliminar) \n   Salir (salir)')
                    accion = input('¿Qué deseas realizar?:   ')
                    
                    if accion == 'crear':
                        registrarN= notasFunciones.Registrar(idUser)
                        print(registrarN)
                    elif accion == 'mostrar':
                        notas = notasFunciones.mostrarTodas()
                        for nota in notas:
                            print(f'{nota[2]} => {nota[3]}  \n')
                    elif accion == 'eliminar':
                        notas = notasFunciones.mostrarTodas()
                        for nota in notas:
                            print(f'{nota[2]}')
                        notaEliminada = input("¿Cual nota va a eliminar?   ")
                        eliminar = notasFunciones.EliminarNota(notaEliminada)
                        print(eliminar)
                    elif accion == 'salir':
                        print('Adios ')
                    else:
                        print('Accion invalida')

    

iniciar()

