import matplotlib.pyplot as plt 


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
primes = [2, 3, 5, 7, 11, 13]
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

# calculating data automatically
x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth = 3)
#ax.plot(primes)

# plotting and styling individual points with scatter
#ax.scatter(2, 4, s=200)
#ax.scatter(x_values, y_values, c=(0, 0.2, 0), s=1)#rgb
#ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)#colormap



# set the range for each axis
#ax.axis([0, 1100, 0, 1100000])

# set chart title and label axes
ax.set_title('Square Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Value', fontsize = 14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()