from datetime import datetime
import matplotlib.pyplot as plt
from math import exp, sqrt

def runge_kutta(f, x_0, y_0, h):
    k_0 = f(x_0, y_0)
    k_1 = f(x_0 + h/2, y_0 + h/2 * k_0)
    k_2 = f(x_0 + h/2, y_0 + h/2 * k_1)
    k_3 = f(x_0 + h, y_0 + h * k_2)

    k = 1/6 * (k_0 + 2.0*k_1 + 2.0*k_2 + k_3)

    x_1 = x_0 + h
    y_1 = y_0 + h * k

    return x_1, y_1


def f(x, y):
    return -0.02*y+0.04*y-0.04*y*y


if __name__=="__main__":
    # Initial values
    x_0 = 0.0
    y_0 = 0.1

    # Step length 
    h = 0.1

    x_values = [x_0]
    y_values = [y_0]

    # Calculate solution
    x = x_0
    y = y_0
    for _ in range(10000):
        x, y = runge_kutta(f, x, y, h)
        x_values.append(x)
        y_values.append(y)
        print(x, y)

    # Plot solution
    plt.plot(x_values, y_values)
    plt.show()