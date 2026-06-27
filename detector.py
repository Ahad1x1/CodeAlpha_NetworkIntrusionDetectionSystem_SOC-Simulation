import time
from collections import defaultdict

# -------------------------
# TRACKERS
# -------------------------
scan_tracker = defaultdict(list)
icmp_tracker = defaultdict(list)

alerted_scans = set()
alerted_icmp = set()

SUSPICIOUS_PORTS = [21, 22, 23, 445, 3389]


# -------------------------
# PORT SCAN DETECTION
# -------------------------
def detect_port_scan(src_ip, dst_port):
    now = time.time()

    scan_tracker[src_ip].append((dst_port, now))

    # keep last 10 seconds
    scan_tracker[src_ip] = [
        (p, t) for p, t in scan_tracker[src_ip]
        if now - t <= 10
    ]

    unique_ports = {p for p, t in scan_tracker[src_ip]}

    if len(unique_ports) > 20 and src_ip not in alerted_scans:
        alerted_scans.add(src_ip)
        return f"PORT SCAN DETECTED from {src_ip}"

    return None


# -------------------------
# ICMP FLOOD DETECTION
# -------------------------
def detect_icmp_flood(src_ip):
    now = time.time()

    icmp_tracker[src_ip].append(now)

    icmp_tracker[src_ip] = [
        t for t in icmp_tracker[src_ip]
        if now - t <= 5
    ]

    if len(icmp_tracker[src_ip]) > 50 and src_ip not in alerted_icmp:
        alerted_icmp.add(src_ip)
        return f"ICMP FLOOD DETECTED from {src_ip}"

    return None


# -------------------------
# SUSPICIOUS PORT DETECTION
# -------------------------
def detect_suspicious_ports(dst_port):
    if dst_port in SUSPICIOUS_PORTS:
        return f"SUSPICIOUS PORT ACCESS: {dst_port}"
    return None


# -------------------------
# LARGE PACKET DETECTION
# -------------------------
def detect_large_payload(size):
    if size > 1000:
        return "LARGE PACKET DETECTED"
    return None