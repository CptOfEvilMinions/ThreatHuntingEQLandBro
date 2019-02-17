from app.model import CreateQuery
from app.helpers import get_abuse_c2_blacklist,\
                        get_abuse_ransomware_blocklist, \
                        get_abuse_ssl_blacklist

def run(file_path, data_type, module):
    # Create empty query string
    query_str = str()

    if module == 'abuse_c2':
        ip_blacklist_lst = get_abuse_c2_blacklist()
        query_str = "bro_conn where destination_address in {0}".format(ip_blacklist_lst).replace('[',"(").replace(']',')')
    elif module == 'abuse_ssl':
        ssl_blacklist_lst = get_abuse_ssl_blacklist()
        query_str = "bro_files where files_sha1 in {0}".format(ssl_blacklist_lst).replace('[',"(").replace(']',')')
    elif module == 'abuse_ransomware':
        ransomware_ip_lst = get_abuse_ransomware_blocklist()
        query_str = "bro_conn where destination_address in {0}".format(ransomware_ip_lst).replace('[',"(").replace(']',')')
    else:
        print ("[-] Unknown threat module")
        exit()

    # Create query object
    query_obj = CreateQuery(file_path, data_type)
    
    # Run query
    query_obj.run_query(query_str)