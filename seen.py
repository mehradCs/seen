#/usr/bin
#by alpha leader
#tel : @the_farzin_hacking
import requests
print ("""
	******WELCOME TO SEENER***********
	******TELEGRAM : @alpha_leader******
	******channel : @the_farzin_hacking****
	******************************************
""")
proxyfile = input("proxy address>>>")
site_url = input("url>>>")
a = 0
try:
    proxyfile = open(proxyfile, "r")
except:
    print("File not found")
    quit()
proxyfile = [el.replace('\n',' ') for el in proxyfile]
for i in proxyfile:
    try:
        requests.get(site_url, proxies = {'http':'http://'+proxyfile[a]})
        print("Available proxy: {}".format(proxyfile[a]))
    except:
        print("proxy isn't available")
    a += 1
