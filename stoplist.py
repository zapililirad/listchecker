#!/usr/bin/env python

import rstr, requests, csv

proxies = {'http': 'http://sbnix1:12345678@proxy.roseurobank.ru:3128/',
           'https': 'https://sbnix1:12345678@proxy.roseurobank.ru:3128/'}

def check_site(url):
    try:
        r = requests.get(url, proxies=proxies, timeout=(3.05, 15))
        print 'Test ' + url + ' --> ' + str(r.status_code)
        return r.status_code
    except Exception as e:
        print 'Test ' + url + ' --> ' + str(e.message)
        return str(e.message)


#pattern = "adobbe\.info"
#url = "http://" + rstr.xeger(pattern)
#check_site(url)
stats = []

with open("C:/temp/stop_global.txt", "r") as file:
    for line in file.readlines():
        response = check_site("http://" + line[1:].replace("\n",""))
        stats.append({'response': response, 'site': line.replace("\n","")})

with open('C:/temp/stop_global.csv', "w") as out_file:
    writer = csv.DictWriter(out_file, delimiter=';', fieldnames=stats[0].keys(), lineterminator='\n')
    writer.writeheader()
    for row in stats:
        writer.writerow(row)