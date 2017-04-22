from lxml import etree
from StringIO import StringIO
from datetime import datetime
import xlsxwriter
 
#----------------------------------------------------------------------
def parseXML(xmlFile):
 
    f = open(xmlFile)
    xml = f.read()
    f.close()

    tree = etree.parse(StringIO(xml))
    print tree.docinfo.doctype
    context = etree.iterparse(StringIO(xml))
    product_dict = {}
    products = []
    for action, elem in context:
        if not elem.text:
            text = "None"
            pass
        else:
            text = elem.text
            print elem.tag + " => " + text
        product_dict[elem.tag] = text
        if elem.tag == "list-item":
            products.append(product_dict)
            product_dict = {}

    return products
    
if __name__ == "__main__":
    parseXML("deneme.xml")
    