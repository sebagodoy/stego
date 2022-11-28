#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from data import *


########################################################################################################################
########################################################################################################################
# Creating Plot, CHx series ############################################################################################
########################################################################################################################

idrx.MayorSection('Creating Plot')

fig, axs = plt.subplots(2, 3, figsize=(14, 6), dpi=90, sharey='row', sharex='all')
plt.subplots_adjust(wspace=.0, hspace=0., left=.06, right=.98, bottom=.3, top=.95)
HoverList = []

# References
RefN111_e = idrx.Plot.RxRef(1.5, 0.)
RefC111_e = idrx.Plot.RxRef(1.5, 0.)
RefCN111_e = idrx.Plot.RxRef(1.5, 0.)

# Place holders
HoverList = []
SectionRefs_N111e = RefN111_e.branch()
SectionRefs_C111e = RefC111_e.branch()
SectionRefs_CN111e = RefCN111_e.branch()


# References
RefN100_e = idrx.Plot.RxRef(1.5, 0.)
RefC100_e = idrx.Plot.RxRef(1.5, 0.)
RefCN100_e = idrx.Plot.RxRef(1.5, 0.)

# Place holders
SectionRefs_N100e = RefN100_e.branch()
SectionRefs_C100e = RefC100_e.branch()
SectionRefs_CN100e = RefCN100_e.branch()

# Start branches
refStart_HCO = 6.
refStart_COH = 10.

# Default parameters
Main_Line_Props = {"StepSpan": .5, "LineStyle": "solid", "LineWidth": 1.5, "AlphaLines": 1., 'T-rate':265 + 273.15}
Main_Line_Props_Co = {"StepSpan": 1., "LineStyle": "solid", "LineWidth": 1.5, "AlphaLines": 1.}
Jump_Line_Props = {"StepSpan": .2, "LineStyle": "solid", "LineWidth": .8, "AlphaLines": 1.}
OH_Line_Props = {"StepSpan": .2, "LineStyle": 'solid', "LineWidth": 2, "AlphaLines": .2}

GibbsOpts = {'T': 265 + 273.15, 'P': 0.01 * 1.}  # 1% CH4
GibbsOpts_H2 = {'T': 265 + 273.15, 'P': 0.25 * 1.}  # 25% H2

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# ----------------------------------------------------------------------------------------------------------------------
# Nickel (111s)---------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Gibbs - Ni(111s)')
plt.axes(axs[0][2])
plt.title('Reaction profile $\longrightarrow$')

# ..............................................................................
# CO series ....................................................................
# ..............................................................................
RefN111_e_CO = RefN111_e.branch()

# CO adsorbs
idrx.Plot.RxStep([COg.Gibbs(**GibbsOpts)+N111s.Gibbs(**GibbsOpts),
                  N1sR17_i.Gibbs(**GibbsOpts)],
                 RefN111_e_CO,
                 Name='CO adsorbs',
                 Hover=HoverList, Color='k', **Jump_Line_Props)


# N/ R17 (bridge): CO.h -> C.h + O.h
idrx.Plot.RxStepTS([N1sR17_i.Gibbs(**GibbsOpts),
                    N1sR17_d.Gibbs(**GibbsOpts),
                    N1sR17_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_CO,
                   Name="N1s/R17(bridge): CO.hcp -> C.hcp + O.hcp",
                   Hover=HoverList, Color="r", **Main_Line_Props)

# N/ Separe {C.h + O.h} + (H2) + {} -> {C.f + H.h } + {O.h + H.h}
idrx.Plot.RxStep([N1sR17_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts_H2) + N111s.Gibbs(**GibbsOpts) ,
                  N1sR21a_i.Gibbs(**GibbsOpts) + N1sR132_i.Gibbs(**GibbsOpts)],
                 Ref=RefN111_e_CO,
                 Name="N1s/(+C jump!) {C.h + O.h} + H2 + {} -> {C.f + H.f} + {O.h + H.h}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([N1sR132_i.Gibbs(**GibbsOpts),
                    N1sR132_d.Gibbs(**GibbsOpts),
                    N1sR132_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_CO,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# R21a by side: C.f + H.h
idrx.Plot.RxStepTS([N1sR21a_i.Gibbs(**GibbsOpts), N1sR21a_TS.Gibbs(**GibbsOpts), N1sR21a_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_CO,
                   Name='N1s/R21a by bridge: C.f + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)


# ..............................................................................
# HCO series ...................................................................
# ..............................................................................
RefN111_e_HCO = RefN111_e.branch()
RefN111_e_HCO.PlotExtend(Until=refStart_HCO, Color='m', Alpha=1, LineWidth=.8)

# Separe CO + O
# N/(+O jump!) {CO.h + O.h(m)} + H2 + {} -> {CO.h + H.h} + {O.f + H.h}
idrx.Plot.RxStep([N111s.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + COg.Gibbs(**GibbsOpts),
                  N1sR5_i.Gibbs(**GibbsOpts)],
                 Ref=RefN111_e_HCO,
                 Name="N1s/(+O jump!) {CO.h} + 1/2 (H2) -> {CO.h + H.h}",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# R5 (bridge): CO.h + H.h -> HCO.htO
idrx.Plot.RxStepTS([N1sR5_i.Gibbs(**GibbsOpts),
                    N1sR5_d.Gibbs(**GibbsOpts),
                    N1sR5_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_HCO,
                   Name="N1s/R5(bridge): CO.h + H.h -> HCO.htO",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# R15 (split): HCO.hcptO -> CH.fcc + O.fcc
idrx.Plot.RxStepTS([N1sR15_i.Gibbs(**GibbsOpts),
                    N1sR15_d.Gibbs(**GibbsOpts),
                    N1sR15_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_HCO,
                   Name="N1s/R15(split): HCO.hcptO -> CH.fcc + O.fcc",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe {CH.f + O.f} + 1/2(H2) + {} -> {CH.h} + {O.f + H.f}
idrx.Plot.RxStep([N1sR15_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + N111s.Gibbs(**GibbsOpts),
                  N1sR21a_f.Gibbs(**GibbsOpts) + N1sR132_i.Gibbs(**GibbsOpts)],
                 Ref=RefN111_e_HCO,
                 Name="N1s/(+ jump CH) {CH.f + O.f} + {H.f} -> {CH.h} + {O.f + H.f}",
                 Hover=HoverList, Color="b", **OH_Line_Props)

# OH elimination, included
idrx.Plot.RxStepTS([N1sR132_i.Gibbs(**GibbsOpts),
                    N1sR132_d.Gibbs(**GibbsOpts),
                    N1sR132_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_HCO,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# Section
SectionRefs_N111e.UpdateFromTail(RefN111_e_HCO)
# stg.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_N111e, Colour="g")


# ..............................................................................
# COH series ...................................................................
# ..............................................................................
RefN111_e_COH = RefN111_e.branch()
RefN111_e_COH.PlotExtend(Until=refStart_COH, Color='m', Alpha=1, LineWidth=.8)

# N/(+O jump!) {CO.h + O.h(m)} + H2 + {} -> {CO.h + H.h} + {O.f + H.h}
idrx.Plot.RxStep([N111s.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + COg.Gibbs(**GibbsOpts),
                  N1sR6_i.Gibbs(**GibbsOpts)],
                 Ref=RefN111_e_COH,
                 Name="N1s/(+O jump!) {CO.h} + 1/2*(H2) -> {CO.h + H.f}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# N1sR6 : CO.h + H.f -> COH.ht
idrx.Plot.RxStepTS([N1sR6_i.Gibbs(**GibbsOpts),
                    N1sR6_d.Gibbs(**GibbsOpts),
                    N1sR6_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_COH,
                   Name="N1s/R6(top): CO.h + H.f -> COH.ht",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# N1sR16 : COH.ht -> C.h + OH.f
idrx.Plot.RxStepTS([N1sR16_i.Gibbs(**GibbsOpts),
                    N1sR16_d.Gibbs(**GibbsOpts),
                    N1sR16_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_COH,
                   Name="N1s/R6(top): COH.ht -> C.h + OH.f",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Ni/ Separe {C.h + OH.f} + 1/2(H2) + {} -> {C.f+H.h} + {OH.f}
idrx.Plot.RxStep([N1sR16_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + N111s.Gibbs(**GibbsOpts),
                  N1sR21a_i.Gibbs(**GibbsOpts) + N1sR132_f.Gibbs(**GibbsOpts)],
                 Ref=RefN111_e_COH,
                 Name="N1s/(+C jump!) {C.h + OH.f} + {H.f} -> {(top)C.f + H.h} + {OH.f}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# R21a by side: C.f + H.h
idrx.Plot.RxStepTS([N1sR21a_i.Gibbs(**GibbsOpts),
                    N1sR21a_TS.Gibbs(**GibbsOpts),
                    N1sR21a_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_e_COH,
                   Name='N1s/R21a by bridge: C.f + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)




SectionRefs_N111e.UpdateFromTail(RefN111_e_COH)
# stg.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_N111e, Colour="m")



# ----------------------------------------------------------------------------------------------------------------------
# Cobalt ---------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Gibbs - Co(111s)')
plt.axes(axs[0][0])
plt.title('Reaction profile $\longrightarrow$')



# ..............................................................................
# CO series ....................................................................
# ..............................................................................
RefC111_e_CO = RefC111_e.branch()

# CO adsorption
idrx.Plot.RxStep([C111s.Gibbs(**GibbsOpts)+COg.Gibbs(**GibbsOpts),
                  C1sR171_i.Gibbs(**GibbsOpts)],
                 Ref=RefC111_e_CO,
                 Name='CO adsorption',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# R17.1 CO.t -(b)-> C.h + O.h
idrx.Plot.RxStepTS([C1sR171_i.Gibbs(**GibbsOpts),
                    C1sR171_d.Gibbs(**GibbsOpts),
                    C1sR171_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_CO,
                   Name="C1s/R17.1 CO.t -(b)-> C.h + O.h",
                   Hover=HoverList, Color="r", **Main_Line_Props)

# Separe {C.h + O.h} + (H2) + {} -> {C.h}(R21-i) + {O.h + H.f}
idrx.Plot.RxStep([C1sR171_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts_H2) + C111s.Gibbs(**GibbsOpts),
                  C1sR21_i.Gibbs(**GibbsOpts) + C1sR13_i.Gibbs(**GibbsOpts)],
                 Ref=RefC111_e_CO,
                 Name="C1s/{C.h + O.h} + (H2) + {} -> {C.h + H.f} + {O.h + H.f}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([C1sR13_i.Gibbs(**GibbsOpts),
                    C1sR13_d.Gibbs(**GibbsOpts),
                    C1sR13_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_CO,
                   Name="C1s/ O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# R21b on top: C.h + H.f -> CH.h
idrx.Plot.RxStepTS([C1sR21_i.Gibbs(**GibbsOpts),
                    C1sR21_TS.Gibbs(**GibbsOpts),
                    C1sR21_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_CO,
                   Name='C1s/R21(top): C.h+H.f->CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)



SectionRefs_C111e.UpdateFromTail(RefC111_e_CO)
# stg.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_C111e, Colour="r")


# ..............................................................................
# HCO series ...................................................................
# ..............................................................................
RefC111_e_HCO = RefC111_e.branch()
RefC111_e_HCO.PlotExtend(Until=refStart_HCO, Color='m', Alpha=1, LineWidth=.8)


# Separe/ {CO.t+O.h} + H2 + {} -> {CO.h+H.} + {O.h+H.f}
idrx.Plot.RxStep([C111s.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+COg.Gibbs(**GibbsOpts),
                  C1sR5h_i.Gibbs(**GibbsOpts)],
                 Ref=RefC111_e_HCO,
                 Name="C/ {CO.t} + 1/2(H2) -> {CO.h+H.hd}",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# -------------------------------- Ruta 1 (HCO.hbO)-----------------------------
RefC111_e_HCOh = RefC111_e_HCO.branch()

# C/R5 CO.h + H.hd -> HCO.hbO
idrx.Plot.RxStepTS([C1sR5h_i.Gibbs(**GibbsOpts),
                    C1sR5h_d.Gibbs(**GibbsOpts),
                    C1sR5h_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_HCOh,
                   Name="C/ CO.h+H.hd -> HCO.hbO(R5)",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# C/R15 HCO.hbO -(split)-> CH.h + O.hm
idrx.Plot.RxStepTS([C1sR15h_i.Gibbs(**GibbsOpts),
                    C1sR15h_d.Gibbs(**GibbsOpts),
                    C1sR15h_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_HCOh,
                   Name="C1s/R15 HCO.fbO -(split)-> CH.h + O.hm",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe {CH.h + O.hm} + H2 + {} -> {CH.h} + {O.h + H.f}
idrx.Plot.RxStep([C1sR15h_f.Gibbs(**GibbsOpts) + 0.5 * H2.Gibbs(**GibbsOpts_H2) + C111s.Gibbs(**GibbsOpts),
                  C1sR21_f.Gibbs(**GibbsOpts) + C1sR13_i.Gibbs(**GibbsOpts)],
                 Ref=RefC111_e_HCOh,
                 Name="C1s/{CH.h + O.hm} + {H.f} -> {CH.h} + {O.h + H.f}",
                 Hover=HoverList, Color="b", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([C1sR13_i.Gibbs(**GibbsOpts),
                    C1sR13_d.Gibbs(**GibbsOpts),
                    C1sR13_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_HCOh,
                   Name="C1s/ O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# -------------------------------- Ruta 2 (HCO.fbO) ----------------------------
RefC111_e_HCOf = RefC111_e_HCO.branch()

# C/R5 CO.h + H.hd -> HCO.hbO
idrx.Plot.RxStepTS([C1sR5f_i.Gibbs(**GibbsOpts),
                    C1sR5f_d.Gibbs(**GibbsOpts),
                    C1sR5f_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_HCOf,
                   Name="C/ CO.h+H.hd -> HCO.fbO",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# C/R15 HCO.fbO -(split)-> CH.h + O.hm
idrx.Plot.RxStepTS([C1sR15f_i.Gibbs(**GibbsOpts),
                    C1sR15f_d.Gibbs(**GibbsOpts),
                    C1sR15f_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_HCOf,
                   Name="C1s/R15 HCO.fbO -(split)-> CH.h + O.hm",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Converge branches
# stg.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_C111e, Colour="g")




# ..............................................................................
# COH series ...................................................................
# ..............................................................................
RefC111_e_COH = RefC111_e.branch()
RefC111_e_COH.PlotExtend(Until=refStart_COH, Color='m', Alpha=1, LineWidth=.8)


# Separe/ {CO.t+O.h} + H2 + {} -> {CO.h+H.} + {O.h + H}
idrx.Plot.RxStep([C111s.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+COg.Gibbs(**GibbsOpts),
                  C1sR6_i.Gibbs(**GibbsOpts)],
                 Ref=RefC111_e_COH,
                 Name="C/ {CO.t} + 1/2(H2) -> {CO.h+H.hd}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)


# R6: CO.h + H.h-> COH.hbt
idrx.Plot.RxStepTS([C1sR6_i.Gibbs(**GibbsOpts),
                    C1sR6_d.Gibbs(**GibbsOpts),
                    C1sR6_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_COH,
                   Name="C/ CO.b+H.h -> COH.h",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# R16: COH.hbt -(t)-> C.h + OH.hd
idrx.Plot.RxStepTS([C1sR16_i.Gibbs(**GibbsOpts),
                    C1sR16_d.Gibbs(**GibbsOpts),
                    C1sR16_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_COH,
                   Name="C1s/R16: COH.hbt -(t)-> C.h + OH.hd",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separe C/ {C.h+OH.hd} + 1/2(H2) + {} -> {C.h + H.h} + {OH.}
idrx.Plot.RxStep([C1sR16_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+ C111s.Gibbs(**GibbsOpts),
                  C1sR21_i.Gibbs(**GibbsOpts) + C1sR13_f.Gibbs(**GibbsOpts)],
                 Ref=RefC111_e_COH,
                 Name="C1s/ {C.h+OH.hd}+1/2(H2)+{} -> {C.h+H.h} + {OH.h}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# R21b on top: C.h + H.f -> CH.h
idrx.Plot.RxStepTS([C1sR21_i.Gibbs(**GibbsOpts),
                    C1sR21_TS.Gibbs(**GibbsOpts),
                    C1sR21_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_e_COH,
                   Name='C1s/R21(top): C.h+H.f->CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)



# Section
SectionRefs_C111e.UpdateFromTail(RefC111_e_COH)
# stg.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_C111e, Colour="m")



# ----------------------------------------------------------------------------------------------------------------------
# Cobalt-Nickel --------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Gibbs - CoNi(111s)')
plt.axes(axs[0][1])
plt.title('Reaction profile $\longrightarrow$')


# ..............................................................................
# CO series ....................................................................
# ..............................................................................
RefCN111_e_CO = RefCN111_e.branch()

# CO adsorption
idrx.Plot.RxStep([CN111s.Gibbs(**GibbsOpts)+COg.Gibbs(**GibbsOpts),
                  CN1sR17bCN_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_e_CO,
                 Name='CO adsorption',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# CN/R17bCN CO.tC -> C.hN + O.hN
idrx.Plot.RxStepTS([CN1sR17bCN_i.Gibbs(**GibbsOpts),
                    CN1sR17bCN_d.Gibbs(**GibbsOpts),
                    CN1sR17bCN_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_CO,
                   Name="CN/R17bCN CO.tC -> C.hN + O.hN",
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separate/ {C.hN+O.hN} + (H2) + {} -> {C.hN (C) } + {O.hN+H.hN}
idrx.Plot.RxStep([CN1sR17bCN_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts_H2) + CN111s.Gibbs(**GibbsOpts),
                  CN1sR21C_i.Gibbs(**GibbsOpts) + CN1sR132C_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_e_CO,
                 Name="CN/ {C.hN+O.hN} + (H2) -> {(C)C.hN+H.hN} + {(C)O.hN+H.hN}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination (C)
idrx.Plot.RxStepTS([CN1sR132C_i.Gibbs(**GibbsOpts),
                    CN1sR132C_d.Gibbs(**GibbsOpts),
                    CN1sR132C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_CO,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# R21 - C : C.hN + H.fN -> CH.hN
idrx.Plot.RxStepTS([CN1sR21C_i.Gibbs(**GibbsOpts),
                    CN1sR21C_TS.Gibbs(**GibbsOpts),
                    CN1sR21C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_CO,
                   Name='CN1s/R21 on top C: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Section
SectionRefs_CN111e.UpdateFromTail(RefCN111_e_CO)
# stg.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_CN111e, Colour="r")


# ..............................................................................
# HCO series ...................................................................
# ..............................................................................
RefCN111_e_HCO = RefCN111_e.branch()
RefCN111_e_HCO.PlotExtend(Until=refStart_HCO, Color='m', Alpha=1, LineWidth=.8)

# ------------------------------------------------ Ruta HCO.hNbOC
RefCN111_e_HCOb = RefCN111_e_HCO.branch()

# Separe/ {CO.tC} + 1/2(H2) -> {(R5b) CO.hN + H.fN}
idrx.Plot.RxStep([CN111s.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+COg.Gibbs(**GibbsOpts),
                  CN1sR5b_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_e_HCOb,
                 Name="{CO.tC} +1/2(H2) -> {(R5b) CO.hN + H.fN}",
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# CN/R5 CO.hN + H.fN -> HCO.hNbOC
idrx.Plot.RxStepTS([CN1sR5b_i.Gibbs(**GibbsOpts),
                    CN1sR5b_d.Gibbs(**GibbsOpts),
                    CN1sR5b_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_HCOb,
                   Name="CN/R5 CO.hN + H.fN -> HCO.hNbOC",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# CN/R15 HCO.hNbOC -> CH.fC + O.fN
idrx.Plot.RxStepTS([CN1sR15C_i.Gibbs(**GibbsOpts),
                    CN1sR15C_d.Gibbs(**GibbsOpts),
                    CN1sR15C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_HCOb,
                   Name="CN/R15 HCO.hNbOC -> CH.fC + O.fN",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe CN/{CH.fC + O.fN} + 1/2(H2) + {} -> {(R21)CH.hN}  + {(R13.2C) O.fN+H.hN}
idrx.Plot.RxStep([CN1sR15C_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + CN111s.Gibbs(**GibbsOpts),
                  CN1sR21C_f.Gibbs(**GibbsOpts) + CN1sR132C_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_e_HCOb,
                 Name="CN/{CH.fC + O.fN} + {H.hN} -> {(R21)CH.hN}  + {(R13.2C) O.fN+H.hN}",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# OH elimination (C)
idrx.Plot.RxStepTS([CN1sR132C_i.Gibbs(**GibbsOpts),
                    CN1sR132C_d.Gibbs(**GibbsOpts),
                    CN1sR132C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_HCOb,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# ------------------------------------------------ Ruta HCO.tCtC (secundaria)
RefCN111_e_HCOt = RefCN111_e_HCO.branch()

# Separe CN/ {CO.tC + O.hC} + H2 + {} -> {CO.hN + H.fN}+{(R13.2C) O.fN+H.hN}
idrx.Plot.RxStep([CN111s.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+COg.Gibbs(**GibbsOpts),
                  CN1sR5bt_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_e_HCOt,
                 Name="CN/ {CO.tC} + 1/2(H2) -> {(R5bt) CO.hN + H.fN}",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# CN/R5bt CO.hN + H.fN -> HCO.tCtC
idrx.Plot.RxStepTS([CN1sR5bt_i.Gibbs(**GibbsOpts),
                    CN1sR5bt_d.Gibbs(**GibbsOpts),
                    CN1sR5bt_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_HCOt,
                   Name="CN/R5 CO.hN + H.fN -> HCO.tCtC",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# CN/R15 HCO.tCtC -> CH.fC + O.fN
idrx.Plot.RxStepTS([CN1sR15tCtC_i.Gibbs(**GibbsOpts),
                    CN1sR15tCtC_d.Gibbs(**GibbsOpts),
                    CN1sR15tCtC_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_HCOt,
                   Name="CN/R15 HCO.tCtC -> CH.fC + O.fN",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Compile Refs
RefCN111_e_HCO.UpdateFromTail(RefCN111_e_HCOb)
SectionRefs_CN111e.UpdateFromTail(RefCN111_e_HCO)
# stg.Plot.AnnotateStepAxis(['$HCO$'], Ref=SectionRefs_CN111e, Colour="g")



# .....................................
# COH series ..........................
# .....................................
RefCN111_e_COH = RefCN111_e.branch()
RefCN111_e_COH.PlotExtend(Until=refStart_COH, Color='m', Alpha=1, LineWidth=.8)


# Separe CN/{(R23-f)CO.tC + O.hC}+ H2 + {} -> {(R6)CO.hN + H.fN}+{(R13.2C)O.fN+H.hN}
idrx.Plot.RxStep([CN111s.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+COg.Gibbs(**GibbsOpts),
                  CN1sR6_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_e_COH,
                 Name="CN/{(R23-f) CO.tC} + 1/2(H2) -> {(R6)CO.hN + H.fN}",
                 Hover=HoverList, Color='m', **Jump_Line_Props)

# CN/R6C CO.hN + H.fN -(C)-> COH.hN
idrx.Plot.RxStepTS([CN1sR6_i.Gibbs(**GibbsOpts),
                    CN1sR6_d.Gibbs(**GibbsOpts),
                    CN1sR6_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_COH,
                   Name="CN/R6C CO.hN + H.fN -(C)-> COH.hN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# CN/R16C COH.hNtC -> C.hN + OH.fN
idrx.Plot.RxStepTS([CN1sR16C_i.Gibbs(**GibbsOpts),
                    CN1sR16C_d.Gibbs(**GibbsOpts),
                    CN1sR16C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_COH,
                   Name="CN/R16C COH.hNtC -> C.hN + OH.fN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separa CN/{(R16C-f)C.hN+OH.fN}+ 1/2(H2) + {} -> {(R21C) C.hN+H.fN} + {(R13.2C-f) OH.fN}
idrx.Plot.RxStep([CN1sR16C_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + CN111s.Gibbs(**GibbsOpts),
                  CN1sR21C_i.Gibbs(**GibbsOpts) + CN1sR132C_f.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_e_COH,
                 Name="CN/{(R16C-f)C.hN+OH.fN}+1/2(H2)+{}->{(R21C)C.hN+H.fN}+{(R13.2C-f)OH.fN}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# R21 - C : C.hN + H.fN -> CH.hN
idrx.Plot.RxStepTS([CN1sR21C_i.Gibbs(**GibbsOpts),
                    CN1sR21C_TS.Gibbs(**GibbsOpts),
                    CN1sR21C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_e_COH,
                   Name='CN1s/R21 on top C: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Section
SectionRefs_CN111e.UpdateFromTail(RefCN111_e_COH)
# stg.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_CN111e, Colour="m")






########################################################################################################################
########################################################################################################################
########################################################################################################################

# (100) ----------------------------------------------------------------------------------------------------------------





# ----------------------------------------------------------------------------------------------------------------------
# Nickel ---------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Gibbs - Ni(100)')
plt.axes(axs[1][2])


# .....................................
# CO series ...........................
# .....................................
RefN100_e_CO = RefN100_e.branch()

# CO adsorption
idrx.Plot.RxStep([N100.Gibbs(**GibbsOpts)+COg.Gibbs(**GibbsOpts),
                  N10R17_i.Gibbs(**GibbsOpts)],
                 Ref=RefN100_e_CO,
                 Name='CO adsorption',
                 Hover=HoverList, Color='k', **Jump_Line_Props)


# N/ {CO.h} -> {C.h+O.h} (R17)
idrx.Plot.RxStepTS([N10R17_i.Gibbs(**GibbsOpts),
                    N10R17_d.Gibbs(**GibbsOpts),
                    N10R17_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_CO,
                   Name='N/R17 CO.h->C.h+O.h',
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separe/ {C+O}+1/2(H2) + {}->{C.h}+{O+H} (Split R17->R21, R13.2)
idrx.Plot.RxStep([N10R17_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts_H2) + N100.Gibbs(**GibbsOpts),
                  N10R21_i.Gibbs(**GibbsOpts) + N10R13_2_i.Gibbs(**GibbsOpts)],
                 Ref=RefN100_e_CO,
                 Name='N/{C.h+O.h} + (H2) + {} -> {C.h + H.h} + {O.h+H.hd}',
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([N10R13_2_i.Gibbs(**GibbsOpts),
                    N10R13_2_d.Gibbs(**GibbsOpts),
                    N10R13_2_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_CO,
                   Name='R13.2 O.h + H.hd -> OH.h',
                   Hover=HoverList, Color='b', **OH_Line_Props)

# N/R21 C.h+H.f->CH
idrx.Plot.RxStepTS([N10R21_i.Gibbs(**GibbsOpts),
                    N10R21_d.Gibbs(**GibbsOpts),
                    N10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_CO,
                   Name='N/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)


# Section
SectionRefs_N100e.UpdateFromTail(RefN100_e_CO)
# stg.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_N100e, Colour="r")


# ..............................................................................
# HCO series ...................................................................
# ..............................................................................
RefN100_e_HCO = RefN100_e.branch()
RefN100_e_HCO.PlotExtend(Until=refStart_HCO, Color='r')

# Separe {CO.h} + 1/2*H2 -> {CO.h + H.hd}
idrx.Plot.RxStep([N100.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + COg.Gibbs(**GibbsOpts),
                  N10R5_i.Gibbs(**GibbsOpts)],
                 Ref=RefN100_e_HCO,
                 Name='N/{CO.h} + 1/2(H2) -> {CO.h+H.hd}',
                 Hover=HoverList, Color='g', **Jump_Line_Props)


# N/ {CO.h + H.hd} -> {HCO.bb} (R5)
idrx.Plot.RxStepTS([N10R5_i.Gibbs(**GibbsOpts),
                    N10R5_d.Gibbs(**GibbsOpts),
                    N10R5_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_HCO,
                   Name='N/R5: CO.h+H.hd->HCO.bb',
                   Hover=HoverList, Color='g', **Main_Line_Props)

# N/ {HCO.bb} -> {CH.h + O.h}} (R15)
idrx.Plot.RxStepTS([N10R15_i.Gibbs(**GibbsOpts),
                    N10R15_d.Gibbs(**GibbsOpts),
                    N10R15_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_HCO,
                   Name='N/R15: HCO.bb->CH.h+O.hd',
                   Hover=HoverList, Color='g', **Main_Line_Props)

# Separe {CH.h + O.h} + 1/2(H2) + {} -> {CH.h} + {O + H}
idrx.Plot.RxStep([N10R15_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + N100.Gibbs(**GibbsOpts),
                  N10R21_f.Gibbs(**GibbsOpts) + N10R13_2_i.Gibbs(**GibbsOpts)],
                 Ref=RefN100_e_HCO,
                 Name='N/{CH.b+O.hd}+1/2(H2)+{} -> {CH.h}+{OH.h}',
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination {O.h + H.hd} -> {OH.h} (R13.2)
idrx.Plot.RxStepTS([N10R13_2_i.Gibbs(**GibbsOpts),
                    N10R13_2_d.Gibbs(**GibbsOpts),
                    N10R13_2_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_HCO,
                   Name='R13.2 O.h + H.hd -> OH.h',
                   Hover=HoverList, Color='b', **OH_Line_Props)

# Name and tick
SectionRefs_N100e.UpdateFromTail(RefN100_e_HCO)
# stg.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_N100e, Colour="g")




# ..............................................................................
# COH series ...................................................................
# ..............................................................................
RefN100_e_COH = RefN100_e.branch()
RefN100_e_COH.PlotExtend(Until=refStart_COH, Color='r')


# Separe/ {CO.h} + 1/2*H2 -> {CO.h + H.hd}
idrx.Plot.RxStep([N100.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + COg.Gibbs(**GibbsOpts),
                  N10R6_i.Gibbs(**GibbsOpts)],
                 Ref=RefN100_e_COH,
                 Name='N/{CO.h} + 1/2(H2) -> {CO.h+H.hd}',
                 Hover=HoverList, Color='m', **Jump_Line_Props)


# N/R6 {CO.h + H.hd} -> {COH.h} (R6)
idrx.Plot.RxStepTS([N10R6_i.Gibbs(**GibbsOpts),
                    N10R6_d.Gibbs(**GibbsOpts),
                    N10R6_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_COH,
                   Name='N/R6: CO.h+H.hd->COH.ht',
                   Hover=HoverList, Color='m', **Main_Line_Props)

# N/R16 {COH.ht} -> {C.h + OH.hd} (R16)
idrx.Plot.RxStepTS([N10R16_i.Gibbs(**GibbsOpts),
                    N10R16_d.Gibbs(**GibbsOpts),
                    N10R16_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_COH,
                   Name='N/R16: COH.ht->C.h+OH.hd',
                   Hover=HoverList, Color='m', **Main_Line_Props)

# Separe/ {C.h + OH.h} + {} -> {C.h + H.hd} + {OH.h} (R16 -> R21, R13.2)
idrx.Plot.RxStep([N10R16_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + N100.Gibbs(**GibbsOpts),
                  N10R21_i.Gibbs(**GibbsOpts) + N10R13_2_f.Gibbs(**GibbsOpts)],
                 Ref=RefN100_e_COH,
                 Name='{C.h + OH.h} + 1/2(H2) + {} -> {C.h + H.h} + {OH.h}',
                 Hover=HoverList, Color='m', **Jump_Line_Props)

# N/R21 C.h+H.f->CH
idrx.Plot.RxStepTS([N10R21_i.Gibbs(**GibbsOpts),
                    N10R21_d.Gibbs(**GibbsOpts),
                    N10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_e_COH,
                   Name='N/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Name and tick
SectionRefs_N100e.UpdateFromTail(RefN100_e_COH)
# stg.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_N100e, Colour="m")


# # ..............................................................................
# # HCOH series ..................................................................
# # ..............................................................................
# RefN100_e_HCOH = RefN100_e_HCO.branch(Step=3)
#
# # {HCO}
# stg.Plot.RxStep([N10R5_f.E0 + 0.5*H2.E0,
#                   N10R7_i.E0+0.38],
#                  Ref=RefN100_e_HCOH,
#                  Name='{HCO.bb} + 1/2(H2) + {} -> {HCO.bb + H.hd}',
#                  Hover=HoverList, Color='orange', **Jump_Line_Props)
#
# # N/R7 {HCO+H}->{HCOH}
# stg.Plot.RxStep([N10R7_i.E0,
#                   N10R7_f.E0],
#                  Ref=RefN100_e_HCOH,
#                    Name='N/R21: {HCO.bb + H.hd} -> {HCOH.bcis}',
#                    Hover=HoverList, Color="orange", **Main_Line_Props)
#
# # N/R8 {HCOH} -> {CH+OH}
# stg.Plot.RxStepTS([N10R8_i.Gibbs(**GibbsOpts),
#                     N10R8_d.Gibbs(**GibbsOpts),
#                     N10R8_f.Gibbs(**GibbsOpts)],
#                    Ref=RefN100_e_HCOH,
#                    Name='N/R21: {HCOH.bcis} -> {CH + OH}',
#                    Hover=HoverList, Color="orange", **Main_Line_Props)
#
# # N/R7 {CH+OH}+{}->{CH}+{OH}
# stg.Plot.RxStep([N10R8_f.Gibbs(**GibbsOpts) + N100.Gibbs(**GibbsOpts),
#                   N10R21_f.Gibbs(**GibbsOpts) + N10R13_2_f.Gibbs(**GibbsOpts)],
#                  Ref=RefN100_e_HCOH,
#                    Name='N/R21: {CH + OH} -> {CH.h} + {OH.h}',
#                    Hover=HoverList, Color="orange", **Main_Line_Props)


# ----------------------------------------------------------------------------------------------------------------------
# Cobalt ---------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Gibbs - Co(100)')
plt.axes(axs[1][0])


# ..............................................................................
# CO series ....................................................................
# ..............................................................................
RefC100_e_CO = RefC100_e.branch()

# CO adsorption
idrx.Plot.RxStep([C100.Gibbs(**GibbsOpts)+COg.Gibbs(**GibbsOpts),
                  C10R17t_i.Gibbs(**GibbsOpts)],
                 Ref=RefC100_e_CO,
                 Name='CO adsorption',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# C/{CO.t} -> {C.h + O.h} (R17t)
idrx.Plot.RxStepTS([C10R17t_i.Gibbs(**GibbsOpts),
                    C10R17t_d.Gibbs(**GibbsOpts),
                    C10R17t_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_CO,
                   Name='C/R17.1d CO.t -> C.h + O.h',
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separe/ {C.h+O.h} + (H2) + {} -> {C.h+H.h}+{O.h+H.h}
idrx.Plot.RxStep([C10R17t_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts_H2) + C100.Gibbs(**GibbsOpts),
                  C10R21_i.Gibbs(**GibbsOpts) + C10R132_i.Gibbs(**GibbsOpts)],
                 Ref=RefC100_e_CO,
                 Name='C/{C.h+O.h}+(H2)+{} -> {C.h+H.h}+{O.h+H.h}',
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination {O.h+H.hd} -> {OH.h} (R13.2)
idrx.Plot.RxStepTS([C10R132_i.Gibbs(**GibbsOpts),
                    C10R132_d.Gibbs(**GibbsOpts),
                    C10R132_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_CO,
                   Name="C/R13.2: O.h + H.h -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# C/R21 C.h+H.f->CH.h
idrx.Plot.RxStepTS([C10R21_i.Gibbs(**GibbsOpts),
                    C10R21_d.Gibbs(**GibbsOpts),
                    C10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_CO,
                   Name='C/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)


# Section
SectionRefs_C100e.UpdateFromTail(RefC100_e_CO)
# stg.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_C100e, Colour="r")



# ..............................................................................
# HCO series ...................................................................
# ..............................................................................
RefC100_e_HCO = RefC100_e.branch()
RefC100_e_HCO.PlotExtend(Until=refStart_HCO, Color='r')


# Separe/ {CO.t + O.h} + 1/2(H2) -> {CO.h + H.hd}
idrx.Plot.RxStep([C100.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + COg.Gibbs(**GibbsOpts),
                  C10R5_i.Gibbs(**GibbsOpts)],
                 Ref=RefC100_e_HCO,
                 Name='C/{CO.t} + 1/2(H2) -> {CO.h+H.hd}',
                 Hover=HoverList, Color='g', **Jump_Line_Props)


# C/R5 CO.h+H.hd -> HCO.bb
idrx.Plot.RxStepTS([C10R5_i.Gibbs(**GibbsOpts),
                    C10R5_d.Gibbs(**GibbsOpts),
                    C10R5_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_HCO,
                   Name="C/R5 CO.h+H.hd -> HCO.bb",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# C/R15 HCO.bb -(split)-> CH.h + O.h
idrx.Plot.RxStepTS([C10R15_i.Gibbs(**GibbsOpts),
                    C10R15_d.Gibbs(**GibbsOpts),
                    C10R15_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_HCO,
                   Name="C/R15: HCO.bb -(split)-> CH.h + O.h",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe {CH.h +O.h} + 1/2(H2) + {} -> {CH.h} + {O.h + O.h}(R132)
idrx.Plot.RxStep([C10R15_f.Gibbs(**GibbsOpts) + 0.5 * H2.Gibbs(**GibbsOpts_H2) + C100.Gibbs(**GibbsOpts),
                  C10R21_f.Gibbs(**GibbsOpts) + C10R132_i.Gibbs(**GibbsOpts)],
                 Ref=RefC100_e_HCO,
                 Name="C/{CH.h +O.h} + 1/2(H2) + {} -> {CH.h} + {O.h + H.h}(R132)",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([C10R132_i.Gibbs(**GibbsOpts),
                    C10R132_d.Gibbs(**GibbsOpts),
                    C10R132_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_HCO,
                   Name="C/R13.2: O.h + H.h -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# Section
SectionRefs_C100e.UpdateFromTail(RefC100_e_HCO)
# stg.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_C100e, Colour="g")



# ..............................................................................
# COH series ...................................................................
# ..............................................................................
RefC100_e_COH = RefC100_e.branch()
RefC100_e_COH.PlotExtend(Until=refStart_COH, Color='r')


# Separe/ {CO.t+O.h}+H2+{}->{CO.h + H.hd}+{O.h+H.h} (split R23->R6, R13.2)
idrx.Plot.RxStep([C100.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + COg.Gibbs(**GibbsOpts),
                  C10R6_i.Gibbs(**GibbsOpts)],
                 Ref=RefC100_e_COH,
                 Name='C/{CO.t+O.h}+H2+{}->{CO.h+H.hd}+{O.h+H.hd}',
                 Hover=HoverList, Color='m', **Jump_Line_Props)


# C/R6 CO.h + H.h -> COH.ht
idrx.Plot.RxStepTS([C10R6_i.Gibbs(**GibbsOpts),
                    C10R6_d.Gibbs(**GibbsOpts),
                    C10R6_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_COH,
                   Name="C/R6: CO.h + H.h -> COH.ht",
                   Hover=HoverList, Color='m', **Main_Line_Props)

# C/R16 COH.ht -(t)-> C.h + OH.hd
idrx.Plot.RxStepTS([C10R16_i.Gibbs(**GibbsOpts),
                    C10R16_d.Gibbs(**GibbsOpts),
                    C10R16_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_COH,
                   Name="C/R16: COH.ht -(t)-> C.h + OH.hd",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separe {C.h + OH.hd} + 1/2(H2) + {} -> {C.h} + {OH.h}
idrx.Plot.RxStep([C10R16_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + C100.Gibbs(**GibbsOpts),
                  C10R21_i.Gibbs(**GibbsOpts) + C10R132_f.Gibbs(**GibbsOpts)],
                 Ref=RefC100_e_COH,
                 Name="C/{C.h + OH.hd}+1/2(H2)+{}->{C.h+H.h}+{OH.h}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# C/R21 C.h+H.f->CH.h
idrx.Plot.RxStepTS([C10R21_i.Gibbs(**GibbsOpts),
                    C10R21_d.Gibbs(**GibbsOpts),
                    C10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_e_COH,
                   Name='C/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Section
SectionRefs_C100e.UpdateFromTail(RefC100_e_COH)
# stg.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_C100e, Colour="m")






# ----------------------------------------------------------------------------------------------------------------------
# Cobalt-Nickel --------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Gibbs - CoNi(100)')
plt.axes(axs[1][1])



# ..............................................................................
# CO series ....................................................................
# ..............................................................................
RefCN100_e_CO = RefCN100_e.branch()

# CO adsorption
idrx.Plot.RxStep([CN100.Gibbs(**GibbsOpts)+COg.Gibbs(**GibbsOpts),
                  CN10R17tC_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_e_CO,
                 Name='CO adsorption',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# CN(R17tC)/ {CO.tC} -> {C.hN + O.hC}
idrx.Plot.RxStepTS([CN10R17tC_i.Gibbs(**GibbsOpts),
                    CN10R17tC_d.Gibbs(**GibbsOpts),
                    CN10R17tC_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_CO,
                   Name="CN/R13tC CO.tC -> C.hN + O.hC",
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separe/ {C.hN + O.hC}+1/2(H2)+{} -> {C.hN} + {(R13C) O.h + H.h} + {}
idrx.Plot.RxStep([CN10R17tC_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts_H2) + CN100.Gibbs(**GibbsOpts),
                  CN10R21_i.Gibbs(**GibbsOpts) + CN10R132C_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_e_CO,
                 Name="CN/ {C.hN + O.hC}+(H2)+{} -> {C.hN+H.hC} + {(R13C) O.h + H.h}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination R13C {O.h + H.h} -(tC)-> {OH.h}
idrx.Plot.RxStepTS([CN10R132C_i.Gibbs(**GibbsOpts),
                    CN10R132C_d.Gibbs(**GibbsOpts),
                    CN10R132C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_CO,
                   Name="CN(R13C)/O.h + H.h -(tC)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN/R21 C.h+H.f->CH.h
idrx.Plot.RxStepTS([CN10R21_i.Gibbs(**GibbsOpts),
                    CN10R21_d.Gibbs(**GibbsOpts),
                    CN10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_CO,
                   Name='CN/R21: C.hN + H.hC -> CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Compile branches, section
# stg.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_CN100e, Colour="r")




# ..............................................................................
# HCO series ...................................................................
# ..............................................................................
RefCN100_e_HCO = RefCN100_e.branch()
RefCN100_e_HCO.PlotExtend(Until=refStart_HCO, Color='m')
SectionRefs_CN100e.UpdateFromTail(RefCN100_e_HCO)

# Separe/ {CO.bCN+O.hC} + H2 + {} -> {CO.hN + H.hNd} + {(R13C) O.h + H.h} (split R23->R5, R13.2C)
idrx.Plot.RxStep([CN100.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+COg.Gibbs(**GibbsOpts),
                  CN10R5tN_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_e_HCO,
                 Name="CN/ {CO.bCN+O.hC}+(H2)+{}->{CO.hN+H.hNd}+{(R13C)O.h+H.h}",
                 Hover=HoverList, Color='g', **Jump_Line_Props)



# CN/R5 CO.hN + H.hNd -> HCO.bbN
idrx.Plot.RxStepTS([CN10R5tN_i.Gibbs(**GibbsOpts),
                    CN10R5tN_d.Gibbs(**GibbsOpts),
                    CN10R5tN_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_HCO,
                   Name="CN/R5 CO.hN + H.hNd -> HCO.bbN",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# CN/R15 HCO.bbN -(b)-> CH.hN + O.hC
idrx.Plot.RxStepTS([CN10R15b_i.Gibbs(**GibbsOpts),
                    CN10R15b_d.Gibbs(**GibbsOpts),
                    CN10R15b_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_HCO,
                   Name="CN10/R15b-d HCO.bbN -(b)-> CH.hN + O.hC",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# Separe/ {CH.hN + O.hC} + 1/2(H2) + {} -> {CH.hN} + {(R13C) O.h + H.h}
idrx.Plot.RxStep([CN10R15b_f.Gibbs(**GibbsOpts) + 0.5 * H2.Gibbs(**GibbsOpts_H2) + CN100.Gibbs(**GibbsOpts),
                  CN10R21_f.Gibbs(**GibbsOpts) + CN10R132C_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_e_HCO,
                 Name="CN/ {CH.hN + O.hC} + 1/2(H2) + {} -> {CH.hN} + {(R13C) O.h + H.h}",
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination R13C {O.h + H.h} -(tC)-> {OH.h}
idrx.Plot.RxStepTS([CN10R132C_i.Gibbs(**GibbsOpts),
                    CN10R132C_d.Gibbs(**GibbsOpts),
                    CN10R132C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_HCO,
                   Name="CN(R13C)/O.h + H.h -(tC)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# Section

# stg.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_CN100e, Colour="g")



# ..............................................................................
# COH series ...................................................................
# ..............................................................................
RefCN100_e_COH = RefCN100_e.branch()
RefCN100_e_COH.PlotExtend(Until=refStart_COH, Color='m', Alpha=1, LineWidth=.8)
SectionRefs_CN100e.UpdateFromTail(RefCN100_e_COH)


# Separe/ {CO.bCN + O.hC}+(H2)+{} -> {CO.hN+H.hNd}+{(R132C)O.h+H.h}
idrx.Plot.RxStep([CN100.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2)+COg.Gibbs(**GibbsOpts),
                  CN10R6tN_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_e_COH,
                 Name="CN/{CO.bCN + O.hC}+(H2)+{} -> {CO.hN+H.hNd}+{(R132C)O.h+H.h}",
                 Hover=HoverList, Color='m', **Jump_Line_Props)



# CN/R6tN CO.hN + H.hNd -> COH.hNtN
idrx.Plot.RxStepTS([CN10R6tN_i.Gibbs(**GibbsOpts),
                    CN10R6tN_d.Gibbs(**GibbsOpts),
                    CN10R6tN_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_COH,
                   Name="CN/R6tN CO.hN + H.hNd -> COH.hNtN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# CN/R16tN COH.hNtN -> C.hN + OH.hN
idrx.Plot.RxStepTS([CN10R16tN_i.Gibbs(**GibbsOpts),
                    CN10R16tN_d.Gibbs(**GibbsOpts),
                    CN10R16tN_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_COH,
                   Name="CN/R16tN COH.hNtN -> C.hN + OH.hN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separe/ {C.hN + OH.hN}+1/2(H2)+{} -> {C.hN+H.hC} + {(R132C)OH.hN}
idrx.Plot.RxStep([CN10R16tN_f.Gibbs(**GibbsOpts) + 0.5*H2.Gibbs(**GibbsOpts_H2) + CN100.Gibbs(**GibbsOpts),
                  CN10R21_i.Gibbs(**GibbsOpts) + CN10R132C_f.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_e_COH,
                 Name="CN/ {C.hN+OH.hN}+1/2(H2)+{}->{C.hN+H.hC}+{(R132C)OH.hN}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# CN/R21 C.h+H.f->CH.h
idrx.Plot.RxStepTS([CN10R21_i.Gibbs(**GibbsOpts),
                    CN10R21_d.Gibbs(**GibbsOpts),
                    CN10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_e_COH,
                   Name='CN/R21: C.hN + H.hC -> CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Sections
# stg.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_CN100e, Colour="m")

idrx.Plot.Align_Rx_Ticks(SectionRefs_CN100e, TSmode=False)


#-----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------ Ending subplot
#-----------------------------------------------------------------------------------------------------------------------

# Ajustes finales de plots

idrx.Plot.ActivateHover(HoverList, fig)
Ley = [Line2D([0], [0], color="k", linewidth=3, linestyle='-', alpha=0.8),
       Line2D([0], [0], color="r", linewidth=3, linestyle='-', alpha=0.8)]

plt.xlim([0, 15])
plt.axes(axs[1][1]); plt.ylim([-70, 190])

# Lado izquierdo
for xax in axs:
    plt.axes(xax[0])
    plt.ylabel("Gibbs free energy (kJ/mol)")
    plt.tick_params(axis="y", direction="in")

# centro y derecho
for iax in [axs[i][j] for i in range(0,2) for j in range(1,3)]:
    plt.axes(iax)
    plt.tick_params(axis="y", direction="inout", length=12.)

# all plots
for iax in [axs[i][j] for i in range(0,2) for j in range(0,3)]:
    plt.axes(iax)
    plt.axhline(y=0., color="k", alpha=.5, linewidth=.4)
    plt.grid(which='major', color='k', linewidth=.5, alpha=.3)
    iax.set_xticklabels([])
    # plt.legend(Ley, ["(111)", "(100)"], prop={'size': 8}, loc='upper right')

# -
# legendas de titulo

labelname = iter(('a)','b)','c)',
                  'd)','e)','f)'))
for xax in axs:
    for yax in xax:
        plt.axes(yax)
        plt.annotate(next(labelname),
                     xy=[.02, .95], xytext=[0, 0],
                     xycoords='axes fraction', textcoords='offset points',
                     ha='left', va='top', size=16, color='k', fontweight='bold',
                     bbox=dict(facecolor='white', edgecolor='white', pad=2.0))

labelname = iter(('Co(111)','NiCo(111)','Ni(111)',
                  'Co(100)','NiCo(100)','Ni(100)'))
for yax in axs[0]:
    plt.axes(yax)
    plt.annotate(next(labelname),
                 xy=[.5, .95], xytext=[0, 0],
                 xycoords='axes fraction', textcoords='offset points',
                 ha='center', va='top', size=12, color='k', fontweight='bold',
                 bbox=dict(facecolor='white', edgecolor='white', pad=2.0))
for yax in axs[1]:
    plt.axes(yax)
    plt.annotate(next(labelname),
                 xy=[0.35, .95], xytext=[0, 0],
                 xycoords='axes fraction', textcoords='offset points',
                 ha='center', va='top', size=12, color='k', fontweight='bold',
                 bbox=dict(facecolor='white', edgecolor='white', pad=2.0))



plt.savefig("./CO_disoc_Gibbs_profile.png", dpi=180)
plt.show()
