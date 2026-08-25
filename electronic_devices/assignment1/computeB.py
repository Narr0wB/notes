
import numpy as np
import matplotlib.pyplot as plt

def err(x, y):
    return ((x - y) / y)

padre_folder = "./padre_data"
g_opt = 9e20
tau = 1e-6
w   = 336e-4
l_p = 34e-4

eq_electron_conc = np.genfromtxt(padre_folder + "/exB" + "/QB_1_electron_conc.txt", delimiter=",", skip_header=4)
eq_hole_conc     = np.genfromtxt(padre_folder + "/exB" + "/QB_1_hole_conc.txt", delimiter=",", skip_header=4)

short_eq_hole_conc = np.genfromtxt(padre_folder + "/exB" + "/QB_2_hole_conc.txt", delimiter=",", skip_header=4)

bias_n1V_electron_conc  = np.genfromtxt(padre_folder + "/exB" + "/QB_3_electron_conc_nV1.txt", delimiter=",", skip_header=4) 
bias_n05V_electron_conc = np.genfromtxt(padre_folder + "/exB" + "/QB_3_electron_conc_nV05.txt", delimiter=",", skip_header=4) 
bias_05V_electron_conc  = np.genfromtxt(padre_folder + "/exB" + "/QB_3_electron_conc_V05.txt", delimiter=",", skip_header=4) 
bias_1V_electron_conc   = np.genfromtxt(padre_folder + "/exB" + "/QB_3_electron_conc_V1.txt", delimiter=",", skip_header=4) 

bias_n1V_hole_conc      = np.genfromtxt(padre_folder + "/exB" + "/QB_3_hole_conc_nV1.txt", delimiter=",", skip_header=4) 
bias_n05V_hole_conc     = np.genfromtxt(padre_folder + "/exB" + "/QB_3_hole_conc_nV05.txt", delimiter=",", skip_header=4) 
bias_05V_hole_conc      = np.genfromtxt(padre_folder + "/exB" + "/QB_3_hole_conc_V05.txt", delimiter=",", skip_header=4) 
bias_1V_hole_conc       = np.genfromtxt(padre_folder + "/exB" + "/QB_3_hole_conc_V1.txt", delimiter=",", skip_header=4) 

bias_n1V_total_current  = np.genfromtxt(padre_folder + "/exB" + "/QB_3_total_current_nV1.txt", delimiter=",", skip_header=4)
bias_n05V_total_current = np.genfromtxt(padre_folder + "/exB" + "/QB_3_total_current_nV05.txt", delimiter=",", skip_header=4)
bias_05V_total_current  = np.genfromtxt(padre_folder + "/exB" + "/QB_3_total_current_V05.txt", delimiter=",", skip_header=4)
bias_1V_total_current   = np.genfromtxt(padre_folder + "/exB" + "/QB_3_total_current_V1.txt", delimiter=",", skip_header=4)

x = eq_electron_conc[:, 0]

y1_1 = eq_electron_conc[:, 1]
y1_2 = eq_hole_conc[:, 1]

ddp = np.gradient(y1_2, x * 1e-4)
print("QB1.3 grad:", f"{ddp[0]:.3e}")
print("QB1.3 exp lp:", (g_opt * tau) / ddp[0])

x2_1 = short_eq_hole_conc[:, 0]
y2_1 = short_eq_hole_conc[:, 1]

y3_1 = bias_n1V_electron_conc[:, 1]
y3_2 = bias_n05V_electron_conc[:, 1]
y3_3 = bias_05V_electron_conc[:, 1]
y3_4 = bias_1V_electron_conc[:, 1]

y3_5 = bias_n1V_hole_conc[:, 1]
y3_6 = bias_n05V_hole_conc[:, 1]
y3_7 = bias_05V_hole_conc[:, 1]
y3_8 = bias_1V_hole_conc[:, 1]

y3_9  = bias_n1V_total_current[:, 1]
y3_10 = bias_n05V_total_current[:, 1]
y3_11 = bias_05V_total_current[:, 1]
y3_12 = bias_1V_total_current[:, 1]


plt.figure(1)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Hole concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y1_2, label=r"$\overline{p(x)}$")

num = np.cosh(((x * 1e-4) - (w / 2))/l_p)
den = np.cosh((w / 2)/l_p)
y1_3 = 10e4 + (g_opt * tau * (1 - (num / den)))
plt.plot(x, y1_3, label=r"$p(x)$")
print("QB1.1 err:", f"{err(y1_2[250], y1_3[250]):.4e}")


plt.legend()
plt.savefig("./plots/QB_1_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(2)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Excess concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y1_1 - 1e16, label=r"$\overline{\Delta p(x)}$")

plt.legend()
plt.savefig("./plots/QB_1_plot_2.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(3)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Excess concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y1_2 - 1e4, label=r"$\overline{\Delta n(x)}$")

plt.legend()
plt.savefig("./plots/QB_1_plot_3.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(4)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Hole concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x2_1, y2_1, label=r"$\overline{p(x)}$")

w_r = 9e-4
num = np.cosh(((x2_1 * 1e-4) - (w_r / 2))/l_p)
den = np.cosh((w_r / 2)/l_p)
y2_2 = 10e4 + (g_opt * tau * (1 - (num / den)))
plt.plot(x2_1, y2_2, label=r"$p(x)$", linestyle="--")

print("QB2 err", f"{err(y2_1[250], y2_2[250]):.4e}")

plt.legend()
plt.savefig("./plots/QB_2_plot.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(5)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Excess concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x2_1, y2_1 - 1e4, label=r"$\overline{\Delta p(x)}$")

plt.legend()
plt.savefig("./plots/QB_2_plot_2.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(6)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Electron concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y3_1, label=r"$\overline{n(x)}$ @ -1V")
plt.plot(x, y3_2, label=r"$\overline{n(x)}$ @ -0.5V")
plt.plot(x, y3_3, label=r"$\overline{n(x)}$ @ 0.5V")
plt.plot(x, y3_4, label=r"$\overline{n(x)}$ @ 1V")

plt.legend()
plt.savefig("./plots/QB_3_plot.png", dpi=300, bbox_inches="tight")



# ----------------------------------------------------------------


plt.figure(7)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Hole concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y3_5, label=r"$\overline{p(x)}$ @ -1V")
plt.plot(x, y3_6, label=r"$\overline{p(x)}$ @ -0.5V")
plt.plot(x, y3_7, label=r"$\overline{p(x)}$ @ 0.5V")
plt.plot(x, y3_8, label=r"$\overline{p(x)}$ @ 1V")

plt.legend()
plt.savefig("./plots/QB_3_plot_2.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(8)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Total current density (A/cm$^2$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y3_9, label=r"$\overline{J}(x)$ @ -1V", alpha=0.5, lw=3, linestyle="-")
plt.plot(x, y3_10, label=r"$\overline{J}(x)$ @ -0.5V", alpha=0.5, lw=3, linestyle="-")
plt.plot(x, y3_11, label=r"$\overline{J}(x)$ @ 0.5V", lw=3, linestyle="--")
plt.plot(x, y3_12, label=r"$\overline{J}(x)$ @ 1V", lw=3, linestyle="--")

plt.legend()
plt.savefig("./plots/QB_3_plot_3.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(9)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Electron concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y3_1, label=r"$n(x)$ @ -1V")
plt.plot(x, y3_2, label=r"$n(x)$ @ -0.5V")
plt.plot(x, y3_3, label=r"$n(x)$ @ 0.5V")
plt.plot(x, y3_4, label=r"$n(x)$ @ 1V")

plt.legend()
plt.savefig("./plots/QB_3_plot_4.png", dpi=300, bbox_inches="tight")



# ----------------------------------------------------------------


plt.figure(10)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Hole concentration ($\text{cm}^{-3}$)")
plt.grid(True, alpha=0.3)

plt.plot(x, y3_5, label=r"$p(x)$ @ -1V")
plt.plot(x, y3_6, label=r"$p(x)$ @ -0.5V")
plt.plot(x, y3_7, label=r"$p(x)$ @ 0.5V")
plt.plot(x, y3_8, label=r"$p(x)$ @ 1V")

plt.legend()
plt.savefig("./plots/QB_3_plot_5.png", dpi=300, bbox_inches="tight")


# ----------------------------------------------------------------


plt.figure(11)

plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"Total current density (A/cm$^2$)")
plt.grid(True, alpha=0.3)

plt.plot(x, (y3_9 - 1), label=r"$J(x)$ @ -1V", alpha=0.5, lw=3, linestyle="-")
plt.plot(x, (y3_10 + 1.3), label=r"$J(x)$ @ -0.5V", alpha=0.5, lw=3, linestyle="-")
plt.plot(x, (y3_11 + 1.3), label=r"$J(x)$ @ 0.5V", lw=3, linestyle="--")
plt.plot(x, (y3_12 - 1), label=r"$J(x)$ @ 1V", lw=3, linestyle="--")

plt.legend()
plt.savefig("./plots/QB_3_plot_6.png", dpi=300, bbox_inches="tight")