from datetime import datetime
import matplotlib.pyplot as plt

x_tol = 1e-3
print(x_tol)

def runge_kutta(f, t_0, x_0, h):
    k_0 = f(t_0, x_0)
    k_1 = f(t_0 + h/2, x_0 + h/2 * k_0)
    k_2 = f(t_0 + h/2, x_0 + h/2 * k_1)
    k_3 = f(t_0 + h, x_0 + h * k_2)

    step_x = x_0 + h/6 * (k_0 + 2.0*k_1 + 2.0*k_2 + k_3)
    k = 1/6 * (k_0 + 2.0*k_1 + 2.0*k_2 + k_3)

    k_1 = f(t_0 + h/4, x_0 + h * k_0/4)
    k_2 = f(t_0 + h/4, x_0 + h * k_1/4)
    k_3 = f(t_0 + h/2, x_0 + h * k_2/2)
    half_step_x = x_0 + h/12 * (k_0 + 2 * k_1 + 2 * k_2 + k_3)

    k_1 = f(t_0 + h, x + h * k_0)
    k_2 = f(t + h, x + h * k_1)
    k_3 = f(t + 2 * h, x + 2 * h * k_2)
    # Combine partial steps.
    dbl_step_x = x + h / 3 * (k_0 + 2 * k_1 + 2 * k_2 + k_3)

    t_1 = t_0 + h
    x_1 = x_0 + h * k

    return t_1, x_1


def f(t, x):
    return -0.1*x+0.04*x-0.04*x*x


if __name__=="__main__":
    t_0 = 0.0
    x_0 = 0.1

    h = 0.1
    h_min = 0.001

    t_values = [t_0]
    x_values = [x_0]

    x = x_0
    t = t_0
    for _ in range(10000):
        t, x = runge_kutta(f, t, x, h)
        x_values.append(x)
        t_values.append(t)
        print(t, x)

    # Plot solution
    plt.plot(t_values, x_values)
    plt.show()