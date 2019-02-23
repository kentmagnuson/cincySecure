#PYTHON3
import subprocess
from shlex import split
#import mysql.connect

def main():
    '''db = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database="")
    cursor = db.cursor()'''


    arp_cmd = ['arp-scan', '-l']

    #update_name = "UPDATE TABELNAME SET name = %s"
    #update_ip = "UPDATE TABELNAME SET ip = %s"
    #update_mac = "UPDATE TABELNAME SET ip = %s"

    run_command = subprocess.Popen(arp_cmd, stdout=subprocess.PIPE)
    output_bytes = run_command.communicate()[0]
    output_str = output_bytes.decode("utf-8")
    output_trim = '\n'.join(output_str.split('\n')[2:-4])
    list = [item.split('\t') for item in output_trim.split('\n')]
    dict = {name: (ip, mac) for ip, mac, name in list}
    print(dict)
    for key, value in dict.items():
        ip = value[0]
        mac = value[1]
        name = key
        #cursor.execute(update_name, (name))
        #cursor.execute(update_ip, (ip))
        #cursor.execute(update_mac, (mac))
        #db.commit()

if __name__ == "__main__":
    main()