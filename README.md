# Base fee
Calculate the base fee to be burned based on the difference between the target resource usage (NetworkUsage) and the actual resource usage.

NewBaseFee = 
    OldBaseFee * 
    (1 + a * (usedUsage - targetUsage))

a == 1/8
InitialOldBaseFee == 1


# Reward
Calculate node-specific rewards based on the BaseReward, adjusted according to the work performed.

```
Reward = 
    BaseReward * 
    { 0.5 * TxofCreateNode / TxofCreateNetwork} *
    { 0.3 * TxofTransferNode / TxofTransferNetwork} *
    { 0.15 * TxofStoreNode / TxofStoreNetwork} *
    { 0.05 * VerifyTxNode / VerifyTxNetwork}
```



## Base reward
```
BaseReward(p) = 
    BaseReward(p-1) * 
    [1 + b * (NetworkUsage(p) - TragetNetworkUsage) / TargetNetworkUsage]

TargetNetworkUsage: 50%
b == 1/8

```

- BaseReward(p): Base Reward for the current period p
- BaseReward(p-1): Base Reward from the previous period
- a: Adjustment coefficient (1/8)
- NetworkUsage(p): Network usage rate for the current period p
- TargetNetworkUsage: Target network usage rate (50%)


## Period
2 week

## Work weight
TxofCreate: 50%
TxofTransfer: 30%
TxofStore: 15%
VerifyTx: 5%






