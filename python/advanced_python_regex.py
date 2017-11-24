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

#Q2
titleCounts = {}
profRegx = re.compile(r'Professor',re.I)
proflist = list(filter(profRegx.match, title))
titleCounts['Professors'] =len(proflist)

assocprofRegx = re.compile(r'Associate',re.I)
assocproflist = list(filter(assocprofRegx.match, title))
titleCounts['Associate Professors'] =len(assocproflist)

assistprofRegx = re.compile(r'Assistant',re.I)
assistproflist = list(filter(assistprofRegx.match, title))
titleCounts['Assistant Professors'] =len(assistproflist)

titleCounts

#Q3 
email[1:]

#Q4

emailCounts = {}
mailmedRegx = re.compile(r'@mail\.med\.upenn\.edu',re.I)
mailmedlist = list(filter(mailmedRegx.search, email))
emailCounts['Mail Med UPenn'] =len(mailmedlist)

ccebmedRegx = re.compile(r'@cceb\.med\.upenn\.edu',re.I)
ccebmedlist = list(filter(ccebmedRegx.search, email))
emailCounts['CCEB Med UPenn'] =len(ccebmedlist)

upennRegx = re.compile(r'@upenn\.edu',re.I)
upennlist = list(filter(upennRegx.search, email))
emailCounts['UPenn'] =len(upennlist)

chopRegx = re.compile(r'@email\.chop\.edu',re.I)
choplist = list(filter(chopRegx.search, email))
emailCounts['Chop'] =len(choplist)

emailCounts