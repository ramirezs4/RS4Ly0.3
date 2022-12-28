from RS4LyConexiones02 import CambioDeKeys
from RS4LyExtra02 import LimpiarPantalla,BC,BF,CBL,FR,BF,CM,CG,CGL,CY,CR,Logo
from RS4LyOpcionesDelMenu02 import Opcion1_IP,Menu_Conexiones,Opcion2_Red,Opcion3_Url,Gracias


Logo()

RevisarCambioDeKey=CambioDeKeys()

if RevisarCambioDeKey !="0":
    LimpiarPantalla()
    Logo()
    print(
        CM+"Menu Principal\n",
        CG+"1 Analisis de ip\n",
        CG+"2-Analisis de red\n",
        CG+"3-Analisis de url\n"+FR,
        "4-Analisis de archivos(No disponible)\n",
        CG+"5-Verificar conexiones y keys personales\n",
        CG+"6-Gracias\n",
        CG+"0-Salir\n"+FR
        )
    Eleccion=input("Seleccione una opcion ---> ")
    
    while Eleccion !="0":

        if Eleccion == "1":
            Opcion1_IP()
        
        if Eleccion =="2":
            Opcion2_Red()
        
        if Eleccion =="3":
            Opcion3_Url()
            
        if Eleccion == "5":
            Menu_Conexiones()
        
        if Eleccion =="6":
            Gracias()
            
        if Eleccion == "0":
            break
            
        else:
            print("La opcion seleccionada en estos momentos no se encuentra disponible")
    
        LimpiarPantalla()
        Logo()
        print(
            CM+"Menu Principal\n",
            CG+"1 Analisis de ip\n",
            CG+"2-Analisis de red\n",
            CG+"3-Analisis de url\n"+FR,
            "4-Analisis de archivos(No disponible)\n",
            CG+"5-Verificar conexiones y keys personales\n",
            CG+"6-Gracias\n",
            CG+"0-Salir\n"+FR
            )
        Eleccion=input("Seleccione una opcion ---> ")
        
    else:
        print("Saliendo")
        exit
        
else:
    print("Saliendo")


