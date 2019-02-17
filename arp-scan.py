try:
    import subprocess
    from subprocess import check_output
    import shlex
    from shlex import split
    import getpass
    from collections import OrderedDict
    from itertools import zip_longest
    from collections import namedtuple
    import mysql.connector
    import datetime
    import time
except ImportError:
    import sys
    sys.exit("USE PYTHON3")

def main():
    print('Script start')

    arp_cmd = 'arp-scan -l | awk '$3 ~ /TP-LINK/''

    process = subprocess.Popen(shlex.split(arp_cmd), stdout=subprocess.PIPE)
    out = process.communicate()[0]
    print(out)



if __name__ == "__main__":
    main()