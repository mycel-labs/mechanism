# Use the network load from `networkresource.py`
from networkresource import P2PNetwork

def calculate_new_base_fee(old_base_fee, current_load, target_load):
    # EthereumのBaseFee計算式: OldBaseFee * (1 + 1/8 * (usedUsage - targetUsage))
    load_factor = (current_load - target_load) / target_load
    adjustment = 1 + (1 / 8 * load_factor)

    # Base Feeの計算（制限なし）
    new_base_fee = old_base_fee * adjustment
    return new_base_fee

# Example: Old fee and target load
old_fee = 100  # Previous base fee
target_load = 50  # Target network load (50%)

# Get the current load from the network simulation
network = P2PNetwork(10)
current_load = network.get_global_load()

# Calculate the new base fee based on the current load
new_fee = calculate_new_base_fee(old_fee, current_load, target_load)
print(f"New base fee: {new_fee:.2f}")
