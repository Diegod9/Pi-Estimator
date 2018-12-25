

import numpy as np
import matplotlib.pyplot as plt
import time as time

# input total number of random points
total_random_points = int(input("\nNumber of random points for Monte Carlo estimate of Pi?\n>"))

# number of random points inside unit cicrle and total random points
inside_circle = 0

# create empty x and y arrays for eventual scatter plot of generated random points
x_plot_array = np.empty(shape=(1,total_random_points))
y_plot_array = np.empty(shape=(1,total_random_points))

# generate random points and count points inside unit circle
# top right quadrant of unit cicrle only
for i in range(0, total_random_points):
    x = np.random.rand()
    x_plot_array = np.append(x_plot_array, [x])
    y = np.random.rand()
    y_plot_array = np.append(y_plot_array, [y])
    x_squared = x**2
    y_squared = y**2
    if np.sqrt(x_squared + y_squared) < 1.0:
        inside_circle += 1
    pi_approx = inside_circle / (i+1) * 4

# Output
print ("\n--------------")
print (f"\nApproximate value for pi: {pi_approx}")
print(f"Number of darts inside the circle: {inside_circle}")
print (f"Difference to exact value of pi: {pi_approx-np.pi}")
print (f"Percent Error: {(pi_approx-np.pi)/np.pi*100}%")

# plot output of random points and circle, top right quadrant only
random_points_plot = plt.scatter(x_plot_array, y_plot_array, color='blue', s=.1)
circle_plot = plt.Circle( ( 0, 0 ), 1, color='red', linewidth=2, fill=False)

ax = plt.gca()
ax.cla()

ax.add_artist(random_points_plot)
ax.add_artist(circle_plot)

plt.show()