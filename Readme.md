# RANDOM WALK PROGRAM
Creating a random walk program that tries to minimise the amount of money a user spends on Lyft. Doing in python

## Problem statement:
Using Monte Carlo simulation technique, perform a random walk simulation to find the optimal block size for which on average, you can walk the most number of blocks with the least amount of money.

## Approach:
Conduct n number of walk trails and compute on average the percentage of walks that are fewer than 6 blocks


## Assumptions:
   1. Looking at walks upto 100 blocks is sufficient for correct deduction for optimisation. 
   1. User takes Lyft only for distances greater than 6 blocks
   1. All lyft rides cost $10
   1. The highest ratio for total blocks walked to total money spent gives the most blocks you can walk for least amount of money
   1. Total amount paid for simulation on a block size sample is at least 1 (this is needed to avoid divide by zero when calculating average) 


## To Dos:
- [X] Implement in python 

