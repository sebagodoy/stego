# Functions to compute kinetic and equilibrium parameters from energies

# dependencies
from numpy import exp, log
from stego.parameters import kb, hh, eV2J


def rate_cte(TS_E, initial_E, Temp):
    # returns a rate constant according to transition state theory from
    # initial and final energies in [eV]
    return (kb * Temp / hh) * exp((initial_E - TS_E) * (eV2J / (kb * Temp)))


def equilibria_cte(final_E, initial_E, Temp):
    # returns rate constant from transition state theory
    # energies in [eV]
    return exp((initial_E - final_E) * (eV2J / (kb * Temp)))

def KIE(E_light_TS, E_light_i, E_heavy_TS, E_heavy_i, temp):
    # returns Kinetic Isotopic Effect, KIE = k(forwads)/k(backwards)
    # same structure as TIE
    return exp((E_heavy_TS - E_heavy_i - E_light_TS + E_light_i) * (eV2J / (kb * temp)))


def TIE(E_light_TS, E_light_i, E_heavy_TS, E_heavy_i, temp):
    # returns Thermodynamic Isotopic Effect, KIE = k(forwads)/k(backwards)
    # same structure as KIE
    return KIE(E_light_TS, E_light_i, E_heavy_TS, E_heavy_i, temp)

# ----------------------------------------------------------------------------------------------------------------------
# Shomate equation

def shomate_Hf(ml, Tin):
    # returns enthalpy according to the Shomate Equation in the NIST format
    # ml: dic,  list of Shomate parameters ('A', ... ) and formation energy 'H0f'
    #           {'A':1.2345, 'b':1.234, ..., 'H0f':1.2345}
    # Tin: float, temperature [K]
    tin=Tin/1000
    return ml['A']*tin + \
		   (ml['B']/2.)*(tin**2) + \
		   (ml['C']/3.)*(tin**3) + \
		   (ml['D']/4.)*(tin**4) - \
		   ml['E']/tin + \
		   ml['F'] - \
		   ml['H'] + \
		   ml['H0f'] #kJ/mol

def shomate_Sf(ml, Tin):
    # returns entropy according to the Shomate Equation in the NIST format
    # ml: dic,  list of Shomate parameters ('A', ... ) and formation energy 'H0f'
    #           {'A':1.2345, 'b':1.234, ..., 'H0f':1.2345}
    # Tin: float, temperature [K]
    tin = Tin/1000
    ss = ml['A']*log(tin) + \
		 ml['B']*tin + \
		 (ml['C']/2.)*(tin**2) + \
		 (ml['D']/3.)*(tin**3) - \
		 ml['E']/(2*(tin**2)) + \
		 ml['G'] #J/K mol
    return ss/1000 #kJ/K mol


def shomate_Gf(ml, Tin):
    # returns free energy according to the Shomate Equation in the NIST format
    # ml: dic,  list of Shomate parameters ('A', ... ) and formation energy 'H0f'
    #           {'A':1.2345, 'b':1.234, ..., 'H0f':1.2345}
    # Tin: float, temperature [K]
    return shomate_Hf(ml, Tin) - Tin*shomate_Sf(ml, Tin)