"""
nozzle_calc.py
--------------
Calculates isentropic flow properties for a convergent-divergent rocket nozzle.

Inputs:
- Exit Mach number (Me)
- Specific heat ratio (gamma)
- Throat diameter (Dt)

Outputs:
- Area ratio (Ae/At)
- Exit pressure ratio (Pe/P0)
- Exit temperature ratio (Te/T0)
- Exit diameter (De)
- Nozzle length (L) for 15° semi-angle
"""

import math

# === Input Parameters ===
Me = 2.8                 # Exit Mach number
gamma = 1.22             # Specific heat ratio
Dt = 20                  # Throat diameter in mm
semi_angle_deg = 15      # Conical nozzle semi-angle (degrees)

# === Calculations ===

# Pressure ratio
Pe_P0 = (1 + ((gamma - 1)/2) * Me**2) ** (-gamma / (gamma - 1))

# Temperature ratio
Te_T0 = (1 + ((gamma - 1)/2) * Me**2) ** -1

# Density ratio (optional)
rhoe_rho0 = (1 + ((gamma - 1)/2) * Me**2) ** (-1 / (gamma - 1))

# Area ratio (Ae/At)
Ae_At = (1 / Me) * ((2 / (gamma + 1)) * (1 + ((gamma - 1)/2) * Me**2)) ** ((gamma + 1) / (2 * (gamma - 1)))

# Exit diameter
De = Dt * math.sqrt(Ae_At)

# Nozzle length (for 15° conical nozzle)
L = (De - Dt) / (2 * math.tan(math.radians(semi_angle_deg)))

# === Output ===
print("===== Isentropic Nozzle Calculations =====")
print(f"Exit Mach Number (Me): {Me}")
print(f"Pressure Ratio (Pe/P0): {Pe_P0:.4f}")
print(f"Temperature Ratio (Te/T0): {Te_T0:.4f}")
print(f"Density Ratio (rho_e/rho_0): {rhoe_rho0:.4f}")
print(f"Area Ratio (Ae/At): {Ae_At:.2f}")
print(f"Throat Diameter (Dt): {Dt} mm")
print(f"Exit Diameter (De): {De:.2f} mm")
print(f"Nozzle Length (L): {L:.2f} mm")
