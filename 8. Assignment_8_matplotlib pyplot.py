***ASSIGNMENT_8***


# Exercise 1

import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016],
    "City A": [500000, 550000, 600000, 650000, 700000, 750000, 800000],
    "City B": [800000, 850000, 900000, 950000, 1000000, 1050000, 1100000],
    "City C": [1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000],
    "City D": [1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000]
}

df = pd.DataFrame(data)

df.plot(x="Year", y=["City A", "City B", "City C", "City D"], marker='o', figsize=(10, 6))

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth of Cities Over Time")
plt.legend()
plt.grid(True)

plt.show()


# Exercise 2

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Hours Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Test Scores": [93, 57, 61, 54, 51, 53, 87, 81, 83, 85]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Hours Studied", y="Test Scores", data=df, color='blue', s=100, edgecolor='black')

plt.xlabel("Hours Studied")
plt.ylabel("Test Scores")
plt.title("Relationship Between Hours Studied and Test Scores")
plt.grid(True)

plt.show()



# Exercise 3

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [11860, 10480, 4997, 5523, 13965, 6011, 13158, 9533, 5158, 9058, 11346, 6675]

plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='skyblue', edgecolor='black')

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Total Sales Per Month")

plt.grid(axis='y', linestyle='--', alpha=0.8)
plt.show()

