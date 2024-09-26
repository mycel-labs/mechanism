def calculate_new_base_fee(old_base_fee, current_usage, target_usage, a):
    # BaseFee calculation formula: OldBaseFee * (1 + a * (usedUsage - targetUsage))
    usage_factor = (current_usage - target_usage) / target_usage
    adjustment = 1 + (a * usage_factor)

    # Calculate the Base Fee
    new_base_fee = old_base_fee * adjustment
    return new_base_fee
