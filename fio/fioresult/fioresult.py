import re
import os

class ResultApi(object):
    """
    API for getting the fio results include IOPS, latency,
    p99 and so on
    """
    def __init__(self, path):
        self.files = []
        self.path = path
        for root, dirs, files in os.walk(self.path):
            for file in files:
                self.files.append(os.path.join(root, file))

    def get_iops(self):
        """
        Get iops results 
        Return: return dict key is file name, value is a list about iops
        """
        iops = {}
        for file in self.files:
            key = os.path.split(file)[-1]
            try :
                with open(file, 'r') as f:
                    iops[key] = re.findall("IOPS=(.*), BW", f.read())
            except IOError:
                print("Open file filed with {0}".format(file))
                return -1
        return iops

    def get_latency(self):
        """
        Get latency results
        Return: return dict key is file name, value is a list about latency(usec)
        """
        latency = {}
        for file in self.files:
            key = os.path.split(file)[-1]
            try:
                with open(file, 'r') as f:
                    lat_usec = [int(float(i)) for i in re.findall("lat \(usec\):.*avg=([0-9]*\.[0-9]*)", f.read())]
                    lat_msec = [int(float(i)*1000) for i in re.findall("lat \(msec\):.*avg=([0-9]*\.[0-9]*)", f.read())]
                    lat_msec.extend(lat_usec)
                    latency[key] = lat_msec
            except IOError:
                print("Open file filed with {0}".format(file))
                return -1
        return latency

    def get_p99(self):
        """
        Get P99 results
        Return: return dict key is file name, value is a list about P99(usec)
        """
        P99 = {}
        for file in self.files:
            key = os.path.split(file)[-1]
            try:
                with open(file, 'r') as f:
                    p99_usec =  [int(float(i)) for i in re.findall("clat percentiles \(usec\):\s.*\s.*\s.*\s.*99.00th=\[ (.*)\], 99.50th", f.read())]
                    p99_msec =  [int(float(i)*1000) for i in re.findall("clat percentiles \(msec\):\s.*\s.*\s.*\s.*99.00th=\[ (.*)\], 99.50th", f.read())]
                    p99_msec.extend(p99_usec)
                    P99[key] = p99_msec
            except IOError:
                print("Open file filed with {0}".format(file))
                return -1
        return P99



    def check_results(self):
        """
        Check fio results status
        Return: all passed return 0
                else return list about filenames
        """
        err = []
        for file in self.files:
            try:
                with open(file,'r') as f:
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
    
