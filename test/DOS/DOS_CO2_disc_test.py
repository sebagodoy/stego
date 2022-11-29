import stego.dedos as ds
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D

# Load the curves
import stego.defaultsrc

N100R23d = ds.DOS("./DOS/DOSCAR_Ni100R23d_k247", Name="N100.R23.d.Ac", Pol=True, Orb="spd", ml=False, Nelect=656)
N100R23d_f = ds.DOS("./DOS/DOSCAR_N10_final", Name="N100.R23.d.Ac", Pol=True, Orb="none", ml=False, Nelect=656)
N100R23d_i = ds.DOS("./DOS/DOSCAR_N10_initial", Name="N100.R23.d.Ac", Pol=True, Orb="none", ml=False, Nelect=656)




# ---------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
fig, axs = plt.subplots(3, 1, sharex='col', figsize=(8,5), gridspec_kw={'height_ratios': [1, 3,1]})
plt.subplots_adjust(wspace=0.05, hspace=0, left=.05, right=.98, top=.98, bottom=.12)


MLine = {'Color':'k',   'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'AlphaLine':1.}
CLine = {'Color':'k',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}
O2Line = {'Color':'r',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}




#----------------------------------------------------------------------------------------------------------------------------

plt.sca(axs[1])
ds.plot_divide_femi()
plt.yticks([])

MoveYCO = iter([y*1 for x in [-i for i in range(9)] for y in (x,)*3])

MLineK = {'Color':'k',   'Filled':True, 'LineStyle': 'solid', 'LineWidth':.4, 'AlphaLine':1.}
OLine = {'Color':'r',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}
OLine2 = {'Color':'r',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}
CLine = {'Color':'k',  'Filled':False, 'LineStyle': 'solid', 'LineWidth':.8, 'Alphaline':1.}


N100R23d.Plot(("66", "+"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine, MoveY=next(MoveYCO))
N100R23d.Plot(("66", "-"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine, MoveY=next(MoveYCO), PlotDown=True)
plt.text(.5, next(MoveYCO)+.1, "$O^{(1)}$", color='r')

N100R23d.Plot(("65", "+"), AmplifyFactor=N100R23d.TotalFactor * .1, **CLine, MoveY=next(MoveYCO))
N100R23d.Plot(("65", "-"), AmplifyFactor=N100R23d.TotalFactor * .1, **CLine, MoveY=next(MoveYCO), PlotDown=True)
plt.text(.5, next(MoveYCO)+.1, "$C$", color='k')

N100R23d.Plot(("67", "+"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine2, MoveY=next(MoveYCO))
N100R23d.Plot(("67", "-"), AmplifyFactor=N100R23d.TotalFactor * .1, **OLine2, MoveY=next(MoveYCO), PlotDown=True)
plt.text(.5, next(MoveYCO)+.1, "$O^{(2)}$", color='r')

N100R23d.WhatCurves()


asd = next(MoveYCO)-2
N100R23d.Plot(("total", "+"), AmplifyFactor=N100R23d.TotalFactor * .08, **MLineK, MoveY=asd)
N100R23d.Plot(("total", "-"), AmplifyFactor=N100R23d.TotalFactor * .08, **MLineK, MoveY=asd, PlotDown=True)


plt.ylim([-7.5,2.5])



#----------------------------------------------------------------------------------------------------------------------------
plt.sca(axs[2])

N100R23d_f.Plot(("global", "+"), AmplifyFactor=N100R23d_f.GlobalFactor * .08, **MLineK, MoveY=0.)
N100R23d_f.Plot(("global", "-"), AmplifyFactor=N100R23d_f.GlobalFactor * .08, **MLineK, MoveY=0., PlotDown=True)

ds.plot_divide_femi()
plt.ylim([-1.5,1.5])
plt.yticks([])

#----------------------------------------------------------------------------------------------------------------------------
plt.sca(axs[0])

N100R23d_i.Plot(("global", "+"), AmplifyFactor=N100R23d_i.GlobalFactor * .08, **MLineK, MoveY=-1.)
N100R23d_i.Plot(("global", "-"), AmplifyFactor=N100R23d_i.GlobalFactor * .08, **MLineK, MoveY=-1., PlotDown=True)

ds.plot_divide_femi()
plt.ylim([-2.5,2.5])
plt.yticks([])


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Final touches to the plot

fig.text(0.02, 0.55, 'Density of States (arbitrary units)',
         fontsize=10, ha='left', va='center', rotation='vertical', fontweight='bold')
fig.text(0.5, 0.02, 'Energy (eV) corrected to the fermi level',
         fontsize=10, ha='center', va='bottom', fontweight='bold')


nametext = iter([r'a) Ni(100)/$*CO_2$', r'd) Ni(100)/$*CO_2\rightarrow *CO^{(2)}+O^{(1)}$', r'b) Ni(100)/$*CO+O$'])
for jax in axs:
    [x.set_linewidth(1.5) for x in jax.spines.values()]
    plt.sca(jax)
    plt.annotate(next(nametext), xy=(.02,.95), xycoords='axes fraction',
             fontsize=12, ha='left', va='top', fontweight='bold')

plt.savefig("./DOS_CO2_disc_test.png", bbox_inches ="tight", dpi=600)

plt.show()

