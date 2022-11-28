#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from data import *


########################################################################################################################
########################################################################################################################
# Creating Plot, CHx series ############################################################################################
########################################################################################################################
idrx.MayorSection('Creating Plot Eletronic')

fig, axs = plt.subplots(2, 3, figsize=(12, 6), dpi=90, sharey='row')
plt.subplots_adjust(wspace=.0, hspace=.1, left=.08, right=.98, bottom=.05, top=.95)
HoverList = []

# References
RefN111_e = idrx.Plot.RxRef(0., 0.)
RefC111_e = idrx.Plot.RxRef(0., 0.)
RefCN111_e = idrx.Plot.RxRef(0., 0.)

# Place holders
HoverList = []
SectionRefs_N111e = RefN111_e.branch()
SectionRefs_C111e = RefC111_e.branch()
SectionRefs_CN111e = RefCN111_e.branch()

# Color ref: https://gist.github.com/thriveth/8560036

# Default parameters
Main_Line_Props = {"StepSpan": .5, "LineStyle": "solid", "LineWidth": 1.5, "AlphaLines": 1., 'T-rate':265 + 273.15}
Main_Line_Props_CO = {"StepSpan": 1.5, "LineStyle": "solid", "LineWidth": 1.5, "AlphaLines": 1.}
Jump_Line_Props = {"StepSpan": .2, "LineStyle": "solid", "LineWidth": .8, "AlphaLines": 1.}
OH_Line_Props = {"StepSpan": .2, "LineStyle": 'solid', "LineWidth": 2, "AlphaLines": .2}


########################################################################################################################
# Nickel (111s)----------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Electronic - Ni(111s)')
plt.axes(axs[0][2])
plt.title('Reaction profile $\longrightarrow$')


# # CO2 gas
# RefN111_e_CO2g = RefN111_e.branch()
# stg.Plot.RxStep([CO2.E0+4*H2.E0, CH4_g.E0 + 2*H2O.E0],
#                  Ref=RefN111_e_CO2g,
#                  Name="Gas Rx",
#                  Hover=HoverList, Color='m', **Main_Line_Props_CO)

# .....................................
# CO2 series ..........................
# .....................................
RefN111_e_CO2 = RefN111_e.branch()

# Ads
idrx.Plot.RxStep([CO2.E0 + N111s.E0,N1sR23_i.E0],
                 Ref=RefN111_e_CO2,
                 Name='N1s/CO2ad:{}+(CO2) -> {CO2.tt}',
                 Hover=HoverList, Color='k', **Jump_Line_Props)



# N/R23 : CO2.tt -> CO.h + O.h(m)

idrx.Plot.RxStepTS([N1sR23_i.E0, N1sR23_d.E0, N1sR23_f.E0],
                   Ref=RefN111_e_CO2,
                   Name="N1s/R23: CO2.tt -> CO.h + O.h(m)",
                   Hover=HoverList, Color='k', **{**Main_Line_Props, "StepSpan": 1.})
# Name
idrx.Plot.AnnotateStepAxis(["$CO_{2}$",''], Ref=RefN111_e_CO2, Colour="k")
SectionRefs_N111e.UpdateFromTail(RefN111_e_CO2)

# .....................................
# CO desorbs ..........................
# .....................................
RefN111_e_CO_d = RefN111_e_CO2.branch()
# RefN111_e_CO.PlotExtend(Until=3., Color='m', Alpha=1, LineWidth=.8)

# N/(+O jump!) {CO.h + O.h(m)} + 1/2(H2) + {} -> {CO.h} + {O.f + H.h}
idrx.Plot.RxStep([N1sR23_f.E0 + 0.5 * H2.E0 + N111s.E0, N1sR17_i.E0 + N1sR132_i.E0],
                 Ref=RefN111_e_CO_d,
                 Name="N1s/(+O jump!) {CO.h + O.h(m)} + 1/2(H2) + {} -> {CO.h} + {O.h + H.f}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

idrx.Plot.RxStep([N1sR17_i.E0, N111s.E0 + COg.E0],
                 Ref=RefN111_e_CO_d,
                 Name="CO desorption",
                 Hover=HoverList, Color='m', **Main_Line_Props_CO)
# # Gas Rx
# stg.Plot.RxStep([COg.E0+3*H2.E0 , CH4_g.E0+H2O.E0],
#                  Ref=RefN111_e_CO_d,
#                  Name="Gas Rx",
#                  Hover=HoverList, Color='m', **Main_Line_Props_CO)







# .....................................
# CO series ...........................
# .....................................
RefN111_e_CO = RefN111_e_CO2.branch()
# RefN111_e_CO.PlotExtend(Until=3., Color='m', Alpha=1, LineWidth=.8)

# N/(+O jump!) {CO.h + O.h(m)} + 1/2(H2) + {} -> {CO.h} + {O.f + H.h}
idrx.Plot.RxStep([N1sR23_f.E0 + 0.5 * H2.E0 + N111s.E0, N1sR17_i.E0 + N1sR132_i.E0],
                 Ref=RefN111_e_CO,
                 Name="N1s/(+O jump!) {CO.h + O.h(m)} + 1/2(H2) + {} -> {CO.h} + {O.h + H.f}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination, branched-out
idrx.Plot.RxStepTS([N1sR132_i.E0, N1sR132_d.E0, N1sR132_f.E0],
                   Ref=RefN111_e_CO, UpdateRef=False,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# N/ R17 (bridge): CO.h -> C.h + O.h
idrx.Plot.RxStepTS([N1sR17_i.E0, N1sR17_d.E0, N1sR17_f.E0],
                   Ref=RefN111_e_CO,
                   Name="N1s/R17(bridge): CO.hcp -> C.hcp + O.hcp",
                   Hover=HoverList, Color="r", **Main_Line_Props)

# N/ Separe {C.h + O.h} + 1/2(H2) + {} -> {C.f} + {O.h + H.h}
idrx.Plot.RxStep([N1sR17_f.E0 + 0.5 * H2.E0 + N111s.E0 , N1s_Cf.E0 + N1sR132_i.E0],
                 Ref=RefN111_e_CO,
                 Name="N1s/(+C jump!) {C.h + O.h} + H2 + {} -> {C.f + H.f} + {O.h + H.h}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([N1sR132_i.E0, N1sR132_d.E0, N1sR132_f.E0],
                   Ref=RefN111_e_CO,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color='b', **OH_Line_Props)

SectionRefs_N111e.UpdateFromTail(RefN111_e_CO)
idrx.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_N111e, Colour="r")


# .....................................
# HCO series ..........................
# .....................................
RefN111_e_HCO = RefN111_e_CO2.branch()
RefN111_e_HCO.PlotExtend(Until=5., Color='m', Alpha=1, LineWidth=.8)

# Separe CO + O
# N/(+O jump!) {CO.h + O.h(m)} + H2 + {} -> {CO.h + H.h} + {O.f + H.h}
idrx.Plot.RxStep([N1sR23_f.E0 + H2.E0 + N111s.E0, N1sR5_i.E0 + N1sR132_i.E0],
                 Ref=RefN111_e_HCO,
                 Name="N1s/(+O jump!) {CO.h + O.h(m)} + H2 + {} -> {CO.h + H.h} + {O.h + H.f}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination, branched-out
RefN111_e_temp_OH = RefN111_e_HCO.branch()
idrx.Plot.RxStepTS([N1sR132_i.E0, N1sR132_d.E0, N1sR132_f.E0],
                   Ref=RefN111_e_temp_OH,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# R5 (bridge): CO.h + H.h -> HCO.htO
idrx.Plot.RxStepTS([N1sR5_i.E0, N1sR5_d.E0, N1sR5_f.E0],
                   Ref=RefN111_e_HCO,
                   Name="N1s/R5(bridge): CO.h + H.h -> HCO.htO",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# R15 (split): HCO.hcptO -> CH.fcc + O.fcc
idrx.Plot.RxStepTS([N1sR15_i.E0, N1sR15_d.E0, N1sR15_f.E0],
                   Ref=RefN111_e_HCO,
                   Name="N1s/R15(split): HCO.hcptO -> CH.fcc + O.fcc",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe {CH.f + O.f} + 1/2(H2) + {} -> {CH.h} + {O.f + H.f}
idrx.Plot.RxStep([N1sR15_f.E0 + 0.5 * H2.E0 + N111s.E0, N1sR21a_f.E0 + N1sR132_i.E0],
                 Ref=RefN111_e_HCO,
                 Name="N1s/(+ jump CH) {CH.f + O.f} + {H.f} -> {CH.h} + {O.f + H.f}",
                 Hover=HoverList, Color="b", **OH_Line_Props)

# OH elimination, included
idrx.Plot.RxStepTS([N1sR132_i.E0, N1sR132_d.E0, N1sR132_f.E0],
                   Ref=RefN111_e_HCO,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# Section
SectionRefs_N111e.UpdateFromTail(RefN111_e_HCO)
idrx.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_N111e, Colour="g")


# .....................................
# COH series ..........................
# .....................................
RefN111_e_COH = RefN111_e_CO2.branch()
RefN111_e_COH.PlotExtend(Until=8., Color='m', Alpha=1, LineWidth=.8)

# Separe CO + O
# N/(+O jump!) {CO.h + O.h(m)} + H2 + {} -> {CO.h + H.h} + {O.f + H.h}
idrx.Plot.RxStep([N1sR23_f.E0 + H2.E0 + N111s.E0, N1sR6_i.E0 + N1sR132_i.E0],
                 Ref=RefN111_e_COH,
                 Name="N1s/(+O jump!) {CO.h + O.h(m)} + 2*{H.f} -> {CO.h + H.f} + {O.h + H.f} + {}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination, branched-out
RefN111_e_temp_OH_2 = RefN111_e_COH.branch()
idrx.Plot.RxStepTS([N1sR132_i.E0, N1sR132_d.E0, N1sR132_f.E0],
                   Ref=RefN111_e_temp_OH_2,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# N1sR6 : CO.h + H.f -> COH.ht
idrx.Plot.RxStepTS([N1sR6_i.E0, N1sR6_d.E0, N1sR6_f.E0],
                   Ref=RefN111_e_COH,
                   Name="N1s/R6(top): CO.h + H.f -> COH.ht",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# N1sR16 : COH.ht -> C.h + OH.f
idrx.Plot.RxStepTS([N1sR16_i.E0, N1sR16_d.E0, N1sR16_f.E0],
                   Ref=RefN111_e_COH,
                   Name="N1s/R6(top): COH.ht -> C.h + OH.f",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Ni/ Separe {C.h + OH.f} + {} -> {C.f} + {OH.f}
idrx.Plot.RxStep([N1sR16_f.E0 + N111s.E0, N1s_Cf.E0 + N1sR132_f.E0],
                 Ref=RefN111_e_COH,
                 Name="N1s/(+C jump!) {C.h + OH.f} + {H.f} -> {(top)C.f + H.h} + {OH.f}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

SectionRefs_N111e.UpdateFromTail(RefN111_e_COH)
idrx.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_N111e, Colour="m")




# .....................................
# CHx series ..........................
# .....................................
RefN111_e_CO.PlotExtend(Until=11.5, Color='r')
RefN111_e_COH.PlotExtend(Until=11.5, Color='m')
RefN111_e_HCO.PlotExtend(Until=12.5 + .4, Color='g')

RefN111_e_CHx = RefN111_e_COH.branch()

# ---- *C+*H -(bridge)-> *CH
# rama paralela, otra referencia
RefN111_e_CHx_2 = RefN111_e_CHx.branch()

idrx.Plot.RxStep([N1s_Cf.E0 + 2. * H2.E0, N1sR21a_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefN111_e_CHx_2, Name="N1s/{C.f}+2*H2->{C.f+H.f}+(3/2)*H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R21a by side: C.f + H.h
idrx.Plot.RxStepTS([N1sR21a_i.E0, N1sR21a_TS.E0, N1sR21a_f.E0],
                   Ref=RefN111_e_CHx_2,
                   Name='N1s/R21a by bridge: C.f + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- *C+*H -(top)-> *CH
# rama principal

idrx.Plot.RxStep([N1s_Cf.E0 + 2. * H2.E0,
                  N1sR21top_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefN111_e_CHx, Name="N1s/{C.f}+2*H2->{C.f+H.f}+(3/2)*H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R21b on top: C.f + H.f -> CH.h
idrx.Plot.RxStepTS([N1sR21top_i.E0, N1sR21top_TS.E0, N1sR21top_f.E0],
                   Ref=RefN111_e_CHx,
                   Name='N1s/R21b on top: C.f + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH+H -> CH2

# Jump N/ R21 -> R9
idrx.Plot.RxStep([N1sR21top_f.E0 + (3. / 2.) * H2.E0, N1sR9top_i.E0 + H2.E0],
                 Ref=RefN111_e_CHx,
                 Name='N1s/{CH.f}+(3/2)H2->{CH.f+H.h}+H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R9 on top: CH.f + H.h -> CH2.f
idrx.Plot.RxStepTS([N1sR9top_i.E0, N1sR9top_TS.E0, N1sR9top_f.E0],
                   Ref=RefN111_e_CHx,
                   Name='N1s/R9 on top: CH.f + H.h -> CH2.f',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH2+H -> CH3

# Jump N/ R0 -> R10
idrx.Plot.RxStep([N1sR9top_f.E0 + H2.E0, N1sR10top_i.E0 + .5 * H2.E0],
                 Ref=RefN111_e_CHx,
                 Name='N1s/{CH2.f}+H2->{CH2.f+H.f}+(1./2.)*H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R10 on top: CH2.f +H.f -> CH3.f
idrx.Plot.RxStepTS([N1sR10top_i.E0, N1sR10top_TS.E0, N1sR10top_f.E0],
                   Ref=RefN111_e_CHx,
                   Name='N1s/R10 on top: CH2.f +H.f -> CH3.f',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH3+H -> CH4

# Jump N/ R10 -> R11
idrx.Plot.RxStep([N1sR10top_f.E0 + .5 * H2.E0, N1sR11top_i.E0],
                 Ref=RefN111_e_CHx,
                 Name='N1s/{CH3.f}+(1/2)H2->{CH3.f+H.f}',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R11 on top: CH3.f +H.f -> CH4.g
idrx.Plot.RxStepTS([N1sR11top_i.E0, N1sR11top_TS.E0, N1sR11top_f.E0],
                   Ref=RefN111_e_CHx,
                   Name='N1s/R11 on top: CH3.f +H.f -> CH4.g',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Jump physisorption
idrx.Plot.RxStep([N1sR11top_f.E0, CH4_g.E0 + N111s.E0],
                 Ref=RefN111_e_CHx,
                 Name='N1s/{}CH4g->{}+CH4g',
                 Hover=HoverList, Color="k", **{**Main_Line_Props, 'StepSpan':.4})





# OH elimination, included
idrx.Plot.RxStepTS([N1sR132_i.E0, N1sR132_d.E0, N1sR132_f.E0],
                   Ref=RefN111_e_CHx,
                   Name="N1s/R13.2 O.f + H.h -> OH.f",
                   Hover=HoverList, Color="b", **OH_Line_Props)
idrx.Plot.RxStep([N1sR132_f.E0+(1/2)*H2.E0, N111s.E0 + H2O.E0],
                 Ref=RefN111_e_CHx,
                 Name="H2O formation",
                 Hover=HoverList, Color='m', **Main_Line_Props_CO)
idrx.Plot.RxStep([N1sR132_f.E0+(1/2)*H2.E0, N111s.E0 + H2O.E0],
                 Ref=RefN111_e_CHx,
                 Name="H2O formation",
                 Hover=HoverList, Color='g', **Main_Line_Props_CO)





# Test Jump whole reaction
# if ShowGlobal_e:
#     RefN111_e_full = RefN111_e.branch(Step=0)
#     stg.Plot.RxStep([N1s_Cf.E0 + 2 * H2.E0,
#                       N111s.E0 + CH4_g.E0],
#                      Ref=RefN111_e_full, Name='N1s/{C.f+H.h}+2*H2->{}+CH4g',
#                      Hover=HoverList, StepSpan=2.4, Color='g', **LineProps)
#     RefN111_e_full.PlotExtend(Until=11., Color="g")

SectionRefs_N111e.UpdateFromTail(RefN111_e_CHx)
idrx.Plot.AnnotateStepAxis(['$CH_{x}$', '$CH_{4(g)}$'], Ref=SectionRefs_N111e, Colour="k")
idrx.Plot.Align_Rx_Ticks(SectionRefs_N111e, TSmode=False)



# ----------------------------------------------------------------------------------------------------------------------
# Cobalt ----------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Electronic - Co(111s)')
plt.axes(axs[0][0])
plt.title('Reaction profile $\longrightarrow$')


# .....................................
# CO2 series ..........................
# .....................................
RefC111_e_CO2 = RefC111_e.branch()

# ads
idrx.Plot.RxStep([CO2.E0 + C111s.E0, C1sR23_i.E0],
                 Ref=RefC111_e_CO2,
                 Name='C1s/R23.1 (CO2)+{} -> {CO2.tt}',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# R23.1 CO2.tt -> CO.t + O.h
idrx.Plot.RxStepTS([C1sR23_i.E0, C1sR23_d.E0, C1sR23_f.E0],
                   Ref=RefC111_e_CO2,
                   Name="C1s/R23.1 CO2.tt -> CO.t + O.h",
                   Hover=HoverList, Color="k", **{**Main_Line_Props, "StepSpan": 1.})
# Section
SectionRefs_C111e.UpdateFromTail(RefC111_e_CO2)
idrx.Plot.AnnotateStepAxis(['$CO_{2}$',''], Ref=SectionRefs_C111e, Colour='k')

# .....................................
# CO desorbs ..........................
# .....................................
RefC111_e_CO_des = RefC111_e_CO2.branch()

# Separe {CO.t+O.h} + 1/2(H2) + {} -> {CO.t} + {O.h+H.f}
idrx.Plot.RxStep([C1sR23_f.E0 + 0.5 * H2.E0 + C111s.E0, C1sR13_i.E0 + C1sR171_i.E0],
                 Ref=RefC111_e_CO_des,
                 Name="C1s/ {CO.t+O.h} + 1/2(H2) + {} -> {CO.t} + {O.h+H.f}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)
# CO desorbs
idrx.Plot.RxStep([C1sR171_i.E0, C111s.E0 + COg.E0],
                 Ref=RefC111_e_CO_des,
                 Name="CO.t desorption",
                 Hover=HoverList, Color='m', **Main_Line_Props_CO)





# .....................................
# CO series ...........................
# .....................................
RefC111_e_CO = RefC111_e_CO2.branch()

# ---------------- from CO.h (secondary path)
RefC111_e_CO_direct_h = RefC111_e_CO.branch()

# Separe {CO.t+O.h} + 1/2(H2) + {} -> {CO.t} + {O.h+H.f}
idrx.Plot.RxStep([C1sR23_f.E0 + 0.5*H2.E0 + C111s.E0, C1sR13_i.E0 + C1sR172_i.E0],
                 Ref=RefC111_e_CO_direct_h,
                 Name="C1s/ {CO.t+O.h} + 1/2(H2) + {} -> {CO.h} + {O.h+H.f}",
                 Hover=HoverList, Color="r", **{**Jump_Line_Props, "StepSpan": .3})

# OH elimination (branched out)
idrx.Plot.RxStepTS([C1sR13_i.E0, C1sR13_d.E0, C1sR13_f.E0],
                   Ref=RefC111_e_CO_direct_h, UpdateRef=False,
                   Name="C1s/ O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# R17.1 CO.h -(b)-> C.h + O.h
idrx.Plot.RxStepTS([C1sR172_i.E0, C1sR172_d.E0, C1sR172_f.E0],
                   Ref=RefC111_e_CO_direct_h,
                   Name="C1s/R17.2 CO.h -(b)-> C.h + O.h",
                   Hover=HoverList, Color="r", **{**Main_Line_Props, "StepSpan": .4})

# ---------------- from CO.t (main path)
RefC111_e_CO_direct_t = RefC111_e_CO.branch()

# Separe {CO.t+O.h} + 1/2(H2) + {} -> {CO.t} + {O.h+H.f}
idrx.Plot.RxStep([C1sR23_f.E0 + 0.5 * H2.E0 + C111s.E0, C1sR13_i.E0 + C1sR171_i.E0],
                 Ref=RefC111_e_CO_direct_t,
                 Name="C1s/ {CO.t+O.h} + 1/2(H2) + {} -> {CO.t} + {O.h+H.f}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination (branched out)
idrx.Plot.RxStepTS([C1sR13_i.E0, C1sR13_d.E0, C1sR13_f.E0],
                   Ref=RefC111_e_CO_direct_t, UpdateRef=False,
                   Name="C1s/ O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# R17.1 CO.t -(b)-> C.h + O.h
idrx.Plot.RxStepTS([C1sR171_i.E0, C1sR171_d.E0, C1sR171_f.E0],
                   Ref=RefC111_e_CO_direct_t,
                   Name="C1s/R17.1 CO.t -(b)-> C.h + O.h",
                   Hover=HoverList, Color="r", **Main_Line_Props)

# Separe {C.h + O.h} + 1/2(H2) + {} -> {C.h}(R21-i) + {O.h + H.f}
idrx.Plot.RxStep([C1sR171_f.E0 + 0.5 * H2.E0 + C111s.E0, C1s_Ch.E0 + C1sR13_i.E0],
                 Ref=RefC111_e_CO_direct_t,
                 Name="C1s/{C.h + O.h} + (H2) + {} -> {C.h + H.f} + {O.h + H.f}",
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([C1sR13_i.E0, C1sR13_d.E0, C1sR13_f.E0],
                   Ref=RefC111_e_CO_direct_t,
                   Name="C1s/ O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# Converge branch
RefC111_e_CO.UpdateFromTail(RefC111_e_CO_direct_t)
SectionRefs_C111e.UpdateFromTail(RefC111_e_CO)
idrx.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_C111e, Colour="r")


# .....................................
# HCO series ..........................
# .....................................
RefC111_e_HCO = RefC111_e_CO2.branch()
RefC111_e_HCO.PlotExtend(Until=5., Color='m', Alpha=1, LineWidth=.8)


# Separe/ {CO.t+O.h} + H2 + {} -> {CO.h+H.} + {O.h+H.f}
idrx.Plot.RxStep([C1sR23_f.E0 + H2.E0 + C111s.E0, C1sR5h_i.E0 + C1sR13_i.E0],
                 Ref=RefC111_e_HCO,
                 Name="C/ {CO.t+O.h}+(H2)+{} -> {CO.h+H.hd}+{O.h+H.f}",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([C1sR13_i.E0, C1sR13_d.E0, C1sR13_f.E0],
                   Ref=RefC111_e_HCO, UpdateRef=False,
                   Name="C1s/R13.2 O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# -------------------------------- Ruta 1 (HCO.hbO)
RefC111_e_HCOh = RefC111_e_HCO.branch()

# C/R5 CO.h + H.hd -> HCO.hbO
idrx.Plot.RxStepTS([C1sR5h_i.E0, C1sR5h_d.E0, C1sR5h_f.E0],
                   Ref=RefC111_e_HCOh,
                   Name="C/ CO.h+H.hd -> HCO.hbO(R5)",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# C/R15 HCO.hbO -(split)-> CH.h + O.hm
idrx.Plot.RxStepTS([C1sR15h_i.E0, C1sR15h_d.E0, C1sR15h_f.E0],
                   Ref=RefC111_e_HCOh,
                   Name="C1s/R15 HCO.fbO -(split)-> CH.h + O.hm",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe {CH.h + O.hm} + H2 + {} -> {CH.h} + {O.h + H.f}
idrx.Plot.RxStep([C1sR15h_f.E0 + 0.5 * H2.E0 + C111s.E0, C1sR21_f.E0 + C1sR13_i.E0],
                 Ref=RefC111_e_HCOh,
                 Name="C1s/{CH.h + O.hm} + {H.f} -> {CH.h} + {O.h + H.f}",
                 Hover=HoverList, Color="b", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([C1sR13_i.E0, C1sR13_d.E0, C1sR13_f.E0],
                   Ref=RefC111_e_HCOh,
                   Name="C1s/ O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# -------------------------------- Ruta 2 (HCO.fbO)
RefC111_e_HCOf = RefC111_e_HCO.branch()

# C/R5 CO.h + H.hd -> HCO.hbO
idrx.Plot.RxStepTS([C1sR5f_i.E0, C1sR5f_d.E0, C1sR5f_f.E0],
                   Ref=RefC111_e_HCOf,
                   Name="C/ CO.h+H.hd -> HCO.fbO",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# C/R15 HCO.fbO -(split)-> CH.h + O.hm
idrx.Plot.RxStepTS([C1sR15f_i.E0, C1sR15f_d.E0, C1sR15f_f.E0],
                   Ref=RefC111_e_HCOf,
                   Name="C1s/R15 HCO.fbO -(split)-> CH.h + O.hm",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Converge branches
RefC111_e_HCO.UpdateFromTail(RefC111_e_HCOh)
SectionRefs_C111e.UpdateFromTail(RefC111_e_HCO)
idrx.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_C111e, Colour="g")




# .....................................
# COH series ..........................
# .....................................
RefC111_e_COH = RefC111_e_CO2.branch()
RefC111_e_COH.PlotExtend(Until=8.5, Color='m', Alpha=1, LineWidth=.8)

# Separe/ {CO.t+O.h} + H2 + {} -> {CO.h+H.} + {O.h + H}
idrx.Plot.RxStep([C1sR23_f.E0 + H2.E0 + C111s.E0, C1sR6_i.E0 + C1sR13_i.E0],
                 Ref=RefC111_e_COH,
                 Name="C/ {CO.t+O.h} + H2 + {} -> {CO.h+H.hd} + {O.h+H.f}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# OH elimination (branched out)
idrx.Plot.RxStepTS([C1sR13_i.E0, C1sR13_d.E0, C1sR13_f.E0],
                   Ref=RefC111_e_COH, UpdateRef=False,
                   Name="C1s/R13.2 O.h + H.f -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# R6: CO.h + H.h-> COH.hbt
idrx.Plot.RxStepTS([C1sR6_i.E0, C1sR6_d.E0, C1sR6_f.E0],
                   Ref=RefC111_e_COH,
                   Name="C/ CO.b+H.h -> COH.h",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# R16: COH.hbt -(t)-> C.h + OH.hd
idrx.Plot.RxStepTS([C1sR16_i.E0, C1sR16_d.E0, C1sR16_f.E0],
                   Ref=RefC111_e_COH,
                   Name="C1s/R16: COH.hbt -(t)-> C.h + OH.hd",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separe C/ {C.h+OH.hd} + {} -> {C.h} + {OH.}
idrx.Plot.RxStep([C1sR16_f.E0 + C111s.E0, C1s_Ch.E0 + C1sR13_f.E0],
                 Ref=RefC111_e_COH,
                 Name="C1s/ {C.h+OH.hd}+{} -> {C.h} + {OH.h}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# Section
SectionRefs_C111e.UpdateFromTail(RefC111_e_COH)
idrx.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_C111e, Colour="m")



# .....................................
# CHx series ..........................
# .....................................
RefC111_e_CO.PlotExtend(Until=11.5, Color="r")
RefC111_e_COH.PlotExtend(Until=11.5, Color="m")
RefC111_e_HCO.PlotExtend(Until=12.9, Color="g")


RefC111_e_CHx = RefC111_e_CO.branch()
RefC111_e_CHx.PlotExtend(Until=11.5, Color='m', Alpha=1, LineWidth=.8)


# ---- *C.h+H2 -(bridge)-> *CH.h
# rama paralela
RefC111_e_CHx_2 = RefC111_e_CHx.branch()

idrx.Plot.RxStep([C1s_Ch.E0 + 2. * H2.E0,
                  C1sR21a_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefC111_e_CHx_2,
                 Name="C1s/{C.h}+2*H2 -> {C.h+H.f}+(3./2.)*H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)
# R21a by side: C.h + H.h -> CH.h
idrx.Plot.RxStepTS([C1sR21a_i.E0, C1sR21a_TS.E0, C1sR21a_f.E0],
                   Ref=RefC111_e_CHx_2,
                   Name='C1s/R21a by bridge: C.h+H.h->CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- *C.h+H2 -(top)-> *CH.h
# principal

idrx.Plot.RxStep([C1s_Ch.E0 + 2. * H2.E0,
                  C1sR21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefC111_e_CHx,
                 Name="C1s/{C.h}+2*H2 -> {C.h+H.f}+(3/2)*H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)
# R21b on top: C.h + H.f -> CH.h
idrx.Plot.RxStepTS([C1sR21_i.E0, C1sR21_TS.E0, C1sR21_f.E0],
                   Ref=RefC111_e_CHx,
                   Name='C1s/R21(top): C.h+H.f->CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH+H -> CH2

# Jump C/ R21 -> R9
idrx.Plot.RxStep([C1sR21_f.E0 + (3. / 2.) * H2.E0,
                  C1sR9_i.E0 + H2.E0],
                 Ref=RefC111_e_CHx,
                 Name='C1s/{CH.h}+(3/2)*H2->{CH.h+H.f}+H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R9: CH.h + H.f -> CH2.h
idrx.Plot.RxStepTS([C1sR9_i.E0, C1sR9_TS.E0, C1sR9_f.E0],
                   Ref=RefC111_e_CHx,
                   Name='C11s/R9 on top: CH.h + H.f -> CH2.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH2+H -> CH3

# Jump C/ R9 -> R10
idrx.Plot.RxStep([C1sR9_f.E0 + H2.E0,
                  C1sR10_i.E0 + .5 * H2.E0],
                 Ref=RefC111_e_CHx,
                 Name='C1s/{CH2.h}+H2->{CH2.h+H.f}+(1/2)H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R10: CH2.h + H.f -> CH3.h
idrx.Plot.RxStepTS([C1sR10_i.E0, C1sR10_TS.E0, C1sR10_f.E0],
                   Ref=RefC111_e_CHx,
                   Name='C1s/R10: CH2.h + H.f -> CH3.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH3+H -> CH4

# Jump C/ R10 -> R11
idrx.Plot.RxStep([C1sR10_f.E0 + .5 * H2.E0,
                  C1sR11_i.E0],
                 Ref=RefC111_e_CHx,
                 Name='C1s/{CH3.h}+(1/2)H2->{CH2.h+H.f}',
                 Hover=HoverList, Color="k", **Jump_Line_Props)
# R11: CH3.h + H.f -> CH4.g
idrx.Plot.RxStepTS([C1sR11_i.E0, C1sR11_TS.E0, C1sR11_f.E0],
                   Ref=RefC111_e_CHx,
                   Name='C1s/R11: CH3.h + H.f -> CH4.g',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Physisorption
idrx.Plot.RxStep([C1sR11_f.E0, CH4_g.E0 + C111s.E0],
                 Ref=RefC111_e_CHx,
                 Name='C1s/R11 {}CH4->{}+CH4g',
                 Hover=HoverList, Color="k", **{**Main_Line_Props, 'StepSpan':.4})

# Jump Test whole path
# if ShowGlobal_e:
#     RefC111_e_full = RefC111_e.branch(Step=0)
#     stg.Plot.RxStep([C1s_Ch.E0 + 2 * H2.E0, C111s.E0 + CH4_g.E0],
#                      Ref=RefC111_e_full, Name='C1s/{C.hN+H.f}+2*H2->{}+CH4g',
#                      Hover=HoverList, StepSpan=2.4, Color='c', **LineProps)
#     RefC111_e_full.PlotExtend(Until=11, Color="c")

SectionRefs_C111e.UpdateFromTail(RefC111_e_CHx)
idrx.Plot.AnnotateStepAxis(['$CH_{x}$', '$CH_{4(g)}$'], Ref=SectionRefs_C111e, Colour="k")
idrx.Plot.Align_Rx_Ticks(SectionRefs_C111e, TSmode=False)



# ----------------------------------------------------------------------------------------------------------------------
# Cobalt-Nickel ----------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Electronic - CoNi(111s)')
plt.axes(axs[0][1])
plt.title('Reaction profile $\longrightarrow$')



# .....................................
# CO2 series ..........................
# .....................................

RefCN111_e_CO2 = RefCN111_e.branch()

# ads
idrx.Plot.RxStep([CO2.E0 + CN111s.E0, CN1sR23_i.E0],
                 Ref=RefCN111_e_CO2,
                 Name='CN1s/(CO2)+{} -> {CO2.tCtC}',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# CN/R23 CO
idrx.Plot.RxStepTS([CN1sR23_i.E0, CN1sR23_d.E0, CN1sR23_f.E0],
                   Ref=RefCN111_e_CO2,
                   Name="CN1s/R23-d CO2.tCtC -> CO.tC + O.hC",
                   Hover=HoverList, Color='k', **{**Main_Line_Props, "StepSpan": 1.})

# Section
SectionRefs_CN111e.UpdateFromTail(RefCN111_e_CO2)
idrx.Plot.AnnotateStepAxis(['$CO_{2}$',''], Ref=RefCN111_e_CO2, Colour='k')



# .....................................
# CO desorbs ..........................
# .....................................
RefCN111_e_CO_desorb = RefCN111_e_CO2.branch()
# RefCN111_e_CO.PlotExtend(Until=3., Color='m', Alpha=1, LineWidth=.8)

# -------------------------------- ruta 1: O+H/C

# Separate/ {CO.tC + O.hC} + 1/2(H2) + {} -> {CO.tC} + {O+H/R13.2C}
idrx.Plot.RxStep([CN1sR23_f.E0 + 0.5 * H2.E0 + CN111s.E0, CN1sR17bCN_i.E0 + CN1sR132C_i.E0],
                 Ref=RefCN111_e_CO_desorb,
                 Name="CN/{CO.tC + O.hC} + 1/2(H2) + {} -> {CO.tC} + {O.fN + H.fN}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# CO desorption
idrx.Plot.RxStep([CN1sR17bCN_i.E0, COg.E0 + CN111s.E0],
                 Ref=RefCN111_e_CO_desorb,
                 Name="CO desorb",
                 Hover=HoverList, Color='m', **Main_Line_Props_CO)









# .....................................
# CO series ...........................
# .....................................
RefCN111_e_CO = RefCN111_e_CO2.branch()
# RefCN111_e_CO.PlotExtend(Until=3., Color='m', Alpha=1, LineWidth=.8)

# -------------------------------- ruta 1: O+H/C

# Separate/ {CO.tC + O.hC} + 1/2(H2) + {} -> {CO.tC} + {O+H/R13.2C}
idrx.Plot.RxStep([CN1sR23_f.E0 + 0.5 * H2.E0 + CN111s.E0, CN1sR17bCN_i.E0 + CN1sR132C_i.E0],
                 Ref=RefCN111_e_CO,
                 Name="CN/{CO.tC + O.hC} + 1/2(H2) + {} -> {CO.tC} + {O.fN + H.fN}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination (C) (branched out)
idrx.Plot.RxStepTS([CN1sR132C_i.E0, CN1sR132C_d.E0, CN1sR132C_f.E0],
                   Ref=RefCN111_e_CO, UpdateRef=False,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN/R17bCN CO.tC -> C.hN + O.hN
idrx.Plot.RxStepTS([CN1sR17bCN_i.E0, CN1sR17bCN_d.E0, CN1sR17bCN_f.E0],
                   Ref=RefCN111_e_CO,
                   Name="CN/R17bCN CO.tC -> C.hN + O.hN",
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separate/ {C.hN+O.hN} + 1/2(H2) + {} -> {C.hN (C) } + {O.hN+H.hN}
idrx.Plot.RxStep([CN1sR17bCN_f.E0 + 0.5 * H2.E0 + CN111s.E0, CN1s_ChN.E0 + CN1sR132C_i.E0],
                 Ref=RefCN111_e_CO,
                 Name="CN/ {C.hN+O.hN} + {H.fN} -> {(C)C.hN+H.hN} + {(C)O.hN+H.hN}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination (C)
idrx.Plot.RxStepTS([CN1sR132C_i.E0, CN1sR132C_d.E0, CN1sR132C_f.E0],
                   Ref=RefCN111_e_CO,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# Section
SectionRefs_CN111e.UpdateFromTail(RefCN111_e_CO)
idrx.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_CN111e, Colour="r")


# .....................................
# HCO series ..........................
# .....................................
RefCN111_e_HCO = RefCN111_e_CO2.branch()
RefCN111_e_HCO.PlotExtend(Until=5, Color='m', Alpha=1, LineWidth=.8)

# ------------------------------------------------ Ruta HCO.hNbOC
RefCN111_e_HCOb = RefCN111_e_HCO.branch()

# Separe/ {CO.tC + O.hC} + (H2) + {} -> {(R5b) CO.hN + H.fN} + {(R13.2C) O.fN+H.hN}
idrx.Plot.RxStep([CN1sR23_f.E0 + H2.E0 + CN111s.E0, CN1sR5b_i.E0 + CN1sR132C_i.E0],
                 Ref=RefCN111_e_HCOb,
                 Name="{CO.tC + O.hC} +(H2) + {} -> {(R5b) CO.hN + H.fN} + {(R13.2C) O.fN+H.hN}",
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination (C) (branched out)
idrx.Plot.RxStepTS([CN1sR132C_i.E0, CN1sR132C_d.E0, CN1sR132C_f.E0],
                   Ref=RefCN111_e_HCOb, UpdateRef=False,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN/R5 CO.hN + H.fN -> HCO.hNbOC
idrx.Plot.RxStepTS([CN1sR5b_i.E0, CN1sR5b_d.E0, CN1sR5b_f.E0],
                   Ref=RefCN111_e_HCOb,
                   Name="CN/R5 CO.hN + H.fN -> HCO.hNbOC",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# CN/R15 HCO.hNbOC -> CH.fC + O.fN
idrx.Plot.RxStepTS([CN1sR15C_i.E0, CN1sR15C_d.E0, CN1sR15C_f.E0],
                   Ref=RefCN111_e_HCOb,
                   Name="CN/R15 HCO.hNbOC -> CH.fC + O.fN",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe CN/{CH.fC + O.fN} + 1/2(H2) + {} -> {(R21)CH.hN}  + {(R13.2C) O.fN+H.hN}
idrx.Plot.RxStep([CN1sR15C_f.E0 + 0.5*H2.E0 + CN111s.E0, CN1sR21C_f.E0 + CN1sR132C_i.E0],
                 Ref=RefCN111_e_HCOb,
                 Name="CN/{CH.fC + O.fN} + {H.hN} -> {(R21)CH.hN}  + {(R13.2C) O.fN+H.hN}",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# OH elimination (C)
idrx.Plot.RxStepTS([CN1sR132C_i.E0, CN1sR132C_d.E0, CN1sR132C_f.E0],
                   Ref=RefCN111_e_HCOb,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# ------------------------------------------------ Ruta HCO.tCtC (secundaria)
RefCN111_e_HCOt = RefCN111_e_HCO.branch()

# Separe CN/ {CO.tC + O.hC} + H2 + {} -> {CO.hN + H.fN}+{(R13.2C) O.fN+H.hN}
idrx.Plot.RxStep([CN1sR23_f.E0 + H2.E0 + CN111s.E0, CN1sR5bt_i.E0 + CN1sR132C_i.E0],
                 Ref=RefCN111_e_HCOt,
                 Name="CN/ {CO.tC + O.hC} + 2*{H.fN} -> {CO.hN + H.fN}+{(R13.2C) O.fN+H.hN} + {}",
                 Hover=HoverList, Color="c", **Jump_Line_Props)

# OH elimination (C) (branched out)
idrx.Plot.RxStepTS([CN1sR132C_i.E0, CN1sR132C_d.E0, CN1sR132C_f.E0],
                   Ref=RefCN111_e_HCOt, UpdateRef=False,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN/R5bt CO.hN + H.fN -> HCO.tCtC
idrx.Plot.RxStepTS([CN1sR5bt_i.E0, CN1sR5bt_d.E0, CN1sR5bt_f.E0],
                   Ref=RefCN111_e_HCOt,
                   Name="CN/R5 CO.hN + H.fN -> HCO.tCtC",
                   Hover=HoverList, Color="c", **Main_Line_Props)

# CN/R15 HCO.tCtC -> CH.fC + O.fN
idrx.Plot.RxStepTS([CN1sR15tCtC_i.E0, CN1sR15tCtC_d.E0, CN1sR15tCtC_f.E0],
                   Ref=RefCN111_e_HCOt,
                   Name="CN/R15 HCO.tCtC -> CH.fC + O.fN",
                   Hover=HoverList, Color="c", **Main_Line_Props)

# Compile Refs
RefCN111_e_HCO.UpdateFromTail(RefCN111_e_HCOb)
SectionRefs_CN111e.UpdateFromTail(RefCN111_e_HCO)
idrx.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_CN111e, Colour="g")



# .....................................
# COH series ..........................
# .....................................
RefCN111_e_COH = RefCN111_e_CO2.branch()
RefCN111_e_COH.PlotExtend(Until=8.5, Color='m', Alpha=1, LineWidth=.8)


# Separe CN/{(R23-f)CO.tC + O.hC}+ H2 + {} -> {(R6)CO.hN + H.fN}+{(R13.2C)O.fN+H.hN}
idrx.Plot.RxStep([CN1sR23_f.E0 + H2.E0 + CN111s.E0, CN1sR6_i.E0 + CN1sR132C_i.E0],
                 Ref=RefCN111_e_COH,
                 Name="CN/{(R23-f)CO.tC + O.hC}+(H2)+{} -> {(R6)CO.hN + H.fN}+{(R13.2C)O.fN+H.hN}",
                 Hover=HoverList, Color='m', **Jump_Line_Props)

# OH elimination (C) (branched out)
idrx.Plot.RxStepTS([CN1sR132C_i.E0, CN1sR132C_d.E0, CN1sR132C_f.E0],
                   Ref=RefCN111_e_COH, UpdateRef=False,
                   Name="CN1s/R13.2C-i O.fN+H.hN -(C)-> OH.fN",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN/R6C CO.hN + H.fN -(C)-> COH.hN
idrx.Plot.RxStepTS([CN1sR6_i.E0, CN1sR6_d.E0, CN1sR6_f.E0],
                   Ref=RefCN111_e_COH,
                   Name="CN/R6C CO.hN + H.fN -(C)-> COH.hN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# CN/R16C COH.hNtC -> C.hN + OH.fN
idrx.Plot.RxStepTS([CN1sR16C_i.E0, CN1sR16C_d.E0, CN1sR16C_f.E0],
                   Ref=RefCN111_e_COH,
                   Name="CN/R16C COH.hNtC -> C.hN + OH.fN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separa CN/{(R16C-f)C.hN+OH.fN}+ {} -> {(R21C) C.hN+H.fN} + {(R13.2C-f) OH.fN}
idrx.Plot.RxStep([CN1sR16C_f.E0 + CN111s.E0, CN1s_ChN.E0 + CN1sR132C_f.E0],
                 Ref=RefCN111_e_COH,
                 Name="CN/{(R16C-f)C.hN+OH.fN}+ {} -> {(R21C) C.hN} + {(R13.2C-f) OH.fN}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# Section
SectionRefs_CN111e.UpdateFromTail(RefCN111_e_COH)
idrx.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_CN111e, Colour="m")





# .....................................
# CHx series ..........................
# .....................................
RefCN111_e_CO.PlotExtend(Until=11.5, Color='r')
RefCN111_e_HCO.PlotExtend(Until=12.5 + .4, Color='g')
RefCN111_e_COH.PlotExtend(Until=11.5, Color='m')

# RefCN111_e_CHx = RefCN111_e.branch()
# RefCN111_e_CHx.PlotExtend(Until=12., Color='m', Alpha=1, LineWidth=.8)

RefCN111_e_CHx = RefCN111_e_COH.branch()

# ---- C.hN+H.fN -(bCN)-> CH.hN
# rama terciaria
RefCN111_e_CHx_3 = RefCN111_e_CHx.branch()

idrx.Plot.RxStep([CN1s_ChN.E0 + 2. * H2.E0,
                  CN1sR21b_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN111_e_CHx_3,
                 Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R21 - bridge CN : C.hN + H.hN -> CH.hN
idrx.Plot.RxStepTS([CN1sR21b_i.E0, CN1sR21b_TS.E0, CN1sR21b_f.E0],
                   Ref=RefCN111_e_CHx_3,
                   Name='CN1s/R21 bridge CN: C.hN+H.hN->CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- C.hN+H.fN -(N)-> CH.hN
# rama secundaria
RefCN111_e_CHx_2 = RefCN111_e_CHx.branch()

idrx.Plot.RxStep([CN1s_ChN.E0 + 2. * H2.E0,
                  CN1sR21N_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN111_e_CHx_2,
                 Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R21 - N : C.hN + H.fN -> CH.hN
idrx.Plot.RxStepTS([CN1sR21N_i.E0, CN1sR21N_TS.E0, CN1sR21N_f.E0],
                   Ref=RefCN111_e_CHx_2,
                   Name='CN1s/R21 on top N: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- C.hN+H.fN -(C)-> CH.hN
# rama principal

idrx.Plot.RxStep([CN1s_ChN.E0 + 2. * H2.E0,
                  CN1sR21C_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN111_e_CHx,
                 Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R21 - C : C.hN + H.fN -> CH.hN
idrx.Plot.RxStepTS([CN1sR21C_i.E0, CN1sR21C_TS.E0, CN1sR21C_f.E0],
                   Ref=RefCN111_e_CHx,
                   Name='CN1s/R21 on top C: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH+H -> CH2

# Jump CN/ R21C -> R9C
idrx.Plot.RxStep([CN1sR21C_f.E0 + (3. / 2.) * H2.E0,
                  CN1sR9C_i.E0 + H2.E0],
                 Ref=RefCN111_e_CHx,
                 Name='CN1s/{CH.hN}+(3/2)H2->{CH.hN+H.fN}+H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R9C: CH.hN + H.fN -> CH2.hNtC
idrx.Plot.RxStepTS([CN1sR9C_i.E0, CN1sR9C_TS.E0, CN1sR9C_f.E0],
                   Ref=RefCN111_e_CHx,
                   Name='CN1s/R9C: CH.hN + H.fN -> CH2.hNtC',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH2+H -> CH3

# Jump CN/ R9C -> R10C
idrx.Plot.RxStep([CN1sR9C_f.E0 + H2.E0,
                  CN1sR10C_i.E0 + .5 * H2.E0],
                 Ref=RefCN111_e_CHx,
                 Name='CN1s/{CH2.hNtC}+H2->{CH2.hNtC+H.fN}+(1/2)H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R10C: CH2.hNtC + H.fN -> CH3.hN
idrx.Plot.RxStepTS([CN1sR10C_i.E0, CN1sR10C_TS.E0, CN1sR10C_f.E0],
                   Ref=RefCN111_e_CHx,
                   Name='CN1s/R10C: CH2.hNtC + H.fN -> CH3.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH3+H -(N)-> CH4
# Secundario
RefCN111_e_CHx_4 = RefCN111_e_CHx.branch()

# Jump CN/ R10C -> R11N
idrx.Plot.RxStep([CN1sR10C_f.E0 + .5 * H2.E0,
                  CN1sR11N_i.E0],
                 Ref=RefCN111_e_CHx_4,
                 Name='CN1s/{CH3.hN}+(1/2)*H2->{CH3.hN+H.fN}',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R11N: CH3.hN + H.fN -> CH4.g
idrx.Plot.RxStepTS([CN1sR11N_i.E0, CN1sR11N_TS.E0, CN1sR11N_f.E0],
                   Ref=RefCN111_e_CHx_4,
                   Name='CN1s/R11N CH3.hN + H.fN -> CH4g',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Physisorption
idrx.Plot.RxStep([CN1sR11N_f.E0,
                  CN111s.E0 + CH4_g.E0],
                 Ref=RefCN111_e_CHx_4,
                 Name='CN1s/{}CH4g->{}+CH4g',
                 Hover=HoverList, Color="k", **{**Main_Line_Props, 'StepSpan':.4})

# ---- CH3+H -(C)-> CH4
# principal

# Jump CN/ R10C -> R11C
idrx.Plot.RxStep([CN1sR10C_f.E0 + .5 * H2.E0,
                  CN1sR11C_i.E0],
                 Ref=RefCN111_e_CHx,
                 Name='CN1s/{CH3.hN}+(1/2)H2->{CH3.hN+H.fN}',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# R11C: CH3.hN + H.fN -> CH4.g
idrx.Plot.RxStepTS([CN1sR11C_i.E0, CN1sR11C_TS.E0, CN1sR11C_f.E0],
                   Ref=RefCN111_e_CHx,
                   Name='CN1s/R11C CH3.hN + H.fN -> CH4g',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# Physisorption
idrx.Plot.RxStep([CN1sR11C_f.E0,
                  CN111s.E0 + CH4_g.E0],
                 Ref=RefCN111_e_CHx,
                 Name='CN1s/{}CH4g->{}+CH4g',
                 Hover=HoverList, Color="k", **{**Main_Line_Props, 'StepSpan':.4})

# Jump Test whole path
# if ShowGlobal_e:
#     RefCN111_e_full = RefCN111_e.branch(Step=0)
#     stg.Plot.RxStep([CN1s_ChN.E0 + 2 * H2.E0,
#                       CN111s.E0 + CH4_g.E0],
#                      Ref=RefCN111_e_full, Name='CN1s/{C.hN+H.hN}+2*H2->{}+CH4g',
#                      Hover=HoverList, StepSpan=2.4, Color='k', **LineProps)
#     RefCN111_e_full.PlotExtend(Until=11., Color="m", **LineProps)


SectionRefs_CN111e.UpdateFromTail(RefCN111_e_CHx)
idrx.Plot.AnnotateStepAxis(['$CH_{x}$', '$CH_{4(g)}$'], Ref=SectionRefs_CN111e, Colour="k")
idrx.Plot.Align_Rx_Ticks(SectionRefs_CN111e, TSmode=False)


########################################################################################################################
########################################################################################################################
########################################################################################################################
# (100) ----------------------------------------------------------------------------------------------------------------

# References
RefN100_e = idrx.Plot.RxRef(0., 0.)
RefC100_e = idrx.Plot.RxRef(0., 0.)
RefCN100_e = idrx.Plot.RxRef(0., 0.)

# Place holders
SectionRefs_N100e = RefN100_e.branch()
SectionRefs_C100e = RefC100_e.branch()
SectionRefs_CN100e = RefCN100_e.branch()




# ----------------------------------------------------------------------------------------------------------------------
# Nickel ---------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Electronic - Ni(100)')
plt.axes(axs[1][2])



# .....................................
# CO2 series ..........................
# .....................................
RefN100_e_CO2 = RefN100_e.branch()

# ads
idrx.Plot.RxStep([CO2.E0 + N100.E0, N10R23_1_i.E0],
                 Ref=RefN100_e_CO2,
                 Name='N100/(CO2)+{} -> {CO2.hbh}',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# N/ {CO2.bhb} -> {CO.b + O.h} (R32.1)
idrx.Plot.RxStepTS([N10R23_1_i.E0, N10R23_1_d.E0, N10R23_1_f.E0],
                   Ref=RefN100_e_CO2,
                   Name='N/R23.1 CO2.bhb->CO.b+O.h',
                   Hover=HoverList, Color='k', **{**Main_Line_Props, "StepSpan": 1.})


# section
SectionRefs_N100e.UpdateFromTail(RefN100_e_CO2)
idrx.Plot.AnnotateStepAxis(['$CO_{2}$',''], Ref=SectionRefs_N100e, Colour='k')


# .....................................
# CO desorb ...........................
# .....................................
RefN100_e_CO_des = RefN100_e_CO2.branch()

# Separe/ {CO.b+O.h} + 1/2(H2) + {} -> {CO.h}+{O.h+H.hd} (Split R23.1 -> R17, R13.2)
idrx.Plot.RxStep([N10R23_1_f.E0 + 0.5 * H2.E0 + N100.E0, N10R17_i.E0 + N10R13_2_i.E0],
                 Ref=RefN100_e_CO_des,
                 Name='N/{CO.b+O.h}+1/2(H2)+{} -> {CO.h}+{O.h+H.hd}',
                 Hover=HoverList, Color='r', **Jump_Line_Props)
# CO desorbs
idrx.Plot.RxStep([N10R17_i.E0, N100.E0 + COg.E0],
                 Ref=RefN100_e_CO_des,
                 Name='CO desorbs',
                 Hover=HoverList, Color='m', **Main_Line_Props_CO)






# .....................................
# CO series ...........................
# .....................................
RefN100_e_CO = RefN100_e_CO2.branch()

# Separe/ {CO.b+O.h} + 1/2(H2) + {} -> {CO.h}+{O.h+H.hd} (Split R23.1 -> R17, R13.2)
idrx.Plot.RxStep([N10R23_1_f.E0 + 0.5 * H2.E0 + N100.E0, N10R17_i.E0 + N10R13_2_i.E0],
                 Ref=RefN100_e_CO,
                 Name='N/{CO.b+O.h}+1/2(H2)+{} -> {CO.h}+{O.h+H.hd}',
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination {O.h+H.hd} -> {OH.h} (R13.2) (branched out)
idrx.Plot.RxStepTS([N10R13_2_i.E0, N10R13_2_d.E0, N10R13_2_f.E0],
                   Ref=RefN100_e_CO, UpdateRef=False,
                   Name='R13.2 O.h + H.hd -> OH.h',
                   Hover=HoverList, Color='b', **OH_Line_Props)

# N/ {CO.h} -> {C.h+O.h} (R17)
idrx.Plot.RxStepTS([N10R17_i.E0, N10R17_d.E0, N10R17_f.E0],
                   Ref=RefN100_e_CO,
                   Name='N/R17 CO.h->C.h+O.h',
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separe/ {C+O}+1/2(H2) + {}->{C.h}+{O+H} (Split R17->R21, R13.2)
idrx.Plot.RxStep([N10R17_f.E0 + 0.5 * H2.E0 + N100.E0, N100_Ch.E0 + N10R13_2_i.E0],
                 Ref=RefN100_e_CO,
                 Name='N/{C.h+O.h}+1/2(H2)+{} -> {C.h}+{O.h+H.hd}',
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([N10R13_2_i.E0, N10R13_2_d.E0, N10R13_2_f.E0],
                   Ref=RefN100_e_CO,
                   Name='R13.2 O.h + H.hd -> OH.h',
                   Hover=HoverList, Color='b', **OH_Line_Props)


# Section
SectionRefs_N100e.UpdateFromTail(RefN100_e_CO)
idrx.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_N100e, Colour="r")


# .....................................
# HCO series ..........................
# .....................................
RefN100_e_HCO = RefN100_e_CO2.branch()
RefN100_e_HCO.PlotExtend(Until=5, Color='r')


# Separe {CO.b + O.h} + H2 + {} -> {CO.h + H.hd} + {O.h + H.hd} (Split R23.1 -> R5, R13.2)
idrx.Plot.RxStep([N10R23_1_f.E0 + H2.E0 + N100.E0, N10R5_i.E0 + N10R13_2_i.E0],
                 Ref=RefN100_e_HCO,
                 Name='N/{CO.b+O.h}+(H2)+{} -> {CO.h+H.hd}+{O.h+H.hd}',
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination {O.h + H.hd} -> {OH.h} (R13.2) (branched out)
idrx.Plot.RxStepTS([N10R13_2_i.E0, N10R13_2_d.E0, N10R13_2_f.E0],
                   Ref=RefN100_e_HCO, UpdateRef=False,
                   Name='R13.2 O.h + H.hd -> OH.h',
                   Hover=HoverList, Color='b', **OH_Line_Props)

# N/ {CO.h + H.hd} -> {HCO.bb} (R5)
idrx.Plot.RxStepTS([N10R5_i.E0, N10R5_d.E0, N10R5_f.E0],
                   Ref=RefN100_e_HCO,
                   Name='N/R5: CO.h+H.hd->HCO.bb',
                   Hover=HoverList, Color='g', **Main_Line_Props)

# N/ {HCO.bb} -> {CH.h + O.h}} (R15)
idrx.Plot.RxStepTS([N10R15_i.E0, N10R15_d.E0, N10R15_f.E0],
                   Ref=RefN100_e_HCO,
                   Name='N/R15: HCO.bb->CH.h+O.hd',
                   Hover=HoverList, Color='g', **Main_Line_Props)

# Separe {CH.h + O.h} + 1/2(H2) + {} -> {CH.h} + {OH.h}
idrx.Plot.RxStep([N10R15_f.E0 + 0.5*H2.E0 + N100.E0, N10R21_f.E0 + N10R13_2_i.E0],
                 Ref=RefN100_e_HCO,
                 Name='N/{CH.b+O.hd}+1/2(H2)+{} -> {CH.h}+{OH.h}',
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination {O.h + H.hd} -> {OH.h} (R13.2)
idrx.Plot.RxStepTS([N10R13_2_i.E0, N10R13_2_d.E0, N10R13_2_f.E0],
                   Ref=RefN100_e_HCO,
                   Name='R13.2 O.h + H.hd -> OH.h',
                   Hover=HoverList, Color='b', **OH_Line_Props)

# Name and tick
SectionRefs_N100e.UpdateFromTail(RefN100_e_HCO)
idrx.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_N100e, Colour="g")




# .....................................
# COH series ..........................
# .....................................
RefN100_e_COH = RefN100_e_CO2.branch()
RefN100_e_COH.PlotExtend(Until=8.5, Color='r')


# Separe/ {CO.b + O.h} + H2 + {} -> {CO.h + H.hd} + {O.h + H.hd} (Split R23.1 -> R6,R13.2)
idrx.Plot.RxStep([N10R23_1_f.E0 + H2.E0 + N100.E0, N10R6_i.E0 + N10R13_2_i.E0],
                 Ref=RefN100_e_COH,
                 Name='N/{CO.b+O.h}+(H2)+{} -> {CO.h+H.hd}+{O.h+H.hd}',
                 Hover=HoverList, Color='m', **Jump_Line_Props)

# OH elimination {O.h + H.hd} -> {OH.h} (R13.2) (branched out)
idrx.Plot.RxStepTS([N10R13_2_i.E0, N10R13_2_d.E0, N10R13_2_f.E0],
                   Ref=RefN100_e_COH, UpdateRef=False,
                   Name='R13.2 O.h + H.hd -> OH.h',
                   Hover=HoverList, Color='b', **OH_Line_Props)

# N/R6 {CO.h + H.hd} -> {COH.h} (R6)
idrx.Plot.RxStepTS([N10R6_i.E0, N10R6_d.E0, N10R6_f.E0],
                   Ref=RefN100_e_COH,
                   Name='N/R6: CO.h+H.hd->COH.ht',
                   Hover=HoverList, Color='m', **Main_Line_Props)

# N/R16 {COH.ht} -> {C.h + OH.hd} (R16)
idrx.Plot.RxStepTS([N10R16_i.E0, N10R16_d.E0, N10R16_f.E0],
                   Ref=RefN100_e_COH,
                   Name='N/R16: COH.ht->C.h+OH.hd',
                   Hover=HoverList, Color='m', **Main_Line_Props)

# Separe/ {C.h + OH.h} + {} -> {C.h + H.hd} + {OH.h} (R16 -> R21, R13.2)
idrx.Plot.RxStep([N10R16_f.E0 + N100.E0, N100_Ch.E0 + N10R13_2_f.E0],
                 Ref=RefN100_e_COH,
                 Name='{C.h + OH.h} + {} -> {C.h} + {OH.h}',
                 Hover=HoverList, Color='m', **Jump_Line_Props)

# Name and tick
SectionRefs_N100e.UpdateFromTail(RefN100_e_COH)
idrx.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_N100e, Colour="m")






# .....................................
# CHx series ..........................
# .....................................
RefN100_e_CO.PlotExtend(Until=11.5, Color='r')
RefN100_e_HCO.PlotExtend(Until=12.5+.4, Color='g')
RefN100_e_COH.PlotExtend(Until=11.5, Color='m')

RefN100_e_CHx = RefN100_e_COH.branch()
# RefN100_e_CHx.PlotExtend(Until=14., Color='m', Alpha=1, LineWidth=.8)


# ---- C.h + H2 -> CH.h
idrx.Plot.RxStep([N100_Ch.E0 + 2 * H2.E0,
                  N10R21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefN100_e_CHx,
                 Name="N/{C.h}+2*H2 -> {C.h +H.h}+(3/2)H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)
# N/R21 C.h+H.f->CH
idrx.Plot.RxStepTS([N10R21_i.E0, N10R21_d.E0, N10R21_f.E0],
                   Ref=RefN100_e_CHx,
                   Name='N/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH-CH2

# Jump C/ R21 -> R9
idrx.Plot.RxStep([N10R21_f.E0 + (3. / 2.) * H2.E0,
                  N10R9_i.E0 + H2.E0],
                 Ref=RefN100_e_CHx,
                 Name='N/{CH.h}+(3/2)H2->{CH.h+H.h}+H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# N/R9 CH.h+H.f->CH2.hb
idrx.Plot.RxStepTS([N10R9_i.E0, N10R9_d.E0, N10R9_f.E0],
                   Ref=RefN100_e_CHx,
                   Name='N/R9: CH.h + H.h -> CH2.hb',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH2-CH3

# Jump C/ R9 -> R10
idrx.Plot.RxStep([N10R9_f.E0 + H2.E0,
                  N10R10_i.E0 + .5 * H2.E0],
                 Ref=RefN100_e_CHx,
                 Name='N/{CH2.hb}+H2 -> {CH2.hb+H.hd}+(1/2)H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)
# N/R10 CH2.hb+H.f->CH3.b3
idrx.Plot.RxStepTS([N10R10_i.E0, N10R10_d.E0, N10R10_f.E0],
                   Ref=RefN100_e_CHx,
                   Name='N/R10: CH2.hb + H.h -> CH3.b3',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH3-CH4

# Jump C/ R10 -> R11
idrx.Plot.RxStep([N10R10_f.E0 + .5 * H2.E0,
                  N10R11_i.E0],
                 Ref=RefN100_e_CHx,
                 Name='N/{CH3.b}+(1/2)H2->{CH3.hb+H.hd}',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# N/R11 CH3.hb + H.hd -> CH4.g
idrx.Plot.RxStepTS([N10R11_i.E0, N10R11_TS.E0, N10R11_f.E0],
                   Ref=RefN100_e_CHx,
                   Name='N/R11: CH3.hb + H.hd -> CH4.g',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- Physisorption
idrx.Plot.RxStep([N10R11_f.E0, N100.E0 + CH4_g.E0],
                 Ref=RefN100_e_CHx,
                 Name='N/{}CH4g->{}+CH4g',
                 Hover=HoverList, Color="k", **{**Main_Line_Props, 'StepSpan':.4})

# Jump Test complete series
# if ShowGlobal_e:
#     RefN_e_2 = RefN100_e.branch(Step=0)
#     stg.Plot.RxStep([N100_Ch.E0 + 2 * H2.E0,
#                       N100.E0 + CH4_g.E0], Ref=RefN_e_2, Name='{C.h+H.h}+2*H2->{}+CH4g',
#                      Hover=HoverList, StepSpan=4.4, **LineProps, Color="orange")
#     RefN_e_2.PlotExtend(Until=11, Color="orange", **LineProps)

SectionRefs_N100e.UpdateFromTail(RefN100_e_CHx)
idrx.Plot.AnnotateStepAxis(['$CH_{x}$', '$CH_{4(g)}$'], Ref=SectionRefs_N100e, Colour="k")
idrx.Plot.Align_Rx_Ticks(SectionRefs_N100e, TSmode=False)

# ----------------------------------------------------------------------------------------------------------------------
# Cobalt ---------------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Electronic - Co(100)')
plt.axes(axs[1][0])



# .....................................
# CO2 series ..........................
# .....................................
RefC100_e_CO2 = RefC100_e.branch()

# ads
idrx.Plot.RxStep([CO2.E0+C100.E0, C10R23_i.E0],
                 Ref=RefC100_e_CO2,
                 Name='C100/(CO2)+{} --> {CO2}',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

idrx.Plot.RxStepTS([C10R23_i.E0, C10R23_d.E0, C10R23_f.E0],
                   Ref=RefC100_e_CO2,
                   Name='C/R23d CO2 -> CO.t + O.h',
                   Hover=HoverList, Color='k', **{**Main_Line_Props, "StepSpan": 1.})
# Section
SectionRefs_C100e.UpdateFromTail(RefC100_e_CO2)
idrx.Plot.AnnotateStepAxis(['$CO_{2}$',''], Ref=SectionRefs_C100e, Colour='k')




# .....................................
# CO desorbs  .........................
# .....................................
RefC100_e_CO_des = RefC100_e_CO2.branch()


# Separe/ {CO.t+O.h}+1/2(H2)+{}->{CO.t}+{O.h+H.h} (split R23->R17, R13.2)
idrx.Plot.RxStep([C10R23_f.E0 + 0.5 * H2.E0 + C100.E0, C10R17t_i.E0 + C10R132_i.E0],
                 Ref=RefC100_e_CO_des,
                 Name='C/{CO.t+O.h}+{H.h}->{CO.t}+{O.h+H.d}',
                 Hover=HoverList, Color='r', **Jump_Line_Props)
# CO desorbs
idrx.Plot.RxStep([C10R17t_i.E0, COg.E0+C100.E0],
                 Ref=RefC100_e_CO_des,
                 Name='CO desorbs',
                 Hover=HoverList, Color='m', **Main_Line_Props_CO
                 )






# .....................................
# CO series ...........................
# .....................................
RefC100_e_CO = RefC100_e_CO2.branch()


# Separe/ {CO.t+O.h}+1/2(H2)+{}->{CO.t}+{O.h+H.h} (split R23->R17, R13.2)
idrx.Plot.RxStep([C10R23_f.E0 + 0.5 * H2.E0 + C100.E0, C10R17t_i.E0 + C10R132_i.E0],
                 Ref=RefC100_e_CO,
                 Name='C/{CO.t+O.h}+{H.h}->{CO.t}+{O.h+H.d}',
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination {O.h+H.hd} -> {OH.h} (R13.2) (branched out)
idrx.Plot.RxStepTS([C10R132_i.E0, C10R132_d.E0, C10R132_f.E0],
                   Ref=RefC100_e_CO, UpdateRef=False,
                   Name="C/R13.2: O.h + H.h -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# C/{CO.t} -> {C.h + O.h} (R17t)
idrx.Plot.RxStepTS([C10R17t_i.E0, C10R17t_d.E0, C10R17t_f.E0],
                   Ref=RefC100_e_CO,
                   Name='C/R17.1d CO.t -> C.h + O.h',
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separe/ {C.h+O.h}+1/2(H2) + {} -> {C.h}+{O.h+H.h} (split R17-> R21, R13.2)
idrx.Plot.RxStep([C10R17t_f.E0 + 0.5 * H2.E0 + C100.E0, C100_Ch.E0 + C10R132_i.E0],
                 Ref=RefC100_e_CO,
                 Name='C/{C.h+O.h}+1/2(H2)+{} -> {C.h+H.h}+{O.h+H.h}',
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination {O.h+H.hd} -> {OH.h} (R13.2)
idrx.Plot.RxStepTS([C10R132_i.E0, C10R132_d.E0, C10R132_f.E0],
                   Ref=RefC100_e_CO,
                   Name="C/R13.2: O.h + H.h -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# Section
SectionRefs_C100e.UpdateFromTail(RefC100_e_CO)
idrx.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_C100e, Colour="r")



# .....................................
# HCO series ..........................
# .....................................
RefC100_e_HCO = RefC100_e_CO2.branch()
RefC100_e_HCO.PlotExtend(Until=5.0, Color='r')


# Separe/ {CO.t+O.h}+H2+{}->{CO.h + H.hd}+{O.h+H.h} (split R23->R5, R13.2)
idrx.Plot.RxStep([C10R23_f.E0 + H2.E0 + C100.E0, C10R5_i.E0 + C10R132_i.E0],
                 Ref=RefC100_e_HCO,
                 Name='C/{CO.t+O.h}+H2+{}->{CO.h+H.hd}+{O.h+H.hd}',
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination {O.h+H.hd} -> {OH.h} (R13.2)
idrx.Plot.RxStepTS([C10R132_i.E0, C10R132_d.E0, C10R132_f.E0],
                   Ref=RefC100_e_HCO, UpdateRef=False,
                   Name="C/R13.2: O.h + H.h -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# C/R5 CO.h+H.hd -> HCO.bb
idrx.Plot.RxStepTS([C10R5_i.E0, C10R5_d.E0, C10R5_f.E0],
                   Ref=RefC100_e_HCO,
                   Name="C/R5 CO.h+H.hd -> HCO.bb",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# C/R15 HCO.bb -(split)-> CH.h + O.h
idrx.Plot.RxStepTS([C10R15_i.E0, C10R15_d.E0, C10R15_f.E0],
                   Ref=RefC100_e_HCO,
                   Name="C/R15: HCO.bb -(split)-> CH.h + O.h",
                   Hover=HoverList, Color="g", **Main_Line_Props)

# Separe {CH.h +O.h} + 1/2(H2) + {} -> {CH.h} + {O.h + O.h}(R132)
idrx.Plot.RxStep([C10R15_f.E0 + 0.5 * H2.E0 + C100.E0, C10R21_f.E0 + C10R132_i.E0],
                 Ref=RefC100_e_HCO,
                 Name="C/{CH.h +O.h} + 1/2(H2) + {} -> {CH.h} + {O.h + H.h}(R132)",
                 Hover=HoverList, Color="g", **Jump_Line_Props)

# OH elimination
idrx.Plot.RxStepTS([C10R132_i.E0, C10R132_d.E0, C10R132_f.E0],
                   Ref=RefC100_e_HCO,
                   Name="C/R13.2: O.h + H.h -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# Section
SectionRefs_C100e.UpdateFromTail(RefC100_e_HCO)
idrx.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_C100e, Colour="g")



# .....................................
# COH series ..........................
# .....................................
RefC100_e_COH = RefC100_e_CO2.branch()
RefC100_e_COH.PlotExtend(Until=8.5, Color='r')


# Separe/ {CO.t+O.h}+H2+{}->{CO.h + H.hd}+{O.h+H.h} (split R23->R6, R13.2)
idrx.Plot.RxStep([C10R23_f.E0 + H2.E0 + C100.E0, C10R6_i.E0 + C10R132_i.E0],
                 Ref=RefC100_e_COH,
                 Name='C/{CO.t+O.h}+H2+{}->{CO.h+H.hd}+{O.h+H.hd}',
                 Hover=HoverList, Color='m', **Jump_Line_Props)

# OH elimination (branched out)
idrx.Plot.RxStepTS([C10R132_i.E0, C10R132_d.E0, C10R132_f.E0],
                   Ref=RefC100_e_COH, UpdateRef=False,
                   Name="C/R13.2: O.h + H.h -(t)-> OH.h",
                   Hover=HoverList, Color="b", **OH_Line_Props)

# C/R6 CO.h + H.h -> COH.ht
idrx.Plot.RxStepTS([C10R6_i.E0, C10R6_d.E0, C10R6_f.E0],
                   Ref=RefC100_e_COH,
                   Name="C/R6: CO.h + H.h -> COH.ht",
                   Hover=HoverList, Color='m', **Main_Line_Props)

# C/R16 COH.ht -(t)-> C.h + OH.hd
idrx.Plot.RxStepTS([C10R16_i.E0, C10R16_d.E0, C10R16_f.E0],
                   Ref=RefC100_e_COH,
                   Name="C/R16: COH.ht -(t)-> C.h + OH.hd",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separe {C.h + OH.hd} + {} -> {C.h} + {OH.h}
idrx.Plot.RxStep([C10R16_f.E0 + C100.E0, C100_Ch.E0 + C10R132_f.E0],
                 Ref=RefC100_e_COH,
                 Name="C/{C.h + OH.hd} + {} -> {C.h} + {OH.h}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# Section
SectionRefs_C100e.UpdateFromTail(RefC100_e_COH)
idrx.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_C100e, Colour="m")




# .....................................
# CHx series ..........................
# .....................................
RefC100_e_CO.PlotExtend(Until=11.5, Color='r')
RefC100_e_HCO.PlotExtend(Until=12.5+.4, Color="g")
RefC100_e_COH.PlotExtend(Until=11.5, Color="m")

RefC100_e_CHx = RefC100_e_CO.branch()
# RefC100_e_CHx.PlotExtend(Until=12., Color='m', Alpha=1, LineWidth=.8)

# ---- C.h + H.h -> CH.h

idrx.Plot.RxStep([C100_Ch.E0 + 2. * H2.E0,
                  C10R21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefC100_e_CHx,
                 Name="C100/{C.h}+2*H2 -> {C.h+H.h}+(3/2)*H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)
# C/R21 C.h+H.f->CH.h
idrx.Plot.RxStepTS([C10R21_i.E0, C10R21_d.E0, C10R21_f.E0],
                   Ref=RefC100_e_CHx,
                   Name='C/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH->CH2

# Jump C/ R21 -> R9
idrx.Plot.RxStep([C10R21_f.E0 + (3. / 2.) * H2.E0,
                  C10R9_i.E0 + H2.E0],
                 Ref=RefC100_e_CHx,
                 Name='C/{CH.h}+(3/2)*H2->{CH.h+H.h}+H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# C/R9 CH.h+H.f->CH2.hb
idrx.Plot.RxStepTS([C10R9_i.E0, C10R9_d.E0, C10R9_f.E0],
                   Ref=RefC100_e_CHx,
                   Name='C/R9: CH.h + H.h -> CH2.h',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH2->CH3

# Jump C/ R9 -> R10
idrx.Plot.RxStep([C10R9_f.E0 + H2.E0,
                  C10R10_i.E0 + .5 * H2.E0],
                 Ref=RefC100_e_CHx,
                 Name='C/{CH2.h}+H2->{CH2.h+H.hd}+(1/2)H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# C/R10 CH2.h + H.hd -> CH3.b3
idrx.Plot.RxStepTS([C10R10_i.E0, C10R10_d.E0, C10R10_f.E0],
                   Ref=RefC100_e_CHx,
                   Name='C/R10: CH2.h + H.hd -> CH3.b',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH3->CH4

# Jump C/ R10 -> R11
idrx.Plot.RxStep([C10R10_f.E0 + .5 * H2.E0,
                  C10R11_i.E0],
                 Ref=RefC100_e_CHx,
                 Name='C/{CH3.h}+{H.h}->{CH3.h+H.hd}',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# C/R11 CH3.b + H.hd -> CH4.g
idrx.Plot.RxStepTS([C10R11_i.E0, C10R11_TS.E0, C10R11_f.E0],
                   Ref=RefC100_e_CHx,
                   Name='C/R11: CH3.b + H.hd -> CH4.g',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- Physisorption
idrx.Plot.RxStep([C10R11_f.E0, C100.E0 + CH4_g.E0],
                 Ref=RefC100_e_CHx,
                 Name='C/{}CH4g->{}+CH4g',
                 Hover=HoverList, Color="k", **{**Main_Line_Props, 'StepSpan':.4})

# Jump test complete
# if ShowGlobal_e:
#     RefC100_e_full = RefC100_e.branch(Step=0)
#     stg.Plot.RxStep([C100_Ch.E0 + 2 * H2.E0,
#                       C100.E0 + CH4_g.E0],
#                      Ref=RefC100_e_full, Name='C/{C.h+H.h}+2*H2 -> {}+CH4g',
#                      Hover=HoverList, StepSpan=4.4, **LineProps)
#     RefC100_e_full.PlotExtend(Until=11., Color="gray", **LineProps)

SectionRefs_C100e.UpdateFromTail(RefC100_e_CHx)
idrx.Plot.AnnotateStepAxis(['$CH_{x}$', '$CH_{4(g)}$'], Ref=SectionRefs_C100e, Colour="k")
idrx.Plot.Align_Rx_Ticks(SectionRefs_C100e, TSmode=False)






# ----------------------------------------------------------------------------------------------------------------------
# Cobalt-Nickel --------------------------------------------------------------------------------------------------------
idrx.MinorSection('Adding steps to Plot: Electronic - CoNi(100)')
plt.axes(axs[1][1])



# .....................................
# CO2 series ..........................
# .....................................
RefCN100_e_CO2 = RefCN100_e.branch()

# ads
idrx.Plot.RxStep([CO2.E0+CN100.E0, CN10R23_i.E0],
                 Ref=RefCN100_e_CO2,
                 Name='CN100/(CO2)+{} -> {CO2.hNbb}',
                 Hover=HoverList, Color='k', **Jump_Line_Props)

# CN/R23 CO2.hNbb -(b)-> CO.bCN + O.hC
idrx.Plot.RxStepTS([CN10R23_i.E0, CN10R23_d.E0, CN10R23_f.E0],
                   Ref=RefCN100_e_CO2,
                   Name="CN/R23 CO2.hNbb -> CO.bCN + O.hC",
                   Hover=HoverList, Color='k', **{**Main_Line_Props, "StepSpan": 1.})

# Section
SectionRefs_CN100e.UpdateFromTail(RefCN100_e_CO2)
idrx.Plot.AnnotateStepAxis(['$CO_{2}$',''], Ref=SectionRefs_CN100e, Colour='k')



# .....................................
# CO desorbs ..........................
# .....................................
RefCN100_e_CO_des = RefCN100_e_CO2.branch()

# Separe/ {CO.bCN+O.hC}+ 1/2(H2) + {} -> {CO.tC} + {O+H/R13.2C}
idrx.Plot.RxStep([CN10R23_f.E0 + 0.5*H2.E0 + CN100.E0, CN10R17tC_i.E0 + CN10R132C_i.E0],
                 Ref=RefCN100_e_CO_des,
                 Name="CN/{CO.bCN+O.hC}+1/2(H2)+{}->{CO.tC} + {O+H/R13.2C}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)
# CO desorbs
idrx.Plot.RxStep([CN10R17tC_i.E0, CN100.E0 + COg.E0],
                 Ref=RefCN100_e_CO_des,
                 Name="CO desorbs",
                 Hover=HoverList, Color='m', **Main_Line_Props_CO
                 )







# .....................................
# CO series ...........................
# .....................................
RefCN100_e_CO = RefCN100_e_CO2.branch()

# ----------------------------------------------- branch 1 CO.tC, OH-R13C
RefCN100_e_CO_1 = RefCN100_e_CO.branch()

# Separe/ {CO.bCN+O.hC}+ 1/2(H2) + {} -> {CO.tC} + {O+H/R13.2C}
idrx.Plot.RxStep([CN10R23_f.E0 + 0.5*H2.E0 + CN100.E0, CN10R17tC_i.E0 + CN10R132C_i.E0],
                 Ref=RefCN100_e_CO_1,
                 Name="CN/{CO.bCN+O.hC}+1/2(H2)+{}->{CO.tC} + {O+H/R13.2C}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination R13C {O.h + H.h} -(tC)-> {OH.h} (branched out)
idrx.Plot.RxStepTS([CN10R132C_i.E0, CN10R132C_d.E0, CN10R132C_f.E0],
                   Ref=RefCN100_e_CO_1, UpdateRef=False,
                   Name="CN(R13C)/O.h + H.h -(tC)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN(R17tC)/ {CO.tC} -> {C.hN + O.hC}
idrx.Plot.RxStepTS([CN10R17tC_i.E0, CN10R17tC_d.E0, CN10R17tC_f.E0],
                   Ref=RefCN100_e_CO_1,
                   Name="CN/R13tC CO.tC -> C.hN + O.hC",
                   Hover=HoverList, Color='r', **Main_Line_Props)

# Separe/ {C.hN + O.hC}+1/2(H2)+{} -> {C.hN} + {(R13C) O.h + H.h} + {}
idrx.Plot.RxStep([CN10R17tC_f.E0 + 0.5 * H2.E0 + CN100.E0, CN100_ChN.E0 + CN10R132C_i.E0],
                 Ref=RefCN100_e_CO_1,
                 Name="CN/ {C.hN + O.hC}+1/2(H2)+{} -> {C.hN} + {(R13C) O.h + H.h}",
                 Hover=HoverList, Color='r', **Jump_Line_Props)

# OH elimination R13C {O.h + H.h} -(tC)-> {OH.h}
idrx.Plot.RxStepTS([CN10R132C_i.E0, CN10R132C_d.E0, CN10R132C_f.E0],
                   Ref=RefCN100_e_CO_1,
                   Name="CN(R13C)/O.h + H.h -(tC)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# ----------------------------------------------- branch 2 CO.tC, OH-R13C
RefCN100_e_CO_2 = RefCN100_e_CO.branch()

# Separe/ {CO.bCN+O.hC}+1/2(H2)+{} -> {CO.hN} + {O+H/R13.2N}
idrx.Plot.RxStep([CN10R23_f.E0 + 0.5*H2.E0 + CN100.E0, CN10R17hN_i.E0 + CN10R132N_i.E0],
                 Ref=RefCN100_e_CO_2,
                 Name="CN/{CO.bCN+O.hC}+1/2(H2)+{}->{CO.hN}+{O+H/R13.2N}",
                 Hover=HoverList, Color='r', **{**Jump_Line_Props, "StepSpan": .3})

# OH elimination R13N {O.h + H.h} -(tN)-> {OH.h} (branched out)
idrx.Plot.RxStepTS([CN10R132N_i.E0, CN10R132N_d.E0, CN10R132N_f.E0],
                   Ref=RefCN100_e_CO_2, UpdateRef=False,
                   Name="CN(R13C)/O.h + H.h -(tN)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN(R17hN)/ {CO.hN} -> {C.hN + O.hC}
idrx.Plot.RxStepTS([CN10R17hN_i.E0, CN10R17hN_d.E0, CN10R17hN_f.E0],
                   Ref=RefCN100_e_CO_2,
                   Name="CN/R13tC CO.hN -> C.hN + O.hC",
                   Hover=HoverList, Color='r', **{**Main_Line_Props, "StepSpan": .4})

# Compile branches, section
RefCN100_e_CO.UpdateFromTail(RefCN100_e_CO_1)
SectionRefs_CN100e.UpdateFromTail(RefCN100_e_CO)
idrx.Plot.AnnotateStepAxis(['$CO$',''], Ref=SectionRefs_CN100e, Colour="r")




# .....................................
# HCO series ..........................
# .....................................
RefCN100_e_HCO = RefCN100_e_CO2.branch()
RefCN100_e_HCO.PlotExtend(Until=5.0, Color='m')


# Separe/ {CO.bCN+O.hC} + H2 + {} -> {CO.hN + H.hNd} + {(R13C) O.h + H.h} (split R23->R5, R13.2C)
idrx.Plot.RxStep([CN10R23_f.E0 + H2.E0 + CN100.E0, CN10R5tN_i.E0 + CN10R132C_i.E0],
                 Ref=RefCN100_e_HCO,
                 Name="CN/ {CO.bCN+O.hC}+(H2)+{}->{CO.hN+H.hNd}+{(R13C)O.h+H.h}",
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination R13C {O.h + H.h} -(tC)-> {OH.h}
idrx.Plot.RxStepTS([CN10R132C_i.E0, CN10R132C_d.E0, CN10R132C_f.E0],
                   Ref=RefCN100_e_HCO, UpdateRef=False,
                   Name="CN(R13C)/O.h + H.h -(tC)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN/R5 CO.hN + H.hNd -> HCO.bbN
idrx.Plot.RxStepTS([CN10R5tN_i.E0, CN10R5tN_d.E0, CN10R5tN_f.E0],
                   Ref=RefCN100_e_HCO,
                   Name="CN/R5 CO.hN + H.hNd -> HCO.bbN",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# CN/R15 HCO.bbN -(b)-> CH.hN + O.hC
idrx.Plot.RxStepTS([CN10R15b_i.E0, CN10R15b_d.E0, CN10R15b_f.E0],
                   Ref=RefCN100_e_HCO,
                   Name="CN10/R15b-d HCO.bbN -(b)-> CH.hN + O.hC",
                   Hover=HoverList, Color='g', **Main_Line_Props)

# Separe/ {CH.hN + O.hC} + 1/2(H2) + {} -> {CH.hN} + {(R13C) O.h + H.h}
idrx.Plot.RxStep([CN10R15b_f.E0 + 0.5 * H2.E0 + CN100.E0, CN10R21_f.E0 + CN10R132C_i.E0],
                 Ref=RefCN100_e_HCO,
                 Name="CN/ {CH.hN + O.hC} + 1/2(H2) + {} -> {CH.hN} + {(R13C) O.h + H.h}",
                 Hover=HoverList, Color='g', **Jump_Line_Props)

# OH elimination R13C {O.h + H.h} -(tC)-> {OH.h}
idrx.Plot.RxStepTS([CN10R132C_i.E0, CN10R132C_d.E0, CN10R132C_f.E0],
                   Ref=RefCN100_e_HCO,
                   Name="CN(R13C)/O.h + H.h -(tC)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# Section
SectionRefs_CN100e.UpdateFromTail(RefCN100_e_HCO)
idrx.Plot.AnnotateStepAxis(['','$HCO$',''], Ref=SectionRefs_CN100e, Colour="g")



# .....................................
# COH series ..........................
# .....................................
RefCN100_e_COH = RefCN100_e_CO2.branch()
RefCN100_e_COH.PlotExtend(Until=8.5, Color='m', Alpha=1, LineWidth=.8)



# Separe/ {CO.bCN + O.hC}+(H2)+{} -> {CO.hN+H.hNd}+{(R132C)O.h+H.h}
idrx.Plot.RxStep([CN10R23_f.E0 + H2.E0 + CN100.E0, CN10R6tN_i.E0 + CN10R132C_i.E0],
                 Ref=RefCN100_e_COH,
                 Name="CN/{CO.bCN + O.hC}+(H2)+{} -> {CO.hN+H.hNd}+{(R132C)O.h+H.h}",
                 Hover=HoverList, Color='m', **Jump_Line_Props)

# OH elimination R13C {O.h + H.h} -(tC)-> {OH.h}
idrx.Plot.RxStepTS([CN10R132C_i.E0, CN10R132C_d.E0, CN10R132C_f.E0],
                   Ref=RefCN100_e_COH, UpdateRef=False,
                   Name="CN(R13C)/O.h + H.h -(tC)-> OH.h",
                   Hover=HoverList, Color='b', **OH_Line_Props)

# CN/R6tN CO.hN + H.hNd -> COH.hNtN
idrx.Plot.RxStepTS([CN10R6tN_i.E0, CN10R6tN_d.E0, CN10R6tN_f.E0],
                   Ref=RefCN100_e_COH,
                   Name="CN/R6tN CO.hN + H.hNd -> COH.hNtN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# CN/R16tN COH.hNtN -> C.hN + OH.hN
idrx.Plot.RxStepTS([CN10R16tN_i.E0, CN10R16tN_d.E0, CN10R16tN_f.E0],
                   Ref=RefCN100_e_COH,
                   Name="CN/R16tN COH.hNtN -> C.hN + OH.hN",
                   Hover=HoverList, Color="m", **Main_Line_Props)

# Separe/ {C.hN + OH.hN}+{} -> {C.hN} + {(R132C)OH.hN}
idrx.Plot.RxStep([CN10R16tN_f.E0 + CN100.E0, CN100_ChN.E0 + CN10R132C_f.E0],
                 Ref=RefCN100_e_COH,
                 Name="CN/ {C.hN + OH.hN}+{} -> {C.hN}+{(R132C)OH.hN}",
                 Hover=HoverList, Color="m", **Jump_Line_Props)

# Sections
SectionRefs_CN100e.UpdateFromTail(RefCN100_e_COH)
idrx.Plot.AnnotateStepAxis(['','$COH$',''], Ref=SectionRefs_CN100e, Colour="m")



# .....................................
# CHx series ..........................
# .....................................
RefCN100_e_CO.PlotExtend(Until=11.5, Color='r')
RefCN100_e_HCO.PlotExtend(Until=12.5+.4, Color='g')
RefCN100_e_COH.PlotExtend(Until=11.5, Color='m')

RefCN100_e_CHx = RefCN100_e_CO.branch()
# RefCN100_e_CHx.PlotExtend(Until=12., Color='m', Alpha=1, LineWidth=.8)


# ---- C.hN + H.hC -> CH.hN
idrx.Plot.RxStep([CN100_ChN.E0 + 2 * H2.E0,
                  CN10R21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN100_e_CHx,
                 Name="CN100/ {C.hN}+2*H2 -> {C.hN+H.hC}+(3/2)H2",
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# CN/R21 C.h+H.f->CH.h
idrx.Plot.RxStepTS([CN10R21_i.E0, CN10R21_d.E0, CN10R21_f.E0],
                   Ref=RefCN100_e_CHx,
                   Name='CN/R21: C.hN + H.hC -> CH.hN',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH -> CH2

# Jump C/ R21 -> R9
idrx.Plot.RxStep([CN10R21_f.E0 + (3. / 2.) * H2.E0,
                  CN10R9_i.E0 + H2.E0],
                 Ref=RefCN100_e_CHx,
                 Name='CN/{CH.hN}+H(3/2)2->{CH.hN+h.hC}+H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# CN/R9 CH.hN+H.hC->CH2.hNb
idrx.Plot.RxStepTS([CN10R9_i.E0, CN10R9_d.E0, CN10R9_f.E0],
                   Ref=RefCN100_e_CHx,
                   Name='CN/R9: CH.hN + H.hC -> CH2.hNb',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH2 -> CH3
# ramificación secundaria
RefCN100_e_CHx_2 = RefCN100_e_CHx.branch()

# Jump C/ R9 -> R10-N
idrx.Plot.RxStep([CN10R9_f.E0 + H2.E0,
                  CN10R10tN_i.E0 + .5 * H2.E0],
                 Ref=RefCN100_e_CHx_2,
                 Name='CN/{CH2.hN}+H2->{CH2.hN+h.hN}+(1/2)H2',
                 Hover=HoverList, Color="r", **Jump_Line_Props)
# CN/R10 tN
idrx.Plot.RxStepTS([CN10R10tN_i.E0, CN10R10tN_TS.E0, CN10R10tN_f.E0],
                   Ref=RefCN100_e_CHx_2,
                   Name='CN/R10-N: CH2.hN + H.hC -> CH3.bN',
                   Hover=HoverList, Color="r", **Main_Line_Props)

# ---- CH3 -> CH4
# ramificación  secundaria (continuación)

# Jump C/ R10 -> R11C (rota CH3)
idrx.Plot.RxStep([CN10R10tN_f.E0 + .5 * H2.E0,
                  CN10R11C_i.E0],
                 Ref=RefCN100_e_CHx_2,
                 Name='{CH3.bC}+(1/2)H2->{CH3.bN(rot)+H.hN}',
                 Hover=HoverList, Color="r", **Jump_Line_Props)

# CN10/R11C: CH3btN + Hh -> CH4.g
idrx.Plot.RxStepTS([CN10R11C_i.E0, CN10R11C_TS.E0, CN10R11C_f.E0],
                   Ref=RefCN100_e_CHx_2,
                   Name='CN/R11C: CH3bC + H.h -> CH4.g',
                   Hover=HoverList, Color="r", **Main_Line_Props)


# ---- CH2 -> CH3
# ramificación primaria

# Jump C/ R9 -> R10-C
idrx.Plot.RxStep([CN10R9_f.E0 + H2.E0,
                  CN10R10tCbC_i.E0 + .5 * H2.E0],
                 Ref=RefCN100_e_CHx,
                 Name='CN/{CH2.hN}+H2->{CH2.hN+h.hN}+(1/2)H2',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# CN/R10 tCbC
idrx.Plot.RxStepTS([CN10R10tCbC_i.E0, CN10R10tCbC_TS.E0, CN10R10tCbC_f.E0],
                   Ref=RefCN100_e_CHx,
                   Name='CN/R10-C: CH2.hN + H.hN -> CH3.bC',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- CH3 -> CH4
# rama principal

# Jump N/ R10 -> R11N (mantiene CH3)
idrx.Plot.RxStep([CN10R10tCbC_f.E0 + .5 * H2.E0,
                  CN10R11N_i.E0],
                 Ref=RefCN100_e_CHx,
                 Name='CN/{CH3.bC}+(1/2)H2->{CH3.bC+h.hN}',
                 Hover=HoverList, Color="k", **Jump_Line_Props)

# CN10/R11N: CH3btC + H.h -> CH4.g
idrx.Plot.RxStepTS([CN10R11N_i.E0, CN10R11N_TS.E0, CN10R11N_f.E0],
                   Ref=RefCN100_e_CHx,
                   Name='CN/R11N: CH3bC + H.h -> CH4.g',
                   Hover=HoverList, Color="k", **Main_Line_Props)

# ---- Physisorption
idrx.Plot.RxStep([CN10R11N_f.E0, CN100.E0 + CH4_g.E0],
                 Ref=RefCN100_e_CHx,
                 Name='CN/{}CH4.gf->{}+CH4',
                 Hover=HoverList, Color="k", **{**Main_Line_Props, 'StepSpan':.4})


# Section
SectionRefs_CN100e.UpdateFromTail(RefCN100_e_CHx)
idrx.Plot.AnnotateStepAxis(['$CH_{x}$', '$CH_{4(g)}$'], Ref=SectionRefs_CN100e, Colour="k")
idrx.Plot.Align_Rx_Ticks(SectionRefs_CN100e, TSmode=False)

# # ---- Physisorption
# stg.Plot.RxStep([CN10R11C_f.E0, CN100.E0 + CH4_g.E0], Ref=RefCN100_e_tail2,
#                Name='CN/{}CH4.gf->{}+CH4', Hover=HoverList, StepSpan=.4, Color='b', **LineProps)

# Check full plot
# if ShowGlobal_e:
#     RefCN_e_full = RefCN100_e.branch(Step=0)
#     stg.Plot.RxStep([CN100_ChN.E0 + 2 * H2.E0,
#                       CN100.E0 + CH4_g.E0],
#                      Ref=RefCN_e_full, Name="CN10/{C.hN}+2*H2 -> {}+CH4",
#                      Hover=HoverList, Color="lime", StepSpan=4.4, **LineProps)
#     RefCN_e_full.PlotExtend(Until=11., Color="lime", **LineProps)

# ------------------------------------------------------------------------------------------------ Ending subplot
# Ajustes finales de plots

idrx.Plot.ActivateHover(HoverList, fig)
Ley = [Line2D([0], [0], color="k", linewidth=3, linestyle='-', alpha=0.8),
       Line2D([0], [0], color="r", linewidth=3, linestyle='-', alpha=0.8)]

# Lado izquierdo
for xax in axs:
    plt.axes(xax[0])
    plt.ylabel("Electronic energy (kJ/mol)")
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

for xax, geom in zip(axs,['(111)','(100)']):
    for iax, type in zip(xax, ['Co','NiCo','Ni']):
        plt.axes(iax)
        plt.annotate(type+geom,
                     xy=[.95, .95], xytext=[0, 0],
                     xycoords='axes fraction', textcoords='offset points',
                     ha='right', va='top', size=12, color='k', fontweight='bold',
                     bbox=dict(facecolor='white', edgecolor='white', pad=2.0))

plt.savefig("./Electronic_profiles.png", dpi=180)
plt.show()


