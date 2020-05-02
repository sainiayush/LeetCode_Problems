## Greedy Algorithms

* Make a greedy choice and reduction to sub-problem.
* Sub-problem is problem with same king but having fewer parameters.
* We have to make sure our greedy choice is a safe move.
    * ##### Examples of safe moves:
        * Put max digit first
        * Find first occurence of first character
        * Cover leftmost point
        * Use item with max value per unit of weight

> Greedy Problems can be faster after sorting.


## Divide and Conquer Strategy
* We have a problem. We divide that problem into sub-problems. This subproblems are similar type as original problem.
* We recursively solve each sub-problem using same strategy.
* Combine the results.
* ##### Standard algorithms: 
    * Binary Search
    * Merge Sort
    * Quick Sort    
    
    
## Dynamic Programming
* Break problem in to sub-problem.
* Find optimal solution sub-problem.
* Store the results of sub-problem .
* Reuse the stored results to reduce the calculation.
* Final Output.
* Two methods for solving DP problems.
    * ##### Memoization (Top Down)
        * It is similar to recursive way of solving a problem.
        * We initialize lookup array.
        * Whenever we need solution to sub-problem, we look into lookup array.
        * If solution present in lookup array, return the value otherwise we calculate the value and put in the lookup array.
    * ##### Tabulation (Bottom Up)
        * Build table from bottom up fashion and return the last value from the table.


* DP applicable to problems having properties :
    * ##### Overlapping sub-problems
    * ##### Optimal substructure

        
