
import requests
import argparse

def csv_downloader(url,index):
    r = requests.get(url)
    decoded_content = r.content.decode('utf-8')

    abuse_data_lst = list()
    for line in decoded_content.splitlines():
        if "#" not in line: 
            abuse_data_lst.append(line.split(',')[index])
    return abuse_data_lst

def get_abuse_ransomware_blocklist():
    url = "https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt"
    print ("[*] Downlading Abuse Ransomware blacklist: {0}".format(url))
    return csv_downloader(url, 0)
    

def get_abuse_ssl_blacklist():
    url = "https://sslbl.abuse.ch/blacklist/sslblacklist.csv"
    print ("[*] Downlading Abuse SSL blacklist: {0}".format(url))
    return csv_downloader(url, 1)


def get_abuse_c2_blacklist():
    url = "https://feodotracker.abuse.ch/downloads/ipblocklist.csv"
    print ("[*] Downlading Abuse C2 blacklist: {0}".format(url))
    return csv_downloader(url, 1)

