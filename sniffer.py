import random

def generate_fake_packet():
    return {
        "src_ip": f"192.168.{random.randint(0,255)}.{random.randint(1,254)}",
        "src_port": random.randint(1024, 65535),
        "dst_ip": f"10.0.{random.randint(0,255)}.{random.randint(1,254)}",
        "dst_port": random.choice([80, 443, 21, 22, 53])
    }