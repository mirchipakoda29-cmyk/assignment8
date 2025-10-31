from dataclasses import dataclass
from queue import PriorityQueue

@dataclass
class Packet:
    source_ip: str
    dest_ip: str
    payload: str
    priority: int   # 0 = High, 1 = Medium, 2 = Low

def fifo_scheduler(packet_list: list) -> list:
    return packet_list[:]

def priority_scheduler(packet_list: list) -> list:
    pq = PriorityQueue()

    for idx, packet in enumerate(packet_list):
        pq.put((packet.priority, idx, packet))  # add tie-breaker

    result = []
    while not pq.empty():
        _, _, pkt = pq.get()
        result.append(pkt)

    return result


# Test case
if __name__ == "__main__":
    packets = [
        Packet("A", "B", "Data Packet 1", 2),
        Packet("A", "B", "Data Packet 2", 2),
        Packet("A", "B", "VOIP Packet 1", 0),
        Packet("A", "B", "Video Packet 1", 1),
        Packet("A", "B", "VOIP Packet 2", 0),
    ]

    print([p.payload for p in fifo_scheduler(packets)])
    print([p.payload for p in priority_scheduler(packets)])
