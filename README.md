# Abstract
Mycel Network is a decentralized network consisting of node operators. This source describes the mint and burn mechanism of the network. Mycel Network's incentive mechanism consists of network usage-based Proof of Work (PoW) and a network usage-based base fee (burn mechanism). This mechanism takes good care of computer resource providers, who are the node operators.

# Base fee
Calculate the base fee to be burned based on the difference between the target resource usage (NetworkUsage) and the actual resource usage.

```
NewBaseFee = 
    OldBaseFee * 
    (1 + a * (usedUsage - targetUsage))

a == 1/8
InitialOldBaseFee == 1
```

# Reward
Calculate node-specific rewards based on the BaseReward, adjusted according to the work performed.

```
Reward = 
    BaseReward(p) * 
    { 0.5 * TxofCreateNode(p) / TxofCreateNetwork(p)} *
    { 0.3 * TxofTransferNode(p) / TxofTransferNetwork(p)} *
    { 0.15 * TxofStoreNode(p) / TxofStoreNetwork(p)} *
    { 0.05 * VerifyTxNode(p) / VerifyTxNetwork(p)}
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
- b: Adjustment coefficient (1/8)
- NetworkUsage(p): Network usage rate for the current period p
- TargetNetworkUsage: Target network usage rate (50%)

## Period
2 weeks

## Work type
TxofCreate: The act of creating a Transferable Account.  
TxofTransfer: Changing the owner of a Transferable Account.  
TxofStore: Storing data held by other nodes.  
VerifyTx: Verifying whether the Proof sent to the MPC account protocol matches the node’s transaction.

## Work weight
TxofCreate: 50%  
TxofTransfer: 30%  
TxofStore: 15%  
VerifyTx: 5%

---

# Simulation Setup

To run the simulation described above, follow the steps below to set up your environment and execute the simulation.

## Setup Instructions

1. **Clone the repository**:
   First, clone this repository to your local machine

   ```sh
   git clone https://github.com/mycel-labs
   mechanism.git
   cd mechanism
   ```

2. Install the required dependencies:
Use pip to install the necessary Python packages listed in requirements.txt:

   ```sh
   pip install -r requirements.txt
   ```
   Make sure you have Python 3.7+ installed on your system.

3. Run the simulation: 
Once the dependencies are installed, you can execute the simulation script, which calculates the base fee and rewards, and visualizes the results.

   ```sh
   python sim.py
   ```
This will run the base fee and reward calculations for the specified periods and display the results using matplotlib.

4. Simulation Output: 
The simulation will generate output that includes the calculated BaseFee and Rewards for each period. You will also see a plot of the fee adjustments and reward distributions over time.








