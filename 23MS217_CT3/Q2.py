# Importing the libraries
import numpy as np
import random
import matplotlib.pyplot as plt


# Starting point and making the list for plotting
gold_price_today_naive = float(input("Enter the today gold price for naive case (in K): "))
gold_price_today_opt = float(input("Enter the today gold price for optimum case (in K): "))
gold_price_list_naive = [gold_price_today_naive]
gold_price_list_opt = [gold_price_today_opt]
day_naive = 0
day_opt = 0
day_list_naive = [day_naive]
day_list_opt = [day_opt]
# Run simulation and probabilistic approach
for i in range(1,11):
    prob = random.randint(1,3)
    if prob == 1: #price increase
        gold_price_today_naive += 5
    elif prob == 3: #price decrease
        gold_price_today_naive -= 5
    else: #price same
        gold_price_today_naive += 0
    day_naive += 1
    gold_price_list_naive.append(gold_price_today_naive) # making the naive list for gold price
    day_list_naive.append(day_naive)
    
    # making the normal distribution for slective value thinking
    o = abs(np.random.normal(0, 1, 1))
    max1 = np.max(o)
    min1 = np.min(o)
    normal = [(x-min1)/(max1-min1) for x in o]
    for x in o:
        if x < 0.4:
            gold_price_today_opt -= 5
        elif x < 0.8:
            gold_price_today_opt += 0
        else :
            gold_price_today_opt += 5
        day_opt += 1
        gold_price_list_opt.append(gold_price_today_opt) # # making the optimistic list for gold price
        day_list_opt.append(day_opt)
            
            
            
# print(day_list_naive,day_list_opt,gold_price_list_naive,gold_price_list_opt)
# plotting the lists.
plt.plot(day_list_naive,gold_price_list_naive,'r-o',label = "naive") 
plt.plot(day_list_opt,gold_price_list_opt,'g-o',label = "optimistic") 
plt.xlabel("day")
plt.ylabel("gold price in K")
plt.title("Gold rate simulation for 10 days")
plt.legend()
plt.grid(True)
plt.show()
print(normal)
         