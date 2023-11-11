
import matplotlib.pyplot as plt
import numpy as np

# Define the temperature and volume arrays for the four stages of the Otto cycle
# Stage 1: Isentropic compression
T1 = 600 # K
V1 = 0.002 # m^3
P1 = 101.325 # kPa
gamma = 1.4
V2 = V1/10
T2 = T1*(V1/V2)**(gamma-1)
P2 = P1*(V1/V2)**gamma
T_s = np.linspace(T1, T2, 100)
V_s = V1*(T_s/T1)**(1/(gamma-1))

# Stage 2: Isobaric heat addition
V3 = V2
P3 = P2
T3 = 2000 # K
V4 = V1
P4 = P3*(V3/V4)**gamma
T4 = T3*(V3/V4)**(gamma-1)
T_h = np.linspace(T2, T3, 100)
V_h = V3*(T_h/T3)**(1/(gamma-1))

# Stage 3: Isentropic expansion
V5 = V4
P5 = P4
T5 = T4*(V4/V5)**(gamma-1)
V6 = V3
P6 = P5*(V5/V6)**gamma
T_c = np.linspace(T5, T1, 100)
V_c = V5*(T_c/T5)**(1/(gamma-1))

# Stage 4: Isobaric heat rejection
V1 = V6
P1 = P6
T1 = T_c[-1]
T_l = np.linspace(T4, T1, 100)
V_l = V1*(T_l/T4)**(1/(gamma-1))

# Convert pressure from Pa to kPa
P1 /= 1000
P2 /= 1000
P3 /= 1000
P4 /= 1000
P5 /= 1000
P6 /= 1000

# Plot the cycle on a PV diagram
fig, ax = plt.subplots()
ax.plot([V1, V2], [P1, P2], 'b-', label='1-2: Isentropic compression')
ax.plot([V2, V3], [P2, P3], 'r-', label='2-3: Isobaric heat addition')
ax.plot([V3, V4], [P3, P4], 'g-', label='3-4: Isentropic expansion')
ax.plot([V4, V1], [P4, P1], 'c-', label='4-1: Isobaric heat rejection')
ax.set_xlabel('Volume (m^3)')
ax.set_ylabel('Pressure (kPa)')
ax.set_title('Otto Cycle on a PV Diagram')
ax.legend()
plt.show()

# Plot the cycle on a TS diagram
fig, ax = plt.subplots()
ax.plot(T_s, V_s, 'b-', label='1-2: Isentropic compression')
ax.plot(T_h, V_h, 'r-', label='2-3: Isobaric heat addition')
ax.plot(T_c, V_c, 'g-', label='3-4: Isentropic expansion')
ax.plot(T_l, V_l, 'c-', label='4-1: Isobaric heat rejection')
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Volume (m^3)')
ax.set_title('Otto Cycle on a TS Diagram')
ax.legend()
plt.show()
