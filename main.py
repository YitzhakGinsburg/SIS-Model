from datetime import datetime
import matplotlib.pyplot as plt
import scipy

b = 0.01
r_values = []
x_values = []
f = lambda t, x: -0.05*x+b*x-b*x*x
for j in range(50):
    solution = scipy.integrate.RK45(fun=f, t0=0, y0=[0.1], t_bound=500, first_step=0.1, max_step=1, rtol=1e-3,
                                        atol=1e-3, vectorized=False)
    for i in range(10000):
        # get solution step state
        solution.step()
        x = solution.y[0]
        # break loop after modeling is finished.
        if solution.status == 'finished':
            break
    r_values.append(b*20)
    x_values.append(x)
    b += 0.005
plt.plot(r_values, x_values)
plt.show()
