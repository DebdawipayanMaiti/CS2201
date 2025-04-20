"""Take marks of three subjects of three students as 
input. marks1 contain the marks of three subjects of 
student 1; similarly store marks2 and marks3. 
Also, take their names. Now store the subjectwise average 
(use numpy.mean(): see https://docs.vultr.com/python/third-party/numpy/mean) in avg and plot 
student-wise average marks using matplotlib.pyplot.bar. An example plot is given below."""



# names = input("Give student first names (space separated, put enter to finish): ").split(" ")
# marks1 = input("Give marks of student 1 (space separated, put enter to finish): ").split(" ")
# marks2 = input("Give marks of student 2 (space separated, put enter to finish): ").split(" ")
# marks3 = input("Give student marks of student 3 (space separated, put enter to finish): ").split(" ")

# import numpy as np
# marks1_np = np.array(marks1, dtype='int')
# marks2_np = np.array(marks2, dtype='int')
# marks3_np = np.array(marks3, dtype='int')
# avg = np.mean([marks1_np, marks2_np, marks3_np], axis = 1)
# print(avg)
# import matplotlib.pyplot as plt
# plt.bar(names, avg)
# plt.xlabel("Students")
# plt.ylabel("Average marks")
# plt.show()

# NOTE: take input in numpy and handling data.




"""Simulate a dice game for a single player named Shakuni. 
The player throws the dice until he gets a six, when he stops. Use random.uniform(a, b) 
[generates uniformly distributed random number between a & b] to simulate the outcome 
using the scheme: random number < 1 ⇒  side ‘one’ appears, random number >=1 and <2 ⇒ side ‘two’ appears 
and so on. Plot the outcomes (along y-axis, with trial number along x-axis) using matplotlib.pyplot.plot. 
Also, indicate the first and last throws as “start” and “stop” respectively on the 
plot using matplotlib.pyplot.text(x, y, t) [prints t on the plot at (x,y)]. An example plot is given below.
"""



# import random
# x = []
# y = []
# for i in range(1, 1000):
#     x.append(i)
#     r = random.uniform(0, 6)
#     if r < 1:
#         print("One")
#         y.append(1)
#     elif r < 2:
#         print("Two")
#         y.append(2)
#     elif r < 3:
#         print("Three")
#         y.append(3)
#     elif r < 4:
#         print("Four")
#         y.append(4)
#     elif r < 5:
#         print("Five")
#         y.append(5)
#     else:
#         print("Six")
#         y.append(6)
#         break
# print(x)
# print(y)
# import matplotlib.pyplot as plt
# plt.plot(x, y, 'o:r')
# plt.xlabel("throws")
# plt.ylabel("number on dice")
# plt.show()
# # plt.savefig("dice.png")



"""Take a sentence (e.g. "Information Retrieval is the science of search engines") as input. Consider a list of stopwords
 (unimportant words) stop.Write a function preprocess that converts the input string to lowercase and removes all the 
 stopwords. Finally print the preprocessed input string on the terminal. The output for the example input will be 
 “information retrieval science search engines”.
"""


# def preprocess(s):
#     s = s.lower()
#     s = s.split()
#     stop = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", 
#         "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
#         "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", 
#         "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
#         "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", 
#         "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", 
#         "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", 
#         "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#     s_out = []
#     for w in s:
#         if w not in stop:
#             s_out.append(w)
#     return s_out
# # str=input("Give a text: ") 
# # print(' '.join(preprocess(str)))


# dict = {"doc1" : "Information Retrieval is the science of search engines", 
#  	"doc2" : "This is the age of information technology", 
#  	"doc3" : "Mathematics in the language of science", 
#  	"doc4" : "Efficient retrieval of important data is the feature of any sound search system.", 
#   	"doc5" : "Gerard Salton is the father of Information Retrieval"}

# for key in dict:
#     dict[key] = preprocess(dict[key])
#     print(' '.join(dict[key]))
    
    
# q = input("Give a string to check words are present: ")
# print(' '.join(preprocess(q)))
# Q1 = 
# if words in q.split():
#     if words in dict[value]:
    
    
# def preprocess(input_string):
#     stop = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", 
#             "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
#             "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
#             "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", 
#             "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", 
#             "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", 
#             "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", 
#             "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", 
#             "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#     words = input_string.lower().split()
#     return set(word for word in words if word not in stop)
# def sort_by_value_desc(item):
#     return item[1]
# documents = {
#     'doc1': "Information Retrieval is the science of search engines",
#     'doc2': "This is the age of information technology",
#     'doc3': "Mathematics in the language of science",
#     'doc4': "Efficient retrieval of important data is the feature of any sound search system.",
#     'doc5': "Gerard Salton is the father of Information Retrieval"
# }
# query = input("Enter a query string: ")
# query_words = preprocess(query)
# at_least_one = []
# all_words = []
# match_counts = {}
# for name in documents:
#     doc_words = preprocess(documents[name])
#     if not query_words.isdisjoint(doc_words):
#         at_least_one.append(name)
#     if query_words.issubset(doc_words):
#         all_words.append(name)
#     match_counts[name] = len(query_words.intersection(doc_words))
# print("Documents containing at least one word from the query:", at_least_one)
# print("Documents containing all words from the query:", all_words)
# sorted_items = sorted(match_counts.items(), key=sort_by_value_desc, reverse=True)
# print("Documents sorted by number of word matches with the query:")
# for item in sorted_items:
#     print(item[0])

    
"""Consider an archery competition where a target is shot at by the participants. Consider that the maximum 
points are obtained by hitting the “bull’s eye” (the centre spot in the yellow zone), where any hit on the 
white zone (or outside) fetches no points. So, each attempt (in the increasing order of success) can be 
termed as 'miss', 'beginner', 'improver', 'seasoned', 'pro' or  'bull’s eye' according as the participant hits 
the white (or outside), black, blue, red, yellow or the bull’s eye respectively. Simulate the competition by a 
normal distribution (use np.random.normal()) such that the probability of hitting the white zone is the 
maximum (occurrence near the mean) and that of hitting the bull’s eye is the minimum (maximum distance away from the mean). 
Finally, plot the distribution of performances after n (large value) attempts as 'miss', 'beginner', 'improver', 'seasoned', 'pro', 
'bull's eye' on a pie chart. An example plot is as below.
"""



# import numpy as np
# s = abs(np.random.normal(0, 1, 1000)) #random sample of size 1000 generated from a normal distribution of mean 0 and s.d. 1
# print(s)
# max1 = np.max(s)
# min1 = np.min(s)
# s1 = [(x-min1)/(max1-min1) for x in s]
# # print(s1)
# sc = np.zeros(6)
# for x in s1:
#     if x < 0.2:
#         sc[0] = sc[0] + 1
#     elif x < 0.4:
#         sc[1] = sc[1] + 1
#     elif x < 0.6:
#         sc[2] = sc[2] + 1
#     elif x < 0.8:
#         sc[3] = sc[3] + 1
#     elif x < 0.95:
#         sc[4] = sc[4] + 1
#     else:
#         sc[5] = sc[5] + 1
# print(sc)
# import matplotlib.pyplot as plt
# plt.pie(sc, labels = ['miss', 'beginner', 'improver', 'seasoned', 'pro', 'bulls-eye']) 
# plt.show()
        

"""Use Rectangular method, Trapezoidal rule and Simpson’s rule applying the original formulas 
to find the approximate integral of the function 1/x in the interval [1, 2]. Compare the approximate values with 
other actual values of the integral. Repeat the above using scipy.integrate for Trapezoidal and Simpson’s rules.
"""

import numpy as np
from scipy.integrate import trapezoid, simpson

# N = 10
# xs, h = np.linspace(1, 2, N, endpoint=False, retstep=True)
# ys = 1 / xs
# # Rectangular Rule
# Irect = h * np.sum(ys)
# print("Rectangular: ",Irect)
# # Trapezoidal Rule (Scipy full name)
# Itrap = trapezoid(ys, xs)
# print("Trapezoidal (scipy): ",Itrap)
# # Simpson's Rule (Scipy full name)
# Isimp = simpson(ys, xs)
# print("Simpson (scipy): ",Isimp)


"""Given the plot of land in the figure below, use the formula of Rectangular rule 
to approximate the area (shown in black). Do the same using both the original formulas 
and scipy implementations of Trapezoidal rule and Simpson’s rule. Compute the actual 
area (hint: use the formula of a circle) and compare the approximate values for this 
area by printing the percentage accuracy (abs(approx-actual)/actual)*100) for all the 
above approximate values.
"""

# # Define parameters
# r = 5
# N = 100  # Number of subintervals (increase for better accuracy)
# xs, h = np.linspace(0, r, N, endpoint=False, retstep=True)
# ys = np.sqrt(r**2 - xs**2)
# # Rectangular rule
# Irect = h * np.sum(ys)
# # Trapezoidal rule
# Itrap = trapezoid(ys, xs)
# # Simpson’s rule
# xs_full = np.linspace(0, r, N + 1)  # Simpson needs odd number of intervals (even number of points)
# ys_full = np.sqrt(r**2 - xs_full**2)
# Isimp = simpson(ys_full, xs_full)
# # Actual area = quarter circle
# actual = (np.pi * r**2) / 4
# # Accuracy
# def accuracy(approx, actual):
#     return abs(approx - actual) / actual * 100
# # Print results
# print("Actual Area =", actual)
# print("Rectangular =", Irect, "Accuracy =", accuracy(Irect, actual), "%")
# print("Trapezoidal =", Itrap, "Accuracy =", accuracy(Itrap, actual), "%")
# print("Simpson =", Isimp, "Accuracy =", accuracy(Isimp, actual), "%")


"""Given the plot of land in the figure below, use the formula of Rectangular rule to 
approximate the area (shown in black). Do the same using both the original formulas and 
scipy implementations of Trapezoidal rule and Simpson’s rule. Compute the actual area 
(hint: area between an ellipse and a circle) and compare the approximate values for this 
area by printing the percentage accuracy (abs(approx-actual)/actual)*100) for all the 
above approximate values.
"""

# # Integration bounds
# a = 4
# b = 5
# N = 100  # Number of intervals
# # Define x values and step size
# xs, h = np.linspace(a, b, N, endpoint=False, retstep=True)
# # Define function: area between upper parts of outer and inner circles
# ys = np.sqrt(36 - xs**2) - np.sqrt(16 - xs**2)
# # Rectangular Rule
# Irect = h * np.sum(ys)
# # Trapezoidal Rule (Scipy)
# Itrap = trapezoid(ys, xs)
# # Simpson’s Rule (Scipy)
# xs_full = np.linspace(a, b, N + 1)
# ys_full = np.sqrt(36 - xs_full**2) - np.sqrt(16 - xs_full**2)
# Isimp = simpson(ys_full, xs_full)
# actual = simpson(ys_full, xs_full)
# # Accuracy function
# def accuracy(approx, actual):
#     return abs(approx - actual) / actual * 100
# # Print results
# print("Actual Area =", actual)
# print("Rectangular =", Irect, "Accuracy =", accuracy(Irect, actual), "%")
# print("Trapezoidal =", Itrap, "Accuracy =", accuracy(Itrap, actual), "%")
# print("Simpson =", Isimp, "Accuracy =", accuracy(Isimp, actual), "%")



"""For the overall betterment of institute performance at the national level, the Football Club of IISER Kolkata has decided 
to apply data science to the player performance statistics. The first application is to segregate the strikers based on 
their goal-scoring performance and expose them to customized training. To be more specific, the strikers with similar goal-scoring performance 
in the similar number of matches, should be trained together.To this end, consider a pool of n (>=10) strikers with 
(num_of_matches, number_of_goals_scores) for each player and apply k-means clustering algorithm (implemented in sklearn) to meaningfully 
cluster them. Use the elbow method to determine the best choice for k and finally plot the clusters with the chosen value of k. You should 
plot the data before and after clustering as well as the elbow plot.An example dataset is uploaded as “data-ungradedset.csv” to WeLearn. 
Please use this dataset (a) without pandas (directly storing them in x, y) and (b) with pandas (read the csv)."""

# import matplotlib.pyplot as plt
# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [10, 2, 14, 4, 9, 5, 4, 10, 10, 2]
# plt.scatter(x, y)
# plt.show()
# from sklearn.cluster import KMeans
# data = list(zip(x, y))
# inertias = []
# for i in range(1,11):
#     kmeans = KMeans(n_clusters=i)
#     kmeans.fit(data)
#     inertias.append(kmeans.inertia_)
# plt.plot(range(1,11), inertias, marker='o')
# plt.title('Elbow method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(data)
# plt.scatter(x, y, c=kmeans.labels_)
# plt.show()

























