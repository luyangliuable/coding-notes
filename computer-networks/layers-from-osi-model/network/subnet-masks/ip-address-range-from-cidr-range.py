import ipaddress

ip = "255.255.255.254"

for cidr in range(32, -1, -1):
    network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    usable_start = network_address + 1
    usable_end = broadcast_address - 1

    print(f"{network_address}	{broadcast_address}		{usable_start}	{usable_end}")

    # print(f"CIDR: {cidr}")
    # print(f"Network Address: {network_address}")
    # print(f"Broadcast Address: {broadcast_address}")
    # print(f"Usable Address Range: {usable_start} - {usable_end}\n")
