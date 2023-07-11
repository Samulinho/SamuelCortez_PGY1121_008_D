import Funciones as fn

while True:
    fn.ver_menu()

    opcion= fn.validar_opcion()
    
    
    if opcion == 1:
        fn.comprar_entradas()
    elif opcion == 2:
         pass
    elif opcion == 3:
        fn.asistentes()
    elif opcion == 4:
        fn.ganancias
    else:
        fn.salir()








