class RewardCalculator:
    def __init__(self, network_usage_current, tx_create_node, tx_create_network, tx_transfer_node, tx_transfer_network, tx_store_node, tx_store_network, verify_tx_node, verify_tx_network, target_network_usage, b):
        # トランザクション情報などの初期化
        self.network_usage_current = network_usage_current
        self.tx_create_node = tx_create_node
        self.tx_create_network = tx_create_network
        self.tx_transfer_node = tx_transfer_node
        self.tx_transfer_network = tx_transfer_network
        self.tx_store_node = tx_store_node
        self.tx_store_network = tx_store_network
        self.verify_tx_node = verify_tx_node
        self.verify_tx_network = verify_tx_network

        # 定数を外部から受け取る
        self.target_network_usage = target_network_usage
        self.b = b

    def calculate_base_reward(self, old_base_reward):
        """
        BaseReward(p)を計算する
        """
        adjustment_factor = 1 + self.b * (self.network_usage_current - self.target_network_usage) / self.target_network_usage
        base_reward = old_base_reward * adjustment_factor
        return base_reward

    def calculate_reward(self, old_base_reward):
        """
        全体のRewardを計算する
        """
        base_reward = self.calculate_base_reward(old_base_reward)

        # 各トランザクションごとの報酬割合を計算
        create_ratio = 0.5 * (self.tx_create_node / self.tx_create_network) if self.tx_create_network > 0 else 0
        transfer_ratio = 0.3 * (self.tx_transfer_node / self.tx_transfer_network) if self.tx_transfer_network > 0 else 0
        store_ratio = 0.15 * (self.tx_store_node / self.tx_store_network) if self.tx_store_network > 0 else 0
        verify_ratio = 0.05 * (self.verify_tx_node / self.verify_tx_network) if self.verify_tx_network > 0 else 0

        # 最終的な報酬の計算
        reward = base_reward * (create_ratio + transfer_ratio + store_ratio + verify_ratio)
        return reward
