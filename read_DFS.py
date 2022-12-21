from pathlib import Path
import io
import re
import subprocess

"""quickbms.exe
    [options]
        <script.BMS>
            <input_archive/folder>
                [output_folder]"""

# quickbms.exe -l "F:/Users/Michael/Documents/Programming/Python/A51/scripts_A51/SFDX.bms" "F:/Users/Michael/Documents/Programming/Python/A51/archives/STRINGS.DFS" > test.txt

quickbms = 'data/quickbms.exe'
options = '-l'
script = 'scripts_A51/SFDX.bms'
archive = 'STRINGS'
archive_path = f'archives/{archive}.DFS'
output = 'extracted'
# quickbms = 'quickbms.exe'
# options = '-l'
# script = 'F:/Users/Michael/Documents/Programming/Python/A51/scripts_A51/SFDX.bms'
# archive = 'HIRES'
# archive_path = f'F:/Users/Michael/Documents/Programming/Python/A51/archives/{archive}.DFS'
# output = '> F:/Users/Michael/Documents/Programming/Python/A51/extracted/test.txt'

# regex = r'\s+([0-9a-f]+)\s(\d+)\s+([a-zA-Z0-9_[\]-]+\.[a-zA-Z0-9]+)\r\n'
regex = r'\s+([\da-f]+)\s(\d+)\s+([\w-]+\.[\w]+)'

# Waits
# subprocess.Popen([quickbms, options, script, archive, output])
# Runs and exits
# subprocess.call([quickbms, options, script, archive, output])

proc = subprocess.Popen([quickbms, options, script, archive_path], stdout=subprocess.PIPE)
out = proc.stdout.read()
out_string = out.decode('utf-8')
with open('stdout.txt', 'w') as f:
    f.write(out_string)

matches = re.findall(regex, out_string)
for match in matches:
    filename = match[2]
    with open('output.txt', 'a') as f:
        f.write(f'{filename}\n')