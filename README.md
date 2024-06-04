# Knapsack-in-python

In this we're discussing the knapsack problem with greedy and dynamic approach.

Greedy approach = Fractional Knapsack
Pesudocode:

    function fractionalKnapsack(items, capacity)
    
          items.sort(key=lambda item: item[0] / item[1],    reverse=True)  
          
         totalValue <- 0
         
        for item in items
        
           if capacity == 0
           
               break
               
           fraction <- min(capacity / item[1], 1)
           
         totalValue += fraction * item[0]
         
         capacity -= fraction * item[1]
         
     return totalValue


Dynamic Programming = O/1 Knapsack
Pesudocode:


    function knapsack(values, weights, capacity)
   
         n <- len(values)
         
         dp <- [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

         for i in range 1 to n + 1
         
            for j in range 1 to capacity + 1
          
                if weights[i - 1] > j
                
                    dp[i][j] = dp[i - 1][j]
                    
               else
               
                    dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])

           return dp[n][capacity]


