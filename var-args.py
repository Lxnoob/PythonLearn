# -*- coding: utf-8 -*-

def Hello(gretting,*arg):
    if (len(arg) == 0):
        print('%s!' % gretting)
    else:
        print('%s！,%s.' % (gretting,','.join(arg)))

Hello('Hi')
Hello('Hi','liu')
Hello('Hi','liu','xuan')
number = ('Hi','liu','xuan')
Hello('Hi',*number)
