import json
#import pprintpp 
import urllib.request
import urllib
import re
import requests 

#__________________________________
def pxxobterlocal():
    r = ''
    localizacao = ''
    accuweatherapikey = 'U2fOxu3wnT1C9N20N40KqfG0w2TlaATv'
   
    r = requests.get('http://www.geoplugin.net/json.gp')
    if r.status_code == 200:
        localizacao = json.loads(r.text)
        pxximplocalizacao(json.loads(r.text))
        lat = localizacao['geoplugin_latitude']
        lon = localizacao['geoplugin_longitude']
        print('lat:{}'.format(lat))
        print('lon:{}'.format(lon))
        
        
    else:
        print('Não foi possivel obter a localização') 

#_________________________________
def pxximplocalizacao(localizacao):
    for key in localizacao:
        print(key, ' : ', localizacao[key])

#__________________________________
def pxxobterip():

    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)

#___________________________________
def pxxget_external_ip():
    
    site = urllib.urlopen("http://checkip.dyndns.org/").read()
    grab = re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
    address = grab[0]
    return address

    # if __== '__main__':
    #   print( get_external_ip() )

#___________________________________
pxxobterlocal()
#pxxobterip()
# a = pxxget_external_ip()
# print(a)
# x=1
