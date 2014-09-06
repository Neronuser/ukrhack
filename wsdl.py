# -*- coding: utf-8 -*-
__author__ = 'roman'
import random
import codecs
import xml.etree.ElementTree as ET
from suds.client import Client

f = codecs.open("tmp.xml","w+",'utf-8')
client = Client("http://testwl.irc.gov.ua:7003/EDRAPI/ws?WSDL")
#f.write(client.service.plsqlSearchByCode("177", 2, "10000035", "10000035", None ,None))
"""tree = ET.parse('U7.xml')
root = tree.getroot()
for name in root.iter('NAME'):
    for value in name.attrib.values():
        if (value == u"Назва КВЕД"):
            print(name.text)
for name in root.iter('ATU_NAME'):
    for value in name.attrib.values():
        print(name.text)"""

for i in range(10):
    for j in range(10):
        for k in range(10):
            strtry = client.service.plsqlSearchByCode(str(i) + str(j) + str(k) + "177", 2, "10000035", "10000035", None ,None)
            if '.</ERROR>' in strtry :
                print(str(i) + str(j) + str(k))
            else:
                f = codecs.open("tr/tr3/U" + str(i) + str(j) + str(k) + "177" + ".xml","w+",'utf-8')
                f.write(strtry)
  #          f = codecs.open("tr/tr2/" + str(i) + str(j) + str(k) + ".xml","w+",'utf-8')
#            f.write(client.service.plsqlSearchByCode("177" + str(i) + str(j) + str(k), 2, "10000035", "10000035", None ,None))




