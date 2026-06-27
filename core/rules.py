def port_scan(src, port):
    if port:
        return True, f"Port scan activity detected from {src}", "HIGH"
    return False, "", ""


def icmp_flood(src):
    return True, f"ICMP flood detected from {src}", "HIGH"


def suspicious_port(port):
    dangerous_ports = [21, 22, 23, 445, 3389]

    if port in dangerous_ports:
        return True, f"Suspicious port access: {port}", "MEDIUM"

    return False, "", ""


def large_packet(size):
    if size > 1000:
        return True, f"Large packet detected ({size} bytes)", "LOW"

    return False, "", ""