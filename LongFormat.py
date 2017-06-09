# -*- coding: utf-8 -*-
"""
"Python Data Science Handbook" for reference:
http://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb
"""

import os

path = './data/'
filelist = os.listdir(path)

listings = dict()
dates = dict()
n = 0

def dictify(e, n, d=listings, dates=dates):
    #print(e)

    if e[10] not in d: 
        #d[e[10]] = {lat: e[6], lng: e[7], date: e[2]} 
        d[e[10]] = {'lat': e[6], 'lng': e[7], 'firstdate': e[2], 'lastdate': e[2]} 
        d[e[10]]['datecount'] = 1 
        d[e[10]]['datelist'] = [e[2]] 

        if e[2] not in dates: 
            dates[e[2]] = {'count': 1, 'num': n} 
            print(n)
        else: 
            dates[e[2]]['count'] += 1 
        
    else: 
        if d[e[10]]['lastdate'] != e[2]: 
            d[e[10]]['datecount'] += 1 
            d[e[10]]['datelist'].append(e[2]) 

        d[e[10]]['lastdate'] = e[2] 
    return d, dates # Return dictionary with counts 

for file in filelist:
    if '.csv' in file:
        with open(path+file, 'rb') as datalines:
            n += 1
            for line in datalines:
                for r in ['\n','\r']:
                    line=line.replace(r,'')
                e = line.split(',')
                e[2] = file[0:10]
                #print(e)
                if 'F' in str(e[11]): e[11] = False
                #if 'TRUE' in str(e[11]): e[11] = True
                e[17] = e[17].split('?', 1)[0]
                if 'vapeshops' in e[18] and e[11] is False: 
                    dictify(e, n)
    
