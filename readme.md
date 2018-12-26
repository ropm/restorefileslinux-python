# Restore purged files - Python

## Installs purged packages based on the given date

Works on Ubuntu 18.04 at least, haven't tested on other OS's. Should work on Linux Debian, for Fedora you would need to replace the apt-get install with yum.

For this script to work you need to copy the history.log from /var/log/apt to your working directory for the script to read the file. 