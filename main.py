from scapy.all import sniff, IP, TCP, UDP, ICMP
from utils.logger import log_event


def packet_callback(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src

        # -------------------------
        # RULE 1: Port Scan (basic)
        # -------------------------
        if packet.haslayer(TCP):
            dport = packet[TCP].dport

            if dport in [21, 22, 23, 445, 3389]:
                log_event(
                    "SUSPICIOUS_PORT",
                    src_ip,
                    f"Accessed port {dport}"
                )

        # -------------------------
        # RULE 2: ICMP Detection
        # -------------------------
        elif packet.haslayer(ICMP):
            log_event(
                "ICMP_TRAFFIC",
                src_ip,
                "ICMP packet detected"
            )

        # -------------------------
        # RULE 3: UDP Traffic
        # -------------------------
        elif packet.haslayer(UDP):
            log_event(
                "UDP_TRAFFIC",
                src_ip,
                "UDP packet detected"
            )


def main():
    print("IDS Running... Monitoring Traffic")
    sniff(prn=packet_callback, store=False)


if __name__ == "__main__":
    main()