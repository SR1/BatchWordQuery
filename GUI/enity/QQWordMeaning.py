#coding=utf-8
#@Filename: QQWordMeaning.py
#@Author: SR1

import json
import util.html as html

class QQWordMeaning:
    '''Represent a word's meaning get from QQDict'''
    def __init__(self, JsonString):
        '''Init the word's meaning '''
        self.JsonString = JsonString
        self.err = None
        self.word = None
        self.pron = None
        self.meaning = []
        self.parse()
        self.decodeHTML()
    
    def parse(self):
        '''parse the word's meaning from json'''
        result = json.loads(self.JsonString)
        # get error status
        if result.get('err'):
            self.err = result.get('err')
        # get word's meaning
        elif result.get('local')[0]:
            local = result.get('local')[0]
            # get the word store as a string
            if local.get('word'):
                self.word = local.get('word')
            # get pronuciation store as a string
            if local.get('pho')[0]:
                self.pron = "[%s]" % local.get('pho')[0]
            # get definition store as a list
            if local.get('des'):
                des = local.get('des')
                for meaning in des:
                    # definition format
                    means = '%s %s'
                    if meaning.get('p') and meaning.get('d'):
                        self.meaning.append(means % (meaning.get('p'), meaning.get('d')))
                    elif meaning.get('d'):
                        self.meaning.append(means % (meaning.get('d'), ''))

    def decodeHTML(self):
        if self.err:
            self.err = html.HTMLdecode(self.err)
        if self.word:
            self.word = html.HTMLdecode(self.word)
        if self.pron:
            self.pron = html.HTMLdecode(self.pron)
        if self.meaning:
            self.meaning = html.HTMLdecode(self.meaning)
             
