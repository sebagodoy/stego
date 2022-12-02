#### Functions that help promp
print('>> Loading promp functions ', end='...')

#### Code execution functions
def CodeStatus(inStr, **kwargs):
	# Reports abut execution: l=(integer) left spaces,  end=(string)  ending of string
	print(' '*kwargs.get('l',4) + '> '+ inStr,  end=kwargs.get('end','\n'))

def CodeErrorExit(inStr, **kwargs):
	# Reports abut execution: l=(integer) left spaces,  end=(string)  ending of string
	print(' ' * int(kwargs.get('l', 2)) + '>> ¡!¡!¡! ' + inStr, end=kwargs.get('end', '\n'))
	raise NameError


def MayorSection(SectionTitle):
	# Promp for sections titles
	print('\n'+'=' * 80 + '\n' + '=' * 8 +' '+ SectionTitle + '\n'+'=' * 80 + '\n')

def MinorSection(SectionTitle):
	# Promp for sections subtitles
	print('\n'+'=' * 80 + '\n' + ' ' * 8 + SectionTitle+'\n')



#### String len formating
def fStringLength(iStr, **kwargs):
	# Add characters to string until length l=(integer)
	length = kwargs.get('l', 10)
	strout = iStr
	if len(strout) < length:
		# Add to the right
		if  kwargs.get('Side','l')=='r': strout += kwargs.get('Filling', ' ') * (length - len(strout))
		# Add to the left, default
		else: strout = kwargs.get('Filling',' ')*(length-len(strout))+strout
	return strout


#### Number formating
def fNum(number, formato):
	# formats number acording to formato=(str)
	# e.g.  fNum(3.1415, '2f') -> 2 decimal float
	#		fNum(3.1415, '2e') -> 2 decimal cientific
	tmpFormato = '{:.'+formato+'}'
	return tmpFormato.format(number)

def fNumLength(number, **kwargs):
	# Chop numbers up to the d=(integer) decimal
	# Add left spaces to string until length l=(integer)
	dec = '{:.'+str(kwargs.get('d',4))+'f}'
	length = kwargs.get('l', 10)
	strout = dec.format(number)
	if len(strout)<length: strout = kwargs.get('Filling',' ')*(length-len(strout))+strout
	return strout

print('Ok')