#### Packages
import matplotlib.pyplot as plt
from .promps import CodeStatus, fStringLength, fNum
from .parameters import eV2J, eV2kJpmol
from .kinetics import rate_cte
from .kinetics import equilibria_cte

print('>> Loading Plot tools', end='...')


################################################################################################################################
################ Reference Object

class RxRef:
	def __init__(self, Pos0=0, En0=0., **kwargs):
		self.RootE = En0
		self.RootX = Pos0
		self.log = [(Pos0, En0)]
		self.TailE = En0
		self.TailX = Pos0
		self.Tail  = (En0, Pos0)
		self.FlatWidth = .4
		self.Color = kwargs.get('Color', 'k')

		if not kwargs.get('Branched'):
			CodeStatus('Reference object created')

	def branch(self, **kwargs):
		# Create new branch
		NewBranch = RxRef(Branched=True)
		# Copy root info
		NewBranch.RootE = self.RootE
		NewBranch.RootX = self.RootX
		# Tail info until step
		EndStep = kwargs.get('Step', None)
		if isinstance(EndStep, int) and int(EndStep) < len(self.log):
			NewBranch.log = [self.log[i] for i in range(0, int(EndStep))]
			NewBranch.TailE = self.log[int(EndStep)][1]
			NewBranch.TailX = self.log[int(EndStep)][0]
			NewBranch.Tail = self.log[int(EndStep)]
		else:
			NewBranch.log	= self.log
			NewBranch.TailE = self.TailE
			NewBranch.TailX = self.TailX
			NewBranch.Tail = (self.TailX, self.TailE)

		CodeStatus('Reference branched from previous')

		return NewBranch

	def Update(self, NewX, NewE, **kwargs):
		self.TailE = NewE
		self.TailX = NewX
		self.Tail = (NewX, NewE)

		if not kwargs.get('Props',None):
			self.log = [i for i in self.log] + [(NewX, NewE, kwargs.get('Props'))]
		else:
			self.log = [i for i in self.log] + [(NewX, NewE)]

	def UpdateFromTail(self, Ref):
		if isinstance(Ref, RxRef):
			self.Update(Ref.TailX, Ref.TailE)
		else:
			CodeStatus('Error trying to pdate reference object from other reference object')

	def EndPoint(self):
		plt.plot([0,0],[1.,1.])

	def PlotExtend(self, SpanX=1, **kwargs):
		# Defaults for plot
		iColor = kwargs.get('Color',self.Color)
		iLineStyle = kwargs.get('LineStyle', 'solid')
		iLineWidth = kwargs.get('LineWidth', .8)
		iAlpha = kwargs.get('Alpha', 1.)
		if 'Until' in kwargs:
			if kwargs.get('Until') >= self.TailX:
				SpanX = kwargs.get('Until')-self.TailX

		# Plot
		plt.plot([self.TailX, self.TailX+SpanX], [self.TailE, self.TailE],
				 color=iColor, linestyle=iLineStyle, alpha=iAlpha,
				 linewidth=iLineWidth, zorder=1.)

		# Update
		self.Update(self.TailX+SpanX, self.TailE)






################################################################################################################################
################ Quick add note
def QuickNote(iStr, ixy, **kwargs):
	# iStr  = String note
	# ixy	= [float , float] position data

	# Default parameters
	iColor = kwargs.get('Color', 'k')
	ixytext = kwargs.get('ixytext',[.5,.5])
	iha = 'center'
	iva  = 'center'

	# Location options
	Loc = kwargs.get('Loc','top-center')
	if Loc == 'top-center':
		ixytext = [.5,.95]
		iva = 'top'
		iha =  'center'
	elif Loc == 'bottom-center':
		ixytext = [.5,.05]
		iva = 'bottom'
		iha =  'center'
	elif Loc == 'top-right':
		ixytext = [.95, .95]
		iva = 'top'
		iha = 'right'
	elif Loc == "out-left-top":
		ixytext = [1.02, .95]
		iva = 'top'
		iha = 'left'
	elif Loc == "out-left-bottom":
		ixytext = [1.01, .05]
		iva = 'bottom'
		iha = 'left'
	elif Loc == "out-left-center":
		ixytext = [1.01, .5]
		iva = 'center'
		iha = 'left'

	ThisNote  = plt.gca().annotate(iStr,
								   xy=ixy, xytext=ixytext,
								   xycoords='data',
								   textcoords='axes fraction',
								   ha=iha, va=iva,
								   size=kwargs.get('Size',12), color='k',
								   bbox = dict(boxstyle='round', facecolor='darkgray', edgecolor=iColor, alpha=.8),
								   arrowprops = dict(arrowstyle='->', color=iColor, alpha=0.5), zorder=100
								   )
	# Anounce creation
	if  kwargs.get('Promp',False):
		CodeStatus('Annotation created', l=8)

	return ThisNote


################################################################################################################################
################ Hover annotation functions

def AddHoverNote(iHoverList, iStr, ixy, **kwargs):
	#### Default parameters
	iColor = kwargs.get('Color','k')
	# Create Note
	ThisNote  =  QuickNote(iStr,  ixy, Promp=False, **kwargs)
	# Occult Note
	ThisNote.set_visible(False)
	# Create pointer
	ThisPoint = plt.gca().scatter(ixy[0],ixy[1], marker='+', color=iColor, alpha=kwargs.get('Alpha',1.), zorder=20)
	# almacenate
	iHoverList.append((ThisPoint, ThisNote))

	# Report
	if kwargs.get('NotePromp',True):
		CodeStatus('Hover-Note created and almacenated', l=8)


def ActivateHover(iHoverList, Figure):
	def hover(event):
		cont = False
		ind = 0
		if event.inaxes:
			for iSc in range(len(iHoverList)):
				if iHoverList[iSc][0].contains(event)[0]:
					cont =  True
					ind = iSc
					break
				else:
					cont = False
					ind = 0
			if cont:
				iHoverList[ind][1].set_visible(True)
				Figure.canvas.draw_idle()
			else:
				for iSc in  iHoverList:
					iSc[1].set_visible(False)
					Figure.canvas.draw_idle()
	Figure.canvas.mpl_connect('motion_notify_event',hover)





################################################################################################################################
#### Add step to plot
def RxStepTS(En, Ref=0., UpdateRef=True,  **kwargs):
	####
	#		Ref	=	float
	#				List  of tuples (x,E) : [(x,E)1, (x,E)2, ...], last is considered
	#		UpdateRef =  True : add tuple to Ref list

	# Get Step only info
	iSpan = float(kwargs.get('StepSpan', 1))
	UnitsFactor = float(kwargs.get('UnitsFactor', eV2kJpmol))

	# Scale input (eV) to kwargs.UnitsFactor, by default in eV->kJ/mol
	for i in range(3):
		En[i]*=UnitsFactor

	# Reference (get Etail, Xtail)
	if isinstance(Ref, RxRef):
		#print('Reference is object-reference')
		Etail = Ref.TailE
		Xtail = Ref.TailX
		FlatWidth = min(Ref.FlatWidth,iSpan*2/4)
		iColor = Ref.Color

	# Override for this step
	iColor = kwargs.get('Color', 'k')
	iLineStyle = kwargs.get('LineStyle', 'solid')
	iLineWidth = kwargs.get('LineWidth', 1.5)
	iAlphaLines = kwargs.get('AlphaLines',.3)
	iHoverLocation = kwargs.get("HoverLocation", "top-center")

	# Energy deltas
	Eaf = En[1]-En[0]
	Eab = En[1]-En[2]
	DE	= En[2]-En[0]

	# Direction
	if kwargs.get('RefDir','F')[0] == 'B':
		iRxDir=-1
		ERef = En[2] - Etail
	else:
		iRxDir = 1
		ERef = En[0] - Etail

	# Positions [ini->TS->fin]
	Pos = [Xtail + i * iSpan * iRxDir for i in [0, 1, 2]]


	# Plot: flats
	plt.plot([Pos[0], Pos[0] + FlatWidth / 2.], [En[0] - ERef] * 2, color=iColor, linestyle=iLineStyle)  # Fin line
	plt.plot([Pos[1] - FlatWidth / 2., Pos[1] + FlatWidth / 2.], [En[1] - ERef] * 2, color=iColor, linestyle=iLineStyle)  # TS line
	plt.plot([Pos[2] - FlatWidth / 2., Pos[2]], [En[2] - ERef] * 2, color=iColor, linestyle=iLineStyle)  # Fin line

	# Plot: slopes
	plt.plot([Pos[0] + FlatWidth / 2., Pos[1] - FlatWidth / 2.], [En[0] - ERef, En[1] - ERef], color=iColor, alpha=iAlphaLines, linestyle=iLineStyle, linewidth=iLineWidth, zorder=5.)
	plt.plot([Pos[1] + FlatWidth / 2., Pos[2] - FlatWidth / 2.], [En[1] - ERef, En[2] - ERef], color=iColor, alpha=iAlphaLines, linestyle=iLineStyle, linewidth=iLineWidth, zorder=5.)


	# Promp
	CodeStatus(fStringLength('Adding reaction step (TS) to current plot', Side='r', l=90, Filling='.'), end=' '+kwargs.get('Name','')+'\n')
	CodeStatus('Activation forward='+fNum(Eaf,'2f')+' ; backward='+fNum(Eab,'2f')+' ; Delta = '+fNum(DE,'2f'), l=8)

	#### Hover option
	if isinstance(kwargs.get('Hover',False), list):
		# TS Note
		TSpoint = plt.scatter(Pos[1], En[1] - ERef, marker='.', color=iColor, alpha=0., zorder=20)  # TS +
		strNote =  kwargs.get('Name','No Name Rx Step')+\
				   '\nDE(Rx)='+fNum(DE,'2f')+' /kJ/mol'+\
				   '\nEa='+fNum(Eaf,'2f')+'('+fNum(Eab,'2f')+') '+', Ea(-ref)='+fNum(En[1]-ERef,'2f')+' /kJ/mol'
		if 'T-rate' in kwargs:
			strNote += '\n k(s-1)='+str('{:.2e}'.format(rate_cte(En[1]/UnitsFactor, En[0]/UnitsFactor, kwargs.get('T-rate', 298))))
			strNote += ' ; k-1(s-1)=' + str('{:.2e}'.format(rate_cte(En[1] / UnitsFactor, En[2] / UnitsFactor, kwargs.get('T-rate', 298))))
			strNote += '\n K=' + str('{:.2e}'.format(equilibria_cte(En[2] / UnitsFactor, En[0] / UnitsFactor, kwargs.get('T-rate', 298))))
		ThisNote = QuickNote(strNote,
							 [Pos[1], En[1] - ERef],
							 Size=kwargs.get('NoteSize',9), Color=iColor, Loc=iHoverLocation)
		ThisNote.set_visible(False)
		kwargs.get('Hover').append((TSpoint, ThisNote))
		# Fin Note
		Endpoint = plt.scatter(Pos[2], En[2] - ERef, marker='+', color=iColor, alpha=0.)  # TS +
		strNote = ""
		if "->" in kwargs.get("Name"): strNote +=" "+kwargs.get("Name").split("->")[1]+"\n"
		strNote +=  'Ef(-ref)='+fNum(En[2]-ERef,'2f')+' /kJ/mol'+'\nE='+fNum(En[2],'2f')+' /kJ/mol\nX='+str(Pos[2])
		ThisNote = QuickNote(strNote,
							 [Pos[2], En[2] - ERef],
							 Size=kwargs.get('NoteSize',9), Color=iColor, Loc=iHoverLocation)
		ThisNote.set_visible(False)
		kwargs.get('Hover').append((Endpoint, ThisNote))
		CodeStatus('Hover-Note created', l=8)


	#### Update references
	if UpdateRef:
		if iRxDir == 1:
			if isinstance(Ref, RxRef):
				Ref.Update(Pos[2], En[2] - ERef)
			elif isinstance(Ref,  list) and isinstance(Ref[-1], tuple):
				Ref.append((Pos[2], En[2] - ERef))
			CodeStatus('Reference updated forward', l=8)
		elif iRxDir == -1:
			if isinstance(Ref, RxRef):
				Ref.Update(Pos[0], En[0] - ERef)
			elif isinstance(Ref,  list) and isinstance(Ref[-1], tuple):
				Ref.append((Pos[0], En[0] - ERef))
			CodeStatus('Reference updated backwards', l=8)
	else:
		if isinstance(Ref, RxRef):
			Ref.Update(Ref.TailX, Ref.TailE)
		else:
			Ref.append(Ref[-1])
		CodeStatus('Reference NOT updated', l=8)

	CodeStatus(fStringLength('Step added', Side='r', l=90, Filling='.'), end='\n\n')


#### Add step to plot
def RxStep(En, Ref=0., UpdateRef=True,  **kwargs):
	####
	#		Ref	=	float
	#				List  of tuples (x,E) : [(x,E)1, (x,E)2, ...], last is considered as starting point
	#		UpdateRef =  True : add tuple to Ref list

	# Get Step only info
	iSpan = float(kwargs.get('StepSpan', 1))
	UnitsFactor = float(kwargs.get('UnitsFactor', eV2kJpmol))

	# Scale input (eV) to kwargs.UnitsFactor, by default in eV->kJ/mol
	for i in range(2):
		En[i]*=UnitsFactor

	# Reference
	if isinstance(Ref, RxRef):
		Etail = Ref.TailE
		Xtail = Ref.TailX
		FlatWidth = min(Ref.FlatWidth,2*iSpan/1.5)
		iColor = Ref.Color

	# Override for this step
	iColor = kwargs.get('Color', 'k')
	iLineStyle = kwargs.get('LineStyle', 'solid')
	iLineWidth = kwargs.get('LineWidth', 1.5)
	iAlphaLines = kwargs.get('AlphaLines', .3)
	iHoverLocation = kwargs.get("HoverLocation","top-center")



	# Energy deltas
	DE	= En[1]-En[0]

	# Direction
	if kwargs.get('RefDir','F')[0] == 'B':
		iRxDir=-1
		ERef = En[1] - Etail
	else:
		iRxDir = 1
		ERef = En[0] - Etail

	# Positions
	Pos = [Xtail + i*iSpan*iRxDir for i in [0,2]]

	# plot: Flats
	plt.plot([Pos[0], Pos[0] + FlatWidth / 2.], [En[0] - ERef]*2, color=iColor, alpha=1., linestyle=iLineStyle)
	plt.plot([Pos[1] - FlatWidth / 2., Pos[1]], [En[1] - ERef]*2, color=iColor, alpha=1., linestyle=iLineStyle)
	# plot: Line
	plt.plot([Pos[0]+FlatWidth/2., Pos[1]-FlatWidth/2.], [En[0] - ERef, En[1] - ERef], color=iColor, alpha=iAlphaLines, linestyle=iLineStyle, linewidth=iLineWidth)

	# Promp
	CodeStatus(fStringLength('Adding reaction step to current plot', Side='r', l=90, Filling='.'), end=' '+kwargs.get('Name','')+'\n')
	CodeStatus('Delta = '+fNum(DE,'2f'), l=8)

	#### Hover option
	if isinstance(kwargs.get('Hover',False),list):
		# Middle: Step info
		strNote = kwargs.get('Name', 'No Name Rx Step') + '\nDE=' + fNum(DE, '2f') + '  /kJ/mol'
		AddHoverNote(kwargs.get('Hover'),strNote,
					 [(Pos[0]+Pos[1])/2., (En[0]+En[1])/2. - ERef],
					 Size=kwargs.get('NoteSize',9), Color=iColor, Alpha=.0, Loc=iHoverLocation)
		# Final: Flat info
		strNote = ""
		if "->" in kwargs.get("Name"): strNote+=" "+kwargs.get("Name").split("->")[1]+"\n"
		strNote += 'Ef(-ref)='+fNum(En[1]-ERef, '2f')+' /eV\nE='+fNum(En[1],'2f')+' /kJ/mol\nX='+str(Pos[1])
		AddHoverNote(kwargs.get('Hover'),strNote,
					 [Pos[1], En[1]-ERef],
					 Size=kwargs.get('NoteSize',9), Color=iColor, Alpha=.0, Loc=iHoverLocation)


	#### Update reference
	if UpdateRef:
		# Forward
		if kwargs.get('RefDir','F')[0] in ['B','b']:
			if isinstance(Ref, RxRef):
				Ref.Update(Pos[0],En[0]-ERef)
			else:
				Ref.append((Pos[0],En[0]-ERef))
			CodeStatus('Reference updated backwards',  l=8)
		# Backwards
		else:
			if isinstance(Ref, RxRef):
				Ref.Update(Pos[1],En[1]-ERef)
			else:
				Ref.append((Pos[1],En[1]-ERef))
			CodeStatus('Reference updated forwards',  l=8)
	else:
		if isinstance(Ref, RxRef):
			Ref.Update(Ref.TailX, Ref.TailE)
		else:
			Ref.append(Ref[-1])
		CodeStatus('Reference NOT updated', l=8)

	CodeStatus(fStringLength('Step added', Side='r', l=90, Filling='.'), end='\n\n')




# #### Add step to plot
#
# #### DEPRECATED AS 11, Nov, 2021
#
# def RxJump(En, Ref, UpdateRef=True, **kwargs):
# 	####
# 	#		Ref	=	float
# 	#				List  of tuples (x,E) : [(x,E)1, (x,E)2, ...], last is considered as starting point
# 	#		UpdateRef =  True : add tuple to Ref list
#
# 	# Energy deltas
# 	DE	= En[1]-En[0]
#
# 	# Default parameters
# 	iColor = kwargs.get('Color','k')
#
# 	# Reference
# 	if isinstance(Ref, RxRef):
# 		Pos = Ref.TailX
# 		Etail = Ref.TailE
# 	elif isinstance(Ref, list) and isinstance(Ref[-1], tuple):
# 		Pos = Ref[-1][0]
# 		Etail = Ref[-1][1]
#
# 	# Direction
# 	if kwargs.get('RefDir','F')[0] == 'B':
# 		ERef = En[0]-Etail+DE
# 	else:
# 		ERef = En[0]-Etail
#
# 
#
# 	# plot
# 	plt.plot([Pos, Pos], [En[0] - ERef, En[1] - ERef], '--',color=iColor, alpha=.4)	# Initial, final
#
# 	# Promp
# 	CodeStatus(fStringLength('Adding reaction jump step to current plot', Side='r', l=90, Filling='.'), end=' '+kwargs.get('Name','')+'\n')
# 	CodeStatus('Delta = '+fNum(DE,'2f'), l=8)
#
# 	#### Hover option
# 	if isinstance(kwargs.get('Hover',False), list):
# 		strNote = kwargs.get('Name', 'No Named Rx Jump Step') + '\nDE=' + fNum(DE, '2f') + '  /eV'
# 		AddHoverNote(kwargs.get('Hover'),strNote, [Pos, (En[0]+En[1])/2. - ERef], Size=kwargs.get('NoteSize',9), NotePromp=True, Color=iColor)
# 		CodeStatus('Hover-Note created', l=8)
#
# 	#### Update reference
# 	if UpdateRef:
# 		# Forwards
# 		if kwargs.get('RefDir', 'F')[0] == 'B':
# 			if isinstance(Ref, RxRef):
# 				Ref.Update(Pos, En[0]-ERef)
# 			elif isinstance(Ref, list) and isinstance(Ref[-1], tuple):
# 				Ref.append((Pos, En[0] - ERef))
# 			CodeStatus('Reference updated backwards', l=8)
# 		# Backwards
# 		else:
# 			if isinstance(Ref, RxRef):
# 				Ref.Update(Pos, En[1]-ERef)
# 			elif isinstance(Ref, list) and isinstance(Ref[-1], tuple):
# 				Ref.append((Pos, En[1] - ERef))
# 			CodeStatus('Reference updated forwards', l=8)
# 	else:
# 		#Not update
# 		if isinstance(Ref, RxRef):
# 			Ref.Update(Ref.TailX, Ref.TailE)
# 		else:
# 			Ref.append(Ref[-1])
# 		CodeStatus('Reference NOT updated', l=8)





def AnnotateStepAxis(Names, Ref, **kwargs):
	### kwargs				Size = text size
	#						Colour = text colour
	#						Level = text level from bottom

	# Checks
	if not isinstance(Names, list): quit('>>>> Names option has to be a list, bye!')
	if not isinstance(Ref, RxRef)  and not isinstance(Ref[-1], tuple):
		quit('>>>> Names option has to be a RxRef object or list of tuples, bye!')

	# Reference - last one
	iSpanLog = 2
	if isinstance(Ref, RxRef):
		Xtail = Ref.TailX
		# Get span
		if len(Ref.log)>1:
			iSpanLog = Ref.TailX - Ref.log[-2][0]

	elif isinstance(Ref, list) and isinstance(Ref[-1], tuple):
		Xtail = Ref[-1][0]


	# Parameters
	iSize	= kwargs.get('Size',8)
	iColour = kwargs.get('Colour','k')
	iSpan = float(kwargs.get('StepSpan', iSpanLog))
	iLevel	= '\n'*(kwargs.get('Level',1)-1)
	Loc = kwargs.get('Loc','bottom')
	Hhandler = kwargs.get('H_Handler', 'center')


	# Positions
	if kwargs.get('RefDir','Forw')[0]=='B':
		Pos=[Xtail+i for i in range(3)]
	else:
		Pos=[Xtail-i*iSpan/2 for i in range(3)]
		Pos.sort()

	# String construction
	iStr=''
	if len(Names)==1:
		iStr = r'$\rightarrow$'+Names[0]
	if len(Names) > 1:
		iStr = Names[0]
		for iNm in Names[1:]:
			iStr+= r'$\rightarrow$' + iNm

	# Position
	if Loc == 'bottom':
		plt.annotate(iLevel+iStr,
					 xy=[(Pos[0]+Pos[-1])/2., 0.],xytext=[0, -5],
					 xycoords=('data', 'axes fraction'), textcoords='offset points',
					 ha=Hhandler, va='top', size=iSize, color=iColour)
	elif Loc=='top':
		plt.annotate(iStr+iLevel,
					 xy=[(Pos[0]+Pos[-1])/2., 1.],xytext=[0, 5],
					 xycoords=('data', 'axes fraction'), textcoords='offset points',
					 ha=Hhandler, va='bottom', size=iSize, color=iColour)



def RxAxis(**kwargs):
	plt.axes(plt.gca()).get_xaxis().set_ticklabels([])
	plt.grid()

	if kwargs.get('EnergyAxis', False):
		if kwargs.get('EnergyAxis', False) == True:
			plt.ylabel('Energy / kJ/mol', size=max(kwargs.get('Size', 16) - 4, 10))
		else:
			plt.ylabel('Energy / '+str(kwargs.get('EnergyAxis', False)), size=max(kwargs.get('Size', 16) - 4, 10))

	Loc = kwargs.get('Loc','top-right-in')
	al = kwargs.get('Alpha', .9)
	co = kwargs.get('Color','k')
	sz = kwargs.get('Size',16)

	if sz < 7 :
		txt = 'Reaction \n coordinate $\longrightarrow$'
		sz = 7
	else:
		txt = '$\longrightarrow$'

	if Loc =='top-right-in':
		plt.annotate(txt, xy=[1., 1.],xytext=[-5, -5],
					 xycoords=('axes fraction', 'axes fraction'), textcoords='offset points',
					 ha='right', va='top', size=sz, color=co,
					 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=al))

	elif Loc =='top-right-out':
		plt.annotate(txt, xy=[1., 1.],xytext=[-5, 5],
					 xycoords=('axes fraction', 'axes fraction'), textcoords='offset points',
					 ha='right', va='bottom', size=sz, color=co,
					 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=al))

	elif Loc =='top-center-in':
		plt.annotate(txt, xy=[.5, 1.],xytext=[0, -5],
					 xycoords=('axes fraction', 'axes fraction'), textcoords='offset points',
					 ha='center', va='top', size=sz, color=co,
					 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=al))

	elif Loc == 'bottom-right-in':
		plt.annotate(txt, xy=[1., 0.], xytext=[-5, 5],
					 xycoords=('axes fraction', 'axes fraction'), textcoords='offset points',
					 ha='right', va='bottom', size=sz, color=co,
					 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=al))

	elif Loc == 'bottom-left-in':
		plt.annotate(txt, xy=[0., 0.], xytext=[5, 5],
					 xycoords=('axes fraction', 'axes fraction'), textcoords='offset points',
					 ha='left', va='bottom', size=sz, color=co,
					 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=al))

	elif Loc == 'bottom-center-in':
		plt.annotate(txt, xy=[0.5, 0.], xytext=[5, 5],
					 xycoords=('axes fraction', 'axes fraction'), textcoords='offset points',
					 ha='center', va='bottom', size=sz, color=co,
					 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=al))

	else:
		plt.annotate(txt, xy=[.5, .5],xytext=[0, 5],
					 xycoords=('axes fraction', 'axes fraction'), textcoords='offset points',
					 ha='center', va='bottom', size=sz, color=co,
					 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=al))

def Align_Rx_Ticks(*args, **kwargs):
	"""Align current plot ticks acording to Reference entries in args and boolena keyword TSmode."""

	TickRange=[]

	EntryList = []
	for iRef in args:
		if isinstance(iRef, RxRef):
			EntryList.append(iRef.log)
		elif isinstance(iRef, list):
			EntryList.append(iRef)


	for iRef in EntryList:
		# Mark TS mode
		if kwargs.get('TSmode',False):
			for i in range(len(iRef)-1):
				if iRef[i][0]==iRef[i+1][0]:
					continue
				iTS=(iRef[i][0]+iRef[i+1][0])/2.
				if iTS not in TickRange: TickRange.append(iTS)

		# Delimitate steps mode
		else:
			for iEntry in iRef:
				if iEntry[0] not in TickRange: TickRange.append(iEntry[0])


	TickRange.sort()


	# Plot limits
	MinShown, MaxShown  = plt.axes(plt.gca()).get_xlim()

	# Limit ticks
	NewTicks = [i for i in TickRange if i>MinShown and i <  MaxShown]

	# Set new ticks
	plt.axes(plt.gca()).set_xticks(NewTicks)





















print('Ok')

