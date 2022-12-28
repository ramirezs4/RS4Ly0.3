from RS4LyExtra02 import LimpiarPantalla,CM,FR,CG,CA,init,SB,SR,FC,CY,CR,CRL,CGL,BC,BF,LogoAnalisisDeRed
from RS4LyAnálisisDeCondiciones02 import Evaluar_Ultimo_ActualizacionRed,Evaluar_Ultimo_ReporteRed,Nivel_De_RiesgoRed,Porcentaje_ReportadosRed,Total_DeReportesRed
init()



def Conjunto_Analisis_De_Red(Red,DataRed1,DataRed2):
    
    B=DataRed1['result']['inetnums'][0]["inetnum"]
    D=DataRed1['result']['inetnums'][0]["as"]["name"]
    E=DataRed1['result']['inetnums'][0]["as"]["type"]
    F=DataRed1['result']['inetnums'][0]["as"]["route"]
    G=DataRed1['result']['inetnums'][0]["as"]["domain"]
    H=DataRed1['result']['inetnums'][0]["description"]
    H=str(H).strip('[]')
    I=DataRed1['result']['inetnums'][0]["modified"]

    try:
        #Informacion de contacto
        A1=DataRed1['result']['inetnums'][0]["abuseContact"][0]["role"]
        A2=DataRed1['result']['inetnums'][0]["abuseContact"][0]["email"]
        A3=DataRed1['result']['inetnums'][0]["abuseContact"][0]["phone"]
        A4=DataRed1['result']['inetnums'][0]["abuseContact"][0]["address"]
        A4=str(A4).strip('[]')
    except:
        A1=""
        A2=""
        A3=""
        A4=""
    
    try:
        A5=DataRed1['result']['inetnums'][0]["adminContact"][0]["person"]
        A6=DataRed1['result']['inetnums'][0]["adminContact"][0]["email"]
        A7=DataRed1['result']['inetnums'][0]["adminContact"][0]["phone"]
        A8=DataRed1['result']['inetnums'][0]["adminContact"][0]["address"]
        A8=str(A8).strip('[]')
        
        A10=DataRed1['result']['inetnums'][0]["techContact"][0]["person"]
        A11=DataRed1['result']['inetnums'][0]["techContact"][0]["email"]
        A12=DataRed1['result']['inetnums'][0]["techContact"][0]["phone"]
        A13=DataRed1['result']['inetnums'][0]["techContact"][0]["address"]
        A13=str(A13).strip('[]')
        
    except:
        A5=""
        A6=""
        A7=""
        A8=""
        A10=""
        A11=""
        A12=""
        A13=""

    B1=DataRed2['data']['numPossibleHosts']
    NivelDeRiesgoRed=Nivel_De_RiesgoRed(DataRed2)
    TotalReportes=Total_DeReportesRed(DataRed2)
    FechaUltimoReporte=Evaluar_Ultimo_ReporteRed(DataRed2)
    FechaUltimaActualizacion=Evaluar_Ultimo_ActualizacionRed(DataRed1)
    PorcentajeDeReportes=Porcentaje_ReportadosRed(DataRed2)
    DireccionesConReportes=str(len(DataRed2["data"]['reportedAddress']))

    LimpiarPantalla()
    
    LogoAnalisisDeRed()
    
    print(
        CA+"El analisis de la Subred "+Red+" arrojo los siguientes resultados:"+FR
        ,SB+"\n a)"+SR+" La direccion pertenece a una red:",CG+"Publica"+FR
        ,SB+"\n b)"+SR+" Rango de la Subred: "+FC+str(B)+FR+", total de direcciones: "+FC+str(B1)+FR
        ,SB+"\n c)"+SR+" De esta subred: "+CY+DireccionesConReportes+FR+" IPs poseen reportes, euivalente a un "+PorcentajeDeReportes
        ,SB+"\n d)"+SR+" Numero total de reportes realizados a esta red:",TotalReportes
        ,SB+"\n e)"+SR+" Desde la ultima vez que se reporto han pasado:",FechaUltimoReporte
        ,SB+"\n f)"+SR+" El nivel de riesgo general es: "+NivelDeRiesgoRed
        ,SB+"\n g)"+SR+" Tipo de uso: "+FC+str(E)+FR
        ,SB+"\n h)"+SR+" Red madre: "+FC+str(F)+FR
        
        ,CM+"\n\nInformacion de Geolocalizacion"+FR
        ,SB+"\n 1A)"+SR+" Nombre de la organizacion: "+FC+str(D)+FR
        ,SB+"\n 2A)"+SR+" El nombre del dominio es: "+FC+str(G)+FR
        ,SB+"\n 3A)"+SR+" Descripcion: "+FC+str(H)+FR
        ,SB+"\n 4A)"+SR+" Fecha de la ultima actualizacion de esta informacion: "+FechaUltimaActualizacion
        ,CM+"\n\nContacto:"+FR
        ,SB+"\n 1B)"+SR+" Regulador "+FC+str(A1)+FR+", correo electronico "+FC+str(A2)+FR+", Numero de contacto "+FC+str(A3)+FR+", Direccion "+FC+str(A4)+FR
        ,SB+"\n 2B)"+SR+" Administrador "+FC+str(A5)+FR+", correo electronico "+FC+str(A6)+FR+", Numero de contacto "+FC+str(A7)+FR+", Direccion "+FC+str(A8)+FR
        ,SB+"\n 3B)"+SR+" Tecnico registrado "+FC+str(A10)+FR+", correo electronico "+FC+str(A11)+FR+", Numero de contacto "+FC+str(A12)+FR+", Direccion "+FC+str(A13)+FR

    )

