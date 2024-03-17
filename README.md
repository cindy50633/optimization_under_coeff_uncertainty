# Robust Optimization of Decision Variables under Coefficient Uncertainty
This repository demonstrate a method for selecting the optimal combination of decision variables from a predefined set,
under the influence of uncertain coefficients.
It specifically addresses the challenge of optimizing the objective function $ax + by + cz$ in the face of coefficient fluctuations,
aiming to identify the most robust combination that minimizes/maximizes the objective function across a range of possible combinations of coefficients $(a, b, c)$.

## Problem Statement
**Objective Function:**
minimize/maximize $(ax + by + cz)$

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

## Application
WIP
