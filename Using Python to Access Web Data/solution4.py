import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1241462.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
info = json.loads(data)
print(info["comments"])
total=0

print ('User count:', len(info["comments"])) 
for item in info["comments"]:
    print('Name', item['name'])
    print('Count', item['count'])
    total=total+(int(item['count']))

print(info)
print('Total Sum :', total)  
    


