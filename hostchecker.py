import sys

zz = sys.stdin

host = 'host'
ip = 'ip'
mac = 'mac'
os = ['os']

for i in zz:
    l = i.split()
    if l[-1] == "PTR":
        # found a host
        print '%s, %s, %s, "%s"' % (host, ip, mac, ' *OR* '.join(os))
        host = l[0]
        ip = mac = ''
        os = []
    elif l[0] == 'ADDR=':
        if l[-1] == 'ipv4':
            ip = l[1]
        elif l[-1] == 'mac':
            mac = l[1]
        else:
            raise "Address type unknown"
    elif l[0] == 'OS=':
        os.append('%s (%s%%)' % (' '.join(l[1:-1]), l[-1]))
