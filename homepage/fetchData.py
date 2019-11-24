import urllib2
import requests
import os
from django.conf import settings as globalSettings
from bs4 import BeautifulSoup
urls = ['','about','locations','sitemap','rope-selection','legal-privacy','work-culture','applicationtips']
for u in urls:
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    langlist = ['en','de','zh']
    for i in langlist:
        cookies = {'lang':i}
        url = 'http://192.168.1.5:8000/'+u
        r = requests.get(url,cookies=cookies)
        test = BeautifulSoup(r.text,  'lxml').text
        text = u +'\n' + test.encode('utf-8')
        file = text
        dupFile = open(os.path.join(PROJECT_PATH, 'renderedFiles/'+i+'/'+u+'.html'), 'w')
        dupFile.write(file)
        dupFile.close()

# change the url to the domain url
# run the file to get the search files updated
