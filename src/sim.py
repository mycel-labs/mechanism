import matplotlib.pyplot as plt
import pandas as pd
from calc import run_simulation  # calc.pyのrun_simulationをインポート

# 複数回のシミュレーションを実行する関数
def run_multiple_simulations(num_simulations, initial_supply):
    results = []
    total_supply = initial_supply  # 初期のtotal supply
    
    for i in range(num_simulations):
        reward, new_base_fee, generated_amount, network_usage = run_simulation()
        
        # total_supplyにgenerated_amountを加算していく
        total_supply += generated_amount
        
        # シミュレーション結果を保存
        results.append({
            "Simulation": i + 1,
            "Reward": reward,
            "Base Fee": new_base_fee,
            "Generated Amount": generated_amount,
            "Network Usage": network_usage * 100,  # ここで * 100 を行う
            "Total Supply": total_supply  # total_supplyを記録
        })
    
    return pd.DataFrame(results)

# ビジュアライズする関数
def visualize_simulation_results(df):
    fig, ax = plt.subplots(4, 1, figsize=(10, 16))

    # Rewardのプロット
    ax[0].plot(df["Simulation"], df["Reward"], marker='o', label='Reward')
    ax[0].set_title('Reward over Simulations')
    ax[0].set_xlabel('Simulation')
    ax[0].set_ylabel('Reward')
    ax[0].legend()

    # Base Feeのプロット
    ax[1].plot(df["Simulation"], df["Base Fee"], marker='o', color='orange', label='Base Fee')
    ax[1].set_title('Base Fee over Simulations')
    ax[1].set_xlabel('Simulation')
    ax[1].set_ylabel('Base Fee')
    ax[1].legend()

    # Generated AmountとNetwork Usageを重ねて表示
    ax2 = ax[2].twinx()  # 2つ目のY軸を作成

    # Generated Amountのプロット (左Y軸)
    ax[2].plot(df["Simulation"], df["Generated Amount"], marker='o', color='green', label='Generated Amount')
    ax[2].set_title('Generated Amount and Network Usage over Simulations')
    ax[2].set_xlabel('Simulation')
    ax[2].set_ylabel('Generated Amount', color='green')
    ax[2].tick_params(axis='y', labelcolor='green')
    ax[2].legend(loc='upper left')

    # Network Usageのプロット (右Y軸)
    ax2.plot(df["Simulation"], df["Network Usage"], marker='o', color='blue', label='Network Usage')
    ax2.set_ylabel('Network Usage (%)', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.legend(loc='upper right')

    # Total Supplyのプロット
    ax[3].plot(df["Simulation"], df["Total Supply"], marker='o', color='purple', label='Total Supply')
    ax[3].set_title('Total Supply over Simulations')
    ax[3].set_xlabel('Simulation')
    ax[3].set_ylabel('Total Supply')
    ax[3].legend()

    # グラフを表示
    plt.tight_layout()
    plt.show()

# メイン処理
if __name__ == "__main__":
    initial_supply = 100_000_000  # 初期供給量
    num_simulations = 100  # シミュレーション回数
    
    # シミュレーション実行
    df_results = run_multiple_simulations(num_simulations, initial_supply)

    # 結果を表示
    print(df_results)

    # 結果をCSVファイルにエクスポート
    csv_file_name = 'simulation_results.csv'
    df_results.to_csv(csv_file_name, index=False)  # index=Falseで行番号をCSVに含めない
    
    print(f"結果を {csv_file_name} に保存しました。")

    # 結果をビジュアライズ
    visualize_simulation_results(df_results)
