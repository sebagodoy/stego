# DOS definition
# Ver 1.1

import matplotlib.pyplot as plt
print(' ' * 4 + '> Loading DOS class')



class DOS:
    def __init__(self, Direction, Pol=True, Orb='spd', ml=False, **kwargs):
        # Direction: direction of DOSCAR file. ex.: "./DOS/DOSCAR"
        # Pol: Boolean, polarized calc
        # Orb = 's', 'sp', 'spd', 'spdf', 'none' ('none' if only global DOS is included)
        # ml : Boolean, True if there is ml partition (i.e. p->px,py,pz, d-> ...)

        # Check initial
        if Orb not in ['s', 'sp', 'spd', 'spdf', 'none']:
            raise NameError(f"The orb option needs to be \'s\', \'sp\', \'spd\' or \'none\'")



        # Open, read Header
        with open(Direction) as f:
            DOSfile = f.readlines()

        self.NAtoms = int(DOSfile[0].split()[0])
        self.Fermi = float(DOSfile[5].split()[3])
        self.NDOS = int(DOSfile[5].split()[2])
        self.Pol = bool(kwargs.get('Pol', True))
        self.Name = kwargs.get("Name") or DOSfile[4].lstrip().rstrip()
        self.Nelec = float(0)
        self.orb = Orb

        # Get list of energies from global block
        self.Elist = []
        for i in range(self.NDOS):
            self.Elist.append(float(DOSfile[6 + i].split()[0]))


        # Get Global (first DOS block, alwasy included)
        self.DOS = {}
        if Pol:
            self.DOS['global'] = {'+': [], '-': []}
            for i in range(self.NDOS):
                self.DOS['global']['+'].append(float(DOSfile[6 + i].split()[1]))
                self.DOS['global']['-'].append(float(DOSfile[6 + i].split()[2]))
        else:
            for i in range(self.NDOS):
                self.DOS['global'] = {'0': []}
                self.DOS['global']['0'].append(float(DOSfile[6 + i].split()[1]))



        # Get by atom
        for iAt in range(self.NAtoms):
            StartIndex = 6 + (self.NDOS + 1) * (iAt + 1)
            # Configure slots
            self.DOS[str(iAt + 1)] = {}




            # ----------------------------------------------------------------------------------------------------------
            if ml:
                if Pol and Orb == 'sp':
                    columnclass = {1: 's+', 2: 's-',
                                   3: 'px+', 4: 'py+', 5: 'pz+', 6: 'px-', 7: 'py-', 8: 'pz-'}
                elif Pol and Orb == 'spd':
                    columnclass = {1: 's+', 2: 's-',
                                   3: 'py+', 4: 'py-', 5: 'pz+', 6: 'pz-', 7: 'px+', 8: 'px-',
                                   9: 'd1+', 10: 'd1-', 11: 'd2+', 12: 'd2-', 13: 'd3+', 14: 'd3-',
                                   15: 'd4+', 16: 'd4-', 17: 'd5+', 18: 'd5-'}
                elif Pol and Orb == 'spdf':
                    columnclass = {1: 's+', 2: 's-',
                                   3: 'py+', 4: 'py-', 5: 'pz+', 6: 'pz-', 7: 'px+', 8: 'px-',
                                   9: 'd1+', 10: 'd1-', 11: 'd2+', 12: 'd2-', 13: 'd3+', 14: 'd3-',
                                   15: 'd4+', 16: 'd4-', 17: 'd5+', 18: 'd5-',
                                   19: 'f1+', 20: 'f1-', 21: 'f2+', 22: 'f2-', 23: 'f3+', 24: 'f3-',
                                   25: 'f4+', 26: 'f4-', 27: 'f5+', 28: 'f5-', 29: 'f6+', 30: 'f6-',
                                   31: 'f7+', 32: 'f7-'}
                elif Pol and Orb == 'none':
                    columnclass = {}
            else:
                if Pol and Orb == 'sp':
                    columnclass = {1: 's+', 2: 's-', 3: 'p+', 4: 'p-'}
                elif Pol and Orb == 'spd':
                    columnclass = {1: 's+', 2: 's-', 3: 'p+', 4: 'p-', 5: 'd+', 6: 'd-'}
                elif Pol and Orb == 'spdf':
                    columnclass = {1: 's+', 2: 's-', 3: 'p+', 4: 'p-', 5: 'd+', 6: 'd-', 7: 'f+', 8: 'f-'}
                elif Pol and Orb == 'none':
                    columnclass = {}

            # Create slots
            for i in columnclass:
                self.DOS[str(iAt + 1)][columnclass[i]] = []

            # Retrieve DOS curves
            for k in range(self.NDOS):
                for Col in columnclass:
                    self.DOS[str(iAt + 1)][columnclass[Col]].append(float(DOSfile[StartIndex + k].split()[Col]))

        #### Add some useful curves
        # global (first block), magnetism
        if Pol:
            self.DiffDOS(('global', 'mag'), ('global', '+'), ('global', '-'))
        # global (first block), sum
        if Pol:
            self.SumDOS(('global', 'sum'), [('global', '+'), ('global', '-')])
        # total (atomic DOS)
        if Pol:
            # valence layer
            # if Orb == "spd" and not ml:
            #     self.SumDOS(("total", "d+"), [(str(iAt + 1), "d+") for iAt in range(self.NAtoms)])
            #     self.SumDOS(("total", "d-"), [(str(iAt + 1), "d-") for iAt in range(self.NAtoms)])
            #     self.SumDOS(("total", "d+-"), [("total", "d+"), ("total", "d-")])
            self.SumDOS(('total', '+'),
                        [(str(i + 1), j) for j in columnclass.values() for i in range(self.NAtoms) if '+' in j])
            self.SumDOS(('total', '-'),
                        [(str(i + 1), j) for j in columnclass.values() for i in range(self.NAtoms) if '-' in j])
            self.DiffDOS(('total', 'mag'), ('total', '+'), ('total', '-'))
        # total (atomic DOS), sum
        self.SumDOS(('total', 'sum'), [(str(i + 1), j) for j in columnclass.values() for i in range(self.NAtoms)])
        # Per atom
        for iAt in range(self.NAtoms):
            self.SumDOS((str(iAt + 1), 'sum'), [(str(iAt + 1), k) for k in columnclass.values()])
            if Pol:
                # valence layer
                # if Orb == "spd" and not ml:
                #     self.SumDOS((str(iAt+1), "d+-"), [(str(iAt + 1), 'd+'), (str(iAt + 1), 'd-')])
                # sum all +
                self.SumDOS((str(iAt + 1), '+'), [(str(iAt + 1), k) for k in columnclass.values() if '+' in k])
                # sum all -
                self.SumDOS((str(iAt + 1), '-'), [(str(iAt + 1), k) for k in columnclass.values() if '-' in k])
                # spin polarization
                self.DiffDOS((str(iAt + 1), 'mag'), (str(iAt + 1), '+'), (str(iAt + 1), '-'))


        #### Scalling factors
        if 'Nelect' in kwargs:
            self.UpdateScaleToElectronsFactor(kwargs.get('Nelect'))
        else:
            self.GlobalFactor = NameError('\n\n' + ' ' * 4 + 'ERROR: You called for the global or total factor of \''
                                          + self.Name +
                                          '\'\n but have not defined how many electrons this global DOS proyection '
                                          '\n represent. Try first defining with the Nelect=# number of electrons flag '
                                          '\n or using the .UpdateScaleToElectronsFactor(# number of electrons) '
                                          'method \n after creating.')
            self.TotalFactor = self.GlobalFactor

        #### Add to a collection
        if 'Add2' in kwargs:
            self.Add2(kwargs.get('Add2'))

        # Report creation
        if kwargs.get("Report", True):
            print(" " * 2 + "-"*45)
            print(" " * 2 + "<> Created a DOS object containing DOS curves")
            print(" " * 6 + f"> Name          : {self.Name}")
            print(" " * 6 + f"> N atoms       : {self.NAtoms}")
            print(" " * 6 + f"> DOS points    : {self.NDOS}")
            print(" " * 6 + f"> Fermi level   : {self.Fermi}")
            if "Nelect" in kwargs:
                print(" " * 6 + f"> N electrons   : {self.Nelec}")
                print(" " * 6 + f"> Global factor : {self.GlobalFactor} (from cell DOS)")
                if not self.orb == 'none':
                    print(" " * 6 + f"> Total factor  : {self.TotalFactor} (from atom proy. DOS)")
            # self.WhatCurves()

    # Identification
    def __repr__(self):
        return 'DOS object: ' + self.Name

    def __str__(self):
        return 'DOS object: ' + self.Name



    # What curves are included in this object
    def WhatCurves(self):
        print('  >> The object called \'' + self.Name + '\' includes the curves:')
        for i in self.DOS:
            print(' ' * 6 + '<> ' + i + ' : ' + ' , '.join([j for j in self.DOS[i]]))




    # Create Scalling factors from electron numbers
    def UpdateScaleToElectronsFactor(self, iElectr):
        self.Nelec = float(int(iElectr))
        # For the global curves
        # Global scalling factor = n electrons/ integral from global block DOS
        if self.Pol:
            self.GlobalFactor = self.Nelec / self.Integral(('global', 'sum'), To=self.Fermi)
        else:
            self.GlobalFactor = self.Nelec / self.Integral(('global', '0'), To=self.Fermi)
        # For the atom projected curves
        # Total scalling factor = n electrons/ integral from total DOS (sum of all atoms and orbitals)
        if not self.orb == 'none':
            self.TotalFactor = self.Nelec / self.Integral(('total', 'sum'), To=self.Fermi)

    # Create New Curve by adding multiple curves
    def SumDOS(self, Index, ListIndex, **kwargs):
        # Creates a new DOS curve from the ones on the dicctionary
        # Index = ('Who', 'What)    tuple of string indexes for the new curve
        #                           New curve created can be accesed
        #                           as self.DOS['Who']['What']
        # ListIndex = [('Who 1','What 1'), ('Who 2','What 2'), ...]
        #                           List of index tuples for the curves
        #                           to combine

        # Checks
        if not isinstance(Index, tuple):
            quit('Attempted to create new DOS curve. Second parameter must be tuple of strings')
        if not (isinstance(Index[0], str) or isinstance(Index[1], str)):
            quit('Attempted to create new DOS curve. Second parameter must be tuple of strings')
        # Check if already exist
        if Index[0] in self.DOS:
            if Index[1] in self.DOS[Index[0]]:
                quit('Attempted to create new DOS curve. But there is already a curve for ' + str(Index) + '.')
        # Check the required curves exist
        try:
            for iTuple in ListIndex:
                self.DOS[iTuple[0]][iTuple[1]]
        except:
            raise NameError(f'Attempted to create new DOS curve. Second parameter '
                'must contain existing curves but some \n'
                f'indexes (\'Who\',\'What\') are not recognized. Specifically {iTuple}')

        # Construct
        # if Index[0] is not a defined dicctionary already
        if not Index[0] in self.DOS:
            self.DOS[Index[0]] = {}
        # Construct curve list
        self.DOS[Index[0]][Index[1]] = []
        for i in range(self.NDOS):
            self.DOS[Index[0]][Index[1]].append(0.)
        # Agregate acordingly
        for iDOS in range(self.NDOS):
            for Curve2Add in ListIndex:
                self.DOS[Index[0]][Index[1]][iDOS] += self.DOS[Curve2Add[0]][Curve2Add[1]][iDOS]

        if kwargs.get('Report', False):
            print(' ' * 4 + '> Created new sum curve indexed as ' + str(Index) + ' from DOS ' + str(ListIndex))

    def AvrgDOS(self, Index, ListIndex, **kwargs):
        # Creates a new DOS curve from the ones on the dicctionary
        # Index = ('Who', 'What)    tuple of string indexes for the new curve
        #                           New curve created can be accesed
        #                           as self.DOS['Who']['What']
        # ListIndex = [('Who 1','What 1'), ('Who 2','What 2'), ...]
        #                           List of index tuples for the curves
        #                           to average

        # first add
        self.SumDOS(Index, ListIndex)
        # Now average
        for i in range(self.NDOS):
            self.DOS[Index[0]][Index[1]][i] *= 1. / len(ListIndex)

        ## Report
        if kwargs.get('Report', False):
            print(' ' * 4 + '> Created new average curve indexed as ' + str(Index) + ' from DOS ' + str(ListIndex))

    def DiffDOS(self, Index, DOSplus, DOSminus, **kwargs):
        # Creates a new DOS curve from two on the dicctionary
        # Index = ('Who', 'What)    tuple of string indexes for the new curve
        #                           New curve created can be accesed
        #                           as self.DOS['Who']['What']
        # ListIndex = [('Who 1','What 1'), ('Who 2','What 2'), ...]
        #                           List of index tuples for the curves
        #                           to combine
        #   Function  tested against ODT: OK

        # Checks
        if not isinstance(Index, tuple):
            quit('Attempted to create new DOS curve. Second parameter must be tuple of strings')
        if not (isinstance(Index[0], str) or isinstance(Index[1], str)):
            quit('Attempted to create new DOS curve. Second parameter must be tuple of strings')
        # Check if already exist
        if Index[0] in self.DOS:
            if Index[1] in self.DOS[Index[0]]:
                quit('Attempted to create new DOS curve. But there is already a curve for ' + str(Index) + '.')
        # Check the required curves exist
        try:
            self.DOS[DOSplus[0]][DOSplus[1]]
            self.DOS[DOSminus[0]][DOSminus[1]]
        except:
            raise NameError(
                f'Attempted to create new DOS curve. Second and third parameters must contain \n'
                f'existing curves but some indexes (\'Who\',\'What\') are not '
                f'recognized. Review {DOSplus} and {DOSminus}')

        # Construct
        # if Index[0] is not a defined dicctionary already
        if not Index[0] in self.DOS:
            self.DOS[Index[0]] = {}
        # Construct curve list
        self.DOS[Index[0]][Index[1]] = []
        for i in range(self.NDOS):
            self.DOS[Index[0]][Index[1]].append(
                self.DOS[DOSplus[0]][DOSplus[1]][i] - self.DOS[DOSminus[0]][DOSminus[1]][i])

        # Report
        if kwargs.get('Report', False):
            print(' ' * 4 + '> Created new difference curve of index  ' + str(Index) + ' from ' + str(
                DOSplus) + ' - ' + str(DOSminus))

    def BandCenter(self, Index, OnlyFilledLevels=False, FermiCorrected=True, **kwargs):
        # Compute the weigthed band center of the band self.DOS[Index[0]][Index[1]]
        # Options:  OnlyFilledLevels = False    Include all levels, filled and empty (default)
        #                                       if want only up to the fermi level use OnlyFilledLevels = True
        #           FermiCorrected = True       Energies are reported corrected to the fermi level as reference
        #           Report                      kwarg: True to report, default False

        # Checks
        try:
            self.DOS[Index[0]][Index[1]]
        except:
            raise NameError(' ' * 4 + '> Attempted to compute weighted '
                                      'band center but failed. Requested '
                                      'band ' + str(Index) + ' does not exist in ' + self.Name)

        # Set Upper limit in fermi
        ELimit = self.Elist[-1] + 1
        if OnlyFilledLevels:
            ELimit = self.Fermi

        # Set Upper and Lower levels
        if "To" in kwargs:
            ELimit = float(kwargs.get("To",False))
            if FermiCorrected:
                ELimit += self.Fermi
        Efrom = self.Elist[0] - 1
        if "From" in kwargs:
            Efrom = float(kwargs.get("From",False))
            if FermiCorrected:
                Efrom += self.Fermi
        if ELimit <= Efrom:
            print("> The requested range for band center calculation, from "+"{:.1f}".format(Efrom) +
                  "eV to "+"{:.1f}".format(ELimit)+"is backwards, try again.")
            quit()

# TODO: Fix From - To

        # Compute
        BandCenter = 0.
        denominador_integral = 0.
        last_added = [0., 0.] # [f*e, f]
        for i in range(self.NDOS):
            # Check energy in range
            if Efrom <= self.Elist[i] <= ELimit:
                last_added = [self.DOS[Index[0]][Index[1]][i] * self.Elist[i], self.DOS[Index[0]][Index[1]][i]]
                BandCenter += self.DOS[Index[0]][Index[1]][i] * self.Elist[i]
                denominador_integral += self.DOS[Index[0]][Index[1]][i]
        # Correct integral division for initial and final values
        # numerical trick for integrals, founded writting it down step by step
        BandCenter -= .5*(self.DOS[Index[0]][Index[1]][0] * self.Elist[0] + last_added[0])
        denominador_integral -= .5*(self.DOS[Index[0]][Index[1]][0] + last_added[1])
        if denominador_integral <= 0.:
            print(" > There are no states in the range from "+"{:.1f}".format(Efrom) +
                  "{:.1f}".format(ELimit))
            quit()

        # Divide
        BandCenter /= denominador_integral

        # Fermi correct
        if FermiCorrected:
            BandCenter -= self.Fermi

        # Report
        if kwargs.get('Report', False):
            print('Band center for '+ self.Name + ", curve " + str(Index), end='')
            if FermiCorrected:
                print(', fermi-corr.', end='')
            if OnlyFilledLevels:
                print(', only filled (E<fermi)', end='')
            print(', range ['+"{:.2f}".format(Efrom)+
                  ' , '+"{:.2f}".format(ELimit)+']'+
                  ' (not corrected, fermi:'+"{:.2f}".format(self.Fermi), end=') ')
            print(' : ' + "{:.2f}".format(BandCenter))

        # Return value
        return BandCenter

    # TODO: add integrate function
    def Integral(self, Index, **kwargs):
        # Integrates area under a DOS curve
        #   Default from first energy (<Fermi) to last energy (>Fermi)
        #   Change levels with From and To kwargs using energy NOT CORRECTED to the fermi level
        #   Function tested against ODT: OK

        # Checks
        try:
            self.DOS[Index[0]][Index[1]]
        except:
            raise NameError(
                'Attempted to integrate DOS curve of indexes ' + str(Index) + ' that does not exist in ' + self.Name)

        # Default energy limits
        intFrom = float(kwargs.get('From', self.Elist[0]-1))
        intTo = float(kwargs.get('To', self.Elist[-1]+1))
        # Compute
        Integral = 0
        for i, E in enumerate(self.Elist[1:], 1):
            # Check energy in range, start from 1 because it integrates point with the previous point
            if E > intFrom and E < intTo:
                Integral += (E - self.Elist[i - 1]) * (
                            self.DOS[Index[0]][Index[1]][i] + self.DOS[Index[0]][Index[1]][i - 1]) / 2.
        # report
        if kwargs.get("Report", False):
            print("Integral for "+self.Name+"-"+str(Index)
                  +", from "+str("{:.3f}".format(intFrom))+" to="+str("{:.3f}".format(intTo))
                  +", int = "+str("{:.4f}".format(Integral)))
        # report
        return Integral

    def FilledFraction(self, Index, Report=False):
        int_full = self.Integral(Index, To=self.Fermi, Report=False)
        int_tot = self.Integral(Index, Report=False)
        if Report:
            print("Filled fraction for "+self.Name+"-"+str(Index)+" = "+"{:.4f}".format(int_full/int_tot))

        return int_full/int_tot


    def Plot(self, Index, **kwargs):
        # Add DOS curve from Index to active plot

        FermiCorrected = kwargs.get('FermiCorrected', True)
        PlotDown = kwargs.get('PlotDown', False)
        PlotVert = kwargs.get('PlotVert', False)
        AmplifyFactor = kwargs.get('AmplifyFactor', 1.)
        MoveY = kwargs.get('MoveY', 0.)
        MoveX = kwargs.get('MoveX', 0.)

        LineWidth = kwargs.get('LineWidth', 1.5)
        LineAlpha = kwargs.get('AlphaLine', 1.)
        LineStyle = kwargs.get('LineStyle', 'solid')
        Color = kwargs.get('Color', 'k')
        Filled = kwargs.get('Filled', True)
        AlphaFill = kwargs.get('AlphaFill', .1)
        ColorFill = kwargs.get('ColorFill', Color)

        # Prepare correction and factor
        Corr = 0.
        if FermiCorrected:
            Corr = self.Fermi

        if PlotDown:
            Fact = -AmplifyFactor
        else:
            Fact = AmplifyFactor

        # Plot
        if PlotVert:
            xplotlist = [k * Fact + MoveX for k in self.DOS[Index[0]][Index[1]]]
            yplotlist = [i - Corr + MoveY for i in self.Elist]
        else:
            xplotlist = [i - Corr + MoveX for i in self.Elist]
            yplotlist = [k * Fact + MoveY for k in self.DOS[Index[0]][Index[1]]]

        if not LineStyle == "noline":
            plt.plot(xplotlist, yplotlist,
                     color=Color, linestyle=LineStyle, linewidth=LineWidth, alpha=LineAlpha)

        if Filled:
            if PlotVert:
                plt.fill_betweenx(yplotlist, MoveX, xplotlist, alpha=AlphaFill, color=ColorFill)
            else:
                plt.fill_between(xplotlist, MoveY, yplotlist, alpha=AlphaFill, color=ColorFill)


def plot_divide_femi(**kwargs):
    if kwargs.get('PlotVert', False):
        plt.axhline(0., linestyle=kwargs.get("ls", "solid"), color="k", linewidth=.5)
    else:
        plt.axvline(0., linestyle=kwargs.get("ls","solid"), color="k", linewidth=.5)


def add_size_bar(**kwargs):
    LeftRight = kwargs.get("MoveX",0.)
    UpDown = kwargs.get("MoveY111",0.)
    plt.plot([.0+LeftRight, .0+LeftRight],
             [.0+UpDown, -1.+UpDown],
             linestyle=kwargs.get('Linestyle','solid'),
             linewidth=kwargs.get('Linewidth',1.8),
             color=kwargs.get('Colour', 'k'))
