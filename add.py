# to use this script, do python add.py folder/[team-file-name].txt in your terminal.

from sys import argv

script, readname = argv

fileread = open(readname, 'r')
filewrite = open('*allteams.txt', 'a')
changelog =  open('changelog.txt', 'a')
fi = open('files-index.txt', 'a')

import time
import datetime

teamname = str(fileread).partition("<open file '")[2].partition('.txt')[0].replace('-', ' ')
filewrite.write('=== [' + teamname.replace('/', '] ') + ' ===\n')
for line in fileread:
	if 'Description:' not in line:
		filewrite.write(line)
d8 = datetime.datetime.strptime(str(datetime.date.today())[:10], '%Y-%m-%d')
changelog.write(str(d8).partition(' ')[0] + ': Added ' + teamname + "\n")
fi.write(teamname.replace(' ', '-') + '.txt\n')
