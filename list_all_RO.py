"""
A module for determining the specific currency code (R0) used to determine the dynamics of exchange rates.
The data is applied in the module all_currency.py.
"""
from xml.etree import ElementTree
import urllib.request

url = 'http://www.cbr.ru/scripts/XML_val.asp?d=0'
document = urllib.request.urlopen(url).read()
tree = ElementTree.fromstring(document)


lst_all_values_currency = []
for currency in tree.findall('Item'):
    Name = currency.find('Name').text
    EngName = currency.find('EngName').text
    Nominal = currency.find('Nominal').text
    ParentCode = currency.find('ParentCode').text.rstrip()
    tpl = (Name, EngName, Nominal, ParentCode)
    lst_all_values_currency.append(tpl)
