import random

class P2PNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.local_load = 0
        self.neighbor_loads = {}
        self.global_load_estimate = 0

    def update_local_load(self):
        # Simulate resource usage (e.g., CPU, memory, network)
        self.local_load = random.uniform(0, 100)

    def share_load_info(self, network):
        for neighbor in network.get_neighbors(self.node_id):
            neighbor.receive_load_info(self.node_id, self.local_load)

    def receive_load_info(self, node_id, load):
        self.neighbor_loads[node_id] = load

    def estimate_global_load(self):
        all_loads = list(self.neighbor_loads.values()) + [self.local_load]
        self.global_load_estimate = sum(all_loads) / len(all_loads)


class P2PNetwork:
    def __init__(self, num_nodes):
        self.nodes = [P2PNode(i) for i in range(num_nodes)]

    def get_neighbors(self, node_id):
        return [node for node in self.nodes if node.node_id != node_id]

    def simulate_network_activity(self):
        for node in self.nodes:
            node.update_local_load()
            node.share_load_info(self)
        for node in self.nodes:
            node.estimate_global_load()

    def get_average_global_load_estimate(self):
        return sum(node.global_load_estimate for node in self.nodes) / len(self.nodes)

    def get_global_load(self):
        self.simulate_network_activity()
        return self.get_average_global_load_estimate()

# Example usage:
network = P2PNetwork(10)  # 10 nodes
current_global_load = network.get_global_load()
print(f"Resource usage: {current_global_load:.2f}%")
