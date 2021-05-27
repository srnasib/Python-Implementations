import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1241461.xml"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
total=0
results = tree.findall('comments/comment') 
print ('User count:', len (results)) 
for item in results: 
    print (item.find('name').text) 
    print (item.find('count').text) 
    total=total+(int(item.find('count').text))

print('Total Sum :', total)  
    
    

    
    




