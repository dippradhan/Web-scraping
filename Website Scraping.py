from urllib.request import urlopen

html = urlopen('https://www.opentable.com.au')

html = urlopen('https://www.opentable.com.au/r/bartronica-melbourne?originId=673e8484-cf1d-465c-9135-c7e92c737efe&corrid=673e8484-cf1d-465c-9135-c7e92c737efe&avt=eyJ2IjoyLCJtIjoxLCJwIjowLCJzIjowLCJuIjowfQ')
print(html.read())



from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen('https://www.opentable.com.au')
html = urlopen('https://www.opentable.com.au/r/di-stasio-carlton?originId=8ca2c2d9-f839-499b-850e-942daee18e1e&corrid=8ca2c2d9-f839-499b-850e-942daee18e1e&avt=eyJ2IjoyLCJtIjoxLCJwIjowLCJzIjowLCJuIjowfQ')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.title)


print(len('https://www.opentable.com.au/r/di-stasio-carlton?originId=8ca2c2d9-f839-499b-850e-942daee18e1e&corrid=8ca2c2d9-f839-499b-850e-942daee18e1e&avt=eyJ2IjoyLCJtIjoxLCJwIjowLCJzIjowLCJuIjowfQ'))

from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
html = urlopen('https://www.opentable.com.au/lolz-view-all/H4sIAAAAAAAA_6tWMlKyUjIyMDLWNTDXNTIKMTK0MrK0MjBQ0lEyRpEBCpiABAytjA0g8qZKVkY6SmZAQV1jcz0LQ1NLHUMTEz1LMzNLoKwFUDzANSjY38_RxzPKNSg-MNQ1KBIoYQmUUHYsS8zMSUzKSXXLL3LJzMtLLfLLLwdKGgItjY4F0kC70hJzilNrAWfjHymiAAAA?originid=75538397-1cb2-4e5d-b23d-90810ed8e7de')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        #print(link.attrs['href'])
        if len(link.attrs['href'])>150 :
            #print(link.attrs['href'])
            html = urlopen(link.attrs['href'])
            bs = BeautifulSoup(html.read(), 'html.parser')
            arddress = bs.find("meta", property="business:contact_data:street_address")
            phone = bs.find("meta", property="business:contact_data:phone_number")
            print(bs.title)
            print(arddress)
            print(phone)




from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen('https://www.opentable.com.au')
html = urlopen('https://www.opentable.com.au/r/di-stasio-carlton?originId=8ca2c2d9-f839-499b-850e-942daee18e1e&corrid=8ca2c2d9-f839-499b-850e-942daee18e1e&avt=eyJ2IjoyLCJtIjoxLCJwIjowLCJzIjowLCJuIjowfQ')
bs = BeautifulSoup(html.read(), 'html.parser')
#print(bs.)

address = bs.find("meta", property="business:contact_data:street_address")
phone = bs.find("meta", property="business:contact_data:phone_number")

print(phone)


url = bs.find("meta", property="og:url")

print(title["content"] if title else "No meta title given")
print(url["content"] if url else "No meta url given")






from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen('http://pythonscraping.com/'
                  'pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()











