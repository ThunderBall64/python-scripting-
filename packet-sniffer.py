import pyshark

cap = pyshark.LiveCapture(interface='en0', bpf_filter='udp port 53')

cap.sniff(packet_count=10)

def print_dns_info(pkt):
    if pkt.dns.qry_name:
        print('DNS Request from %s: %s' % (pkt.ip.src, pkt.dns.qry_name))
    elif pkt.dns.resp_name:
        print('DNS Response from %s: %s' % (pkt.ip.src, pkt.dns.resp_name))

cap.apply_on_packets(print_dns_info, timeout=100)