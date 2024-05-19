
from CSVPacket import CSVPackets
import argparse

IPProtos = [0 for x in range(256)]
numBytes = 0
numPackets = 0
tcpServices = {}
udpServices = {}
ipCounts = {}
destCounts = {}
protocol_filter = [47, 50, 51, 89]

def increment_dict(dictionary, key):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def process_packet(pkt, count_ip=False):
    global numBytes, numPackets
    numBytes += pkt.length
    numPackets += 1
    proto = pkt.proto & 0xff
    IPProtos[proto] += 1
    
    if count_ip and (proto in protocol_filter):
        increment_dict(ipCounts, pkt.ipdst)

    if proto == 6: 
        increment_dict(tcpServices, pkt.tcpdport)
        increment_dict(destCounts, (pkt.ipdst, 'tcp', pkt.tcpdport))
        increment_dict(ipCounts, pkt.ipdst)
    elif proto == 17:  
        increment_dict(udpServices, pkt.udpdport)
        increment_dict(destCounts, (pkt.ipdst, 'udp', pkt.udpdport))
        increment_dict(ipCounts, pkt.ipdst)

def print_stats():
    print(f"Num packets: {numPackets}, Num bytes: {numBytes}")
    print("IP Protocols:")
    for i in range(256):
        if IPProtos[i] != 0:
            print(f"{i:3d}: {IPProtos[i]:9d}")

    print("TCP Services (port: count):")
    for port, count in sorted(tcpServices.items()):
        if port <= 1024:
            print(f"{port:5d}: {count:9d}")

    print("UDP Services (port: count):")
    for port, count in sorted(udpServices.items()):
        if port <= 1024:
            print(f"{port:5d}: {count:9d}")

def print_ip_counts():
    for ip, count in sorted(ipCounts.items(), key=lambda item: item[1], reverse=True):
        print(f"{ip}: {count}")

def print_server_counts():
    server_connections = {}
    for (ip, proto, port), count in destCounts.items():
        if ip not in server_connections:
            server_connections[ip] = {}
        if (proto, port) not in server_connections[ip]:
            server_connections[ip][(proto, port)] = 0
        server_connections[ip][(proto, port)] += 1

    for ip, services in sorted(server_connections.items(), key=lambda item: len(item[1]), reverse=True):
        service_list = ", ".join([f"{proto}/{port}" for (proto, port) in services])
        print(f"{ip} has {len(services)} distinct services: {service_list}")

def main():
    parser = argparse.ArgumentParser(description='Process some packet data.')
    parser.add_argument('csvfile', type=str, help='Input CSV file')
    parser.add_argument('--stats', action='store_true', help='Show stats')
    parser.add_argument('--countip', action='store_true', help='Count IP addresses')
    parser.add_argument('--connto', action='store_true', help='Count connections to services')
    args = parser.parse_args()

    with open(args.csvfile, 'r') as csvfile:
        for pkt in CSVPackets(csvfile):
            process_packet(pkt, count_ip=args.countip)

    if args.stats:
        print_stats()
    if args.countip:
        print_ip_counts()
    if args.connto:
        print_server_counts()

if __name__ == '__main__':
    main()
