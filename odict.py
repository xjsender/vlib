#!/usr/bin/env python


class odict(dict):
    '''odict is an Object Dictionary.  It subclasses builtin dict object.
    It allows dot (.) syntax.
    
    The the following become equivalent:

        order.book.product_id    same as    order['book']['product_id']
    '''    

    def __setattr__(self, key, value): self[key] = value
    def __getattr__(self, key): return self[key]
    
if __name__ == '__main__':
    #o = odict({'a':1, 2:3})
    o = odict(a=1, b=2)
    print o
    print o.a
    o.b = 4
    print o['b']
    print o
