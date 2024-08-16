

# Simple Port Scanner CLI
This is a lightweight, multithreaded command-line utility for scanning open ports on a target host. The tool makes use of Python's `socket`, `threading`, and `argparse` libraries for scanning open ports and saving the results to a file.I

## Features
- **Multithreaded Port Scanning**: Scans multiple ports concurrently, improving speed and efficiency.
- **Timeout Configuration**: Set custom timeout values for connections to avoid waiting too long for each port.
- **Save Scan Results**: Option to save the results to a text file for future reference.
- **Port Range Specification**: Choose a range of ports to scan, from a starting port to an end port.

## Planned Features
- Multiple host scanning
- Service version detection
- will add these later on

## Installation

1. Clone this repository:
    git clone https://github.com/Fruitpunch44/CLI-PortScanner
2. Navigate into the directory:
    cd CLI-PortScanner
3. Ensure you have Python installed, preferably Python 3.x.

## Usage

To run the port scanner:

python portscanner_cli.py Host [-sp START_PORT] [-ep END_PORT] [-T TIMEOUT] [-S SAVE_RESULT]

### Arguments
- **Host**: (Required) The target host to scan.
- **-sp, --start_port**: (Optional) The starting port for the scan (default: 1).
- **-ep, --end_port**: (Optional) The end port for the scan (default: 600).
- **-T, --Timeout**: (Optional) Timeout for socket connections (default: 0.5 seconds).
- **-S, --Save_result**: (Optional) File to save the scan results (default: `saves.txt`).

### Example

Scan ports 20 to 100 on host `192.168.1.1` and save results to `output.txt`:
python port_scanner.py 192.168.1.1 -sp 20 -ep 100 -S output.txt

---

Feel free to modify it as you see fit, especially when you add more features!
