#Q1

import re
import csv
 
name = []
degree = []
title = []
email = []
 
with open('/Users/williamstokvis/ds/metis/metisgh/prework/dsp/python/faculty.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        name.append(row[0])
        degree.append(row[1])
        title.append(row[2])
        email.append(row[3])
        
counts = {}
phdRegx = re.compile(r'ph\.?d',re.I)
phdlist = list(filter(phdRegx.search, degree))
counts['PH.D'] =len(phdlist)

scdRegx = re.compile(r'sc\.?d',re.I)
scdlist = list(filter(scdRegx.search, degree))
counts['Sc.D'] =len(scdlist)

mdRegx = re.compile(r'm\.?d',re.I)
mdlist = list(filter(mdRegx.search, degree))
counts['M.D'] =len(mdlist)

mphRegx = re.compile(r'mph',re.I)
mphlist = list(filter(mphRegx.search, degree))
counts['MPH'] =len(mphlist)

bsedRegx = re.compile(r'b\.s\.ed',re.I)
bsedlist = list(filter(bsedRegx.search, degree))
counts['B.S.Ed'] =len(bsedlist)

msRegx = re.compile(r'm\.?s',re.I)
mslist = list(filter(msRegx.search, degree))
counts['MS'] =len(mslist)

jdRegx = re.compile(r'j\.?d',re.I)
jdlist = list(filter(jdRegx.search, degree))
counts['J.D.'] =len(jdlist)

maRegx = re.compile(r'ma',re.I)
malist = list(filter(maRegx.search, degree))
counts['M.A.'] =len(malist)
counts
