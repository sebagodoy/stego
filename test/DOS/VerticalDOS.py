import stego.dedos as ds
import matplotlib.pyplot as plt


N100R23d = ds.DOS("./DOS/DOSCAR_Ni100R23d_k247", Name="N100.R23.d.Ac", Pol=True, Orb="spd", ml=False, Nelect=656)

fig, axs = plt.subplots(1, 1, sharey='row', figsize=(4.5,6.5))
plt.subplots_adjust(wspace=0., hspace=0., left=.16, right=.98, top=.95, bottom=.06)


MLine = {'Color':'k',   'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'AlphaLine':1.}
CLine = {'Color':'k',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}
O2Line = {'Color':'r',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}




#----------------------------------------------------------------------------------------------------------------------------

MoveYCO = iter([y*1 for x in [-i for i in range(9)] for y in (x,)*3])

MLineK = {'Color':'k',   'Filled':True, 'LineStyle': 'solid', 'LineWidth':.4, 'AlphaLine':1.}
OLine = {'Color':'r',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}
OLine2 = {'Color':'r',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}
CLine = {'Color':'k',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}


N100R23d.Plot(("66", "+"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine, MoveX=next(MoveYCO), PlotVert=True)
N100R23d.Plot(("66", "-"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine, MoveX=next(MoveYCO), PlotDown=True, PlotVert=True)
plt.text(next(MoveYCO)+.1, .5, "$O^{(1)}$", color='r')

N100R23d.Plot(("65", "+"), AmplifyFactor=N100R23d.TotalFactor * .1, **CLine, MoveX=next(MoveYCO), PlotVert=True)
N100R23d.Plot(("65", "-"), AmplifyFactor=N100R23d.TotalFactor * .1, **CLine, MoveX=next(MoveYCO), PlotDown=True, PlotVert=True)
plt.text(next(MoveYCO)+.1, .5, "$C$", color='k')

N100R23d.Plot(("67", "+"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine2, MoveX=next(MoveYCO), PlotVert=True)
N100R23d.Plot(("67", "-"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine2, MoveX=next(MoveYCO), PlotDown=True, PlotVert=True)
plt.text(next(MoveYCO)+.1, .5, "$O^{(1)}$", color='r')

N100R23d.WhatCurves()


asd = next(MoveYCO)-2
N100R23d.Plot(("total", "+"), AmplifyFactor=N100R23d.TotalFactor * .08, **MLineK, MoveX=asd, PlotVert=True)
N100R23d.Plot(("total", "-"), AmplifyFactor=N100R23d.TotalFactor * .08, **MLineK, MoveX=asd, PlotDown=True, PlotVert=True)

# -------------------------------------------------------------------------------------------------------
# Final touches to plot

plt.title(r'TS: Ni(100)/$*CO_2\rightarrow *CO^{(2)}+*O^{(1)}$', fontweight='bold')
plt.ylabel('Energy- $e_f$, (eV)', labelpad=.05, fontweight='bold')
plt.xlabel('DOS, arbitrary units', fontweight='bold')
ds.plot_divide_femi(PlotVert=True)
plt.xticks([])
plt.xlim([-7.5,4])
plt.ylim([-23,7.])
plt.savefig("./DOS_vertical_test.png", bbox_inches ="tight", dpi=600)
plt.show()