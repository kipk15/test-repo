import matplotlib.pyplot as plt 

squares = [1, 4, 9, 16, 25]
primes = [2, 3, 5, 7, 11, 13]

fig, ax = plt.subplots()
ax.plot(squares)
ax.plot(primes)

plt.show()