from RS4LyConsultas02 import ConsultaDeREDAbuseDb
from RS4LyAnálisisDeCondiciones02 import Reportes_Todo,Reportes_Bajos,Reportes_Medios,Reportes_Altos,Contar_ElementosLista
from RS4LyExtra02 import CB,CR,CBL,FR,CG,CGL,CRL,FC,CM,CY,CRL,SB,SR,CA



#IP Quality Score
DataUrlIPQUALITYSCOREB={'message': 'Success.', 'success': True, 'unsafe': False, 'domain': 'yahoo.com', 'ip_address': '74.6.231.21', 'server': 'N/A', 'content_type': 'text/html; charset=utf-8', 'status_code': 200, 'page_size': 193903, 'domain_rank': 18, 'dns_valid': True, 'parking': False, 'spamming': False, 'malware': False, 'phishing': False, 'suspicious': False, 'adult': False, 'risk_score': 0, 'category': 'N/A', 'domain_age': {'human': '28 years ago', 'timestamp': 790405200, 'iso': '1995-01-18T00:00:00-05:00'}, 'request_id': '9vQuVKCscY'}
Data_URL_IP_QUalityScore={'message': 'Success.', 'success': True, 'unsafe': True, 'domain': 'rarible.fan', 'ip_address': '172.173.198.6', 'server': '', 'content_type': 'text/html', 'status_code': 200, 'page_size': 461533, 'domain_rank': 0, 'dns_valid': True, 'parking': False, 'spamming': False, 'malware': False, 'phishing': True, 'suspicious': True, 'adult': False, 'risk_score': 91, 'category': 'Phishing', 'domain_age': {'human': '3 days ago', 'timestamp': 1671761689, 'iso': '2022-12-22T21:14:49-05:00'}, 'request_id': '9vQzNHQeYk'}

#URL Abstract Api
Data_URL_Abstract_Api={'ip_address': '172.173.198.6', 'city': None, 'city_geoname_id': None, 'region': None, 'region_iso_code': None, 'region_geoname_id': None, 'postal_code': None, 'country': 'Germany', 'country_code': 'DE', 'country_geoname_id': 2921044, 'country_is_eu': True, 'continent': 'Europe', 'continent_code': 'EU', 'continent_geoname_id': 6255148, 'longitude': 9.491, 'latitude': 51.2993, 'security': {'is_vpn': False}, 'timezone': {'name': 'Europe/Berlin', 'abbreviation': 'CET', 'gmt_offset': 1, 'current_time': '15:34:43', 'is_dst': False}, 'flag': {'emoji': '🇩🇪', 'unicode': 'U+1F1E9 U+1F1EA', 'png': 'https://static.abstractapi.com/country-flags/DE_flag.png', 'svg': 'https://static.abstractapi.com/country-flags/DE_flag.svg'}, 'currency': {'currency_name': 'Euros', 'currency_code': 'EUR'}, 'connection': {'autonomous_system_number': 8075, 'autonomous_system_organization': 'MICROSOFT-CORP-MSN-AS-BLOCK', 'connection_type': 'Corporate', 'isp_name': 'Oath Holdings Inc.', 'organization_name': 'AOL Inc.'}}
DataUrl2B={'ip_address': '74.6.143.26', 'city': 'Lockport', 'city_geoname_id': 5125011, 'region': 'New York', 'region_iso_code': 'NY', 'region_geoname_id': 5128638, 'postal_code': '14095', 'country': 'United States', 'country_code': 'US', 'country_geoname_id': 6252001, 'country_is_eu': False, 'continent': 'North America', 'continent_code': 'NA', 'continent_geoname_id': 6255149, 'longitude': -78.6913, 'latitude': 43.1721, 'security': {'is_vpn': False}, 'timezone': {'name': 'America/New_York', 'abbreviation': 'EST', 'gmt_offset': -5, 'current_time': '09:37:37', 'is_dst': False}, 'flag': {'emoji': '🇺🇸', 'unicode': 'U+1F1FA U+1F1F8', 'png': 'https://static.abstractapi.com/country-flags/US_flag.p png', 'svg': 'https://static.abstractapi.com/country-flags/US_flag.svg'}, 'currency': {'currency_name': 'USD', 'currency_code': 'USD'}, 'connection': {'autonomous_system_number': 26101, 'autonomous_system_organization': 'YAHOO-BF1', 'connection_type': 'Corporate', 'isp_name': 'Oath Holdings Inc.', 'organization_name': 'Oath Holdings Inc'}}      

#Virus Total
DataUrlVirusTotalB={'scan_id': 'ed91698b5823a5e4424726955dd3fd437d9cfdc46f7b8988cded5da779cc7483-1671888618', 'resource': 'www.yahoo.com', 'url': 'http://www.yahoo.com/', 'response_code': 1, 'scan_date': '2022-12-24 13:30:18', 'permalink': 'https://www.virustotal.com/gui/url/ed91698b5823a5e4424726955dd3fd437d9cfdc46f7b8988cded5da779cc7483/detection/u-ed91698b5823a5e4424726955dd3fd437d9cfdc46f7b8988cded5da779cc7483-1671888618', 'verbose_msg': 'Scan finished, scan information embedded in this object', 'filescan_id': None, 'positives': 0, 'total': 90, 'scans': {'Bkav': {'detected': False, 'result': 'unrated site'}, 'CMC Threat Intelligence': {'detected': False, 'result': 'clean site'}, 'Snort IP sample list': {'detected': False, 'result': 'clean site'}, 'VX Vault': {'detected': False, 'result': 'clean site'}, 'ViriBack': {'detected': False, 'result': 'clean site'}, 'Comodo Valkyrie Verdict': {'detected': False, 'result': 'clean site'}, 'PhishLabs': {'detected': False, 'result': 'unrated site'}, 'K7AntiVirus': {'detected': False, 'result': 'clean site'}, 'CINS Army': {'detected': False, 'result': 'clean site'}, 'Quttera': {'detected': False, 'result': 'clean site'}, 'BlockList': {'detected': False, 'result': 'clean site'}, 'PrecisionSec': {'detected': False, 'result': 'unrated site'}, 'OpenPhish': {'detected': False, 'result': 'clean site'}, '0xSI_f33d': {'detected': False, 'result': 'unrated site'}, 'Feodo Tracker': {'detected': False, 'result': 'clean site'}, 'Web Security Guard': {'detected': False, 'result': 'clean site'}, 'Scantitan': {'detected': False, 'result': 'clean site'}, 'AlienVault': {'detected': False, 'result': 'clean site'}, 'Sophos': {'detected': False, 'result': 'clean site'}, 'Phishtank': {'detected': False, 'result': 'clean site'}, 'CyberCrime': {'detected': False, 'result': 'clean site'}, 'Spam404': {'detected': False, 'result': 'clean site'}, 'SecureBrain': {'detected': False, 'result': 'clean site'}, 'Hoplite Industries': {'detected': False, 'result': 'clean site'}, 'CRDF': {'detected': False, 'result': 'clean site'}, 'Rising': {'detected': False, 'result': 'clean site'}, 'Fortinet': {'detected': False, 'result': 'clean site'}, 'alphaMountain.ai': {'detected': False, 'result': 'clean site'}, 'Lionic': {'detected': False, 'result': 'clean site'}, 'Cyble': {'detected': False, 'result': 'clean site'}, 'Seclookup': {'detected': False, 'result': 'clean site'}, 'Virusdie External Site Scan': {'detected': False, 'result': 'clean site'}, 'Artists Against 419': {'detected': False, 'result': 'clean site'}, 'Google Safebrowsing': {'detected': False, 'result': 'clean site'}, 'SafeToOpen': {'detected': False, 'result': 'unrated site'}, 'ADMINUSLabs': {'detected': False, 'result': 'clean site'}, 'ESTsecurity': {'detected': False, 'result': 'clean site'}, 'Juniper Networks': {'detected': False, 'result': 'clean site'}, 'Heimdal Security': {'detected': False, 'result': 'clean site'}, 'AutoShun': {'detected': False, 'result': 'unrated site'}, 'Trustwave': {'detected': False, 'result': 'clean site'}, 'AICC (MONITORAPP)': {'detected': False, 'result': 'clean site'}, 'CyRadar': {'detected': False, 'result': 'clean site'}, 'Dr.Web': {'detected': False, 'result': 'clean site'}, 'Emsisoft': {'detected': False, 'result': 'clean site'}, 'Abusix': {'detected': False, 'result': 'clean site'}, 'Webroot': {'detected': False, 'result': 'clean site'}, 'Avira': {'detected': False, 'result': 'clean site'}, 'securolytics': {'detected': False, 'result': 'clean site'}, 'Antiy-AVL': {'detected': False, 'result': 'clean site'}, 'Acronis': {'detected': False, 'result': 'clean site'}, 'Quick Heal': {'detected': False, 'result': 'clean site'}, 'URLQuery': {'detected': False, 'result': 'clean site'}, 'Viettel Threat Intelligence': {'detected': False, 'result': 'clean site'}, 'DNS8': {'detected': False, 'result': 'clean site'}, 'benkow.cc': {'detected': False, 'result': 'clean site'}, 'EmergingThreats': {'detected': False, 'result': 'clean site'}, 'Chong Lua Dao': {'detected': False, 'result': 'clean site'}, 'Yandex Safebrowsing': {'detected': False, 'result': 'clean site', 'detail': 'http://yandex.com/infected?l10n=en&url=http://www.yahoo.com/'}, 'Lumu': {'detected': False, 'result': 'unrated site'}, 'Kaspersky': {'detected': False, 'result': 'clean site'}, 'Sucuri SiteCheck': {'detected': False, 'result': 'clean site'}, 'desenmascara.me': {'detected': False, 'result': 'clean site'}, 'URLhaus': {'detected': False, 'result': 'clean site'}, 'PREBYTES': {'detected': False, 'result': 'clean site'}, 'StopForumSpam': {'detected': False, 'result': 'clean site'}, 'Blueliv': {'detected': False, 'result': 'clean site'}, 'Netcraft': {'detected': False, 'result': 'unrated site'}, 'ZeroCERT': {'detected': False, 'result': 'clean site'}, 'Phishing Database': {'detected': False, 'result': 'clean site'}, 'MalwarePatrol': {'detected': False, 'result': 'clean site'}, 'Sangfor': {'detected': False, 'result': 'clean site'}, 'IPsum': {'detected': False, 'result': 'clean site'}, 'Malwared': {'detected': False, 'result': 'clean site'}, 'BitDefender': {'detected': False, 'result': 'clean site'}, 'GreenSnow': {'detected': False, 'result': 'clean site'}, 'G-Data': {'detected': False, 'result': 'clean site'}, 'Cyan': {'detected': False, 'result': 'unrated site'}, 'VIPRE': {'detected': False, 'result': 'unrated site'}, 'SCUMWARE.org': {'detected': False, 'result': 'clean site'}, 'PhishFort': {'detected': False, 'result': 'unrated site'}, 'malwares.com URL checker': {'detected': False, 'result': 'clean site'}, 'Forcepoint ThreatSeeker': {'detected': False, 'result': 'clean site'}, 'Certego': {'detected': False, 'result': 'clean site'}, 'ESET': {'detected': False, 'result': 'clean site'}, 'Threatsourcing': {'detected': False, 'result': 'clean site'}, 'MalSilo': {'detected': False, 'result': 'clean site'}, 'Nucleon': {'detected': False, 'result': 'clean site'}, 'ThreatHive': {'detected': False, 'result': 'clean site'}, 'Bfore.Ai PreCrime': {'detected': False, 'result': 'clean site'}}}
Data_URL_vrusTotal={'scan_id': 'adfa08ed6abba9d43c0f0469cbbcfa5362421f0f13ee77c8d14a8e4a668b05be-1671891529', 'resource': 'rarible.fan', 'url': 'http://rarible.fan/', 'response_code': 1, 'scan_date': '2022-12-24 14:18:49', 'permalink': 'https://www.virustotal.com/gui/url/adfa08ed6abba9d43c0f0469cbbcfa5362421f0f13ee77c8d14a8e4a668b05be/detection/u-adfa08ed6abba9d43c0f0469cbbcfa5362421f0f13ee77c8d14a8e4a668b05be-1671891529', 'verbose_msg': 'Scan finished, scan information embedded in this object', 'filescan_id': None, 'positives': 1, 'total': 90, 'scans': {'Bkav': {'detected': False, 'result': 'unrated site'}, 'CMC Threat Intelligence': {'detected': False, 'result': 'clean site'}, 'Snort IP sample list': {'detected': False, 'result': 'clean site'}, 'VX Vault': {'detected': False, 'result': 'clean site'}, 'ViriBack': {'detected': False, 'result': 'clean site'}, 'Comodo Valkyrie Verdict': {'detected': False, 'result': 'unrated site'}, 'PhishLabs': {'detected': False, 'result': 'unrated site'}, 'K7AntiVirus': {'detected': False, 'result': 'clean site'}, 'CINS Army': {'detected': False, 'result': 'clean site'}, 'Quttera': {'detected': False, 'result': 'clean site'}, 'BlockList': {'detected': False, 'result': 'clean site'}, 'PrecisionSec': {'detected': False, 'result': 'unrated site'}, 'OpenPhish': {'detected': False, 'result': 'clean site'}, '0xSI_f33d': {'detected': False, 'result': 'unrated site'}, 'Feodo Tracker': {'detected': False, 'result': 'clean site'}, 'Web Security Guard': {'detected': False, 'result': 'clean site'}, 'Scantitan': {'detected': False, 'result': 'clean site'}, 'AlienVault': {'detected': False, 'result': 'clean site'}, 'Sophos': {'detected': False, 'result': 'clean site'}, 'Phishtank': {'detected': False, 'result': 'clean site'}, 'CyberCrime': {'detected': False, 'result': 'clean site'}, 'Spam404': {'detected': False, 'result': 'clean site'}, 'SecureBrain': {'detected': False, 'result': 'clean site'}, 'Hoplite Industries': {'detected': False, 'result': 'clean site'}, 'CRDF': {'detected': False, 'result': 'clean site'}, 'Rising': {'detected': False, 'result': 'clean site'}, 'Fortinet': {'detected': False, 'result': 'clean site'}, 'alphaMountain.ai': {'detected': False, 'result': 'clean site'}, 'Lionic': {'detected': False, 'result': 'clean site'}, 'Cyble': {'detected': False, 'result': 'clean site'}, 'Seclookup': {'detected': False, 'result': 'clean site'}, 'Virusdie External Site Scan': {'detected': False, 'result': 'clean site'}, 'Artists Against 419': {'detected': False, 'result': 'clean site'}, 'Google Safebrowsing': {'detected': False, 'result': 'clean site'}, 'SafeToOpen': {'detected': False, 'result': 'unrated site'}, 'ADMINUSLabs': {'detected': False, 'result': 'clean site'}, 'ESTsecurity': {'detected': False, 'result': 'clean site'}, 'Juniper Networks': {'detected': False, 'result': 'clean site'}, 'Heimdal Security': {'detected': False, 'result': 'clean site'}, 'AutoShun': {'detected': False, 'result': 'unrated site'}, 'Trustwave': {'detected': False, 'result': 'clean site'}, 'AICC (MONITORAPP)': {'detected': False, 'result': 'clean site'}, 'CyRadar': {'detected': False, 'result': 'clean site'}, 'Dr.Web': {'detected': False, 'result': 'clean site'}, 'Emsisoft': {'detected': False, 'result': 'clean site'}, 'Abusix': {'detected': False, 'result': 'clean site'}, 'Webroot': {'detected': False, 'result': 'clean site'}, 'Avira': {'detected': False, 'result': 'clean site'}, 'securolytics': {'detected': False, 'result': 'clean site'}, 'Antiy-AVL': {'detected': False, 'result': 'clean site'}, 'Acronis': {'detected': False, 'result': 'clean site'}, 'Quick Heal': {'detected': False, 'result': 'clean site'}, 'URLQuery': {'detected': False, 'result': 'unrated site'}, 'Viettel Threat Intelligence': {'detected': False, 'result': 'clean site'}, 'DNS8': {'detected': False, 'result': 'clean site'}, 'benkow.cc': {'detected': False, 'result': 'clean site'}, 'EmergingThreats': {'detected': False, 'result': 'clean site'}, 'Chong Lua Dao': {'detected': False, 'result': 'clean site'}, 'Yandex Safebrowsing': {'detected': False, 'result': 'clean site', 'detail': 'http://yandex.com/infected?l10n=en&url=http://rarible.fan/'}, 'Lumu': {'detected': False, 'result': 'unrated site'}, 'Kaspersky': {'detected': False, 'result': 'unrated site'}, 'Sucuri SiteCheck': {'detected': False, 'result': 'clean site'}, 'desenmascara.me': {'detected': False, 'result': 'clean site'}, 'URLhaus': {'detected': False, 'result': 'clean site'}, 'PREBYTES': {'detected': False, 'result': 'clean site'}, 'StopForumSpam': {'detected': False, 'result': 'clean site'}, 'Blueliv': {'detected': False, 'result': 'clean site'}, 'Netcraft': {'detected': False, 'result': 'unrated site'}, 'ZeroCERT': {'detected': False, 'result': 'clean site'}, 'Phishing Database': {'detected': False, 'result': 'clean site'}, 'MalwarePatrol': {'detected': False, 'result': 'clean site'}, 'Sangfor': {'detected': False, 'result': 'clean site'}, 'IPsum': {'detected': False, 'result': 'clean site'}, 'Malwared': {'detected': False, 'result': 'clean site'}, 'BitDefender': {'detected': False, 'result': 'clean site'}, 'GreenSnow': {'detected': False, 'result': 'clean site'}, 'G-Data': {'detected': False, 'result': 'clean site'}, 'Cyan': {'detected': False, 'result': 'unrated site'}, 'VIPRE': {'detected': False, 'result': 'unrated site'}, 'SCUMWARE.org': {'detected': False, 'result': 'clean site'}, 'PhishFort': {'detected': True, 'result': 'malicious site'}, 'malwares.com URL checker': {'detected': False, 'result': 'clean site'}, 'Forcepoint ThreatSeeker': {'detected': False, 'result': 'unrated site'}, 'Certego': {'detected': False, 'result': 'clean site'}, 'ESET': {'detected': False, 'result': 'clean site'}, 'Threatsourcing': {'detected': False, 'result': 'clean site'}, 'MalSilo': {'detected': False, 'result': 'clean site'}, 'Nucleon': {'detected': False, 'result': 'clean site'}, 'ThreatHive': {'detected': False, 'result': 'clean site'}, 'Bfore.Ai PreCrime': {'detected': False, 'result': 'clean site'}}}

#Who Is XML
DataUrlWhoIsXMLB={'ip': '74.6.143.25', 'location': {'country': 'US', 'region': 'New York', 'city': 'East Village', 'lat': 40.72927, 'lng': -73.98736, 'postalCode': '', 'timezone': '-05:00', 'geonameId': 5116093}, 'domains': ['media-router-fp73.prod.media.vip.bf1.yahoo.com', 'yahoo.com', 'pmvcoin.app', 'atsv2-fp-shed.wg1.b.yahoo.com', 'charpunk.com'], 'as': {'asn': 26101, 'name': 'YAHOO-BF1', 'route': '74.6.143.0/24', 'domain': '', 'type': ''}, 'isp': 'Oath Holdings Inc.', 'connectionType': ''}
Data_URL_Whois_XML={'ip': '172.173.198.6', 'location': {'country': 'US', 'region': 'Virginia', 'city': 'Washington', 'lat': 38.71345, 'lng': -78.15944, 'postalCode': '22747', 'timezone': '-05:00', 'geonameId': 4792307}, 'domains': ['home-kyberswap-com.net', 'raribleaccess.org', 'rariblelogin.site', 'rariblemarketplace.net', 'homerarible.org'], 'as': {'asn': 8075, 'name': 'MICROSOFT-CORP-MSN-AS-BLOCK', 'route': '172.160.0.0/11', 'domain': '', 'type': 'Content'}, 'isp': 'Microsoft', 'connectionType': ''}

#DataRed1
#Red="66.240.205.0/24"

#DataRed2
Red="89.248.163.0/24"
DataRed1=ConsultaDeREDAbuseDb(Red)
with open("DataRed2.txt", "w") as IPQ:
    IPQ.write(str(DataRed1))
    IPQ.close()

DataRed2={'data': {'networkAddress': '66.240.205.0', 'netmask': '255.255.255.0', 'minAddress': '66.240.205.1', 'maxAddress': '66.240.205.254', 'numPossibleHosts': 254, 'addressSpaceDesc': 'Internet', 'reportedAddress': [{'ipAddress': '66.240.205.34', 'numReports': 1924, 'mostRecentReport': '2022-12-27T23:45:30+00:00', 'abuseConfidenceScore': 100, 'countryCode': 'US'}]}}
     
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

Listas_DeReportes(DataRed2=DataRed1)