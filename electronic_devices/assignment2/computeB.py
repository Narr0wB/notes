
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

def err(x, y):
    return (x - y)/y

pf = "./padre_data"

bias_conduction_band = np.genfromtxt(pf + "/exB" + "/ConductionBandPotential.txt", delimiter=",", skip_header=4)
bias_valence_band    = np.genfromtxt(pf + "/exB" + "/ValenceBandPotential.txt", delimiter=",", skip_header=4)
bias_intrinsic_fermi = np.genfromtxt(pf + "/exB" + "/ElectrostaticPotential.txt", delimiter=",", skip_header=4)
# bias_qfp             = np.genfromtxt(pf + "/exB" + "/pQuasiFermiLevel.txt", delimiter=",", skip_header=4)
# bias_qfn             = np.genfromtxt(pf + "/exB" + "/nQuasiFermiLevel.txt", delimiter=",", skip_header=4)
bias_charge          = np.genfromtxt(pf + "/exB" + "/NetChargeConcentration.txt", delimiter=",", skip_header=4)
bias_efield          = np.genfromtxt(pf + "/exB" + "/ElectricField.txt", delimiter=",", skip_header=4)
bias_ec              = np.genfromtxt(pf + "/exB" + "/ElectronCurrent.txt", delimiter=",", skip_header=4)
bias_hc              = np.genfromtxt(pf + "/exB" + "/HoleCurrent.txt", delimiter=",", skip_header=4)
bias_tc              = np.genfromtxt(pf + "/exB" + "/TotalCurrent.txt", delimiter=",", skip_header=4)

eq_conduction_band = np.genfromtxt(pf + "/exA" + "/QA1_conduction_band.txt", delimiter=",", skip_header=4)
eq_valence_band    = np.genfromtxt(pf + "/exA" + "/QA1_valence_band.txt", delimiter=",", skip_header=4)
eq_intrinsic_fermi = np.genfromtxt(pf + "/exA" + "/QA1_intrinsic_fermi.txt", delimiter=",", skip_header=4)
eq_fermi           = np.genfromtxt(pf + "/exA" + "/QA1_fermi_level.txt", delimiter=",", skip_header=4)
eq_charge          = np.genfromtxt(pf + "/exA" + "/QA2_net_charge.txt", delimiter=",", skip_header=4)
eq_efield          = np.genfromtxt(pf + "/exA" + "/QA3_electric_field.txt", delimiter=",", skip_header=4)

iv_reverse = np.genfromtxt(pf + "/exB" + "/QB2_reverse_iv.txt", delimiter=",", skip_header=4)
iv_forward = np.genfromtxt(pf + "/exB" + "/QB2_iv.txt", delimiter=",", skip_header=4)


plt.figure(1)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Energy (eV)")
plt.grid(True, alpha=0.3)

h_1 = 155
l_1 = 25
h_2 = 160
l_2 = 25

plt.plot(bias_conduction_band[l_1:h_1, 0], bias_conduction_band[l_1:h_1, 1], label=r"$\overline{E_{c}}$ @ 0.6V")
plt.plot(bias_valence_band[l_1:h_1, 0], bias_valence_band[l_1:h_1, 1], label=r"$\overline{E_{v}}$ @ 0.6V")
plt.plot(bias_intrinsic_fermi[l_1:h_1, 0], bias_intrinsic_fermi[l_1:h_1, 1] * -1, label=r"$\overline{E_{f_i}}$ @ 0.6V")

plt.plot(eq_conduction_band[l_2:h_2, 0], eq_conduction_band[l_2:h_2, 1], label=r"$\overline{E_{c}}$ @ eq.", linestyle="--")
plt.plot(eq_valence_band[l_2:h_2, 0], eq_valence_band[l_2:h_2, 1], label=r"$\overline{E_{v}}$ @ eq.", linestyle="--")
plt.plot(eq_intrinsic_fermi[l_2:h_2, 0], eq_intrinsic_fermi[l_2:h_2, 1] * -1, label=r"$\overline{E_{f_i}}$ @ eq.", linestyle="--")

plt.legend()
plt.savefig("./plots/QB1_plot.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


plt.figure(2)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Charge (C/$\text{cm}^{3}$)")
plt.grid(True, alpha=0.3)

plt.plot(bias_charge[25:155, 0], bias_charge[25:155, 1], label=r"$\overline{\rho}(x)$ @ 0.6V")
plt.plot(eq_charge[25:150, 0], eq_charge[25:150, 1], label=r"$\overline{\rho}(x)$ @ eq.", linestyle="--")
plt.axvline(167.816, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168.045, color="gray", linestyle=":", alpha=0.8)

plt.legend()
plt.savefig("./plots/QB1_plot_2.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


plt.figure(3)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Charge (C/$\text{cm}^{3}$)")
plt.grid(True, alpha=0.3)

xp = 0.133
xn = 0.022

x = np.linspace(167.4, 168.5, 200)
conditions = [x < (168 - xp), x > (168 - xp), x > 168, x > (168 + xn)] 
functions = [lambda x: 0, lambda x: -1e16 * 1.6e-19, lambda x: 6e16 * 1.6e-19, lambda x: 0]
y_1 = np.piecewise(x, conditions, functions)
conditions = [x < (168 - 0.29), x > (168 - 0.29), x > 168, x > (168 + 0.05)] 
functions = [lambda x: 0, lambda x: -1e16 * 1.6e-19, lambda x: 6e16 * 1.6e-19, lambda x: 0]
y_2 = np.piecewise(x, conditions, functions)
plt.plot(x, y_1, label=r"$\rho(x)$ @ 0.6V")
plt.plot(x, y_2, label=r"$\rho(x)$ @ eq.", linestyle="--")
plt.axvline(168 - xp, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168 + xn, color="gray", linestyle=":", alpha=0.8)

plt.legend()
plt.savefig("./plots/QB1_plot_3.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


plt.figure(4)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Electric Field (V/cm)")
plt.grid(True, alpha=0.3)

plt.plot(bias_efield[25:155, 0], bias_efield[25:155, 1], label=r"$\overline{E}(x)$ @ 0.6V")
plt.plot(eq_efield[25:180, 0], eq_efield[25:180, 1], label=r"$\overline{E}(x)$ @ eq.", linestyle="--")
plt.axvline(167.816, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168.045, color="gray", linestyle=":", alpha=0.8)

plt.legend()
plt.savefig("./plots/QB1_plot_4.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


plt.figure(5)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Electric Field (V/cm)")
plt.grid(True, alpha=0.3)

es = 1.04e-12
xp = 0.12
xn = 0.022
xj = 168

x = np.linspace(167.4, 168.4, 200)

conditions = [x < (xj - xp), x > (xj - xp), x > xj, x > (xj + xn)] 
functions = [lambda x: 0, lambda x: (-1e16/es)*((x - xj) + xp)*(1e-4 * 1.6e-19), lambda x: (-1e16/es)*(xp * 1e-4 * 1.6e-19) + (6e16/es)*(x - xj)*(1e-4 * 1.6e-19), lambda x: 0]
y1 = np.piecewise(x, conditions, functions)
plt.axvline(168 - xp, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168 + xn, color="gray", linestyle=":", alpha=0.8)

xp = 0.29
xn = 0.05
conditions = [x < (xj - xp), x > (xj - xp), x > xj, x > (xj + xn)] 
functions = [lambda x: 0, lambda x: (-1e16/es)*((x - xj) + xp)*(1e-4 * 1.6e-19), lambda x: (-1e16/es)*(xp * 1e-4 * 1.6e-19) + (6e16/es)*(x - xj)*(1e-4 * 1.6e-19), lambda x: 0]
y2 = np.piecewise(x, conditions, functions)

plt.plot(x, y1, label=r"$E(x)$ @ 0.6V")
plt.plot(x, y2, label=r"$E(x)$ @ eq.", linestyle="--")
print(np.min(y1))
print(np.min(bias_efield[:, 1]))
print(err(np.min(y1), np.min(bias_efield[:, 1])))

plt.legend()
plt.savefig("./plots/QB1_plot_5.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


fig, ax = plt.subplots(num=6)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Current density (A/$\text{cm}^{2}$)")

l = 0 
h = 200 
plt.ylim(-0.5, 0.5)
plt.plot(bias_ec[l:h, 0], bias_ec[l:h, 1], label=r"$\overline{J_{n}}$")
plt.legend()
plt.grid(True, alpha=0.3)

axins = inset_axes(ax, width="30%", height=1.5, loc="lower right") 
axins.plot(bias_ec[l:h, 0], bias_ec[l:h, 1])
axins.set_xlim(167.8, 168.2)
axins.set_ylim(0.1, 0.3)
axins.set_xticks([])
axins.set_yticks([])
mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5")

plt.savefig("./plots/QB1_plot_6.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


fig, ax = plt.subplots(num=7)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Current density (A/$\text{cm}^{2}$)")

l = 0 
h = 200 
plt.ylim(-0.5, 0.5)
plt.plot(bias_hc[l:h, 0], bias_hc[l:h, 1], label=r"$\overline{J_{p}}$")
plt.legend()
plt.grid(True, alpha=0.3)

axins = inset_axes(ax, width="30%", height=1.5, loc="lower right") 
axins.plot(bias_hc[l:h, 0], bias_hc[l:h, 1])
axins.set_xlim(167.8, 168.2)
axins.set_ylim(-0.1, 0.1)
axins.set_xticks([])
axins.set_yticks([])
mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5")

plt.savefig("./plots/QB1_plot_7.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


plt.figure(8)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Current density (A/$\text{cm}^{2}$)")
plt.ylim(-0.5, 0.5)

l = 0 
h = 200 
plt.plot(bias_tc[l:h, 0], bias_tc[l:h, 1], label=r"$\overline{J}$")
plt.grid(True, alpha=0.3)

plt.legend()
plt.savefig("./plots/QB1_plot_8.png", dpi=300, bbox_inches="tight", pad_inches=0.005)


# ----------------------------------------------------------------


# --- 1. Constants & Parameters ---
q = 1.602e-19       # Charge (C)
kb = 1.38e-23       # Boltzmann (J/K)
T = 300             # Temperature (K)
epsilon_0 = 8.854e-14 # F/cm (Vacuum permittivity)
epsilon_si = 11.7   # Relative permittivity of Silicon
epsilon = epsilon_si * epsilon_0

# Device Doping & Dimensions
NA = 1e16           # p-side doping (cm^-3)
ND = 6e16           # n-side doping (cm^-3)
ni = 1.0e10         # Intrinsic concentration (cm^-3) - using standard approx
Va = 0.6            # Applied Bias (V)
L_device_um = 336   # Total Length (um)
xj_um = 168         # Junction Position (um)

# Carrier Properties (From your previous inputs)
mun = 1258          # Electron mobility (cm^2/Vs)
mup = 446           # Hole mobility (cm^2/Vs)
taun = 2e-7         # Lifetime (s)
taup = 2e-7         # Lifetime (s)

# --- 2. Derived Calculations ---
Vt = (kb * T) / q   # Thermal Voltage (~0.0259 V)

# Diffusion Coefficients (Einstein Relation)
Dn = mun * Vt
Dp = mup * Vt

# Diffusion Lengths
Ln = np.sqrt(Dn * taun) # in cm
Lp = np.sqrt(Dp * taup) # in cm

# Built-in Potential
Vbi = Vt * np.log((NA * ND) / ni**2)

# Depletion Width (W) under Bias Va
# Note: If Va > Vbi, this breaks. Assuming Va < Vbi.
W_cm = np.sqrt((2 * epsilon * (Vbi - Va)) / q * (1/NA + 1/ND))
W_um = W_cm * 1e4   # Convert to microns

# Depletion Edges (xn and xp)
# Conservation of charge: xp * NA = xn * ND  ->  xn = xp * (NA/ND)
# W = xp + xn = xp(1 + NA/ND)
xp_um = W_um / (1 + NA/ND)
xn_um = W_um - xp_um

# Positions in microns
x_p_edge = xj_um - xp_um
x_n_edge = xj_um + xn_um

# --- 3. Current Density Calculations ---
# Minority Carrier Concentrations at Depletion Edges (law of the junction)
# np0 = ni^2 / NA (electrons in p-side equilibrium)
# pn0 = ni^2 / ND (holes in n-side equilibrium)
np0 = ni**2 / NA
pn0 = ni**2 / ND

# Boundary Excess Concentrations
delta_np_0 = np0 * (np.exp(Va/Vt) - 1) # Excess electrons at p-edge
delta_pn_0 = pn0 * (np.exp(Va/Vt) - 1) # Excess holes at n-edge

# Diffusion Current Densities at the Edges (Maximums)
# Jn_diff_max = q * Dn * (delta_n / Ln)
# Jp_diff_max = q * Dp * (delta_p / Lp)
Jn_max = q * Dn * delta_np_0 / Ln
Jp_max = q * Dp * delta_pn_0 / Lp
J_total = Jn_max + Jp_max

# --- 4. Spatial Arrays & Piecewise Functions ---
x_um = np.linspace(0, L_device_um, 1000)
x_cm = x_um * 1e-4  # Convert x to cm for formulas

# Define conditions for regions
# Region 1: P-Side Neutral (0 to depletion edge)
# Region 2: Depletion (constant current assumed)
# Region 3: N-Side Neutral (depletion edge to end)
cond_p = x_um < x_p_edge
cond_dep = (x_um >= x_p_edge) & (x_um <= x_n_edge)
cond_n = x_um > x_n_edge

# --- Calculate Jn(x) ---
def calc_Jn(x_arr_um):
    y = np.zeros_like(x_arr_um)
    
    # 1. P-side: Electrons are minority, diffusing away from junction
    # Formula: Jn(x) = Jn_max * exp( (x - edge) / Ln )
    # (Note: x is less than edge, so argument is negative)
    mask_p = x_arr_um < x_p_edge
    dist_p = (x_arr_um[mask_p] - x_p_edge) * 1e-4 # distance in cm (negative)
    y[mask_p] = Jn_max * np.exp(dist_p / Ln)
    
    # 2. N-side: Electrons are Majority. 
    # J_total is constant. Jn = J_total - Jp(minority)
    mask_n = x_arr_um > x_n_edge
    dist_n = (x_arr_um[mask_n] - x_n_edge) * 1e-4 # distance in cm (positive)
    # Jp decays as we go deeper into N-side
    Jp_minority = Jp_max * np.exp(-dist_n / Lp) 
    y[mask_n] = J_total - Jp_minority

    # 3. Depletion: Assume constant (Lossless transport)
    y[(x_arr_um >= x_p_edge) & (x_arr_um <= x_n_edge)] = Jn_max
    
    return y

# --- Calculate Jp(x) ---
# Jp(x) is simply J_total - Jn(x)
Jn_vals = calc_Jn(x_um)
Jp_vals = J_total - Jn_vals

# --- 5. Plotting ---
plt.figure(9, figsize=(10, 6))

plt.plot(x_um, Jn_vals, label=r'$J_n$', linewidth=2)
plt.plot(x_um, Jp_vals, label=r'$J_p$', linewidth=2)
plt.plot(x_um, np.ones_like(x_um)*J_total, 'k--', label=r'$J_{\text{tot}}$', linewidth=1.5)

# Visualizing the Depletion Region
# plt.axvline(x_p_edge, color='gray', linestyle=':', alpha=0.5)
# plt.axvline(x_n_edge, color='gray', linestyle=':', alpha=0.5)
# plt.text(xj_um, J_total*1.05, 'Depletion Region', ha='center', fontsize=9, color='gray')

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Current density (A/cm$^2$)")
plt.legend()
plt.grid(True, alpha=0.3)

# Use scientific notation for Y-axis if needed
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.savefig("./plots/QB1_plot_9.png", dpi=300, bbox_inches="tight", pad_inches=0.005)

# --- Text Output for verification ---
print(f"Junction Position: {xj_um} um")
print(f"Depletion Width: {W_um:.4f} um (xp={xp_um:.4f}, xn={xn_um:.4f})")
print(f"Diffusion Lengths: Ln={Ln*1e4:.2f} um, Lp={Lp*1e4:.2f} um")
print(f"Total Current Density: {J_total:.4e} A/cm^2")
print(err(J_total, 0.236))


# ----------------------------------------------------------------

fig, ax = plt.subplots(num=10)

plt.xlabel(r"Bias applied (V)")
plt.ylabel(r"Current (A)")
plt.grid(True, alpha=0.3)
plt.axvline(0.6, color='gray', linestyle=':', alpha=0.5)
plt.text(0.5, 0.3e-5, r'$V_{\gamma}$', ha='center', fontsize=12, color='gray')

plt.plot(iv_reverse[:, 0], iv_reverse[:, 1], label=r"I (reverse bias)")
plt.plot(iv_forward[:, 0], iv_forward[:, 1], label=r"I (forward bias)")
plt.legend()

axins = inset_axes(ax, width="30%", height=1.5, loc="center")
axins.plot(iv_reverse[:, 0], iv_reverse[:, 1])
axins.set_xlim(-1.5, -1)
axins.set_ylim(-2e-7, 1e-6)
axins.set_xticks([])
axins.set_yticks([-2e-7, -1e-14, 1e-6])
axins.set_yticklabels(["-8e-14", r"$-I_{s}$", "-1e-14"])
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.savefig("./plots/QB2_plot.png", dpi=300, bbox_inches="tight", pad_inches=0.005)