#!/usr/bin/env python

import sys
import json
import urllib2

"""
dict - Chinese/English Translation
@author zhangpeng(244267727@qq.com)
@date   2015.01.28

"""

class Dict:
    key = '511917621'
    keyFrom = 'zangdls'
    api = 'http://fanyi.youdao.com/openapi.do?keyfrom=zangdls&key=511917621&type=data&doctype=json&version=1.1&q='
    content = None

    def __init__(self, argv):
        if len(argv) >= 1:
        	for i in range(1, len(argv)) :
        		self.api = self.api + ' ' +  argv[i]
        	self.translate()
        else:
            print 'ERROR'

    def translate(self):
        content = urllib2.urlopen(self.api).read()
        self.content = json.loads(content)
        self.parse()

    def parse(self):
        code = self.content['errorCode']
        if code == 0:  # Success
            try:
                u = self.content['basic']['us-phonetic']
                e = self.content['basic']['uk-phonetic']
                explains = self.content['basic']['explains']
            except KeyError:
                u = 'None'
                e = 'None'
                explains = 'None'
            print '\033[1;31m################################### \033[0m'
            print '\033[1;31m# \033[0m', self.content['query'], self.content['translation'][0], '(U:', u, 'E:', e, ')'
            if explains != 'None':
                for i in range(0, len(explains)):
                    print '\033[1;31m# \033[0m', explains[i]
            else:
                print '\033[1;31m# \033[0m Explains None'
            print '\033[1;31m################################### \033[0m'
        elif code == 20:  # Text too long

            print 'WORD TOO LONG'
        elif code == 30:  # Trans error
            print 'TRANSLATE ERROR'
        elif code == 40:  # Don't support this language
            print 'CAN\'T SUPPORT THIS LANGUAGE'
        elif code == 50:  # Key failed
            print 'KEY FAILED'
        elif code == 60:  # Don't have this word
            print 'DO\'T HAVE THIS WORD'

if __name__ == '__main__':
    Dict(sys.argv)
