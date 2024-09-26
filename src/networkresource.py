import random

class P2PNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.node_usage = 0
        self.neighbor_usages = {}
        self.network_usage_estimate = 0

    def update_node_usage(self):
        # Simulate resource usage (e.g., CPU, memory, network)
        self.node_usage = random.uniform(0, 100)

    def share_usage_info(self, network):
        for neighbor in network.get_neighbors(self.node_id):
            neighbor.receive_usage_info(self.node_id, self.node_usage)

    def receive_usage_info(self, node_id, usage):
        self.neighbor_usages[node_id] = usage

    def estimate_network_usage(self):
        all_usages = list(self.neighbor_usages.values()) + [self.node_usage]
        self.network_usage_estimate = sum(all_usages) / len(all_usages)


class P2PNetwork:
    def __init__(self, num_nodes):
        self.nodes = [P2PNode(i) for i in range(num_nodes)]

    def get_neighbors(self, node_id):
        return [node for node in self.nodes if node.node_id != node_id]

    def simulate_network_activity(self):
        for node in self.nodes:
            node.update_node_usage()
            node.share_usage_info(self)
        for node in self.nodes:
            node.estimate_network_usage()

    def get_average_network_usage_estimate(self):
        return sum(node.network_usage_estimate for node in self.nodes) / len(self.nodes)

    def get_network_usage(self):
        self.simulate_network_activity()
        return self.get_average_network_usage_estimate()

# Example usage:
network = P2PNetwork(10)  