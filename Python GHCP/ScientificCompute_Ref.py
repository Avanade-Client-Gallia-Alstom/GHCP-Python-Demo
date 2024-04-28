import numpy as np
from scipy.integrate import odeint

import matplotlib.pyplot as plt

def electrical_system(state, t):
    # Define the differential equation for the electrical system
    def system_equation(state, t):
        # Define the parameters and variables of the electrical system
        R = 1.0  # Resistance
        L = 0.5  # Inductance
        C = 0.2  # Capacitance
        V = 10.0  # Voltage source

        # Extract the variables from the state vector
        i, q = state

        # Define the differential equations for current and charge
        di_dt = (V - R * i - q / C) / L
        dq_dt = i

        return [di_dt, dq_dt]

    # Solve the differential equation using scipy's odeint function
    solution = odeint(system_equation, state, t)

    # Extract the current and charge from the solution
    current = solution[:, 0]
    charge = solution[:, 1]

    # Plot the current and charge as a function of time
    plt.plot(t, current, label='Current')
    plt.plot(t, charge, label='Charge')
    plt.xlabel('Time')
    plt.ylabel('Current/Charge')
    plt.legend()
    plt.show()

# Example usage
state = [0.0, 0.0]  # Initial state: current = 0, charge = 0
t = np.linspace(0, 10, 100)  # Time range: 0 to 10 seconds with 100 points
electrical_system(state, t)