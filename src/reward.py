class RewardCalculator:
    def __init__(self, network_usage_current, tx_create_node, tx_create_network, tx_transfer_node, tx_transfer_network, tx_store_node, tx_store_network, verify_tx_node, verify_tx_network, target_network_usage, b):
        # Initialize transaction information and other variables
        self.network_usage_current = network_usage_current
        self.tx_create_node = tx_create_node
        self.tx_create_network = tx_create_network
        self.tx_transfer_node = tx_transfer_node
        self.tx_transfer_network = tx_transfer_network
        self.tx_store_node = tx_store_node
        self.tx_store_network = tx_store_network
        self.verify_tx_node = verify_tx_node
        self.verify_tx_network = verify_tx_network

        # Receive constants from external sources
        self.target_network_usage = target_network_usage
        self.b = b

    def calculate_base_reward(self, old_base_reward):
        """
        Calculate BaseReward(p)
        """
        adjustment_factor = 1 + self.b * (self.network_usage_current - self.target_network_usage) / self.target_network_usage
        base_reward = old_base_reward * adjustment_factor
        return base_reward

    def calculate_reward(self, old_base_reward):
        """
        Calculate the total Reward
        """
        base_reward = self.calculate_base_reward(old_base_reward)

        # Calculate reward ratios for each transaction type
        create_ratio = 0.5 * (self.tx_create_node / self.tx_create_network) if self.tx_create_network > 0 else 0
        transfer_ratio = 0.3 * (self.tx_transfer_node / self.tx_transfer_network) if self.tx_transfer_network > 0 else 0
        store_ratio = 0.15 * (self.tx_store_node / self.tx_store_network) if self.tx_store_network > 0 else 0
        verify_ratio = 0.05 * (self.verify_tx_node / self.verify_tx_network) if self.verify_tx_network > 0 else 0

        # Final reward calculation
        reward = base_reward * (create_ratio + transfer_ratio + store_ratio + verify_ratio)
        return reward
