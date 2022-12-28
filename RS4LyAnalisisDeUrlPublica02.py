from RS4LyConsultas02 import ConsultaDeURLIpQualityScore,ConsultaDeURLWhoisXML1,ConsultaDeURLVirusTotal
from RS4LyAnálisisDeCondiciones02 import CambiarTrueUrl,TotalAVUrl,Lista_Fuentes
from RS4LyExtra02 import LimpiarPantalla,BC,BF,CBL,FR,BF,CM,CG,CGL,CY,CR,SB,SR,CA,FR


def Conjunto_Analisis_URL(URL,Data_URL_IP_QUalityScore,Data_URL_vrusTotal,Data_URL_Whois_XML):
        Data_URL_IP_QUalityScore=ConsultaDeURLIpQualityScore(URL)
        Data_URL_vrusTotal=ConsultaDeURLVirusTotal(URL)
        Data_URL_Whois_XML=ConsultaDeURLWhoisXML1(URL)

        #Informacion de seguridad
        A1=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore['unsafe'])
        A3=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore['parking'])
        A4=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore['spamming'])
        A5=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore["malware"])
        A6=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore['phishing'])
        A7=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore['suspicious'])
        A8=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore['adult'])

        #Puntuacion de riesgo
        A9=Data_URL_IP_QUalityScore['risk_score']
        A10=Data_URL_IP_QUalityScore['category']

        #Informacion DNS
        A2=Data_URL_IP_QUalityScore['domain']
        A12=CambiarTrueUrl(Cambiar=Data_URL_IP_QUalityScore['dns_valid'])

        #Virus Total
        try:
            CC1=TotalAVUrl(Calculo=Data_URL_vrusTotal['positives'])
            CC2=Data_URL_vrusTotal['total']
            D1=Data_URL_Whois_XML['domains']
        except:
            None
                      
        print( 
        CA+"El analisis de la Url "+URL+" arrojo los siguientes resultados:"+FR
        ,SB+"\n a)"+SR+" Puntuacion de riesgo",A9
        ,SB+"\n b)"+SR+" Categoria General",A10
        
        ,CM+"\n\nInformacion DNS:"+FR
        ,SB+"\n a)"+SR+" Dominio actual",A2
        ,SB+"\n b)"+SR+" Dominios asociados",D1
        ,SB+"\n c)"+SR+" Parking de dominio",A3
        ,SB+"\n d)"+SR+" DNS validado",A12
        
        ,CM+"\n\nFuentes:"+FR
        
        ,"\n\n"+BC+" 1) IP Quality Score:"+BF
        ,"\n  a) Maliciosa:",A1
        ,"\n  b) Spam:",A4
        ,"\n  c) Malware",A5
        ,"\n  d) Phishing",A6
        ,"\n  e) Sospechosa",A7
        ,"\n  f) Contenido para adultos",A8
        
        ,"\n\n"+BC+" 2) Virus Total:"+BF
        ,SB+"\n a)"+SR+" Se analizo con un total de ",CC2," AV, ","se encuentra positivo en: ",CC1,"\n"
        )
        
        print(Lista_Fuentes(Data_URL_vrusTotal))
        
        input("Presione Enter para continuar")