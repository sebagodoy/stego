# Packages
from stego.promps import CodeErrorExit

from stego.parameters import Nav, kb, hh, cc, eV2J
from numpy import pi, exp, prod, log

print('>> Loading thermodynamic module', end='...')


########################################################################################################################
# Basic thermodynamic partitions

def qTras(inM, inT, inP):
    # inM = Masa			/[AMU = g/mol]
    # inT = Temperature		/[K]
    # inP = Pressure		/[bar]
    inP = inP * 100000  # bar -> Pa
    inM = inM / (Nav * 1000)  # g/mol -> kG/particle
    frac1 = 2 * pi * inM * kb * inT / (hh ** 2.)
    frac2 = kb * inT / inP
    return frac2 * (frac1 ** (3. / 2.))  # /[Adim]


def qRot(Geom, RotT, Tin, SymmNum):
	# Rotational partition function [Adim.]
    # Geometry = 'Diatomic homonuclear', 'Diatomic Heteronuclear' or 'Poliatomic'
    # RotT	=	Rotational temperature or list if poliatomic /[K]
    # Tin =		Temperature /[K]
    # SymmNum = Rotational symmetry number (HCl:1, H2/O2/Cl2=2, NH3:3, CH4:12)

    # Check geometry
    if 'Diatomic' in Geom:
        # Diatomic, Symmnumber = 1 or 2, len(RotT) = 1
        return Tin / (SymmNum * RotT)
    elif 'Poliatomic' in Geom:
        if not len(RotT) == 3:
            CodeErrorExit('Poliatomic molecule needs three rotational temperatures to compute qRot')
        return (pi * (Tin ** 3) / ((SymmNum ** 2) * prod(RotT))) ** 0.5 #/adim
    else:
        CodeErrorExit('Geometry not recognized')


def qVib(FreqIn: list, Tin: float):
	# vibrational partition function [Adim.]
    # FreqIn = [real freqs list]	/[cm-1]
    # Tin = Temperature				/[K]
    qV = 1
    for iF in FreqIn:
        vibTemp = hh * cc * iF * 100. / kb  # /[Adim.]
        fracUp = exp(-vibTemp / (2. * Tin))
        fracDown = 1. - exp(-vibTemp / Tin)
        qV *= fracUp / fracDown
    return qV  # /[Adim.]


def qEl(*args, **kwargs):
	# Electronic partition function [Adim.]
    # Asumes excited states in such high energy that are inaccesible
    # and spin multiplicity of ground state = 1
    return 1.


########################################################################################################################
# Energetic contributions by partition
# default output in eV

def Etras(inT):
	# Translational energy [eV]
    # inT = Temperature		/[K]
    return (3. / 2.) * (kb * inT / eV2J)  # /(eV)


def ZPVE(FreqIn: list):
	# Zero Point Vibrational Energy, ZPVE [eV]
    # FreqIn = [real freqs list]	/[cm-1]
    sZPVE = 0.
    for iF in FreqIn:
        sZPVE += (hh * cc * iF * 100) / (2 * eV2J)
    return sZPVE  # /(eV)


def Evib(FreqIn:list, Tin:float):
	# Vibrational energy [eV]
    # FreqIn = [real freqs list]	/[cm-1]
    # Tin = Temperature				/[K]
    Ev = 0.
    for iF in FreqIn:
        vibTemp = hh * cc * iF * 100. / kb  # /[Adim.]
        Ev += vibTemp / (exp(vibTemp / Tin) - 1.)
    return Ev * (kb / eV2J)  # /[eV]


def Erot(Geometry:str, Tin: float):
	# Rotational energy [eV]
    # Geometry =	'Diatomic homonuclear'
    #				'Diatomic Heteronuclear'
    #				'Polyatomic'
    # Tin = Temperature  /[K]
    if "Diatomic" in Geometry:
        return kb * Tin / eV2J  # /[eV]
    elif 'Poliatomic' in Geometry:
        return (3. / 2.) * kb * Tin / eV2J  # /[eV]
    else:
        CodeErrorExit('Geometry option not recognized, must be \
        Diatomic homonuclear, Diatomic heteronuclear or Polyatomic')


########################################################################################################################
# Entropic contributions by partition
# default output in eV/K

def Stras(iinM, iinT, iinP):
    # Translational entropy [eV/K]
    # inM = Masa			/[AMU = g/mol]
    # inT = Temperature		/[K]
    # inP = Pressure		/[bar]
    qT = qTras(iinM, iinT, iinP)
    return kb * (log(qT) + 5. / 2.) / eV2J  # /[eV/K]


def Srot(Geom, RotT, Tin, SymmNum):
	# Rotational entropy [eV/K]
    # Geom	=	'Diatomic homonuclear', 'Diatomic Heteronuclear' or 'Poliatomic'
    # RotT	=	Rotational temperature / K, 1 for diatomics 3 for everything else.
    # Tin	=	Temperature / K
    # SymmNum =	Rotational symmetry number (1 for HCl, 2 for H2, 3 for NH3, 12 for CH4)
    # print("Rot Sym number = " + str(SymmNum))
    qR = qRot(Geom, RotT, Tin, SymmNum)
    if 'Diatomic' in Geom:
        return kb * (log(qR) + 1.) / eV2J  # /[eV/K]
    elif Geom == 'Poliatomic':
        return kb * (log(qR) + 3. / 2.) / eV2J  # /[eV/K]


def Svib(FreqIn, Tin):
    # Vibrational entropy [eV/K]
    # FreqIn = [Real fres list]	/[cm-1]
    # Tin = Temperature			/[K]
    Sv = 0
    for iFq in FreqIn:
        rotTonT = hh * cc * iFq * 100. / (kb * Tin)  # /[Adim.]
        # print('(Rot T)/T = ' + str(rotTonT))
        frac = rotTonT / (exp(rotTonT) - 1.)  # /[Adim.]
        lo = log(1. - exp(-rotTonT))  # /[Adim.]
        Sv += kb * (frac - lo) / eV2J  # /[eV/K]
    return Sv  # /[eV/K]


print('Ok')
