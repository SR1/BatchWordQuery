#!/usr/bin/python
# Filename: beidanci.py

import httplib
import urllib
import time
import json
import HTMLParser
import sys

def noHTML(line):
    return HTMLParser.HTMLParser().unescape(line)

def getWord(keyword):
    host = r"""dict.qq.com"""
    path = '/dict?q='+keyword
    h = httplib.HTTPConnection(host,80)
    h.request('GET', path)#, params)
    result = h.getresponse().read()
    result = json.loads(result)
    word = keyword
    pron = ''
    mean = "can't find the word's meaning"
    if result.get('local')!=None :
        word = result['local'][0]['word']
        if result['local'][0].get('pho')!=None :
            pron = '['+noHTML(result['local'][0]['pho'][0])+']'
        mean = ''
        for m in result['local'][0]['des']:
            if m.get('p')!=None :
                mean += noHTML(m['p'])
                mean += ' '
                if reciteMode :
                    print noHTML(m['p']),
            if m.get('d')!=None :
                mean += noHTML(m['d'])
                mean += '   '
                if reciteMode :                
                    print noHTML(m['d'])
        if reciteMode :  
            print pron
        if reciteMode :
            while True:
                ans = raw_input('This word is:')
                if ans == keyword :
                    print 'Well done, Lawrence'
                    break
                else :
                    print 'Try again~'
    return (word, pron, mean)

today = time.strftime('%Y%m%d',time.localtime(time.time()))

if len(sys.argv)!=1 :
    reciteMode = False
    while True:
        choice = raw_input('If you want to enter recite mode?\nPlese enter yes or no to continue :')
        if choice == 'yes':
            reciteMode = True
            break
        elif choice == 'no':
            break
    inputFile = sys.argv[1];
    inputFilename = sys.argv[1].split('/')[-1].split('.')[0]
    outputFile = './buildList/'+inputFilename+'_test@'+today+'.txt'
    fin = open(inputFile, 'rU')
    fout = open(outputFile,'w')
    for line in fin :
        word = getWord(line.replace('\n',''))
        fout.write(word[0])
        fout.write(word[1].encode('UTF-8'))
        fout.write(word[2].encode('UTF-8'))
        fout.write('\n')
        print ''
        print ''
        print ''
        print word[0],
        print word[1],
        print word[2].encode('UTF-8')
        print ''
        print ''
        print ''
    fin.close()
    fout.close()
else:
    print """You haven't offer a file path"""
