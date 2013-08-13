#!/usr/bin/python
# Filename: chadanci.py

import httplib
import json

def getWord(keyword):
    host = r"""dict.qq.com"""
    path = '/dict?q='+keyword
    h = httplib.HTTPConnection(host,80)
    h.request('GET', path)
    result = h.getresponse().read()
    result = json.loads(result)
    word = keyword
    pron = ''
    mean = "can't find the word's meaning"
    if result.get('local')!=None :
        word = result['local'][0]['word']
        if result['local'][0].get('pho')!=None :
            pron = '['+result['local'][0]['pho'][0]+']'
        mean = ''
        for m in result['local'][0]['des']:
            if m.get('p')!=None :
                mean += m['p']
                mean += ' '
            if m.get('d')!=None :
                mean += m['d']
                mean += '   '
    return (word, pron, mean)

inputFile = 'list.txt'
outputFile = 'done.txt'
fin = open(inputFile, 'rU')
fout = open(outputFile,'w')
for line in fin :
    word = getWord(line.replace('\n',''))
    fout.write(word[0])
    fout.write(word[1].encode('UTF-8'))
    fout.write(word[2].encode('UTF-8'))
    fout.write('\n')
    print word[0],
    print word[1],
    print word[2].encode('UTF-8')
    print ''
fin.close()
fout.close()

