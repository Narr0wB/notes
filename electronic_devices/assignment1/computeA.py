
import numpy as np
import matplotlib.pyplot as plt 

def err(x, y):
    return ((x - y) / y)

padre_folder = "./padre_data"
q = 1.60e-19

eq_conduction_band   = np.genfromtxt(padre_folder + "/exA" + "/QA_1_conduction_band.txt", delimiter=",", skip_header=4)
eq_valence_band      = np.genfromtxt(padre_folder + "/exA" + "/QA_1_valence_band.txt", delimiter=",", skip_header=4)
eq_intrinsic_fermi   = np.genfromtxt(padre_folder + "/exA" + "/QA_1_intrinsic_fermi.txt", delimiter=",", skip_header=4)
eq_fermi_level       = np.genfromtxt(padre_folder + "/exA" + "/QA_1_fermi.txt", delimiter=",", skip_header=4)
eq_electron_conc     = np.genfromtxt(padre_folder + "/exA" + "/QA_2_electron_concentration.txt", delimiter=",", skip_header=4)
eq_hole_conc         = np.genfromtxt(padre_folder + "/exA" + "/QA_2_hole_concentration.txt", delimiter=",", skip_header=4)

bias_conduction_band = np.genfromtxt(padre_folder + "/exA" + "/QA_3_conduction_band.txt", delimiter=",", skip_header=4)
bias_valence_band    = np.genfromtxt(padre_folder + "/exA" + "/QA_3_valence_band.txt", delimiter=",", skip_header=4)
bias_intrinsic_fermi = np.genfromtxt(padre_folder + "/exA" + "/QA_3_intrinsic_fermi.txt", delimiter=",", skip_header=4)
bias_fermi_level     = np.genfromtxt(padre_folder + "/exA" + "/QA_3_qfn.txt", delimiter=",", skip_header=4)
bias_e_field         = np.genfromtxt(padre_folder + "/exA" + "/QA_3_efield.txt", delimiter=",", skip_header=4)
bias_IV_char         = np.genfromtxt(padre_folder + "/exA" + "/QA_3_IV_char.txt", delimiter=",", skip_header=4)

temp_conduction_band = np.genfromtxt(padre_folder + "/exA" + "/QA_4_conduction_band.txt", delimiter=",", skip_header=4)
temp_valence_band    = np.genfromtxt(padre_folder + "/exA" + "/QA_4_valence_band.txt", delimiter=",", skip_header=4)
temp_intrinsic_fermi = np.genfromtxt(padre_folder + "/exA" + "/QA_4_intrinsic_fermi.txt", delimiter=",", skip_header=4)
temp_fermi_level     = np.genfromtxt(padre_folder + "/exA" + "/QA_4_fermi.txt", delimiter=",", skip_header=4)
temp_electron_conc   = np.genfromtxt(padre_folder + "/exA" + "/QA_4_electron_concentration.txt", delimiter=",", skip_header=4)
temp_hole_conc       = np.genfromtxt(padre_folder + "/exA" + "/QA_4_hole_concentration.txt", delimiter=",", skip_header=4)

x = eq_conduction_band[:, 0]

y1_1 = eq_conduction_band[:, 1]
y1_2 = eq_valence_band[:, 1]
y1_3 = eq_intrinsic_fermi[:, 1] * -1
y1_4 = eq_fermi_level[:, 1]

y2_1 = eq_electron_conc[:, 1]
y2_2 = eq_hole_conc[:, 1]

y3_1 = bias_conduction_band[:, 1]
y3_2 = bias_valence_band[:, 1]
y3_3 = bias_intrinsic_fermi[:, 1] * -1
y3_4 = bias_fermi_level[:, 1] * -1
y3_5 = bias_e_field[:, 1] * -1

y4_1 = temp_conduction_band[:, 1]
y4_2 = temp_valence_band[:, 1]
y4_3 = temp_intrinsic_fermi[:, 1] * -1
y4_4 = temp_fermi_level[:, 1]
y4_5 = temp_electron_conc[:, 1]
y4_6 = temp_hole_conc[:, 1]

print("Q1, Ef - Efi:", y1_4[100] - y1_3[100])
print("", y1_1[100] - y1_4[100])
print("", y1_4[100] - y1_2[100])
print("", y2_1[100])

print("Q3, Ef - Efi", y3_4[100] - y3_3[100])
print("Q3, Ec - Ef", y3_1[100] - y3_4[100])
print("Q3, Ef - Ev", y3_4[100] - y3_2[100])

print("Q4, Ef - Efi", y4_4[100] - y4_3[100])
print("Q4, Ec - Ef", y4_1[100] - y4_4[100])
print("Q4, Ef - Ev", y4_4[100] - y4_2[100])
print("Q4, n", y4_5[100])
print("Q4, p", f"{y4_6[100]:.2e}")

m, c = np.polyfit(bias_IV_char[:, 1], bias_IV_char[:, 0], 1)
print(m, c)

plt.figure(1)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Energy (eV)")
plt.grid(True, alpha=0.3)

plt.plot(x, y1_1, label=r"$\overline{E_{c}}$")
plt.plot(x, y1_2, label=r"$\overline{E_{v}}$")
plt.plot(x, y1_3, label=r"$\overline{E_{f_i}}$")
plt.plot(x, y1_4, label=r"$\overline{E_{f}}$")

plt.legend()
plt.savefig("./plots/QA_1_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(2)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y2_1, label=r"$\overline{n_{n0}}$")
plt.plot(x, y2_2, label=r"$\overline{p_{n0}}$")

plt.yscale('log')

ticks = [10 ** (i) for i in range(0, 17, 2)]
plt.yticks(ticks)

plt.legend()
plt.savefig("./plots/QA_2_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(3)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, [1e16] * len(x), label=r"$n_{n0}$")
plt.plot(x, [1e4] * len(x), label=r"$p_{n0}$")

plt.yscale('log')

ticks = [10 ** (i) for i in range(0, 17, 2)]
plt.yticks(ticks)

plt.legend()
plt.savefig("./plots/QA_2_plot_2.png", dpi=300, bbox_inches="tight")

# ----------------------------------------------------------------


plt.figure(4)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Energy (eV)")
plt.grid(True, alpha=0.3)

plt.plot(x, y3_1, label=r"$\overline{E_{c}}$")
plt.plot(x, y3_2, label=r"$\overline{E_{v}}$")
plt.plot(x, y3_3, label=r"$\overline{E_{f_i}}$")
plt.plot(x, y3_4, label=r"$\overline{E_{f}}$")

plt.legend()
plt.savefig("./plots/QA_3_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(5)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"E (V/cm)")
plt.grid(True, alpha=0.3)

plt.plot(x, y3_5, label=r"$\overline{E}$")

plt.legend()
plt.savefig("./plots/QA_3_plot_2.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(6)

plt.xlabel(r"Voltage (V)")
plt.ylabel(r"Current ($\mu$A)")
plt.grid(True, alpha=0.3)

plt.plot(bias_IV_char[:, 0], bias_IV_char[:, 1] * 1e6, label=r"$\overline{I}$")

plt.legend()
plt.savefig("./plots/QA_3_plot_3.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------

plt.figure(7)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Energy (eV)")
plt.grid(True, alpha=0.3)

plt.plot(x, y4_1, label=r"$\overline{E_{c}}$")
plt.plot(x, y4_2, label=r"$\overline{E_{v}}$")
plt.plot(x, y4_3, label=r"$\overline{E_{f_i}}$")
plt.plot(x, y4_4, label=r"$\overline{E_{f}}$")

plt.legend()
plt.savefig("./plots/QA_4_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------

plt.figure(8)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y4_5, label=r"$\overline{n}$")
plt.plot(x, y4_6, label=r"$\overline{p}$")

plt.yscale('log')

ticks = [10 ** (i) for i in range(0, 19, 2)]
plt.yticks(ticks)

plt.legend()
plt.savefig("./plots/QA_4_plot_2.png", dpi=300, bbox_inches="tight")

