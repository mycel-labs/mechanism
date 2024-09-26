def calculate_new_base_fee(old_base_fee, current_usage, target_usage, a):
    # BaseFee計算式: OldBaseFee * (1 + a * (usedUsage - targetUsage))
    usage_factor = (current_usage - target_usage) / target_usage
    adjustment = 1 + (a * usage_factor)

    # Base Feeの計算
    new_base_fee = old_base_fee * adjustment
    return new_base_fee
