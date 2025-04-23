# Importing of Matplotlib Library
import matplotlib.pyplot as plt
# Defining Countries List
countrey = ["Canada","China","Denmark","France","India","Israel","Italy","Netherlanda","Norway","Switzerland","UK","USA","Venezuela"]
# Defining Number of turings list
Number_Turing = [6,2,1,1,1,6,1,1,2,1,7,52,1]
# plotting the pie chart
plt.pie(Number_Turing,labels=countrey)
# Giving title
plt.title("countrywise turing awards")
plt.legend()
# Showing the plot
plt.show()
# Saving the file
plt.savefig("pie.png")