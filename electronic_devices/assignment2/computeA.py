
import numpy as np
import matplotlib.pyplot as plt

def err(x, y):
    return abs(x - y)/y

pf = "./padre_data"

eq_conduction_band = np.genfromtxt(pf + "/exA" + "/QA1_conduction_band.txt", delimiter=",", skip_header=4)
eq_valence_band    = np.genfromtxt(pf + "/exA" + "/QA1_valence_band.txt", delimiter=",", skip_header=4)
eq_intrinsic_fermi = np.genfromtxt(pf + "/exA" + "/QA1_intrinsic_fermi.txt", delimiter=",", skip_header=4)
eq_fermi           = np.genfromtxt(pf + "/exA" + "/QA1_fermi_level.txt", delimiter=",", skip_header=4)

net_charge         = np.genfromtxt(pf + "/exA" + "/QA2_net_charge.txt", delimiter=",", skip_header=4)

e_field            = np.genfromtxt(pf + "/exA" + "/QA3_electric_field.txt", delimiter=",", skip_header=4)


l = 25 
h = 165 
y11 = eq_conduction_band[l:h, 1]
y12 = eq_valence_band[l:h, 1]
y13 = eq_intrinsic_fermi[l:h, 1] * -1
y14 = eq_fermi[l:90, 1]

plt.figure(1)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Energy (eV)")
plt.grid(True, alpha=0.3)

plt.plot(eq_conduction_band[l:h, 0], y11, label=r"$\overline{E_{c}}$")
plt.plot(eq_valence_band[l:h, 0], y12, label=r"$\overline{E_{v}}$")
plt.plot(eq_intrinsic_fermi[l:h, 0], y13, label=r"$\overline{E_{f_i}}$")
plt.plot(eq_fermi[l:90, 0], y14, label=r"$\overline{E_{f}}$")

plt.legend()
plt.savefig("./plots/QA1_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(2)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Charge (C/$\text{cm}^{3}$)")
plt.grid(True, alpha=0.3)

l_c = 25
h_c = 150
plt.plot(net_charge[l_c:h_c, 0], net_charge[l_c:h_c, 1], label=r"$\overline{\rho}(x)$")

plt.axvline(167.65, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168.1, color="gray", linestyle=":", alpha=0.8)

plt.legend()
plt.savefig("./plots/QA2_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(3)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Charge (C/$\text{cm}^{3}$)")
plt.grid(True, alpha=0.3)

x = np.linspace(167.4, 168.5, 200)
conditions = [x < (168 - 0.29), x > (168 - 0.29), x > 168, x > (168 + 0.05)] 
functions = [lambda x: 0, lambda x: -1e16 * 1.6e-19, lambda x: 6e16 * 1.6e-19, lambda x: 0]
y = np.piecewise(x, conditions, functions)
plt.plot(x, y, label=r"$\rho(x)$")
plt.axvline(167.71, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168.05, color="gray", linestyle=":", alpha=0.8)

plt.legend()
plt.savefig("./plots/QA2_plot_2.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(4)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Electric Field (V/cm)")
plt.grid(True, alpha=0.3)

l_e = 20
h_e = 190
plt.plot(e_field[l_e:h_e, 0], e_field[l_e:h_e, 1], label=r"$\overline{E}(x)$")
plt.axvline(167.65, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168.1, color="gray", linestyle=":", alpha=0.8)

plt.legend()
plt.savefig("./plots/QA3_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(5)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Electric Field (V/cm)")
plt.grid(True, alpha=0.3)

es = 1.04e-12
xp = 0.29
xn = 0.05
xj = 168

x = np.linspace(166.4, 169, 200)
conditions = [x < (xj - xp), x > (xj - xp), x > xj, x > (xj + xn)] 
functions = [lambda x: 0, lambda x: (-1e16/es)*((x - xj) + xp)*(1e-4 * 1.6e-19), lambda x: (-1e16/es)*(xp * 1e-4 * 1.6e-19) + (6e16/es)*(x - xj)*(1e-4 * 1.6e-19), lambda x: 0]
y = np.piecewise(x, conditions, functions)
plt.plot(x, y, label=r"$E(x)$")
plt.axvline(167.71, color="gray", linestyle=":", alpha=0.8)
plt.axvline(168.05, color="gray", linestyle=":", alpha=0.8)

plt.legend()
plt.savefig("./plots/QA3_plot_2.png", dpi=300, bbox_inches="tight")