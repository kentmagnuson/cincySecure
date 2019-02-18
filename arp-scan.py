try:
    import subprocess
    from subprocess import check_output
    import shlex
    from shlex import split
    #import getpass
    #from collections import OrderedDict
    #from itertools import zip_longest
    import mysql.connector
    import datetime
    import time
except ImportError:
    import sys
    sys.exit("USE PYTHON3")

def main():
    print('Script start')

    timestamp_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')
    print('Time: ' + timestamp_str)

    arp_cmd = "arp-scan -l | awk '$3 ~ /TP-LINK/'"

    #ENTER SHIT HERE - SQL LOGIN
    db = mysql.connector.connect(user='test', password='test', host='LOCALHOST', database='')
    cursor = db.cursor()

    #ENTER SHIT HERE - SQL COMMANDS
    update_ip = "UPDATE table SET ip = %s"
    update_mac = "UPDATE table SET mac = %s WHERE ip = %s"
    update_name = "UPDATE table SET name = %s WHERE ip = %s"

    process = subprocess.Popen(arp_cmd, shell=True, stdout=subprocess.PIPE)
    out = process.communicate()[0]
    output = out.decode("UTF-8")
    out_split = output.split('\n')
    kent = len(out_split[0].split()) - 1
    for row in out_split[1:]:
        print(row.split(None, kent))
    print(kent)

    dict = {ip: (mac, name) for ip, mac, name in zip(output)}

    if dict != "{}":
        for key, value in dict:
            ip = key[0]
            mac = key[1]
            name = key[2]
            cursor.execute(update_ip, (ip))
            cursor.execute(update_mac, (mac, ip))
            cursor.execute(update_name, (name, ip))
    else:
        print('found nothing')

if __name__ == "__main__":
    main()