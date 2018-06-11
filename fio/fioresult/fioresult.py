import re
import os

class ResultApi(object):
    """
    API for getting the fio results include IOPS, latency,
    p99 and so on
    """
    def __init__(self, path):
        self.path = path

    def get_iops(self):
        pass

    def get_latency(self):
        pass

    def get_p99(self):
        pass

    def check_results(self):
        """
        Check fio results status
        Return: all passed return 0
                else return list about filenames
        """
        err = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                try:
                    with open(os.path.join(root, file),'r') as f:
                        if "err= 0" not in f.read():
                            err.append(file)
                        else:
                            continue
                except IOError:
                    print("Open file filed with {0}".format(file))
        if len(err) == 0:
            return 0
        else:
            return err
    
        print("Path is", self.path)
