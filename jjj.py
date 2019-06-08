
from bs4 import BeautifulSoup
customattr="""<p data-custom="custom">custom attribute
example</p>"""
customSoup = BeautifulSoup(customattr,features="html.parser")
using_attrs = customSoup.find(attrs={'data-custom':'custom'})
print(using_attrs)

