from app import main
import argparse

# Command line parser
parser = argparse.ArgumentParser()

parser.add_argument("--file_path", '-f', required=True, help="File location to log file")
parser.add_argument("--data_type", '-d', required=True, help="Data type of logs")

parser.add_argument("--module", choices=['abuse_c2', 'abuse_ssl', 'abuse_ransomware'])
args = parser.parse_args()

print ("[+] Module: {0}".format(args.module))

if __name__ == "__main__":
    main.run(args.file_path, args.data_type, args.module)
    