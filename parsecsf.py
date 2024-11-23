# Import CIE Lab data from X-Rite CxF – Color Exchange Format to csv
#
import xml.etree.ElementTree as ET

inputFile = 'democxf.cxf'
outputFile = 'demo.csv'

# declare the namespaces:
ns = {'cc': 'http://colorexchangeformat.com/CxF3-core',
      'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

tree = ET.parse(inputFile)
root = tree.getroot()

out = open(outputFile, "w")

for r in root.findall("cc:Resources", ns):
    for oc in r.findall("cc:ObjectCollection", ns):
        for o in oc.findall("cc:Object", ns):
            s = o.attrib['Name']
            #print(s)
            cv = o.find("cc:ColorValues", ns)
            cie = cv.find("cc:ColorCIELab", ns)
            #print(cie.attrib['ColorSpecification'])
            l = cie.find("cc:L", ns).text
            a = cie.find("cc:A", ns).text
            b = cie.find("cc:B", ns).text
            s = s + "," + l + "," + a + "," + b
            print(s)
            out.write(s + "\n")

out.close()

             

