# Packages
import numpy as np

from stego.parameters import eV2J, kb
import stego.thermo as thermo
from .promps import CodeStatus, CodeErrorExit



print('>> Loading Index-classes module', end='...')

class SingleItem:
	def __init__(self, **kwargs):
		"""
		Default values available for all kind of model
		"""
		# Identification
		self.Name 		= kwargs.get('Name','No name given')	# Name
		self.G_ID 		= kwargs.get('G_ID', None)				# Job ID of geometry job
		self.F_ID		= kwargs.get('F_ID', None)				# Job ID of frequency job
		# Run info
		self.Accuracy	= kwargs.get('Acc', None)				# Precision level, personal reference
		self.TS			= kwargs.get('TS', None)				# TS if transition state, otherwise stable geom
		# Content
		self.Species	= None									# Species in the model
		# Energy input
		self.E0			= float(	kwargs.get('E0', 0.))-float(	kwargs.get('dipolE0',0)) + float(kwargs.get('D',0.))
																# Energy, pure electronic - dipol correction
		self.D			= float(	kwargs.get('D', 0.))		# Dispersion/other-kind-of correction
		self.Dtype 		= str(		kwargs.get('Dtype', None))	# Kind of correction
		self.DIP		= float(	kwargs.get('dipolE0',0))	# Extra dipole correction added to E0
		self.E0noDIP		= float(	kwargs.get('E0', 0.))		# Energy, no dipol correction added

		# Frequencies
		self.FreqR		= kwargs.get('FreqR', None)				# List of real frequencies
		self.FreqI		= kwargs.get('FreqI', None)				# List of imaginary frequencies

		# Extras
		self.Notes		= kwargs.get('Notes', None)


	def __str__(self):
		return 'Item type' + str(self.__class__)+' '+self.Name


	# The following functions shuld be overwrited for every kind of item, e.g. gas models include translational energy
	# but adsorbed models does not.

	#### ---------------- Base for Partition functions
	def q_tras(self, **kwargs):
		CodeErrorExit('q-tras not overwrited by child class')
	def q_rot(self, **kwargs):
		CodeErrorExit('q-rot not overwrited by child class')
	def q_vib(self, **kwargs):
		CodeErrorExit('q-vib not overwrited by child class')
	def q_el(self, **kwargs):
		CodeErrorExit('q-el not overwrited by child class')

	#### ---------------- Base for thermo Energy contributions
	def ZPVE(self, **kwargs):
		CodeErrorExit('ZPVE not overwrited by child class')
	def Etras(self, **kwargs):
		CodeErrorExit('Etras not overwrited by child class')
	def Erot(self, **kwargs):
		CodeErrorExit('Erot not overwrited by child class')
	def Evib(self, **kwargs):
		CodeErrorExit('Evib not overwrited by child class')
	def Eel(self, **kwargs):
		CodeErrorExit('Eel not overwrited by child class')

	#### ---------------- Base for thermo Entropy contributions
	def Stras(self, **kwargs):
		CodeErrorExit('Svib not overwrited by child class')
	def Srot(self, **kwargs):
		CodeErrorExit('Svib not overwrited by child class')
	def Svib(self, **kwargs):
		CodeErrorExit('Svib not overwrited by child class')
	def Sel(self, **kwargs):
		return 0.


	#### ---------------- Thermodynamic functions
	def Internal(self, **kwargs):
		# U = (E0 + Eel) + Etras + Erot + (ZPVE + Evib)
		CodeErrorExit('Internal energy not ovewritted by child class')
	def Enthalpy(self, **kwargs):
		# H = U + kbT
		CodeErrorExit('Enthalpy not ovewritted by child class')
	def Entropy(self, **kwargs):
		# S = Sel + Stras + Srot + Svib
		CodeErrorExit('Enthalpy not ovewritted by child class')
	def Gibbs(self, **kwargs):
		# H-TS
		outH = self.Enthalpy(**kwargs)
		outS = self.Entropy(**kwargs)
		out = outH - kwargs.get('T') * outS
		if kwargs.get("Report", True):
			CodeStatus(f"For [{self.Name}], G/eV="+str(out)+", H/eV="+str(outH)+", S/(eV/K)="+str(outS))
		return out
	def E0ZPVE(self, **kwargs):
		# E0 + ZPVE
		return self.E0 + self.ZPVE()



#### ---------------------------------------------------------------- Clean surface class
class CleanSurf(SingleItem):
	def __init__(self, **kwargs):
		# Get parent's properties and functions
		SingleItem.__init__(self, **kwargs)
		# Overwrite them
		self.F_ID 		= None
		self.FreqR 		= None
		self.FreqI 		= None
		self.Species 	= None

	#### ---- Overwrite Partition functions
	def q_tras(self, **kwargs):
		return 1
	def q_vib(self, **kwargs):
		return 1
	def q_rot(self, **kwargs):
		return 1.
	def q_el(self, **kwargs):
		return 1.

	#### ---- Overwrite thermo Energy functions
	def ZPVE(self, **kwargs):
		# Phonons are sistematically ignored
		return 0.
	def Etras(self, **kwargs):
		# Surface does not move
		return 0
	def Erot(self, **kwargs):
		# Surface does not rotate
		return 0.
	def Evib(self, **kwargs):
		# Phonons are sistematically ignored
		return 0.
	def Eel(self, **kwargs):
		# Bottom of well reference
		# Negligible population of higher levels is assumed
		return 0.

	#### ---- Overwrite thermo Entropy functions
	def Stras(self, **kwargs):
		# Surface does not move
		return 0
	def Srot(self, **kwargs):
		# Surface does not rotate
		return 0.
	def Svib(self, **kwargs):
		# Phonons are sistematically ignored
		return 0.
	def Sel(self, **kwargs):
		# Bottom of well reference
		# Negligible population of higher levels is assumed
		return 0.

	#### ---- Thermodynamic functions
	def Internal(self, **kwargs):
		# Etras = Erot = ZPVE = Evib = Eel = 0
		return self.E0
	def Enthalpy(self, **kwargs):
		# No pressure effect: dontt include kbT
		return self.Internal(**kwargs)
	def Entropy(self, **kwargs):
		# Only one state: Stras = Srot = Svib = Sel = 0
		return 0.




################################################################
#### ---------------------------------------------------------------- Adsorbed surface class
class AdsSurf(SingleItem):
	def __init__(self, **kwargs):
		# Get parent's attributes and functions
		SingleItem.__init__(self, **kwargs)
		# Overwrite them


	#### ---- Overwrite Partition functions
	def q_tras(self, **kwargs):
		# Surface does not move
		return 1.
	def q_rot(self, **kwargs):
		# Surface does not rotate (as a whole)
		# Adsorbate rotations would count as diferent structures
		return 1.
	def q_vib(self, **kwargs):
		# Check input
		try:
			iT = float(kwargs.get('T')) # T[K]
			self.FreqR[0]	# Freq list [cm-1]
		except:
			CodeErrorExit('Need a list of frea freqs[cm-1] and T[K] to compute qTras')
		# Compute
		return thermo.qVib(self.FreqR, iT)
	def q_el(self, **kwargs):
		# Bottom of well reference
		# Negligible population of higher levels is assumed
		return 1.


	#### ---- Overwrite thermo Energy functions
	def Etras(self, **kwargs):
		# Surface does not move
		return 0.
	def Erot(self, **kwargs):
		# Surface does not rotate (as a whole)
		# Adsorbate rotations would count as diferent structures
		return 0.
	def ZPVE(self, **kwargs):
		# Check input
		try:
			self.FreqR[0]	# Freq list [cm-1]
		except:
			CodeErrorExit('Can\'t compute ZPVE without freqs.')
		# Compute
		print("ZPVE(eV)" + str(thermo.ZPVE(self.FreqR)))
		return thermo.ZPVE(self.FreqR) #/[eV]
	def Evib(self, **kwargs):
		# Check input
		try:
			iT = float(kwargs.get('T'))
			self.FreqR[0]
		except:
			CodeErrorExit('Needs real frequencies to compute E vib.')
		# Compute
		print("Evib(eV)=" + str(thermo.Evib(self.FreqR, iT)))
		return thermo.Evib(self.FreqR, iT)
	def Eel(self, **kwargs):
		# Bottom of well reference
		# Negligible population of higher levels is assumed
		return 0.


	#### ---- Overwrite thermo Entropy functions
	def Stras(self, **kwargs):
		# Surface does not move
		return 0.
	def Srot(self, **kwargs):
		# Surface does not rotate (as a whole)
		# Adsorbate rotations would count as diferent structures
		return 0.
	def Svib(self, **kwargs):
		# Check input
		try:
			iT  = float(kwargs.get('T')) # T[K]
			self.FreqR[0] # FreqR list [cm-1]
		except:
			CodeErrorExit('Need real frequencies list [cm-1] and T [K] to compute Svib')
		# Compute
		print("Svib(eV/K)=" + str(thermo.Svib(self.FreqR, iT)))
		return thermo.Svib(self.FreqR, iT) #/[eV/K]
	def Sel(self, **kwargs):
		return 0.


	#### ---- Thermodynamic functions
	def Internal(self, **kwargs):
		# Etras = Erot = Eel = 0
		# Internal = E0 + Evib
		print("E0(ev)="+str(self.E0))
		return self.E0 + self.ZPVE(**kwargs) + self.Evib(**kwargs)
	def Enthalpy(self, **kwargs):
		# No pressure effect: dont include kbT
		return self.Internal(**kwargs)
	def Entropy(self, **kwargs):
		# Binded: Stras = Srot = 0, low T: Sel = 0
		return self.Svib(**kwargs)




################################################################
#### ---------------------------------------------------------------- Gas class
class Gas(SingleItem):
	def __init__(self, **kwargs):
		# Get parent's properties and functions
		SingleItem.__init__(self, **kwargs)
		# Overwrite/Add them
		self.mass = kwargs.get('Mass') # [AMU = g/mol]
		self.Geometry = kwargs.get('Geometry')
		self.RotSym	= kwargs.get('RotSymNum')
		self.RotTemp = kwargs.get('RotT') # Rotational temperatures [K]

	#### ---- Partition functions

	def q_tras(self, **kwargs):
		# Check input
		try:
			iT = float(kwargs.get('T')) # T[K]
			iP = float(kwargs.get('P')) # P[bar]
			int(self.mass)					# mass [AMU=g/mol]
		except:
			CodeErrorExit('Need atomic mass [AMU=g/mol], T [K] and P[bar] to compute q traslational')
		# Compute
		return thermo.qTras(self.mass, iT, iP)

	def q_rot(self, **kwargs):
		# Check input
		try:
			'a' in self.Geometry	# 'Diatomic homonuclear', 'Diatomic heteronuclear' or 'Polyatomic'
			iT = float(kwargs.get('T'))	# T[K]
			self.RotSym
			if self.RotTemp == None: raise NameError('Missing Rot temp.')
		except:
			CodeErrorExit('Need rotational temperatures, symmetry, temperature and geometry for qRot of gas '+self.Name)
		# Compute
		return thermo.qRot(self.Geometry, self.RotTemp, iT, self.RotSym)

	def q_vib(self, **kwargs):
		# Check input
		try:
			iT = float(kwargs.get('T')) # T[K]
			self.FreqR[0]	# Freq list [cm-1]
		except:
			CodeErrorExit('Need a list of frea freqs[cm-1] and T[K] to compute qTras')
		# Compute
		return thermo.qVib(self.FreqR, iT)

	def q_el(self, *args, **kwargs):
		return thermo.qEl()

	#### ---- thermo energy contributions

	def Etras(self, **kwargs):
		# Check input
		try:
			iT = float(kwargs.get('T'))
		except:
			CodeErrorExit('Needs T to compute E traslational')
		# Compute
		print("Etras(eV)=" + str(thermo.Etras(iT)))
		return thermo.Etras(iT)	#/[eV]

	def Erot(self, **kwargs):
		# Check input
		try:
			iT = float(kwargs.get('T'))
			'a' in self.Geometry
		except:
			CodeErrorExit('Needs T and Geometry property to compute E rot')
		# Compute
		print("Erot(eV)=" + str(thermo.Erot(self.Geometry, iT)))
		return thermo.Erot(self.Geometry, iT)

	def ZPVE(self, **kwargs):
		# Check input
		try:
			self.FreqR[0]	# Freq list [cm-1]
		except:
			CodeErrorExit('Can\'t compute ZPVE without freqs.')
		# Compute
		print('ZPVE(eV)=' + str(thermo.ZPVE(self.FreqR)))
		return thermo.ZPVE(self.FreqR) #/[eV]

	def Evib(self, **kwargs):
		# Check input
		try:
			iT = float(kwargs.get('T'))
			self.FreqR[0]
		except:
			CodeErrorExit('Needs real frequencies to compute E vib.')
		# Compute
		print('Ev(eV)=' + str(thermo.Evib(self.FreqR, iT)))
		return thermo.Evib(self.FreqR, iT)

	def Eel(self, **kwargs):
		# Bottom of well as reference
		# Negligible population of higher levels is assumed
		return 0.

	#### ---- thermo entropy contributions

	def Stras(self, **kwargs):
		# TODO: Units already checked, all Ok
		# Check input
		try:
			iT = float(kwargs.get('T')) # T[K]
			iP = float(kwargs.get('P')) # P[bar]
			self.mass					# mass [AMU=g/mol]
		except:
			CodeErrorExit('Need atomic mass [AMU=g/mol], T [K] and P[bar] to compute q tras and then Stras')
		# Compute
		print('Stras(eV)='+str(kb*(np.log(self.q_tras(**kwargs))+5./2.)/eV2J))
		return kb*(np.log(self.q_tras(**kwargs))+5./2.)/eV2J	#/[eV/K]

	def Srot(self, **kwargs):
		# Check input
		try:
			self.Geometry				# 'Diatomic homonuclear', 'Diatomic heteronuclear' or 'Polyatomic'
			iT = float(kwargs.get('T'))	# T[K]
			# self.RotSym+1.
			if self.RotTemp == None: raise NameError('Missing rotational temperature')
		except:
			CodeErrorExit('Need rotational temperatures[K], symmetry, temperature[K] and geometry for Srot of gas')
		# Compute
		print('Srot(eV)=' + str(thermo.Srot(self.Geometry, self.RotTemp, iT, self.RotSym)))
		return thermo.Srot(self.Geometry, self.RotTemp, iT, self.RotSym)

	def Svib(self, **kwargs):
		# Check input
		try:
			iT  = float(kwargs.get('T')) # T[K]
			self.FreqR[0] # FreqR list [cm-1]
		except:
			CodeErrorExit('Need real frequencies list [cm-1] and T [K] to compute Svib')
		# Compute
		print("Svib(eV)=" + str(thermo.Svib(self.FreqR, iT)))
		return thermo.Svib(self.FreqR, iT) #/[eV/K]

	def Sel(self, **kwargs):
		# Bottom of well reference
		# Negligible population of higher levels is assumed
		return 0


	#### ---- Thermodynamic functions
	def Internal(self, **kwargs):
		# Eel = 0
		# Internal = E0 + Etras + Erot  + ZPVE + Evib
		return self.E0 + self.Etras(**kwargs) + self.Erot(**kwargs) + self.ZPVE(**kwargs) + self.Evib(**kwargs)
	def Enthalpy(self, **kwargs):
		# Includes pressure effect: H = U + kbT
		return self.Internal(**kwargs)+kb*kwargs.get('T')/eV2J #[eV]
	def Entropy(self, **kwargs):
		# Svib = 0
		return self.Stras(**kwargs)+self.Srot(**kwargs)+self.Svib(**kwargs)




################################################################
#### ---------------------------------------------------------------- Physisorbed Class
class PhysSurf(Gas):
	# Inherits __init__ with gas parameters:
	# self.		mass  [AMU=g/mol], Geometry ['Diatomic homonuclear', 'Diatomic heteronuclear' or 'Polyatomic'],
	# 			RotSym [Rotational symmetry number], RotTemp [3 Rotational temperatures, K]

	#### --- Partition functions
	def q_tras(self, **kwargs):
		# translation not considered for physisorbed species, for now
		return 1.
	# Inherits q_rot, q_vib, q_el

	#### --- thermo energy contributions
	def Etras(self, **kwargs):
		# traslation not considered for physisorbed species, for now
		return 0.
	# Inherits Erot, ZPVE, Evib, Eel

	#### --- thermo entropy contributions
	def Stras(self, **kwargs):
		# translation not considered for physisorbed species, for now
		return 0.
	# Inherits Srot, Svib, Sel

	#### --- Thermodynamic functions
	# Inherits Internal and Entropy from Gas class, Gibbs from SingleItem class
	def Enthalpy(self, **kwargs):
		# Does not include pressure effect: H = U
		return self.Internal(**kwargs)





print('Ok')