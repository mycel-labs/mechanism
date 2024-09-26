from networkresource import P2PNetwork
from reward import RewardCalculator
from basefee import calculate_new_base_fee  # Import from basefee.py

# Function to encapsulate the simulation logic
def run_simulation():
    # Retrieve the network usage
    network = P2PNetwork(10)  # Create a P2P network with 10 nodes
    current_network_usage = network.get_network_usage()

    # Set variables for reward calculation
    old_base_reward = 100  # Previous base reward
    network_usage_current = current_network_usage / 100  # Convert usage from percentage to ratio
    target_usage = 0.5  # Target network usage (shared between reward and base fee)
    
    # Reward adjustment
    b = 1 / 8  # Adjustment coefficient

    # Set variables for the base fee
    old_base_fee = 1  # Previous base fee
    a = 1 / 8  # Adjustment coefficient for the base fee

    # Hypothetical transaction information (example)
    tx_create_node = 100
    tx_create_network = 500
    tx_transfer_node = 50
    tx_transfer_network = 200
    tx_store_node = 30
    tx_store_network = 100
    verify_tx_node = 20
    verify_tx_network = 80

    # Instantiate RewardCalculator and calculate the reward
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
        target_usage,  # Pass the constant here
        b  # Pass the coefficient here
    )

    # Calculate and display the reward
    reward = calculator.calculate_reward(old_base_reward)

    # Calculate and display the base fee
    new_base_fee = calculate_new_base_fee(old_base_fee, current_network_usage, target_usage, a)

    # Calculate the Generated Amount
    generated_amount = reward - new_base_fee
    
    # Return network_usage_current as part of the result
    return reward, new_base_fee, generated_amount, network_usage_current
