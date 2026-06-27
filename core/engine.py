from scapy.all import IP, TCP, ICMP
from utils.logger import log_event
from core.rules import port_scan, icmp_flood, suspicious_port, large_packet


def process_packet(packet):

    if not packet.haslayer(IP):
        return

    src = packet[IP].src
    size = len(packet)

    if packet.haslayer(TCP):
        port = packet[TCP].dport

        ok, msg, sev = port_scan(src, port)
        if ok:
            log_event("PORT_SCAN", src, msg, sev)

        ok, msg, sev = suspicious_port(port)
        if ok:
            log_event("SUSPICIOUS_PORT", src, msg, sev)

    if packet.haslayer(ICMP):
        ok, msg, sev = icmp_flood(src)
        if ok:
            log_event("ICMP_FLOOD", src, msg, sev)

    ok, msg, sev = large_packet(size)
    if ok:
        log_event("ANOMALY", src, msg, sev)