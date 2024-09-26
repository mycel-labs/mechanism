import matplotlib.pyplot as plt
import pandas as pd
from calc import run_simulation  # Importing run_simulation from calc.py

# Function to run multiple simulations
def run_multiple_simulations(num_simulations, initial_supply):
    results = []
    total_supply = initial_supply  # Initial total supply
    
    for i in range(num_simulations):
        reward, new_base_fee, generated_amount, network_usage = run_simulation()
        
        # Add generated_amount to total_supply
        total_supply += generated_amount
        
        # Save the simulation results
        results.append({
            "Simulation": i + 1,
            "Reward": reward,
            "Base Fee": new_base_fee,
            "Generated Amount": generated_amount,
            "Network Usage": network_usage * 100,  # Multiply by 100 here
            "Total Supply": total_supply  # Record total_supply
        })
    
    return pd.DataFrame(results)

# Function to visualize the simulation results
def visualize_simulation_results(df):
    fig, ax = plt.subplots(4, 1, figsize=(10, 16))

    # Plot for Reward
    ax[0].plot(df["Simulation"], df["Reward"], marker='o', label='Reward')
    ax[0].set_title('Reward over Simulations')
    ax[0].set_xlabel('Simulation')
    ax[0].set_ylabel('Reward')
    ax[0].legend()

    # Plot for Base Fee
    ax[1].plot(df["Simulation"], df["Base Fee"], marker='o', color='orange', label='Base Fee')
    ax[1].set_title('Base Fee over Simulations')
    ax[1].set_xlabel('Simulation')
    ax[1].set_ylabel('Base Fee')
    ax[1].legend()

    # Display Generated Amount and Network Usage together
    ax2 = ax[2].twinx()  # Create a second Y-axis

    # Plot for Generated Amount (left Y-axis)
    ax[2].plot(df["Simulation"], df["Generated Amount"], marker='o', color='green', label='Generated Amount')
    ax[2].set_title('Generated Amount and Network Usage over Simulations')
    ax[2].set_xlabel('Simulation')
    ax[2].set_ylabel('Generated Amount', color='green')
    ax[2].tick_params(axis='y', labelcolor='green')
    ax[2].legend(loc='upper left')

    # Plot for Network Usage (right Y-axis)
    ax2.plot(df["Simulation"], df["Network Usage"], marker='o', color='blue', label='Network Usage')
    ax2.set_ylabel('Network Usage (%)', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.legend(loc='upper right')

    # Plot for Total Supply
    ax[3].plot(df["Simulation"], df["Total Supply"], marker='o', color='purple', label='Total Supply')
    ax[3].set_title('Total Supply over Simulations')
    ax[3].set_xlabel('Simulation')
    ax[3].set_ylabel('Total Supply')
    ax[3].legend()

    # Display the graphs
    plt.tight_layout()
    plt.show()

# Main process
if __name__ == "__main__":
    initial_supply = 100_000_000  # Initial supply amount
    num_simulations = 100  # Number of simulations
    
    # Run the simulations
    df_results = run_multiple_simulations(num_simulations, initial_supply)

    # Display the results
    print(df_results)

    # Export the results to a CSV file
    csv_file_name = 'simulation_results.csv'
    df_results.to_csv(csv_file_name, index=False)  # index=False to exclude row numbers from the CSV
    
    print(f"Results saved to {csv_file_name}.")

    # Visualize the results
    visualize_simulation_results(df_results)
