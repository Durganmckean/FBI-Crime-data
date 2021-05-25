#violent_crimes_plot[DM].py
import matplotlib.pyplot as plt

violentCrimesFile = open('violentCrimes.txt')
crimesList = violentCrimesFile.readlines()

print(crimesList)

#convert the crimesist from strings to integers
for i in range(len(crimesList)):
    crimesList[i] = float(crimesList[i])

print(crimesList)

dates = range(2000, 2020)

plt.plot(dates, crimesList)
plt.show()