#!/usr/bin/env python
from fioresult import fioresult

if __name__ == "__main__":
   f = fioresult.ResultApi("/home/wangchen/18.01/")
   #print f.check_results() 
   #print f.get_iops() 
   #print f.get_latency() 
   print f.get_p99() 
