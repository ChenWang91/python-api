#!/usr/bin/env python
from fioresult import fioresult

if __name__ == "__main__":
   f = fioresult.ResultApi("/home/wangchen/performance/test/4k/18.01/")
   print f.check_results() 
