# BBRv3 Performance Evaluation

## Overview

This repository contains resources related to the performance evaluation of BBRv3, a congestion control algorithm for optimizing network traffic. In this study, we assess the performance of BBRv3 under various scenarios and compare it to other congestion control algorithms, such as CUBIC. The paper associated with this research offers valuable insights into BBRv3's behavior and its suitability for different networking conditions.

## Paper Abstract

[Link to Full Paper: https://www.sciencedirect.com/science/article/pii/S0140366424001658]

The first version of the Bottleneck Bandwidth and Round-Trip Time (BBRv1) congestion control algorithm (CCA), introduced by Google in 2016, marked a significant advancement in network communication. It presented high performance in scenarios with high packet losses and routers equipped with small buffers. Unlike traditional loss-based algorithms like CUBIC and Reno, which rely solely on detecting packet losses as a sign of congestion, BBRv1 took a novel approach. It aimed to find the optimal balance between maximizing throughput and minimizing delay, disregarding packet losses. However, this approach presented fairness issues when interacting with loss-based algorithms. To address these fairness problems, BBRv2 was developed as a successor to BBRv1. BBRv2 incorporated multiple metrics, including available bandwidth, loss rates, Round-trip Time (RTT), and Explicit Congestion Notification (ECN) markings, to model network conditions. This approach improved the fairness with loss-based CCAs. Despite the improvements introduced in BBRv2, some issues and performance limitations were identified. Therefore, in 2023, Google released BBRv3, which fixed the bugs observed in BBRv2 and tuned performance parameters to ensure a better coexistence among competing flows.

This paper presents an evaluation of BBRv3 through experiments conducted in both emulated and real network environments. The experiments include scenarios with different numbers of competing flows, propagation delays, loss rates, and buffer sizes. The experiments presented in this paper also include the effects of RTT unfairness and how BBRv3 performs under such conditions. The comparison is performed with CUBIC, which is one the most widely used CCA. Additionally, the influence of Active Queue Management (AQM) algorithms is examined. Furthermore, this paper investigates how BBRv3's estimation of the bottleneck link varies concerning the RTT. Lastly, after each experiment, this paper analyzes which conditions are more suitable for using BBRv3 efficiently. 

Results indicate that the coexistence of BBRv3 with CUBIC depends on the buffer size and the number of competing flows. It exhibits fairness issues with a small number of BBRv3 flows, but these issues improve as the count of BBRv3 flows increases. Optimal coexistence is achieved with a buffer size between BDP and 10BDP. In terms of loss resilience, BBRv3 maintains high throughput and experiences lower retransmissions even when subjected to loss rates of approximately 1\%. Furthermore, the fairness of BBRv3 with loss-based CCAs is influenced by the buffer size and the RTT. Smaller buffers negatively impact flows with lower RTTs. Implementing the FQ-CoDel AQM algorithm helps mitigate RTT unfairness across various buffer sizes. It is also observed that BBRv3 consistently maintains low queue occupancy. Lastly, in scenarios where short flows compete with long flows, BBRv3 presents low Flow Completion  Times (FCTs) even with large buffer sizes.

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

Feel free to customize the topology and test parameters by modifying the Python scripts.

## Access to the VM
Send your request to gomezgaj [at] email [dot] sc [dot] edu and I will be sharing it with you.
