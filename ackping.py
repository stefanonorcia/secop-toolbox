def tcp_ping(host, port):
    ''' TCP Ping '''
    ans, unans = sr(IP(dst=host)/TCP(dport=port, flags="S"))
# ans, unans = sr(IP(dst='192.168.56.99-105') / TCP(dport=80, flags='A'))
    ans.summary(lambda(s, r): r.sprintf("%IP.src% is alive"))
# ans.summary(lambda(s, r): r.sprintf('{IP: %IP.src% is alive}'))


