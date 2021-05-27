# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
total=0
print( tags[17].contents[0])
print( tags[17].get('href', None))

html1 = urlopen((tags[17].get('href', None)), context=ctx).read()
soup1 = BeautifulSoup(html1, "html.parser")
tags1 = soup1('a')
print( tags1[17].contents[0])
print( tags1[17].get('href', None))

html2 = urlopen((tags1[17].get('href', None)), context=ctx).read()
soup2 = BeautifulSoup(html2, "html.parser")
tags2 = soup2('a')
print( tags2[17].contents[0])
print( tags2[17].get('href', None))

html3 = urlopen((tags2[17].get('href', None)), context=ctx).read()
soup3 = BeautifulSoup(html3, "html.parser")
tags3 = soup3('a')
print( tags3[17].contents[0])
print( tags3[17].get('href', None))

html4 = urlopen((tags3[17].get('href', None)), context=ctx).read()
soup4 = BeautifulSoup(html4, "html.parser")
tags4 = soup4('a')
print( tags4[17].contents[0])
print( tags4[17].get('href', None))

html5 = urlopen((tags4[17].get('href', None)), context=ctx).read()
soup5 = BeautifulSoup(html5, "html.parser")
tags5 = soup5('a')
print( tags5[17].contents[0])
print( tags5[17].get('href', None))

html6 = urlopen((tags5[17].get('href', None)), context=ctx).read()
soup6 = BeautifulSoup(html6, "html.parser")
tags6 = soup6('a')
print( tags6[17].contents[0])
print( tags6[17].get('href', None))



##print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
   # print('URL:', tag.get('href', None))
   # print('Contents:', tag.contents[0])
   # print('Attrs:', tag.attrs)