# imported libs
import argparse
import socket
import threading


# create the function to scan open ports alongside error handling s
def scan(host, ports, timeout):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(timeout)
    try:
        soc.connect((host, ports))
        print(f'{ports} is open on {host}')
        open_ports.append(ports)
        soc.close()
    except Exception as E:
        print(f'port {ports} {E}')


# creating the parser object
parser = argparse.ArgumentParser("simple port scanner utility on cli")

# creating the arguments
parser.add_argument("Host", help="enter the target host", type=str)  # positional arguments
parser.add_argument("-sp", "--start_port", help="port you want to scan", type=int, default=1)  # optional args
parser.add_argument("-ep", "--end_port", help="you can use this to scan for a range between the "  # optional args
                                              "start port and this", type=int, default=600)  # optional args
parser.add_argument("-T", "--Timeout", help="This specifies the timeout in seconds", type=float,
                    default=0.5)  # optional args
parser.add_argument("-S", "--Save_result", help="saves the result of the scan", type=str, default="saves.txt")

# parse the arguments into the cli
args = parser.parse_args()

# creating an empty list of threads
threads = []
open_ports = []

# setting thread instance
for port in range(args.start_port, args.end_port):
    port_threading = threading.Thread(target=scan, args=(args.Host, port, args.Timeout,))
    threads.append(port_threading)
    port_threading.start()

# stacking the threads
for thread in threads:
    thread.join()

with open(args.Save_Result, "w") as args.Save_Result:
    for port in open_ports:
        args.Save_Result.write(f'port {port} is open on {args.Host}')
        print(f'successfully saved as {args.S}')

# things to add
# handle multiple host scanning
# service version detection
