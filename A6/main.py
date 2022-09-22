import matplotlib.pyplot as plt
import numpy as np

ratings = open("ratings.csv", 'r')
roster = open('roster.csv', 'r')

ratingsP=[]
ratingsR=[]

def parse():
    for line in ratings:
        x = line.split(',', 1)
        ratingsP.append(x[0])
        ratingsR.append(float(x[1].split("'\'")[0]))

parse()
print(ratingsP, ratingsR)

plt.bar(ratingsP,ratingsR)
plt.title('Professor Ratings')
plt.xlabel('Professor')
plt.ylabel('Rating')
plt.show()


