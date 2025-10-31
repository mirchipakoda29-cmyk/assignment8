# ip_utils.py

def ip_to_binary(ip_address: str) -> str:
    # Split into 4 octets
    octets = ip_address.split(".")
    
    # Convert each octet to 8-bit binary
    binary_octets = [format(int(o), "08b") for o in octets]
    
    # Join to form 32-bit binary
    return "".join(binary_octets)


def get_network_prefix(ip_cidr: str) -> str:
    ip, prefix_len = ip_cidr.split("/")
    prefix_len = int(prefix_len)

    # full 32-bit binary of IP
    binary_ip = ip_to_binary(ip)

    # return only first prefix_len bits
    return binary_ip[:prefix_len]


# ✅ Quick test (you can remove later)
if __name__ == "__main__":
    print(ip_to_binary("192.168.1.1"))
    print(get_network_prefix("200.23.16.0/23"))
