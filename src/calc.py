from networkresource import P2PNetwork
from reward import RewardCalculator
from basefee import calculate_new_base_fee  # basefee.pyからインポート

def main():
    # ネットワークの使用率を取得する
    network = P2PNetwork(10)  # 10ノードのP2Pネットワークを作成
    current_network_usage = network.get_network_usage()
    print(f"Network Usage: {current_network_usage:.2f}%")

    # 報酬計算のための変数を設定する
    old_base_reward = 100  # 前回のベース報酬
    network_usage_current = current_network_usage / 100  # 使用率を百分率から比率に変換
    target_usage = 0.5  # ターゲットネットワーク使用率 (報酬とベースフィーで共通)
    
    # reward adjestment
    b = 1 / 8  # 調整係数

    # Base Feeのための変数を設定
    old_base_fee = 1  # 前回のベースフィー
    a = 1 / 8  # Base fee の調整係数

    # トランザクション情報を仮定する（例）
    tx_create_node = 100
    tx_create_network = 500
    tx_transfer_node = 50
    tx_transfer_network = 200
    tx_store_node = 30
    tx_store_network = 100
    verify_tx_node = 20
    verify_tx_network = 80

    # RewardCalculatorのインスタンス化と報酬の計算
    calculator = RewardCalculator(
        network_usage_current, 
        tx_create_node, 
        tx_create_network, 
        tx_transfer_node, 
        tx_transfer_network, 
        tx_store_node, 
        tx_store_network, 
        verify_tx_node, 
        verify_tx_network,
        target_usage,  # ここで定数を渡す
        b  # ここで係数を渡す
    )

    # 報酬を計算して表示
    reward = calculator.calculate_reward(old_base_reward)
    print(f"Calculated reward: {reward}")

    # ベースフィーの計算と表示
    new_base_fee = calculate_new_base_fee(old_base_fee, current_network_usage, target_usage, a)
    print(f"New base fee: {new_base_fee:.2f}")

    # Generated Amountの計算
    generated_amount = reward - new_base_fee
    print(f"Generated amount: {generated_amount:.2f}")

# このスクリプトが直接実行された場合のみ、main()を実行する
if __name__ == "__main__":
    main()
