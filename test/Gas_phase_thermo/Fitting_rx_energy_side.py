# Test: Fitting correction factor for CO and CO2
# v 1.0 (20-oct-2022, sagg)

# Dependencies
import matplotlib.pyplot as plt
from scipy.optimize import minimize

from stego.parameters import eV2kJpmol
from stego.kinetics import shomate_Hf, shomate_Gf
from Databin import * # Molecular objects and parameters (in different file for better organization)

####################################################################################################################
#### Determine CO/CO2 fitting energy for thermodynamic consistecy of methanation reactions  ########################
####################################################################################################################

# Define plot
fig, [axCO, axCO2] = plt.subplots(1,2, sharex='col', figsize=(9.5,3.5))
plt.subplots_adjust(hspace=0., right=.98, top=.96, left=.1, bottom=.12)

T_list = [iT for iT in range(280, 273 + 350, 20)]


# ----------------------------------------------------------------------------------------------------------------------
# Reaction energies (G:Gibbs free energy, H:enthalpy) for the CO and CO2 methanation computed using
# the Shomate equation

G_NIST_COrx = [shomate_Gf(CH4_NIST, iT) + shomate_Gf(H2O_NIST, iT)
			   - shomate_Gf(CO_NIST, iT) - 3 * shomate_Gf(H2_NIST, iT) for iT in T_list]
H_NIST_COrx = [shomate_Hf(CH4_NIST, iT) + shomate_Hf(H2O_NIST, iT)
			   - shomate_Hf(CO_NIST, iT) - 3 * shomate_Hf(H2_NIST, iT) for iT in T_list]

G_NIST_CO2rx =[shomate_Gf(CH4_NIST, iT) + 2 * shomate_Gf(H2O_NIST, iT)
			   - shomate_Gf(CO2_NIST, iT) - 4 * shomate_Gf(H2_NIST, iT) for iT in T_list]
H_NIST_CO2rx =[shomate_Hf(CH4_NIST, iT) + 2 * shomate_Hf(H2O_NIST, iT)
			   - shomate_Hf(CO2_NIST, iT) - 4 * shomate_Hf(H2_NIST, iT) for iT in T_list]

# Adding to plot NIST (Shomate) reaction enthalpy and free energy
axCO.plot(T_list, G_NIST_COrx, 'o', color='g', label='$\Delta$G (NIST)', markersize=6)
axCO.plot(T_list, H_NIST_COrx, 'o', color='b', label='$\Delta$H (NIST)')

axCO2.plot(T_list, G_NIST_CO2rx, 'o', color='g', label='$\Delta$G (NIST)')
axCO2.plot(T_list, H_NIST_CO2rx, 'o', color='b', label='$\Delta$H (NIST)')

# ----------------------------------------------------------------------------------------------------------------------
# Define list of reaction energies (return: [Gibbs], [enthalpy]) at the list of temperatures including an energy
# correction to the CO and CO2 energy
def MethanationCO(COcorrection):
	GibbsRx = []; EnthalpyRx = []
	for iT in T_list:
		GibbsRx.append(
			CH4_g.Gibbs(T=iT, P=1.) + H2O.Gibbs(T=iT, P=1.)
			- (CO.Gibbs(T=iT, P=1.) + COcorrection) - 3 * H2.Gibbs(T=iT, P=1.)
		)

		EnthalpyRx.append(
			CH4_g.Enthalpy(T=iT, P=1.) + H2O.Enthalpy(T=iT, P=1.)
			- (CO.Enthalpy(T=iT, P=1.) + COcorrection) - 3 * H2.Enthalpy(T=iT, P=1.)
		)

	return [i*eV2kJpmol for i in GibbsRx], [j*eV2kJpmol for j in EnthalpyRx]

def MethanationCO2(CO2correction):
	GibbsRx = []; EnthalpyRx = []
	for iT in T_list:
		GibbsRx.append(
			CH4_g.Gibbs(T=iT, P=1.) + 2 * H2O.Gibbs(T=iT, P=1.)
			- (CO2.Gibbs(T=iT, P=1.) + CO2correction) - 4 * H2.Gibbs(T=iT, P=1.)
		)

		EnthalpyRx.append(
			CH4_g.Enthalpy(T=iT, P=1.) + 2 * H2O.Enthalpy(T=iT, P=1.)
			- (CO2.Enthalpy(T=iT, P=1.) + CO2correction) - 4 * H2.Enthalpy(T=iT, P=1.)
		)

	return [i*eV2kJpmol for i in GibbsRx], [j*eV2kJpmol for j in EnthalpyRx]


# Adds to plot DFT reaction energies without any correction (correction factor = 0.)
Rx_DFTGibbs_CO, Rx_DFTH_CO = MethanationCO(0.)
axCO.plot(T_list, Rx_DFTGibbs_CO, ':', color='g', label='$\Delta$G RPBE')
axCO.plot(T_list, Rx_DFTH_CO, ':', color='b', label='$\Delta$H RPBE')

Rx_DFTGibbs_CO2, Rx_DFTH_CO2 = MethanationCO2(0.)
axCO2.plot(T_list, Rx_DFTGibbs_CO2, ':', color='g', label='$\Delta$G RPBE')
axCO2.plot(T_list, Rx_DFTH_CO2, ':', color='b', label='$\Delta$H RPBE')

# Define functions to minimize error between DFT and NIST(Shomate values), fit manipulating
# the CO and CO2 correction energies. Considers G and H error simultaneously.
def minimizacion_COmeth(afactor):
	resG, resH = MethanationCO(afactor)
	DeltaG = sum([(i-j) ** 2 for i,j in zip(resG, G_NIST_COrx)])
	DEltaH = sum([(i-j) ** 2 for i,j in zip(resH, H_NIST_COrx)])
	return DEltaH+DeltaG

def minimizacion_CO2meth(afactor):
	resG, resH = MethanationCO2(afactor)
	DeltaG = sum([(i-j) ** 2 for i,j in zip(resG, G_NIST_CO2rx)])
	DEltaH = sum([(i-j) ** 2 for i,j in zip(resH, H_NIST_CO2rx)])
	return DEltaH+DeltaG

# Performs minimization
minminCO = minimize(minimizacion_COmeth,.2).x[0]
minminCO2 = minimize(minimizacion_CO2meth,.2).x[0]
print("CO fit correction  = "+str(minminCO))
print("CO2 fit correction = "+str(minminCO2))
input(' continue ? ')

# Adds to plot DFT reaction energies with fitted energy correction
Rx_DFTGibbs_CO, Rx_DFTH_CO = MethanationCO(minminCO)
axCO.plot(T_list, Rx_DFTGibbs_CO, '--', color='g', label='$\Delta$G RPBE-$CO$ fit')
axCO.plot(T_list, Rx_DFTH_CO, '--', color='b', label='$\Delta$H RPBE-$CO$ fit')

Rx_DFTGibbs_CO2, Rx_DFTH_CO2 = MethanationCO2(minminCO2)
axCO2.plot(T_list, Rx_DFTGibbs_CO2, '--', color='g', label='$\Delta$G RPBE-$CO_2$ fit')
axCO2.plot(T_list, Rx_DFTH_CO2, '--', color='b', label='$\Delta$H RPBE-$CO_2$ fit')


# Final touches for a nice plot
axCO.set_title(r"a) $CO+3H_2 \rightarrow CH_4+H_2O$", y=.9, fontsize=12, fontweight='bold')
axCO2.set_title(r"b) $CO_2+4H_2 \rightarrow CH_4+2H_2O$", y=.9, fontsize=12, fontweight='bold')
for iax in [axCO2, axCO]:
	iax.legend(loc='center right', ncol=1, prop={'size': 8}, bbox_to_anchor=(.98, .35))
	iax.axvline(x=298.15, color='k', alpha=0.5, linewidth=2.)
	iax.annotate('25.0 °C', xy=(298.15-5, 0.8), xycoords=("data", "axes fraction"),
				 va="baseline", ha="center", fontsize=10, color='k', rotation=90)
	plt.sca(iax)
	plt.ylabel('Reaction energy, kJ/mol', fontweight='bold')

plt.sca(axCO2)
plt.xlabel('Temperature, K', fontweight='bold')

plt.savefig('./Fitting_rx_energy_side.png')

plt.show()
