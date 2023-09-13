# BBRv3 Performance Evaluation

## Overview

This repository contains resources related to the performance evaluation of BBRv3, a congestion control algorithm for optimizing network traffic. In this study, we assess the performance of BBRv3 under various scenarios and compare it to other congestion control algorithms, such as CUBIC. The paper associated with this research offers valuable insights into BBRv3's behavior and its suitability for different networking conditions.

## Paper Abstract

[Link to Full Paper (coming soon)]

This paper presents a comprehensive evaluation of BBRv3, considering scenarios with different numbers of competing flows, RTTs, loss rates, and buffer sizes. The experiments shed light on BBRv3's coexistence with CUBIC, its resilience to packet losses, fairness considerations, queue occupancy, bottleneck bandwidth estimation, flow completion times, and optimal configurations in various network conditions. 

## Repository Contents

- **Experiments:** This directory contains scripts and resources used for conducting the experiments outlined in the paper.

- **Data:** Here, you'll find datasets and raw results obtained during the experiments.

- **Figures:** Visualizations and plots created based on the experiment data.

## How to Use

To replicate the experiments or explore the data and visualizations, follow these steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/gomezgaona/bbr3.git
```
2. Navigate in the experiment directory
```bash
cd experiments
```
3. Enter the directory of one of the experiments (e.g., RTT_Unfairness)
```bash
cd RTT_Unfairness
```
4. Run the topology file
```bash
python3 topo.py
```
5. Run the experiment script associated with the topology
```bash
python3 run_RTT_Unfariness.py
```

Feel free to customize the topology and test parameters by modifying the Python scripts

## Access to the VM
Send your request to gomezgaj [at] email [dot] sc [dot] edu and I will be sharing it with you.
