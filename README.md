# Robust Optimization of Decision Variables under Coefficient Uncertainty
This repository demonstrates a method for selecting the optimal combination of decision variables from a predefined set,
under the influence of uncertain coefficients.
It aims to identify a robust combination that effectively minimizes or maximizes the objective function,
considering a wide range of potential variations in both the coefficients($a, b, c$) and decision variables from a predefined table ($x, y, z$)."

## Problem Statement
**Objective Function:**
minimize/maximize $(ax + by + cz)$

The example in this repo is minimize case.

**Constraints:**
1. $a>=0, b>=0, c>=0$
2. $a+b+c=1$
3. ideal value of $(a, b, c)$ and possible fluctuations for each are defined
4. a predefined table of all combinations of $(x, y, z)$ that act as decision variables

**Objecitve**:
#### The goal is to find a combination of $(x, y, z)$ among given table that delivers the best expected performance, taking into account the variability and likelihood of different $(a, b, c)$ scenarios.

## Methodology
The approach consists of two main steps:
1. **Coefficient Uncertainty Analysis (`coeff_analysis.py`)**: Analyzes the fluctuations of coefficient $(a, b, c)$, by generating a set of feasible parameter combinations along with their appearance rates based on a simple linear formula. This step lays the foundation for understanding the impact of parameter variability on the objective function.
2. **Optimization of Decision Variables (`decision_optimization.py`)**: Assesses each predefined combination of $(x, y, z)$ and the best selection order across across different possible coefficient combinations. It computes a performance score for each variable combination, aiming to identify the combination that minimizes/maximizes the objective function in a robust manner.

## Application Example: Cost Minimization in Tapioca Store Ingredient Procurement

### Objective
Minimize procurement costs for milk, tea, and tapioca pearls by leveraging price differences across supermarkets.

### Coefficients
- **a, b, c:** Daily sales ratios for milk, tea, and tapioca pearls which might changed day by day. This sums up to 1.

### Decision Variables from Given Table
- **x, y, z:** Variable prices for milk, tea, and tapioca pearls across 10 supermarkets, reflecting the cost landscape's complexity and variability. Converting this to a table satisfy the uncertainty we can have in choosing xyz.

### Approach
1. **Market Analysis:** Identify price variations for each ingredient across supermarkets.
2. **Supermarket Selection:** Choose supermarkets that offer the best prices aligned with the sales ratios of milk, tea, and tapioca pearls, minimizing overall costs.

By applying the equation \(ax + by + cz\) within this framework, the store can in the given order would effectively minimize ingredient costs, enhancing profitability.
