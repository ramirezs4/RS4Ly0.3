from RS4LyAPIKEYS02 import ApiKey_IP_Abuse_DB,ApiKey_IP_Quality_Score,ApiKey_Virus_Total,ApiKey_IP_AbstractApi,ApiKey_Whois_XML
import requests
import json
import socket


def ConsultaDeIPVirusTotal(IP1):
    LinkDeLaApi="https://www.virustotal.com/vtapi/v2/ip-address/report"
    he={'apikey': ApiKey_Virus_Total, 'ip':IP1}
    DataDeVT2=requests.get(url=LinkDeLaApi, params=he)
    #Activar este print si quiere ver el codigo de estatus (200=correcta)
    #print(DataDeVT2)
    DataDeVT2=json.loads(DataDeVT2.text)
    return(DataDeVT2)

def ConsultaDeIPAbuseDb(IP1):
    LinkDeLaApi="https://api.abuseipdb.com/api/v2/check"
    IP1={'ipAddress': IP1}
    he={"Accept":"application\json","key":ApiKey_IP_Abuse_DB}
    DataDeIpAbuseDb1=requests.get(url=LinkDeLaApi,headers=he,params=IP1)
    #Activar este print si quiere ver el codigo de estatus (200=correcta)
    #print(DataDeIpAbuseDb1)
    DataDeIpAbuseDb1=json.loads(DataDeIpAbuseDb1.text)
    return(DataDeIpAbuseDb1)

def ConsultaDeIPQualityScore(IP1):
    LinkDeLaApi="https://ipqualityscore.com/api/json/ip/"
    LinkFinal=LinkDeLaApi+ApiKey_IP_Quality_Score+"/"+IP1
    DataDeIpQualityScore1=requests.get(url=LinkFinal)
    #Activar este print si quiere ver el codigo de estatus (200=correcta)
    #print(DataDeIpQualityScore1)
    DataDeIpQualityScore1=json.loads(DataDeIpQualityScore1.text)
    return(DataDeIpQualityScore1)

def ConsultaDeAbstractApi(IP1):
    LinkDeLaApi="https://ipgeolocation.abstractapi.com/v1/"
    LinkFinal=LinkDeLaApi+"?api_key="+ApiKey_IP_AbstractApi+"&ip_address="+IP1
    DataDeIpAbstractApi1=requests.get(url=LinkFinal)
    #Activar este print si quiere ver el codigo de estatus (200=correcta)
    #print(DataDeIpAbstractApi1)
    DataDeIpAbstractApi1=json.loads(DataDeIpAbstractApi1.text)
    return(DataDeIpAbstractApi1)

def ConsultaDeREDAbuseDb(Red):
    Api="a88139fc2a07687fa3c0c406d71d4e6f8af34506414d7a5fcc6c143d82c50a6e6f52f98e942d48ec"
    LinkDeLaApi="https://api.abuseipdb.com/api/v2/check-block"
    Red={'network': Red}
    he={"Accept":"application\json","key":ApiKey_IP_Abuse_DB}
    DataDeIpAbuseDb2=requests.get(url=LinkDeLaApi,headers=he,params=Red)
    #Activar este print si quiere ver el codigo de estatus (200=correcta)
    #print(DataDeIpAbuseDb2)
    DataDeIpAbuseDb2=json.loads(DataDeIpAbuseDb2.text)
    return(DataDeIpAbuseDb2)

def ConsultaDeRedWhoisXML(Red):
    url="https://ip-netblocks.whoisxmlapi.com/api/v2?apiKey="
    Buscar_A=Red.index("/")
    ip="&ip="+Red[:Buscar_A]
    CIDR="&mask="+Red[Buscar_A+1:]
    UrlFinal=url+ApiKey_Whois_XML+ip+CIDR
    DataDeWhoIs=requests.get(url=UrlFinal)
    DataDeWhoIs=(DataDeWhoIs.json())
    return(DataDeWhoIs)

def ConsultaDeIPWhoisXML1(IP1):
    Url="https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey="
    IP1="&ipAddress="+IP1
    LinkFinal=Url+ApiKey_Whois_XML+IP1
    DataDeWhoIs=requests.get(url=LinkFinal)
    DataDeWhoIs=DataDeWhoIs.json()
    return DataDeWhoIs
    
def ConsultaDeURLVirusTotal(URL):
    Url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': ApiKey_Virus_Total, 'resource':URL}
    DataDeVirusTotal = requests.get(url=Url, params=params)
    DataDeVirusTotal=(DataDeVirusTotal.json())
    return(DataDeVirusTotal)  

def ConsultaDeURLIpQualityScore(URL):
    LinkDeLaApi="https://ipqualityscore.com/api/json/url/"
    LinkDeLaApi=LinkDeLaApi+ApiKey_IP_Quality_Score+"/"+URL
    DataDeVT1=requests.get(url=LinkDeLaApi)
    #Activar este print si quiere ver el codigo de estatus (200=correcta)
    #print(DataDeVT1)
    DataDeVT1=(DataDeVT1.json())
    return(DataDeVT1)

def ConsultaDeURLWhoisXML1(URL):
    def IpDeUrl(URL):
        try:
            IpDeLaUrl=socket.gethostbyname(URL)
            IpDeLaUrl=(ConsultaDeIPWhoisXML1(IP1=IpDeLaUrl))
            return IpDeLaUrl
        except:
            return "Error"
        
    return (IpDeUrl(URL))

def ConsultaDeURLAbstractApi(URL):
    def IpDeUrl(URL):
        try:
            IpDeLaUrl=socket.gethostbyname(URL)
            IpDeLaUrl=(ConsultaDeAbstractApi(IP1=IpDeLaUrl))
            return IpDeLaUrl
        except:
            return "Error"
        
    return (IpDeUrl(URL))

def Guardar_Consultas_txt(IP1):
    VirusTotal=ConsultaDeIPVirusTotal(IP1)
    with open("VirusTotal.txt", "w") as VT:
        VT.write(str(VirusTotal))
        VT.close()

    IPAbuse=ConsultaDeIPAbuseDb(IP1)
    with open("IPAbuseDB.txt", "w") as IPAB:
        IPAB.write(str(IPAbuse))
        IPAB.close()

    AbstractApi=ConsultaDeAbstractApi(IP1)
    with open("AbstractApi.txt", "w",encoding="utf-8") as ABS:
        ABS.write(str(AbstractApi) )
        ABS.close()

    IPqual=ConsultaDeIPQualityScore(IP1)
    with open("IPQUAL.txt", "w") as IPQ:
        IPQ.write(str(IPqual))
        IPQ.close()
            
def Guardar_Consulta_Url_txt(URL):
    DataUrl1=ConsultaDeURLVirusTotal(URL)
    with open("VirusTotalUrl1.txt", "w") as IPQ:
            IPQ.write(str(DataUrl1))
            IPQ.close()
    DataUrl2=ConsultaDeURLIpQualityScore(URL)
    with open("IpQualityScoreUrl2.txt", "w") as IPQ:
            IPQ.write(str(DataUrl2))
            IPQ.close()
    DataUrl3=ConsultaDeURLWhoisXML1(URL)
    with open("WhoIsXMLURL1.txt", "w") as IPQ:
            IPQ.write(str(DataUrl3))
            IPQ.close()

