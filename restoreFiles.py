import subprocess

#open the log file
try:
    f = open('history.log')
except Exception as e:
    print('Copy the history.log file from /var/log/apt to your working directory. Error message: ' + str(e))
    exit()
#get the purge starting date inputs from the user
date1 = input('Start-Date of the purge as yyyy-mm-dd: ')
date2 = input('Starting time of the purge as hh:mm:ss: ')
space = ' '*2
start_date = date1 + space + date2

#loop for start date
for line in f:
    if line.startswith('Start-Date: ' + start_date):
        break
#loop for purge and split the line to packages and use Popen to install the purged packages
for line in f:        
        if line.startswith('Purge: '):
            print('Found a purge, date: ' + start_date)
            packages = line.split(' ')
            for i in range(1, len(packages)):
                if packages[i].startswith('('):
                    continue
                print('Starting the installation...')
                pack = packages[i] + ' ' + packages[i+1]
                packed = pack.strip(',')
                y_or_n = input('Install next package y/n? Package name: '+packed)
                if y_or_n == 'y':
                    p = subprocess.Popen('apt-get install ' + packages[i], shell=True)
                    p.wait()
                else:
                    print('Package not installed.')
f.close()
print('Did not find any purges.')