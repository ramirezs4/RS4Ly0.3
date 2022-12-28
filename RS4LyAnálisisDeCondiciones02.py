from RS4LyExtra02 import CB,CR,CBL,FR,CG,CGL,CRL,FC,CM,CY,CRL,SB,SR,CA
from RS4LyVerificacionDeDatos02 import Verificacion_Hostname
from datetime import datetime
import ipaddress
from tabulate import tabulate

def Validar_Red(Red):
    try:
        Red = ipaddress.ip_network(Red)
        if Red.is_private:
            return "Privada"
        else:
            return "Publica"
    except:
        return "Red no valida"

def Validar_IP1(IP1):
    try:
        IP1=ipaddress.ip_address(IP1)
        if IP1.is_private:
            return "Privada"
        else:
            return "Publica"
    except:
        return "IP no valida"

#Puntuacion de abuso
def Puntuacion_IndividualJunta(Usar):
    Usar=int(Usar)
    while(Usar>0):
        if(Usar<20):
            return Posibles_Puntuaciones(2)
        elif(Usar<30):
            return Posibles_Puntuaciones(3)
        elif(Usar<40):
            return Posibles_Puntuaciones(4)
        elif(Usar<50):
            return Posibles_Puntuaciones(5)
        elif(Usar<60):
            return Posibles_Puntuaciones(6)
        elif(Usar<70):
            return Posibles_Puntuaciones(7)
        elif(Usar<80):
            return Posibles_Puntuaciones(8)
        elif(Usar<90):
            return Posibles_Puntuaciones(9)
        elif(Usar>=90):
            return Posibles_Puntuaciones(10)
    else:
        return Posibles_Puntuaciones(1)

def Puntuacion_GENERAL(Data1,Data2):
    Usar1=Data1["data"]['abuseConfidenceScore']
    Usar2=Data2["fraud_score"]
    while(Usar1>1 or Usar2>1):
        if(Usar1<20 and Usar2<20):
            return Posibles_Puntuaciones(2)
        elif(Usar1<30 and Usar2<30):
            return Posibles_Puntuaciones(3)
        elif(Usar1<40 and Usar2<40):
            return Posibles_Puntuaciones(4)
        elif(Usar1<50 and Usar2<50):
            return Posibles_Puntuaciones(5)
        elif(Usar1<60 and Usar2<60):
            return Posibles_Puntuaciones(6)
        elif(Usar1<70 or Usar2<70):
            return Posibles_Puntuaciones(7)
        elif(Usar1<80 or Usar2<80):
            return Posibles_Puntuaciones(8)
        elif(Usar1<90 or Usar2<90):
            return Posibles_Puntuaciones(9)
        elif(Usar1>=90 or Usar2>=90):
            return Posibles_Puntuaciones(10)
    else:
        return Posibles_Puntuaciones(1)
    
def Posibles_Puntuaciones(Valor):
    Puntuaciones={
        1: CG+"0-Muy Bajo"+FR,
        2: CGL+"1-Bajo"+FR,
        3: CGL+"2-Bajo Alto"+FR,
        4: CGL+"4-Medio Bajo"+FR,
        5: CRL+"5-Medio"+FR,
        6: CRL+"6-Medio Alto"+FR,
        7: CR+"7-Alto bajo"+FR,
        8: CR+"8-Alto"+FR,
        9: CR+"9-Muy Alto"+FR,
        10: CR+"10-Extremo"+FR
    }
    return Puntuaciones.get(Valor,"No fue posible calcular el riesgo")

def Evaluar_Cantidad(Cantidad):
    Valoracion={
        1: CG+", Nulo"+FR,
        2: CGL+", Bajo"+FR,
        3: CRL+", Medio"+FR,
        4: CR+", Alto"+FR,
        5: CR+", Masivo"+FR
    }
    return Valoracion.get(Cantidad,"No fue posible realizar el calculo")

def Num_De_UsuariosYReportes(Data1,Para):
    if Para=="usuario":
        Usar=int(Data1["data"]['numDistinctUsers'])
    elif Para=="reporte":
        Usar=int(Data1["data"]['totalReports'])

    while True:
        if Usar==0:
            return FC+str(Usar)+FR+Evaluar_Cantidad(1)
        elif(Usar<3):
            return FC+str(Usar)+FR+Evaluar_Cantidad(2)
        elif(Usar<6):
            return FC+str(Usar)+FR+Evaluar_Cantidad(3)
        elif(Usar<9):
            return FC+str(Usar)+FR+Evaluar_Cantidad(4)
        elif(Usar>=9):
            return FC+str(Usar)+FR+Evaluar_Cantidad(5)
        else:
            return FC+str(Usar)+CY+", No se pudo Calcular"+FR

    
       
def Fecha_Ultimo_Report(Data1):
    try:
        FechaBruta=Data1["data"]["lastReportedAt"]
        Buscar=FechaBruta.index("T")
        AñoMesDia=FechaBruta[:Buscar]
        Hora=FechaBruta[Buscar+1:-6]
        ProcesarFecha=AñoMesDia+" "+Hora
        ProcesarFecha=datetime.strptime(ProcesarFecha[2:],"%y-%m-%d %H:%M:%S")
        FechaActual=datetime.now(tz=None)
        return str(FechaActual-ProcesarFecha)

    except:
        return "nunca"

def Evaluar_Ultimo_Reporte(Data1):
        try:
            Dias=Fecha_Ultimo_Report(Data1)
            Buscar=Dias.index("d")
            Dias1=int(Dias[:Buscar-1])
            DiasStr=Dias[:Buscar-1]
            
            if Dias1 == 0:
                DiasStr="0"
                return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
            elif Dias1 < 3:
                DiasStr="1"
                return (CR+DiasStr+" dias, Menos de 2 dias"+FR)
            elif Dias1 < 7:
                return (CRL+DiasStr+" dias, Menos de 1 semana"+FR)
            elif Dias1 > 7 and Dias1 < 14:
                return (CRL+DiasStr+" dias, Mas de 1 semana"+FR)
            elif Dias1 >= 14 and Dias1 < 30:
                return (CRL+DiasStr+" dias, Mas de 2 semanas"+FR)
            elif Dias1 > 30 and Dias1 < 60:
                return (CGL+DiasStr+" dias, Mas de 1 mes"+FR)
            elif Dias1 > 60 and Dias1 < 120:
                return (CG+DiasStr+" dias, Mas de 2 meses"+FR)
            elif Dias1 > 120:
                return (CG+DiasStr+" dias, Mas de 4 meses"+FR)
        
        except ValueError:
            try:
                Horas=Fecha_Ultimo_Report(Data1)
                Buscar=":"
                for Buscar in str(Horas):
                    DiasStr="0"
                    return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
                else:
                    None
            except ValueError:    
                return (CG+"No tiene registros de reportes"+FR)

def Info_Geografica(Data2):
    A=(FC+"Codigo del pais "+FR)
    B=(FC+", Region "+FR)
    C=(FC+", City "+FR)
    D=str(Data2["country_code"])
    E=str(Data2["region"])
    F=str(Data2["city"])
    GeograIP=A+D+B+E+C+F
    return GeograIP

def Trafico_NoHumano(Data2):    
    if(Data2["bot_status"]==True): 
        return CR+"si"+FR
    else: 
        return CG+"No"+FR

def Conexion_Proxy(Data2):
    if(Data2["proxy"]==True): 
        return CR+"si"+FR
    else: 
        return CG+"No"+FR

def Nodo_Tor(Data2):
    if(Data2["active_tor"]==True and Data2["tor"]==True):
        return CR+"si"+FR
    else: 
        return CG+"No"+FR

def Limpiao_No1(Data1):
    if(Data1["data"]["abuseConfidenceScore"]>30): 
        return CR+"Maliciosa"+FR
    else: 
        return CG+"Limpia"+FR

def Limpia_No2(Data2):
    if(Data2["fraud_score"]>30): 
        return CR+"Maliciosa"+FR
    else: 
        return CG+"Limpia"+FR

def Limpia_No3(Data3):
    try:
        Detect=int(len(Data3["detected_urls"]))
        Resolu=int(len(Data3["resolutions"]))
        Muest=int(len(Data3["detected_referrer_samples"]))
        if(Detect>2 and Resolu>1 and Muest>2):
            return CR+"Maliciosa"+FR
        else: 
            return CG+"Limpia"+FR
        
    except KeyError:
        return CG+"Limpia"+FR

def Verificar_resoluciones(Data3):
    try:
        RegistroDeNombres=len(Data3['resolutions'])
        if RegistroDeNombres>0:
            return RegistroDeNombres
        else:
            return 0
    except KeyError:
        return 0

def Numero_DeRegistrosHN(Data3):
    NumeroDeRegistros=Verificar_resoluciones(Data3)
    
    while NumeroDeRegistros>0:
    #Nombre de host a los que ha resolvido esta ip
        if NumeroDeRegistros==1:
            return FC+"1, "+FR+Posibles_Puntuaciones(1)
        elif NumeroDeRegistros==2:
            return FC+"2, "+FR+Posibles_Puntuaciones(2)
        elif NumeroDeRegistros==3:
            return FC+"3, "+FR+Posibles_Puntuaciones(3)
        elif NumeroDeRegistros==4:
            return FC+"4, "+FR+Posibles_Puntuaciones(4)
        elif NumeroDeRegistros==5:
            return FC+"5, "+FR+Posibles_Puntuaciones(5)
        elif NumeroDeRegistros==6:
            return FC+"6, "+FR+Posibles_Puntuaciones(6)
        elif NumeroDeRegistros==7:
            return FC+"7, "+FR+Posibles_Puntuaciones(7)
        elif NumeroDeRegistros==8:
            return FC+"8, "+FR+Posibles_Puntuaciones(8)
        elif NumeroDeRegistros==9:
            return FC+"9, "+FR+Posibles_Puntuaciones(9)
        elif NumeroDeRegistros>=10:
            return FC+str(int(NumeroDeRegistros))+", "+FR+Posibles_Puntuaciones(10)
    else:
        return CG+"No se encontraron registros de la misma"+FR

def Informacion_Resolucion(Data1,Data2,Data3):    
    Resolu1=Verificar_resoluciones(Data3)
    Resoluciones=Numero_DeRegistrosHN(Data3)
    
    def Nombre_actual(Data1):
        try:
            Verificacion=Verificacion_Hostname(Data1,Data2)
            return Verificacion
        except KeyError:
                Verificacion=Data1['data']['hostnames']
                return Verificacion
            
    NombreActual=str(Nombre_actual(Data1))
    
    if Resolu1==0:
        print(
            CM+"\nRegistro de resoluciones"+FR
            ,SB+"\n 1)"+SR+" Posee registros de cambio de nombre: "+CG+"No"+FR
            ,SB+"\n 2)"+SR+" Cuantos cambios presenta: "+Resoluciones
            ,SB+"\n "+SR+CM+"3) Historial:"+FR
            ,SB+"\n   a)"+SR+" Nombre actual:"+FC+NombreActual+FR)
        
    elif Resolu1>=3:
        print(
            CM+"\nRegistro de resoluciones"+FR
            ,SB+"\n 1)"+SR+" Posee registros de cambio de nombre: "+CY+"Si"+FR
            ,SB+"\n 2)"+SR+" Cuantos cambios presenta: "+Resoluciones
            ,SB+"\n "+SR+CM+"3) Historial:"+FR
            ,SB+"\n   a)"+SR+" Nombre actual:"+FC+str(Data1["data"]["hostnames"])+FR
            ,SB+"\n   b)"+SR+" Nombres anteriores y fecha del resultado:"
            ,SB+"\n    b.1) Nombre "+SR+CY+Data3["resolutions"][0]["hostname"]+FR+", Fecha del resultado "+FC+Data3["resolutions"][0]["last_resolved"]+FR
            ,SB+"\n    b.2) Nombre "+SR+CY+Data3["resolutions"][1]["hostname"]+FR+", Fecha del resultado "+FC+Data3["resolutions"][1]["last_resolved"]+FR
            ,SB+"\n    b.3) Nombre "+SR+CY+Data3["resolutions"][2]["hostname"]+FR+", Fecha del resultado "+FC+Data3["resolutions"][2]["last_resolved"]+FR
        )

def CambiarTrueUrl(Cambiar):
    if Cambiar == False: return CG+"No"+FR
    else: return CR+"Si"+FR

#Tabla de fuentes
def Lista_Fuentes(Data_URL_vrusTotal):
    ListaScans=['Fortinet','Comodo Valkyrie Verdict','Sophos','CMC Threat Intelligence','Kaspersky','Google Safebrowsing','VX Vault','ESTsecurity','ESET','alphaMountain.ai','PhishLabs','CINS Army','Spam404','OpenPhish','Web Security Guard','PhishFort','Phishing Database','IPsum','BitDefender']
    ListaCompleta=[]
    ListaParcial=[]

    for CC4 in ListaScans:
        if CC4 in Data_URL_vrusTotal['scans']:
            Detectado=str(Data_URL_vrusTotal['scans'][CC4]['detected'])
            if Detectado == "True": Detectado=CR+"Si"+FR
            else: Detectado=CG+"No"+FR
            
            Categoria=str(Data_URL_vrusTotal['scans'][CC4]['result'])
            if Categoria == "clean site": Categoria=CG+"Limpio"+FR
            elif Categoria == "malicious site": Categoria=CR+"Malicioso"+FR
            elif Categoria == "unrated site": Categoria=CY+"N/A"+FR
            else: Categoria == str(Data_URL_vrusTotal['scans'][CC4]['result'])
            
            if Detectado == CR+"Si"+FR: CC4=CR+CC4+FR
            elif Categoria == CY+"N/A"+FR: CC4=CY+CC4+FR
            else: CC4=CG+CC4+FR
                
            #print(CC4+": Registrado "+Detectado+", clasificacion "+Categoria)
            ListaCompleta.append([CC4,Detectado,Categoria])

    return(tabulate(ListaCompleta, headers=[CA+"Fuentes","Detectado","clasificacion"+FR]))


def TotalAVUrl(Calculo):
    CalculoStr=str(Calculo)
    Calculo=int(Calculo)
    
    if Calculo == 0:
        CalculoStr=CalculoStr+Evaluar_Cantidad(2)
    elif Calculo == 1:
        CalculoStr=CalculoStr+Evaluar_Cantidad(3)
    elif Calculo == 2 or Calculo == 3:
        CalculoStr=CalculoStr+Evaluar_Cantidad(4)
    elif Calculo > 3:
        CalculoStr=CalculoStr+Evaluar_Cantidad(5)
    else:
        CalculoStr=CalculoStr+Evaluar_Cantidad(1)
    return CalculoStr

def Urls_Detectadas(Data3):
    
    def Urls_NDetectadas(Data3):
        try:
            return (len(Data3['detected_urls']))
        except KeyError:
            return 0

    UrlsDetectadas=Urls_NDetectadas(Data3)

    if UrlsDetectadas>3:
        print(
            CM+"\nUrls en esta direccion"+FR
            ,SB+"\n 1)"+SR+" Se encontraron direcciones en esta direccion: "+CY+"Si"+FR
            ,SB+"\n 2)"+SR+" Cuantas fueron detectadas como maliciosas: "+str(UrlsDetectadas)
            ,SB+"\n "+SR+CM+"3) Historial:"+FR
            ,SB+"\n   b)"+SR+" Urls detectadas como maliciosas:"
            ,SB+"\n    b.1) "+SR+CY+str(Data3['detected_urls'][0]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][0]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][0]["positives"])+FR
            ,SB+"\n    b.2) "+SR+CY+str(Data3['detected_urls'][1]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][1]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][1]["positives"])+FR
            ,SB+"\n    b.3) "+SR+CY+str(Data3['detected_urls'][2]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][2]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][2]["positives"])+FR
            ,SB+"\n    b.4) "+SR+CY+str(Data3['detected_urls'][3]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][3]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][3]["positives"])+FR
        )
        
    else:
        print(
        CM+"\nUrls en esta direccion"+FR
        ,SB+"\n 1)"+SR+" Se encontraron direcciones en esta direccion: "+CG+"No"+FR
        ,SB+"\n 2)"+SR+" Cuantas fueron detectadas como maliciosas: "+CG+"0"+FR
    )

#Fecha del ultimo reporte
def Fecha_Ultimo_ReportRed(DataRed2):
    try:
        FechaBruta=(DataRed2["data"]['reportedAddress'][0]['mostRecentReport'])
        Buscar=FechaBruta.index("T")
        AñoMesDia=FechaBruta[:Buscar]
        Hora=FechaBruta[Buscar+1:-6]
        
        ProcesarFecha=AñoMesDia+" "+Hora

        ProcesarFecha=datetime.strptime(ProcesarFecha[2:],"%y-%m-%d %H:%M:%S")
        FechaActual=datetime.now(tz=None)
        return str(FechaActual-ProcesarFecha)

    except AttributeError:
        return "nunca"    

#Fecha del ultimo reporte
def Fecha_Actualizacion(DataRed1):
    try:
        
        FechaBruta=(DataRed1['result']['inetnums'][0]["modified"])
        Buscar=FechaBruta.index("T")
        AñoMesDia=FechaBruta[:Buscar]
        Hora=FechaBruta[Buscar+1:-1]
        
        ProcesarFecha=AñoMesDia+" "+Hora
        ProcesarFecha=datetime.strptime(ProcesarFecha,"%Y-%m-%d %H:%M:%S")
        FechaActual=datetime.now(tz=None)

        return str(FechaActual-ProcesarFecha)

    except AttributeError:
        return "nunca"
    
def Fecha_ReporteRed(DataRed2):
    try:
        
        FechaBruta=(DataRed2["data"]["reportedAddress"][0]["mostRecentReport"])
        Buscar=FechaBruta.index("T")
        AñoMesDia=FechaBruta[:Buscar]
        
        ProcesarFecha=AñoMesDia
        ProcesarFecha=datetime.strptime(ProcesarFecha,"%Y-%m-%d")
        FechaActual=datetime.now(tz=None)

        return str(FechaActual-ProcesarFecha)

    except:
        return "nunca"

def Evaluar_Ultimo_ReporteRed(DataRed2):
        try:
            Dias=Fecha_ReporteRed(DataRed2)
            Buscar=Dias.index("d")
            Dias1=int(Dias[:Buscar-1])
            DiasStr=Dias[:Buscar-1]
            
            if Dias1 == 0:
                DiasStr="0"
                return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
            elif Dias1 < 3:
                DiasStr="1"
                return (CR+DiasStr+" dias, Menos de 2 dias"+FR)
            elif Dias1 < 7:
                return (CRL+DiasStr+" dias, Menos de 1 semana"+FR)
            elif Dias1 > 7 and Dias1 < 30:
                return (CRL+DiasStr+" dias, Mas de 1 semana"+FR)
            elif Dias1 > 30 and Dias1 < 60:
                return (CGL+DiasStr+" dias, Mas de 1 mes"+FR)
            elif Dias1 > 60 and Dias1 < 120:
                return (CG+DiasStr+" dias, Mas de 2 meses"+FR)
            elif Dias1 > 120:
                return (CG+DiasStr+" dias, Mas de 4 meses"+FR)
        
        except ValueError:
            try:
                Horas=Fecha_Ultimo_Report(DataRed2)
                Buscar=":"
                for Buscar in str(Horas):
                    DiasStr="0"
                    return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
                else:
                    None
            except ValueError:    
                return (CG+"No tiene registros de reportes"+FR)
    
def Evaluar_Ultimo_ActualizacionRed(DataRed1):
        try:
            Dias=Fecha_Actualizacion(DataRed1)
            Buscar=Dias.index("d")
            Dias1=int(Dias[:Buscar-1])
            DiasStr=Dias[:Buscar-1]
            
            if Dias1 == 0:
                DiasStr="0"
                return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
            elif Dias1 < 3:
                DiasStr="1"
                return (CR+DiasStr+" dias, Menos de 2 dias"+FR)
            elif Dias1 < 7:
                return (CRL+DiasStr+" dias, Menos de 1 semana"+FR)
            elif Dias1 > 7 and Dias1 < 30:
                return (CRL+DiasStr+" dias, Mas de 1 semana"+FR)
            elif Dias1 > 30 and Dias1 < 60:
                return (CGL+DiasStr+" dias, Mas de 1 mes"+FR)
            elif Dias1 > 60 and Dias1 < 120:
                return (CG+DiasStr+" dias, Mas de 2 meses"+FR)
            elif Dias1 > 120:
                return (CG+DiasStr+" dias, Mas de 4 meses"+FR)
        
        except ValueError:
            try:
                Horas=Fecha_Ultimo_Report(DataRed1)
                Buscar=":"
                for Buscar in str(Horas):
                    DiasStr="0"
                    return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
                else:
                    None
            except ValueError:    
                return (CG+"No tiene registros de reportes"+FR)
    
def Nivel_De_RiesgoRed(DataRed2):
    THost=len(DataRed2["data"]['reportedAddress'])
    A=0
    Contador=0
    while Contador < THost:
            Host=int(DataRed2["data"]['reportedAddress'][Contador]['numReports'])
            A=A+Host
            Contador=Contador+1   
    else:
        None
         
    B=round((int(len(DataRed2["data"]['reportedAddress']))/int(DataRed2["data"]['numPossibleHosts']))*100)
    
    while(A>1 or B>1):
        if(A<5 and B<2):
            return Posibles_Puntuaciones(2)
        elif(A<10 and B<4):
            return Posibles_Puntuaciones(3)
        elif(A<20 and B<5):
            return Posibles_Puntuaciones(4)
        elif(A<30 and B<6):
            return Posibles_Puntuaciones(5)
        elif(A<40 and B<8):
            return Posibles_Puntuaciones(6)
        elif(A<50 or B<10):
            return Posibles_Puntuaciones(7)
        elif(A<60 or B<15):
            return Posibles_Puntuaciones(8)
        elif(A<70 or B<20):
            return Posibles_Puntuaciones(9)
        elif(A>=70 or B>=20):
            return Posibles_Puntuaciones(10)
    else:
        return Posibles_Puntuaciones(1)
    
#Porcentaje de hosts reportados
def Porcentaje_ReportadosRed(DataRed2):
    Calculo=round((int(len(DataRed2["data"]['reportedAddress']))/int(DataRed2["data"]['numPossibleHosts']))*100)
    #Calculo=str(Calculo)+"%"
    while Calculo>1:
        if(Calculo<5):
            return FC+str(Calculo)+"%"+FR+Evaluar_Cantidad(2)
        elif(Calculo<10):
            return FC+str(Calculo)+"%"+FR+Evaluar_Cantidad(3)
        elif(Calculo<15):
            return FC+str(Calculo)+"%"+FR+Evaluar_Cantidad(4)
        elif(Calculo>15):
            return FC+str(Calculo)+"%"+FR+Evaluar_Cantidad(5)
    else:
        Calculo="0%"
        return FC+Calculo+FR+Evaluar_Cantidad(1)

#Numero total de reportes que tienen las ip pertecientes a la red ingresada
def Total_DeReportesRed(DataRed2):
    THost=len(DataRed2["data"]['reportedAddress'])
    SumReportes=0
    Contador=0
    while Contador < THost:
            Host=int(DataRed2["data"]['reportedAddress'][Contador]['numReports'])
            SumReportes=SumReportes+Host
            Contador=Contador+1   
    else:
        None

    while SumReportes>0:
        if(SumReportes<3):
            return FC+str(SumReportes)+FR+Evaluar_Cantidad(2)
        elif(SumReportes<6):
            return CY+str(SumReportes)+FR+Evaluar_Cantidad(3)
        elif(SumReportes<9):
            return CRL+str(SumReportes)+FR+Evaluar_Cantidad(4)
        elif(SumReportes>9):
            return CR+str(SumReportes)+FR+Evaluar_Cantidad(5)
    else:
        SumReportes="0"
        return FC+SumReportes+FR+Evaluar_Cantidad(1)
    
    return SumReportes

#Crear Lista con ips con altos, medios y bajos reportes por separado 
def Reportes_Altos(DataRed2):
    Contador=0
    AltosReportes=[]
    THost=len(DataRed2["data"]['reportedAddress'])
    
    while Contador < THost:
        Host=int(DataRed2["data"]['reportedAddress'][Contador]['numReports'])
        if Host > 50:
            AltosReportes.append(DataRed2["data"]['reportedAddress'][Contador]["ipAddress"])
        else:
            None    
        Contador=Contador+1
    
    if len(AltosReportes)<1:
        AltosReportes="Ninguna IP del rango posee un numero alto de reportes"
        
    return AltosReportes

def Reportes_Medios(DataRed2):
    Contador=0
    MediosReportes=[]
    THost=len(DataRed2["data"]['reportedAddress'])
    
    while Contador < THost:
        Host=int(DataRed2["data"]['reportedAddress'][Contador]['numReports'])
        if Host < 50 and Host > 7:
            MediosReportes.append(DataRed2["data"]['reportedAddress'][Contador]["ipAddress"])
        else:
            None    
        Contador=Contador+1
    
    if len(MediosReportes)<1:
        MediosReportes="Ninguna IP del rango posee un numero medio de reportes"
        
    return MediosReportes

def Reportes_Bajos(DataRed2):
    Contador=0
    BajosReportes=[]
    THost=len(DataRed2["data"]['reportedAddress'])
    
    while Contador < THost:
        Host=int(DataRed2["data"]['reportedAddress'][Contador]['numReports'])
        if Host < 7:
            BajosReportes.append(DataRed2["data"]['reportedAddress'][Contador]["ipAddress"])
        else:
            None    
        Contador=Contador+1
    
    if len(BajosReportes)<1:
        BajosReportes="Ninguna IP del rango posee un numero Bajo de reportes"
        
    return BajosReportes

def Reportes_Todo(DataRed2):
    Contador=0
    THost=len(DataRed2["data"]['reportedAddress'])
    TodosReportes=[]
    
    while Contador < THost:
        TodosReportes.append(DataRed2["data"]['reportedAddress'][Contador]["ipAddress"])
        Contador=Contador+1
    else:
        None
        
    if len(TodosReportes)<1:
        TodosReportes="Ninguna ip de la red posee reportes"
    
    return TodosReportes
     
#Menu para mostrar listas de reportes
def Listas_DeReportes(DataRed2):
    ReportesBajos=Reportes_Bajos(DataRed2)
    ReportesMedios=Reportes_Medios(DataRed2)
    ReportesAltos=Reportes_Altos(DataRed2)
    
    ContarReportesBajos=str(Contar_ElementosLista(DataRed2,ReportesBajos,ReportesMedios="",ReportesAltos=""))
    ContarReportesMedios=str(Contar_ElementosLista(DataRed2,ReportesBajos="",ReportesMedios=ReportesMedios,ReportesAltos=""))
    ContarReportesAltos=str(Contar_ElementosLista(DataRed2,ReportesBajos="",ReportesMedios="",ReportesAltos=ReportesAltos)) 
    
    if len(DataRed2["data"]['reportedAddress'])>1:
        print(
            CM+"\nListas con las Ips segun el numero de reportes"+FR
            ,SB+"\n 1)"+SR+CG+" Bajo"+FR+": IPs con mas de 1 reporte y menos de 7: "+str(ContarReportesBajos)
            ,SB+"\n 2)"+SR+CY+" Medio"+FR+": IPs con mas de 7 reporte y menos de 50: "+str(ContarReportesMedios)
            ,SB+"\n 3)"+SR+CR+" Alto"+FR+": IPs con mas de 50 reportes: "+str(ContarReportesAltos)
            ,SB+"\n 0)"+SR+CGL+" Salir\n"+FR
        )
        Eleccion=input("Seleccione una opcion ---> ")
        while Eleccion !=0:
        
            if Eleccion == "1":
                print(Reportes_Bajos(DataRed2))
                input("\nPresione Enter para continuar")
            elif Eleccion == "2":
                print(Reportes_Medios(DataRed2))
                input("\nPresione Enter para continuar")
            elif Eleccion == "3":
                print(Reportes_Altos(DataRed2))
                input("\nPresione Enter para continuar")
            elif Eleccion == "4":
                print(Reportes_Todo(DataRed2))
                input("\nPresione Enter para continuar")
            elif Eleccion == "0":
                break
            
            else:
                print(CG+"\nLa opcion seleccionada en estos momentos no se encuentra disponible"+FR)
                input("\nPresione Enter para continuar")
                
            print(
                CM+"\nListas con las Ips segun el numero de reportes"+FR
                ,SB+"\n 1)"+SR+CG+" Bajo"+FR+": IPs con mas de 1 reporte y menos de 7: "+str(ContarReportesBajos)
                ,SB+"\n 2)"+SR+CY+" Medio"+FR+": IPs con mas de 7 reporte y menos de 50: "+str(ContarReportesMedios)
                ,SB+"\n 3)"+SR+CR+" Alto"+FR+": IPs con mas de 50 reportes: "+str(ContarReportesAltos)
                ,SB+"\n 0)"+SR+CGL+" Salir\n"+FR
            )
            Eleccion=input("Seleccione una opcion ---> ")
        else:
            print("Regresando")
           
    else:
        print("Ninguna ip de la red posee reportes")

def Contar_ElementosLista(DataRed2,ReportesBajos,ReportesMedios,ReportesAltos):
    
    Red=len(DataRed2["data"]["networkAddress"])
    if Red <10:
        elemento=DataRed2["data"]["networkAddress"][:5]
    elif Red <10:
        elemento=DataRed2["data"]["networkAddress"][:6]
    
    Contador=0
    if ReportesBajos !="Ninguna IP del rango posee un numero Bajo de reportes" and len(ReportesBajos)>5:
        for elemento in ReportesBajos:
            Contador+=1
    elif ReportesMedios !="Ninguna IP del rango posee un numero medio de reportes" and len(ReportesMedios)>5:
        for elemento in ReportesMedios:
            Contador+=1
    elif ReportesAltos !="Ninguna IP del rango posee un numero alto de reportes" and len(ReportesAltos)>5:
        for elemento in ReportesAltos:
            Contador+=1
    
    while Contador>0:
        if(Contador<3):
            return FC+str(Contador)+FR+Evaluar_Cantidad(2)
        elif(Contador<6):
            return CY+str(Contador)+FR+Evaluar_Cantidad(3)
        elif(Contador<9):
            return CRL+str(Contador)+FR+Evaluar_Cantidad(4)
        elif(Contador>9):
            return CR+str(Contador)+FR+Evaluar_Cantidad(5)
    else:
        Contador="0"
        return FC+Contador+FR+Evaluar_Cantidad(1)
 



