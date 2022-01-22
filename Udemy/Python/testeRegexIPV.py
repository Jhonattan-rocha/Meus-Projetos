import re

octeto = '255'
regex = re.compile(r'\b(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])(?:\.?|$)\b', flags=re.VERBOSE)

for c in range(301):
    ip = f'{c}.{c}.{c}.{c}'
    reg = regex.findall(ip)
    print(ip, reg, len(reg) == 4)
