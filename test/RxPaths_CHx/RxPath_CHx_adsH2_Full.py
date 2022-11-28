#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from RxPath_CxOyHz_Databin import *

stg.MayorSection('Carbon hydrogenation')
stg.MinorSection('Adding data')
########################################################################################################################
stg.CodeStatus('Adding data: Gases')


########################################################################################################################
########################################################################################################################
# Creating Plot, CHx series ############################################################################################
########################################################################################################################
stg.MayorSection('Creating Plot')

fig, axs = plt.subplots(1, 3, figsize=(12, 4), dpi=90, sharey='row')
plt.subplots_adjust(wspace=.0, left=.1, right=.98)
HoverList = []

RefN111_e = stg.Plot.RxRef(0., 0.)
RefC111_e = stg.Plot.RxRef(0., 0.)
RefCN111_e = stg.Plot.RxRef(0., 0.)

NiColor = "k"
CoColor = "k"
CoNiColor1 = "k"

LineProps = {"AlphaLines": 1., "LineWidth": .8}
ShowGlobal_e = True

########################################################################################################################
# Nickel (111s)----------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Electronic - Ni(111s)')
plt.axes(axs[2])
plt.title('Electronic - Ni')

# ---- *C+*H -(bridge)-> *CH

RefN111_e_2 = RefN111_e.branch(Step=0)
stg.Plot.RxStep([N1s_Cf.E0 + 2. * H2.E0,
                  N1sR21a_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefN111_e_2, Name="N1s/{C.f}+2*H2->{C.f+H.f}+(3/2)*H2",
                 Hover=HoverList, Color=NiColor, LineStyle="-", **LineProps, StepSpan=.2)
# R21a by side: C.f + H.h
stg.Plot.RxStepTS([N1sR21a_i.E0, N1sR21a_TS.E0, N1sR21a_f.E0], Ref=RefN111_e_2,
                   Name='N1s/R21a by bridge: C.f + H.h -> CH.h',
                   Hover=HoverList, Color=NiColor, **LineProps, LineStyle="-")

# ---- *C+*H -(top)-> *CH

stg.Plot.RxStep([N1s_Cf.E0 + 2. * H2.E0,
                  N1sR21top_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefN111_e, Name="N1s/{C.f}+2*H2->{C.f+H.f}+(3/2)*H2",
                 Hover=HoverList, Color=NiColor, **LineProps, StepSpan=.2)
# R21b on top: C.f + H.f -> CH.h
stg.Plot.RxStepTS([N1sR21top_i.E0, N1sR21top_TS.E0, N1sR21top_f.E0], Ref=RefN111_e,
                   Name='N1s/R21b on top: C.f + H.h -> CH.h',
                   Hover=HoverList, Color=NiColor, **LineProps)

# ---- CH+H -> CH2

# Jump N/ R21 -> R9
stg.Plot.RxStep([N1sR21top_f.E0 + (3. / 2.) * H2.E0,
                  N1sR9top_i.E0 + H2.E0], Ref=RefN111_e,
                 Name='N1s/{CH.f}+(3/2)H2->{CH.f+H.h}+H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps)
# R9 on top: CH.f + H.h -> CH2.f
stg.Plot.RxStepTS([N1sR9top_i.E0, N1sR9top_TS.E0, N1sR9top_f.E0], Ref=RefN111_e,
                   Name='N1s/R9 on top: CH.f + H.h -> CH2.f',
                   Hover=HoverList, Color=NiColor, **LineProps)

# ---- CH2+H -> CH3

# Jump N/ R0 -> R10
stg.Plot.RxStep([N1sR9top_f.E0 + H2.E0,
                  N1sR10top_i.E0 + .5 * H2.E0], Ref=RefN111_e,
                 Name='N1s/{CH2.f}+H2->{CH2.f+H.f}+(1./2.)*H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps)
# R10 on top: CH2.f +H.f -> CH3.f
stg.Plot.RxStepTS([N1sR10top_i.E0, N1sR10top_TS.E0, N1sR10top_f.E0], Ref=RefN111_e,
                   Name='N1s/R10 on top: CH2.f +H.f -> CH3.f',
                   Hover=HoverList, Color=NiColor, **LineProps)

# ---- CH3+H -> CH4

# Jump N/ R10 -> R11
stg.Plot.RxStep([N1sR10top_f.E0 + .5 * H2.E0,
                  N1sR11top_i.E0], Ref=RefN111_e,
                 Name='N1s/{CH3.f}+(1/2)H2->{CH3.f+H.f}',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps)
# R11 on top: CH3.f +H.f -> CH4.g
stg.Plot.RxStepTS([N1sR11top_i.E0, N1sR11top_TS.E0, N1sR11top_f.E0], Ref=RefN111_e,
                   Name='N1s/R11 on top: CH3.f +H.f -> CH4.g',
                   Hover=HoverList, Color=NiColor, **LineProps)

# Jump physisorption
stg.Plot.RxStep([N1sR11top_f.E0,
                  CH4_g.E0 + N111s.E0], Ref=RefN111_e,
                 Name='N1s/{}CH4g->{}+CH4g', Hover=HoverList, Color=NiColor, **LineProps, StepSpan=.4)

# Cobalt ----------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Electronic - Co(111s)')
plt.axes(axs[0])
plt.title('Electronic - Co')

# ---- *C.h+H2 -(bridge)-> *CH.h
RefC111_e_2 = RefC111_e.branch(Step=0)
stg.Plot.RxStep([C1s_Ch.E0 + 2. * H2.E0,
                  C1sR21a_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefC111_e_2, Name="C1s/{C.h}+2*H2 -> {C.h+H.f}+(3./2.)*H2",
                 Hover=HoverList, Color=CoColor, **LineProps, StepSpan=.2, LineStyle="-")
# R21a by side: C.h + H.h -> CH.h
stg.Plot.RxStepTS([C1sR21a_i.E0, C1sR21a_TS.E0, C1sR21a_f.E0], Ref=RefC111_e_2,
                   Name='C1s/R21a by bridge: C.h+H.h->CH.h',
                   Hover=HoverList, Color=CoColor, **LineProps, LineStyle="-")

# ---- *C.h+H2 -(top)-> *CH.h
stg.Plot.RxStep([C1s_Ch.E0 + 2. * H2.E0,
                  C1sR21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefC111_e, Name="C1s/{C.h}+2*H2 -> {C.h+H.f}+(3/2)*H2",
                 Hover=HoverList, Color=CoColor, **LineProps, StepSpan=.2)
# R21b on top: C.h + H.f -> CH.h
stg.Plot.RxStepTS([C1sR21_i.E0, C1sR21_TS.E0, C1sR21_f.E0], Ref=RefC111_e,
                   Name='C1s/R21(top): C.h+H.f->CH.h',
                   Hover=HoverList, Color=CoColor, **LineProps)

# ---- CH+H -> CH2

# Jump C/ R21 -> R9
stg.Plot.RxStep([C1sR21_f.E0 + (3. / 2.) * H2.E0,
                  C1sR9_i.E0 + H2.E0], Ref=RefC111_e,
                 Name='C1s/{CH.h}+(3/2)*H2->{CH.h+H.f}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps)
# R9: CH.h + H.f -> CH2.h
stg.Plot.RxStepTS([C1sR9_i.E0, C1sR9_TS.E0, C1sR9_f.E0], Ref=RefC111_e,
                   Name='C11s/R9 on top: CH.h + H.f -> CH2.h',
                   Hover=HoverList, Color=CoColor, **LineProps)

# ---- CH2+H -> CH3

# Jump C/ R9 -> R10
stg.Plot.RxStep([C1sR9_f.E0 + H2.E0,
                  C1sR10_i.E0 + .5 * H2.E0], Ref=RefC111_e,
                 Name='C1s/{CH2.h}+H2->{CH2.h+H.f}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps)
# R10: CH2.h + H.f -> CH3.h
stg.Plot.RxStepTS([C1sR10_i.E0, C1sR10_TS.E0, C1sR10_f.E0], Ref=RefC111_e,
                   Name='C1s/R10: CH2.h + H.f -> CH3.h',
                   Hover=HoverList, Color=CoColor, **LineProps)

# ---- CH3+H -> CH4

# Jump C/ R10 -> R11
stg.Plot.RxStep([C1sR10_f.E0 + .5 * H2.E0,
                  C1sR11_i.E0], Ref=RefC111_e,
                 Name='C1s/{CH3.h}+(1/2)H2->{CH2.h+H.f}',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps)
# R11: CH3.h + H.f -> CH4.g
stg.Plot.RxStepTS([C1sR11_i.E0, C1sR11_TS.E0, C1sR11_f.E0], Ref=RefC111_e,
                   Name='C1s/R11: CH3.h + H.f -> CH4.g',
                   Hover=HoverList, Color=CoColor, **LineProps)

# Physisorption
stg.Plot.RxStep([C1sR11_f.E0, CH4_g.E0 + C111s.E0], Ref=RefC111_e,
                 Name='C1s/R11 {}CH4->{}+CH4g',
                 Hover=HoverList, Color=CoColor, StepSpan=.4, **LineProps)

# Cobalt-Nickel ----------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Electronic - CoNi(111s)')
plt.axes(axs[1])
plt.title('Electronic - NiCo')

# ---- C.hN+H.fN -(C)-> CH.hN

stg.Plot.RxStep([CN1s_ChN.E0 + 2. * H2.E0,
                  CN1sR21C_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN111_e, Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps, StepSpan=.2)
# R21 - C : C.hN + H.fN -> CH.hN
stg.Plot.RxStepTS([CN1sR21C_i.E0, CN1sR21C_TS.E0, CN1sR21C_f.E0], Ref=RefCN111_e,
                   Name='CN1s/R21 on top C: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- C.hN+H.fN -(N)-> CH.hN

RefCN111_e_1 = RefCN111_e.branch(Step=0)
stg.Plot.RxStep([CN1s_ChN.E0 + 2. * H2.E0,
                  CN1sR21N_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN111_e_1, Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps, StepSpan=.2)
# R21 - N : C.hN + H.fN -> CH.hN
stg.Plot.RxStepTS([CN1sR21N_i.E0, CN1sR21N_TS.E0, CN1sR21N_f.E0], Ref=RefCN111_e_1,
                   Name='CN1s/R21 on top N: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- C.hN+H.fN -(bCN)-> CH.hN

RefCN111_e_2 = RefCN111_e.branch(Step=0)
stg.Plot.RxStep([CN1s_ChN.E0 + 2. * H2.E0,
                  CN1sR21b_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN111_e_2, Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps, StepSpan=.2)
# R21 - bridge CN : C.hN + H.hN -> CH.hN
stg.Plot.RxStepTS([CN1sR21b_i.E0, CN1sR21b_TS.E0, CN1sR21b_f.E0], Ref=RefCN111_e_2,
                   Name='CN1s/R21 bridge CN: C.hN+H.hN->CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- CH+H -> CH2

# Jump CN/ R21C -> R9C
stg.Plot.RxStep([CN1sR21C_f.E0 + (3. / 2.) * H2.E0,
                  CN1sR9C_i.E0 + H2.E0],
                 Ref=RefCN111_e, Name='CN1s/{CH.hN}+(3/2)H2->{CH.hN+H.fN}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps)
# R9C: CH.hN + H.fN -> CH2.hNtC
stg.Plot.RxStepTS([CN1sR9C_i.E0, CN1sR9C_TS.E0, CN1sR9C_f.E0],
                   Ref=RefCN111_e, Name='CN1s/R9C: CH.hN + H.fN -> CH2.hNtC',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- CH2+H -> CH3

# Jump CN/ R9C -> R10C
stg.Plot.RxStep([CN1sR9C_f.E0 + H2.E0,
                  CN1sR10C_i.E0 + .5 * H2.E0],
                 Ref=RefCN111_e, Name='CN1s/{CH2.hNtC}+H2->{CH2.hNtC+H.fN}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps)
# R10C: CH2.hNtC + H.fN -> CH3.hN
stg.Plot.RxStepTS([CN1sR10C_i.E0, CN1sR10C_TS.E0, CN1sR10C_f.E0],
                   Ref=RefCN111_e, Name='CN1s/R10C: CH2.hNtC + H.fN -> CH3.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- CH3+H -(C)-> CH4

# Jump CN/ R10C -> R11C
stg.Plot.RxStep([CN1sR10C_f.E0 + .5 * H2.E0,
                  CN1sR11C_i.E0],
                 Ref=RefCN111_e, Name='CN1s/{CH3.hN}+(1/2)H2->{CH3.hN+H.fN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps)
# R11C: CH3.hN + H.fN -> CH4.g
stg.Plot.RxStepTS([CN1sR11C_i.E0, CN1sR11C_TS.E0, CN1sR11C_f.E0],
                   Ref=RefCN111_e, Name='CN1s/R11C CH3.hN + H.fN -> CH4g',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# Physisorption
stg.Plot.RxStep([CN1sR11C_f.E0,
                  CN111s.E0 + CH4_g.E0],
                 Ref=RefCN111_e, Name='CN1s/{}CH4g->{}+CH4g',
                 Hover=HoverList, StepSpan=.4, Color=CoNiColor1, **LineProps)

# ---- CH3+H -(N)-> CH4

# Jump CN/ R10C -> R11N
RefCN111_e_tail = RefCN111_e.branch(Step=6)
stg.Plot.RxStep([CN1sR10C_f.E0 + .5 * H2.E0,
                  CN1sR11N_i.E0],
                 Ref=RefCN111_e_tail, Name='CN1s/{CH3.hN}+(1/2)*H2->{CH3.hN+H.fN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps)
# R11N: CH3.hN + H.fN -> CH4.g
stg.Plot.RxStepTS([CN1sR11N_i.E0, CN1sR11N_TS.E0, CN1sR11N_f.E0],
                   Ref=RefCN111_e_tail, Name='CN1s/R11N CH3.hN + H.fN -> CH4g',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)
# Physisorption
stg.Plot.RxStep([CN1sR11N_f.E0,
                  CN111s.E0 + CH4_g.E0],
                 Ref=RefCN111_e_tail, Name='CN1s/{}CH4g->{}+CH4g',
                 Hover=HoverList, StepSpan=.4, Color=CoNiColor1, **LineProps)


########################################################################################################################
# (100) ----------------------------------------------------------------------------------------------------------------

RefN100_e = stg.Plot.RxRef(0., 0.)
RefC100_e = stg.Plot.RxRef(0., 0.)
RefCN100_e = stg.Plot.RxRef(0., 0.)


NiColor = "r"
CoColor = "r"
CoNiColor1 = "r"

# Nickel ---------------------------------------------------------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Electronic - Ni(100)')
plt.axes(axs[2])

# ---- C.h + H2 -> CH.h
stg.Plot.RxStep([N100_Ch.E0 + 2 * H2.E0,
                  N10R21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefN100_e, Name="N/{C.h}+2*H2 -> {C.h +H.h}+(3/2)H2",
                 Hover=HoverList, Color=NiColor, **LineProps, StepSpan=.2)
# N/R21 C.h+H.f->CH
stg.Plot.RxStepTS([N10R21_i.E0, N10R21_d.E0, N10R21_f.E0], Ref=RefN100_e,
                   Name='N/R21: C.h + H.h -> CH.h', Hover=HoverList, Color=NiColor, **LineProps)

# ---- CH-CH2

# Jump C/ R21 -> R9
stg.Plot.RxStep([N10R21_f.E0 + (3. / 2.) * H2.E0,
                  N10R9_i.E0 + H2.E0],
                 Ref=RefN100_e, Name='N/{CH.h}+(3/2)H2->{CH.h+H.h}+H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps)
# N/R9 CH.h+H.f->CH2.hb
stg.Plot.RxStepTS([N10R9_i.E0, N10R9_d.E0, N10R9_f.E0],
                   Ref=RefN100_e, Name='N/R9: CH.h + H.h -> CH2.hb',
                   Hover=HoverList, Color=NiColor, **LineProps)

# ---- CH2-CH3

# Jump C/ R9 -> R10
stg.Plot.RxStep([N10R9_f.E0 + H2.E0,
                  N10R10_i.E0 + .5 * H2.E0],
                 Ref=RefN100_e, Name='N/{CH2.hb}+H2 -> {CH2.hb+H.hd}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps)
# N/R10 CH2.hb+H.f->CH3.b3
stg.Plot.RxStepTS([N10R10_i.E0, N10R10_d.E0, N10R10_f.E0],
                   Ref=RefN100_e, Name='N/R10: CH2.hb + H.h -> CH3.b3',
                   Hover=HoverList, Color=NiColor, **LineProps)

# ---- CH3-CH4

# Jump C/ R10 -> R11
stg.Plot.RxStep([N10R10_f.E0 + .5 * H2.E0,
                  N10R11_i.E0],
                 Ref=RefN100_e, Name='N/{CH3.b}+(1/2)H2->{CH3.hb+H.hd}',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps)
# N/R11 CH3.hb + H.hd -> CH4.g
stg.Plot.RxStepTS([N10R11_i.E0, N10R11_TS.E0, N10R11_f.E0],
                   Ref=RefN100_e, Name='N/R11: CH3.hb + H.hd -> CH4.g',
                   Hover=HoverList, Color=NiColor, **LineProps)
# ---- Physisorption
stg.Plot.RxStep([N10R11_f.E0, N100.E0 + CH4_g.E0], Ref=RefN100_e,
                 Name='N/{}CH4g->{}+CH4g', Hover=HoverList, StepSpan=.4, Color=NiColor, **LineProps)

# Cobalt ---------------------------------------------------------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Electronic - Co(100)')
plt.axes(axs[0])

# ---- C.h + H.h -> CH.h
stg.Plot.RxStep([C100_Ch.E0 + 2. * H2.E0,
                  C10R21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefC100_e, Name="C100/{C.h}+2*H2 -> {C.h+H.h}+(3/2)*H2",
                 Hover=HoverList, Color=CoColor, **LineProps, StepSpan=.2)
# C/R21 C.h+H.f->CH.h
stg.Plot.RxStepTS([C10R21_i.E0, C10R21_d.E0, C10R21_f.E0], Ref=RefC100_e,
                   Name='C/R21: C.h + H.h -> CH.h', Hover=HoverList, Color=CoColor, **LineProps)

# ---- CH->CH2
# Jump C/ R21 -> R9
stg.Plot.RxStep([C10R21_f.E0 + (3. / 2.) * H2.E0,
                  C10R9_i.E0 + H2.E0],
                 Ref=RefC100_e, Name='C/{CH.h}+(3/2)*H2->{CH.h+H.h}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps)
# C/R9 CH.h+H.f->CH2.hb
stg.Plot.RxStepTS([C10R9_i.E0, C10R9_d.E0, C10R9_f.E0], Ref=RefC100_e,
                   Name='C/R9: CH.h + H.h -> CH2.h', Hover=HoverList, Color=CoColor, **LineProps)

# ---- CH2->CH3
# Jump C/ R9 -> R10
stg.Plot.RxStep([C10R9_f.E0 + H2.E0,
                  C10R10_i.E0 + .5 * H2.E0],
                 Ref=RefC100_e, Name='C/{CH2.h}+H2->{CH2.h+H.hd}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps)
# C/R10 CH2.h + H.hd -> CH3.b3
stg.Plot.RxStepTS([C10R10_i.E0, C10R10_d.E0, C10R10_f.E0], Ref=RefC100_e,
                   Name='C/R10: CH2.h + H.hd -> CH3.b', Hover=HoverList, Color=CoColor, **LineProps)

# ---- CH3->CH4
# Jump C/ R10 -> R11
stg.Plot.RxStep([C10R10_f.E0 + .5 * H2.E0,
                  C10R11_i.E0],
                 Ref=RefC100_e, Name='C/{CH3.h}+{H.h}->{CH3.h+H.hd}',
                 Hover=HoverList, Color=CoColor, StepSpan=.2, **LineProps)
# C/R11 CH3.b + H.hd -> CH4.g
stg.Plot.RxStepTS([C10R11_i.E0, C10R11_TS.E0, C10R11_f.E0],
                   Ref=RefC100_e, Name='C/R11: CH3.b + H.hd -> CH4.g',
                   Hover=HoverList, Color=CoColor, **LineProps)
# ---- Physisorption
stg.Plot.RxStep([C10R11_f.E0, C100.E0 + CH4_g.E0],
                 Ref=RefC100_e, Name='C/{}CH4g->{}+CH4g',
                 Hover=HoverList, StepSpan=.4, Color=CoColor, **LineProps)

# Cobalt-Nickel --------------------------------------------------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Electronic - CoNi(100)')
plt.axes(axs[1])

# ---- C.hN + H.hC -> CH.hN
stg.Plot.RxStep([CN100_ChN.E0 + 2 * H2.E0,
                  CN10R21_i.E0 + (3. / 2.) * H2.E0],
                 Ref=RefCN100_e, Name="CN100/ {C.hN}+2*H2 -> {C.hN+H.hC}+(3/2)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps, StepSpan=.2)
# CN/R21 C.h+H.f->CH.h
stg.Plot.RxStepTS([CN10R21_i.E0, CN10R21_d.E0, CN10R21_f.E0],
                   Ref=RefCN100_e, Name='CN/R21: C.hN + H.hC -> CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- CH->CH2
# Jump C/ R21 -> R9
stg.Plot.RxStep([CN10R21_f.E0 + (3. / 2.) * H2.E0,
                  CN10R9_i.E0 + H2.E0],
                 Ref=RefCN100_e, Name='CN/{CH.hN}+H(3/2)2->{CH.hN+h.hC}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps)
# CN/R9 CH.hN+H.hC->CH2.hNb
stg.Plot.RxStepTS([CN10R9_i.E0, CN10R9_d.E0, CN10R9_f.E0],
                   Ref=RefCN100_e, Name='CN/R9: CH.hN + H.hC -> CH2.hNb',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- CH2->CH3
# Jump C/ R9 -> R10-C
stg.Plot.RxStep([CN10R9_f.E0 + H2.E0,
                  CN10R10tCbC_i.E0 + .5 * H2.E0],
                 Ref=RefCN100_e, Name='CN/{CH2.hN}+H2->{CH2.hN+h.hN}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps)
# CN/R10 tCbC
stg.Plot.RxStepTS([CN10R10tCbC_i.E0, CN10R10tCbC_TS.E0, CN10R10tCbC_f.E0], Ref=RefCN100_e,
                   Name='CN/R10-C: CH2.hN + H.hN -> CH3.bC', Hover=HoverList, Color=CoNiColor1, **LineProps)

# ---- CH3->CH4
# Jump N/ R10 -> R11N (mantiene CH3)
stg.Plot.RxStep([CN10R10tCbC_f.E0 + .5 * H2.E0,
                  CN10R11N_i.E0],
                 Ref=RefCN100_e, Name='CN/{CH3.bC}+(1/2)H2->{CH3.bC+h.hN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps)
# CN10/R11N: CH3btC + H.h -> CH4.g
stg.Plot.RxStepTS([CN10R11N_i.E0, CN10R11N_TS.E0, CN10R11N_f.E0],
                   Ref=RefCN100_e, Name='CN/R11N: CH3bC + H.h -> CH4.g',
                   Hover=HoverList, Color=CoNiColor1, **LineProps)
# ---- Physisorption
stg.Plot.RxStep([CN10R11N_f.E0, CN100.E0 + CH4_g.E0],
                 Ref=RefCN100_e, Name='CN/{}CH4.gf->{}+CH4',
                 Hover=HoverList, StepSpan=.4, Color=CoNiColor1, **LineProps)

# -------------------------------- Ramification

# ---- CH2->CH3

# Jump C/ R9 -> R10-N
RefCN100_e_tail2 = RefCN100_e.branch(Step=4)
stg.Plot.RxStep([CN10R9_f.E0 + H2.E0,
                  CN10R10tN_i.E0 + .5 * H2.E0],
                 Ref=RefCN100_e_tail2, Name='CN/{CH2.hN}+H2->{CH2.hN+h.hN}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, LineStyle="-", **LineProps)
# CN/R10 tN
stg.Plot.RxStepTS([CN10R10tN_i.E0, CN10R10tN_TS.E0, CN10R10tN_f.E0],
                   Ref=RefCN100_e_tail2, Name='CN/R10-N: CH2.hN + H.hC -> CH3.bN',
                   Hover=HoverList, Color=CoNiColor1, LineStyle="-", StepSpan=1., **LineProps)

# ---- CH3->CH4

# Jump C/ R10 -> R11C (rota CH3)
stg.Plot.RxStep([CN10R10tN_f.E0 + .5 * H2.E0,
                  CN10R11C_i.E0],
                 Ref=RefCN100_e_tail2, Name='{CH3.bC}+(1/2)H2->{CH3.bN(rot)+H.hN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, LineStyle="-", **LineProps)
# CN10/R11C: CH3btN + Hh -> CH4.g
stg.Plot.RxStepTS([CN10R11C_i.E0, CN10R11C_TS.E0, CN10R11C_f.E0],
                   Ref=RefCN100_e_tail2, Name='CN/R11C: CH3bC + H.h -> CH4.g',
                   Hover=HoverList, Color=CoNiColor1, LineStyle="-", **LineProps)


# ------------------------------------------------------------------------------------------------ Ending subplot

stg.Plot.ActivateHover(HoverList, fig)
Ley = [Line2D([0], [0], color="k", linewidth=3, linestyle='-', alpha=0.8),
       Line2D([0], [0], color="r", linewidth=3, linestyle='-', alpha=0.8)]
plt.axes(axs[0])
plt.ylabel("Electronic energy (kJ/mol)")
# Lefft plot
plt.tick_params(axis="y", direction="in")
# other plots
for iax in axs[1:]:
    plt.axes(iax)
    plt.tick_params(axis="y", direction="inout", length=12.)
# all plots
for iax in axs:
    plt.axes(iax)
    plt.axhline(y=0., color="k", alpha=.5, linewidth=.4)
    plt.xlabel(f"Reaction coordinate $\longrightarrow$")
    iax.set_xticks([])

    # Legend
    plt.legend(Ley, ["(111)", "(100)"], prop={'size': 8}, loc='upper right')

plt.savefig("./EnergyProfile_Electronic_CHx_python_raw.png", dpi=180)
plt.show()


########################################################################################################################
########################################################################################################################
# Creating Plot, CHx series ############################################################################################
########################################################################################################################
stg.MayorSection('Creating Plot - Gibbs')

fig, axs = plt.subplots(1, 3, figsize=(12, 5), dpi=90, sharey='row')
plt.subplots_adjust(wspace=.0, left=.1, right=.98)
HoverList = []

RefN111_G = stg.Plot.RxRef(0., 0.)
RefC111_G = stg.Plot.RxRef(0., 0.)
RefCN111_G = stg.Plot.RxRef(0., 0.)

NiColor = "k"
CoColor = "k"
CoNiColor1 = "k"

LineProps111 = {"AlphaLines": 1., "LineWidth": .9, "LineStyle": (0,(1,1))}
GibbsOpts = {'T': 265 + 273.15, 'P': 0.01 * 1.}  # 1% CH4
ShowGlobal_G = False

########################################################################################################################
# Nickel (111s)----------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Gibbs - Ni(111s)')
plt.axes(axs[2])
plt.title('Gibbs - Ni')

# ---- *C+*H -(bridge)-> *CH

RefN111_G_2 = RefN111_G.branch(Step=0)
stg.Plot.RxStep([N1s_Cf.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  N1sR21a_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefN111_G_2, Name="N1s/{C.f}+2*H2->{C.f+H.f}+(3/2)*H2",
                 Hover=HoverList, Color=NiColor, **LineProps111, StepSpan=.2)
# R21a by side: C.f + H.h
stg.Plot.RxStepTS([N1sR21a_i.Gibbs(**GibbsOpts), N1sR21a_TS.Gibbs(**GibbsOpts), N1sR21a_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_G_2, Name='N1s/R21a by bridge: C.f + H.h -> CH.h',
                   Hover=HoverList, Color=NiColor, **LineProps111)

# ---- *C+*H -(top)-> *CH

stg.Plot.RxStep([N1s_Cf.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  N1sR21top_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefN111_G, Name="N1s/{C.f}+2*H2->{C.f+H.f}+(3/2)*H2",
                 Hover=HoverList, Color=NiColor, **LineProps111, StepSpan=.2)
# R21b on top: C.f + H.f -> CH.h
stg.Plot.RxStepTS([N1sR21top_i.Gibbs(**GibbsOpts), N1sR21top_TS.Gibbs(**GibbsOpts), N1sR21top_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_G, Name='N1s/R21b on top: C.f + H.h -> CH.h',
                   Hover=HoverList, Color=NiColor, **LineProps111)

# ---- CH+H -> CH2

# Jump N/ R21 -> R9
stg.Plot.RxStep([N1sR21top_f.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts),
                  N1sR9top_i.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts)], Ref=RefN111_G,
                 Name='N1s/{CH.f}+(3/2)H2->{CH.f+H.h}+H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps111)
# R9 on top: CH.f + H.h -> CH2.f
stg.Plot.RxStepTS([N1sR9top_i.Gibbs(**GibbsOpts), N1sR9top_TS.Gibbs(**GibbsOpts), N1sR9top_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_G, Name='N1s/R9 on top: CH.f + H.h -> CH2.f',
                   Hover=HoverList, Color=NiColor, **LineProps111)

# ---- CH2+H -> CH3

# Jump N/ R0 -> R10
stg.Plot.RxStep([N1sR9top_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts),
                  N1sR10top_i.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts)], Ref=RefN111_G,
                 Name='N1s/{CH2.f}+H2->{CH2.f+H.f}+(1./2.)*H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps111)
# R10 on top: CH2.f +H.f -> CH3.f
stg.Plot.RxStepTS([N1sR10top_i.Gibbs(**GibbsOpts), N1sR10top_TS.Gibbs(**GibbsOpts), N1sR10top_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_G, Name='N1s/R10 on top: CH2.f +H.f -> CH3.f',
                   Hover=HoverList, Color=NiColor, **LineProps111)

# ---- CH3+H -> CH4

# Jump N/ R10 -> R11
stg.Plot.RxStep([N1sR10top_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  N1sR11top_i.Gibbs(**GibbsOpts)], Ref=RefN111_G,
                 Name='N1s/{CH3.f}+(1/2)H2->{CH3.f+H.f}',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps111)
# R11 on top: CH3.f +H.f -> CH4.g
stg.Plot.RxStepTS([N1sR11top_i.Gibbs(**GibbsOpts), N1sR11top_TS.Gibbs(**GibbsOpts), N1sR11top_f.Gibbs(**GibbsOpts)],
                   Ref=RefN111_G, Name='N1s/R11 on top: CH3.f +H.f -> CH4.g',
                   Hover=HoverList, Color=NiColor, **LineProps111)

# Jump physisorption
stg.Plot.RxStep([N1sR11top_f.Gibbs(**GibbsOpts),
                  CH4_g.Gibbs(**GibbsOpts) + N111s.Gibbs(**GibbsOpts)], Ref=RefN111_G,
                 Name='N1s/{}CH4g->{}+CH4g', Hover=HoverList, Color=NiColor, **LineProps111, StepSpan=.4)

# Test Jump whole reaction
if ShowGlobal_G:
    RefN111_G_full = RefN111_G.branch(Step=0)
    stg.Plot.RxStep([N1s_Cf.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                      N111s.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                     Ref=RefN111_G_full, Name='N1s/{C.f+H.h}+2*H2->{}+CH4g',
                     Hover=HoverList, StepSpan=2.4, Color='g', **LineProps111)
    RefN111_G_full.PlotExtend(Until=11., Color="g")

# Cobalt ----------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Gibbs - Co(111s)')
plt.axes(axs[0])
plt.title('Gibbs - Co')

# ---- *C.h+H2 -(bridge)-> *CH.h
RefC111_G_2 = RefC111_G.branch(Step=0)
stg.Plot.RxStep([C1s_Ch.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  C1sR21a_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefC111_G_2, Name="C1s/{C.h}+2*H2 -> {C.h+H.f}+(3./2.)*H2",
                 Hover=HoverList, Color=CoColor, **LineProps111, StepSpan=.2)
# R21a by side: C.h + H.h -> CH.h
stg.Plot.RxStepTS([C1sR21a_i.Gibbs(**GibbsOpts), C1sR21a_TS.Gibbs(**GibbsOpts), C1sR21a_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_G_2, Name='C1s/R21a by bridge: C.h+H.h->CH.h',
                   Hover=HoverList, Color=CoColor, **LineProps111)

# ---- *C.h+H2 -(top)-> *CH.h
stg.Plot.RxStep([C1s_Ch.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  C1sR21_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefC111_G, Name="C1s/{C.h}+2*H2 -> {C.h+H.f}+(3/2)*H2",
                 Hover=HoverList, Color=CoColor, **LineProps111, StepSpan=.2)
# R21b on top: C.h + H.f -> CH.h
stg.Plot.RxStepTS([C1sR21_i.Gibbs(**GibbsOpts), C1sR21_TS.Gibbs(**GibbsOpts), C1sR21_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_G, Name='C1s/R21(top): C.h+H.f->CH.h',
                   Hover=HoverList, Color=CoColor, **LineProps111)

# ---- CH+H -> CH2

# Jump C/ R21 -> R9
stg.Plot.RxStep([C1sR21_f.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts),
                  C1sR9_i.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts)], Ref=RefC111_G,
                 Name='C1s/{CH.h}+(3/2)*H2->{CH.h+H.f}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps111)
# R9: CH.h + H.f -> CH2.h
stg.Plot.RxStepTS([C1sR9_i.Gibbs(**GibbsOpts), C1sR9_TS.Gibbs(**GibbsOpts), C1sR9_f.Gibbs(**GibbsOpts)], Ref=RefC111_G,
                   Name='C11s/R9 on top: CH.h + H.f -> CH2.h',
                   Hover=HoverList, Color=CoColor, **LineProps111)

# ---- CH2+H -> CH3

# Jump C/ R9 -> R10
stg.Plot.RxStep([C1sR9_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts),
                  C1sR10_i.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts)], Ref=RefC111_G,
                 Name='C1s/{CH2.h}+H2->{CH2.h+H.f}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps111)
# R10: CH2.h + H.f -> CH3.h
stg.Plot.RxStepTS([C1sR10_i.Gibbs(**GibbsOpts), C1sR10_TS.Gibbs(**GibbsOpts), C1sR10_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_G, Name='C1s/R10: CH2.h + H.f -> CH3.h',
                   Hover=HoverList, Color=CoColor, **LineProps111)

# ---- CH3+H -> CH4

# Jump C/ R10 -> R11
stg.Plot.RxStep([C1sR10_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  C1sR11_i.Gibbs(**GibbsOpts)], Ref=RefC111_G,
                 Name='C1s/{CH3.h}+(1/2)H2->{CH2.h+H.f}',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps111)
# R11: CH3.h + H.f -> CH4.g
stg.Plot.RxStepTS([C1sR11_i.Gibbs(**GibbsOpts), C1sR11_TS.Gibbs(**GibbsOpts), C1sR11_f.Gibbs(**GibbsOpts)],
                   Ref=RefC111_G, Name='C1s/R11: CH3.h + H.f -> CH4.g',
                   Hover=HoverList, Color=CoColor, **LineProps111)

# Physisorption
stg.Plot.RxStep([C1sR11_f.Gibbs(**GibbsOpts), CH4_g.Gibbs(**GibbsOpts) + C111s.Gibbs(**GibbsOpts)], Ref=RefC111_G,
                 Name='C1s/R11 {}CH4->{}+CH4g',
                 Hover=HoverList, Color=CoColor, StepSpan=.4, **LineProps111)

# Jump Test whole path
if ShowGlobal_G:
    RefC111_G_full = RefC111_G.branch(Step=0)
    stg.Plot.RxStep([C1s_Ch.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                      C111s.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                     Ref=RefC111_G_full, Name='C1s/{C.hN+H.f}+2*H2->{}+CH4g',
                     Hover=HoverList, StepSpan=2.4, Color='c', **LineProps111)
    RefC111_G_full.PlotExtend(Until=11, Color="c")

# Cobalt-Nickel ----------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Gibbs - CoNi(111s)')
plt.axes(axs[1])
plt.title('Gibbs - NiCo')

# ---- C.hN+H.fN -(C)-> CH.hN

stg.Plot.RxStep([CN1s_ChN.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  CN1sR21C_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G, Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps111, StepSpan=.2)
# R21 - C : C.hN + H.fN -> CH.hN
stg.Plot.RxStepTS([CN1sR21C_i.Gibbs(**GibbsOpts), CN1sR21C_TS.Gibbs(**GibbsOpts), CN1sR21C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_G, Name='CN1s/R21 on top C: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps111)

# ---- C.hN+H.fN -(N)-> CH.hN

RefCN111_G_1 = RefCN111_G.branch(Step=0)
stg.Plot.RxStep([CN1s_ChN.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  CN1sR21N_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G_1, Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps111, StepSpan=.2)
# R21 - N : C.hN + H.fN -> CH.hN
stg.Plot.RxStepTS([CN1sR21N_i.Gibbs(**GibbsOpts), CN1sR21N_TS.Gibbs(**GibbsOpts), CN1sR21N_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_G_1, Name='CN1s/R21 on top N: C.hN+H.fN->CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps111)

# ---- C.hN+H.fN -(bCN)-> CH.hN

RefCN111_G_2 = RefCN111_G.branch(Step=0)
stg.Plot.RxStep([CN1s_ChN.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  CN1sR21b_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G_2, Name="CN1s/{C.hN}+2*H2 -> {C.hN+H.fN}+(3./2.)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps111, StepSpan=.2)
# R21 - bridge CN : C.hN + H.hN -> CH.hN
stg.Plot.RxStepTS([CN1sR21b_i.Gibbs(**GibbsOpts), CN1sR21b_TS.Gibbs(**GibbsOpts), CN1sR21b_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_G_2, Name='CN1s/R21 bridge CN: C.hN+H.hN->CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps111)

# ---- CH+H -> CH2

# Jump CN/ R21C -> R9C
stg.Plot.RxStep([CN1sR21C_f.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts),
                  CN1sR9C_i.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G, Name='CN1s/{CH.hN}+(3/2)H2->{CH.hN+H.fN}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps111)
# R9C: CH.hN + H.fN -> CH2.hNtC
stg.Plot.RxStepTS([CN1sR9C_i.Gibbs(**GibbsOpts), CN1sR9C_TS.Gibbs(**GibbsOpts), CN1sR9C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_G, Name='CN1s/R9C: CH.hN + H.fN -> CH2.hNtC',
                   Hover=HoverList, Color=CoNiColor1, **LineProps111)

# ---- CH2+H -> CH3

# Jump CN/ R9C -> R10C
stg.Plot.RxStep([CN1sR9C_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts),
                  CN1sR10C_i.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G, Name='CN1s/{CH2.hNtC}+H2->{CH2.hNtC+H.fN}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps111)
# R10C: CH2.hNtC + H.fN -> CH3.hN
stg.Plot.RxStepTS([CN1sR10C_i.Gibbs(**GibbsOpts), CN1sR10C_TS.Gibbs(**GibbsOpts), CN1sR10C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_G, Name='CN1s/R10C: CH2.hNtC + H.fN -> CH3.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps111)

# ---- CH3+H -(C)-> CH4

# Jump CN/ R10C -> R11C
stg.Plot.RxStep([CN1sR10C_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  CN1sR11C_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G, Name='CN1s/{CH3.hN}+(1/2)H2->{CH3.hN+H.fN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps111)
# R11C: CH3.hN + H.fN -> CH4.g
stg.Plot.RxStepTS([CN1sR11C_i.Gibbs(**GibbsOpts), CN1sR11C_TS.Gibbs(**GibbsOpts), CN1sR11C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_G, Name='CN1s/R11C CH3.hN + H.fN -> CH4g',
                   Hover=HoverList, Color=CoNiColor1, **LineProps111)

# Physisorption
stg.Plot.RxStep([CN1sR11C_f.Gibbs(**GibbsOpts),
                  CN111s.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G, Name='CN1s/{}CH4g->{}+CH4g',
                 Hover=HoverList, StepSpan=.4, Color=CoNiColor1, **LineProps111)

# ---- CH3+H -(N)-> CH4

# Jump CN/ R10C -> R11N
RefCN111_G_tail = RefCN111_G.branch(Step=6)
stg.Plot.RxStep([CN1sR10C_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  CN1sR11N_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G_tail, Name='CN1s/{CH3.hN}+(1/2)*H2->{CH3.hN+H.fN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps111)
# R11N: CH3.hN + H.fN -> CH4.g
stg.Plot.RxStepTS([CN1sR11N_i.Gibbs(**GibbsOpts), CN1sR11N_TS.Gibbs(**GibbsOpts), CN1sR11N_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN111_G_tail, Name='CN1s/R11N CH3.hN + H.fN -> CH4g',
                   Hover=HoverList, Color=CoNiColor1, **LineProps111)
# Physisorption
stg.Plot.RxStep([CN1sR11N_f.Gibbs(**GibbsOpts),
                  CN111s.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                 Ref=RefCN111_G_tail, Name='CN1s/{}CH4g->{}+CH4g',
                 Hover=HoverList, StepSpan=.4, Color=CoNiColor1, **LineProps111)

# Jump Test whole path
if ShowGlobal_G:
    RefCN111_G_full = RefCN111_G.branch(Step=0)
    stg.Plot.RxStep([CN1s_ChN.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                      CN111s.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                     Ref=RefCN111_G_full, Name='CN1s/{C.hN+H.hN}+2*H2->{}+CH4g',
                     Hover=HoverList, StepSpan=2.4, Color='k', **LineProps111)
    RefCN111_G_full.PlotExtend(Until=11., Color="m", **LineProps111)

########################################################################################################################
# (100) ----------------------------------------------------------------------------------------------------------------

RefN100_G = stg.Plot.RxRef(0., 0.)
RefC100_G = stg.Plot.RxRef(0., 0.)
RefCN100_G = stg.Plot.RxRef(0., 0.)

NiColor = "r"
CoColor = "r"
CoNiColor1 = "r"

LineProps100 = {"AlphaLines": 1., "LineWidth": .8, "LineStyle": 'solid'}

# Nickel ---------------------------------------------------------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Gibbs - Ni(100)')
plt.axes(axs[2])

# ---- C.h + H2 -> CH.h
stg.Plot.RxStep([N100_Ch.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                  N10R21_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefN100_G, Name="N/{C.h}+2*H2 -> {C.h +H.h}+(3/2)H2",
                 Hover=HoverList, Color=NiColor, **LineProps100, StepSpan=.2)
# N/R21 C.h+H.f->CH
stg.Plot.RxStepTS([N10R21_i.Gibbs(**GibbsOpts), N10R21_d.Gibbs(**GibbsOpts), N10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_G, Name='N/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color=NiColor, **LineProps100)

# ---- CH-CH2

# Jump C/ R21 -> R9
stg.Plot.RxStep([N10R21_f.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts),
                  N10R9_i.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts)],
                 Ref=RefN100_G, Name='N/{CH.h}+(3/2)H2->{CH.h+H.h}+H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps100)
# N/R9 CH.h+H.f->CH2.hb
stg.Plot.RxStepTS([N10R9_i.Gibbs(**GibbsOpts), N10R9_d.Gibbs(**GibbsOpts), N10R9_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_G, Name='N/R9: CH.h + H.h -> CH2.hb',
                   Hover=HoverList, Color=NiColor, **LineProps100)

# ---- CH2-CH3

# Jump C/ R9 -> R10
stg.Plot.RxStep([N10R9_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts),
                  N10R10_i.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts)],
                 Ref=RefN100_G, Name='N/{CH2.hb}+H2 -> {CH2.hb+H.hd}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps100)
# N/R10 CH2.hb+H.f->CH3.b3
stg.Plot.RxStepTS([N10R10_i.Gibbs(**GibbsOpts), N10R10_d.Gibbs(**GibbsOpts), N10R10_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_G, Name='N/R10: CH2.hb + H.h -> CH3.b3',
                   Hover=HoverList, Color=NiColor, **LineProps100)

# ---- CH3-CH4

# Jump C/ R10 -> R11
stg.Plot.RxStep([N10R10_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  N10R11_i.Gibbs(**GibbsOpts)],
                 Ref=RefN100_G, Name='N/{CH3.b}+(1/2)H2->{CH3.hb+H.hd}',
                 Hover=HoverList, StepSpan=.2, Color=NiColor, **LineProps100)
# N/R11 CH3.hb + H.hd -> CH4.g
stg.Plot.RxStepTS([N10R11_i.Gibbs(**GibbsOpts), N10R11_TS.Gibbs(**GibbsOpts), N10R11_f.Gibbs(**GibbsOpts)],
                   Ref=RefN100_G, Name='N/R11: CH3.hb + H.hd -> CH4.g',
                   Hover=HoverList, Color=NiColor, **LineProps100)
# ---- Physisorption
stg.Plot.RxStep([N10R11_f.Gibbs(**GibbsOpts), N100.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)], Ref=RefN100_G,
                 Name='N/{}CH4g->{}+CH4g', Hover=HoverList, StepSpan=.4, Color=NiColor, **LineProps100)

# Jump Test complete series
if ShowGlobal_G:
    RefN_G_2 = RefN100_G.branch(Step=0)
    stg.Plot.RxStep([N100_Ch.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                      N100.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)], Ref=RefN_G_2, Name='{C.h+H.h}+2*H2->{}+CH4g',
                     Hover=HoverList, StepSpan=4.4, **LineProps100, Color="orange")
    RefN_G_2.PlotExtend(Until=11, Color="orange", **LineProps100)

# Cobalt ---------------------------------------------------------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Gibbs - Co(100)')
plt.axes(axs[0])

# ---- C.h + H.h -> CH.h
stg.Plot.RxStep([C100_Ch.Gibbs(**GibbsOpts) + 2. * H2.Gibbs(**GibbsOpts),
                  C10R21_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefC100_G, Name="C100/{C.h}+2*H2 -> {C.h+H.h}+(3/2)*H2",
                 Hover=HoverList, Color=CoColor, **LineProps100, StepSpan=.2)
# C/R21 C.h+H.f->CH.h
stg.Plot.RxStepTS([C10R21_i.Gibbs(**GibbsOpts), C10R21_d.Gibbs(**GibbsOpts), C10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_G, Name='C/R21: C.h + H.h -> CH.h',
                   Hover=HoverList, Color=CoColor, **LineProps100)

# ---- CH->CH2
# Jump C/ R21 -> R9
stg.Plot.RxStep([C10R21_f.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts),
                  C10R9_i.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts)],
                 Ref=RefC100_G, Name='C/{CH.h}+(3/2)*H2->{CH.h+H.h}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps100)
# C/R9 CH.h+H.f->CH2.hb
stg.Plot.RxStepTS([C10R9_i.Gibbs(**GibbsOpts), C10R9_d.Gibbs(**GibbsOpts), C10R9_f.Gibbs(**GibbsOpts)], Ref=RefC100_G,
                   Name='C/R9: CH.h + H.h -> CH2.h', Hover=HoverList, Color=CoColor, **LineProps100)

# ---- CH2->CH3
# Jump C/ R9 -> R10
stg.Plot.RxStep([C10R9_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts),
                  C10R10_i.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts)],
                 Ref=RefC100_G, Name='C/{CH2.h}+H2->{CH2.h+H.hd}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoColor, **LineProps100)
# C/R10 CH2.h + H.hd -> CH3.b3
stg.Plot.RxStepTS([C10R10_i.Gibbs(**GibbsOpts), C10R10_d.Gibbs(**GibbsOpts), C10R10_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_G, Name='C/R10: CH2.h + H.hd -> CH3.b',
                   Hover=HoverList, Color=CoColor, **LineProps100)

# ---- CH3->CH4
# Jump C/ R10 -> R11
stg.Plot.RxStep([C10R10_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  C10R11_i.Gibbs(**GibbsOpts)],
                 Ref=RefC100_G, Name='C/{CH3.h}+{H.h}->{CH3.h+H.hd}',
                 Hover=HoverList, Color=CoColor, StepSpan=.2, **LineProps100)
# C/R11 CH3.b + H.hd -> CH4.g
stg.Plot.RxStepTS([C10R11_i.Gibbs(**GibbsOpts), C10R11_TS.Gibbs(**GibbsOpts), C10R11_f.Gibbs(**GibbsOpts)],
                   Ref=RefC100_G, Name='C/R11: CH3.b + H.hd -> CH4.g',
                   Hover=HoverList, Color=CoColor, **LineProps100)
# ---- Physisorption
stg.Plot.RxStep([C10R11_f.Gibbs(**GibbsOpts), C100.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                 Ref=RefC100_G, Name='C/{}CH4g->{}+CH4g',
                 Hover=HoverList, StepSpan=.4, Color=CoColor, **LineProps100)

# Jump test complete
if ShowGlobal_G:
    RefC100_G_full = RefC100_G.branch(Step=0)
    stg.Plot.RxStep([C100_Ch.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                      C100.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                     Ref=RefC100_G_full, Name='C/{C.h+H.h}+2*H2 -> {}+CH4g',
                     Hover=HoverList, StepSpan=4.4, **LineProps100)
    RefC100_G_full.PlotExtend(Until=11., Color="gray", **LineProps100)

# Cobalt-Nickel --------------------------------------------------------------------------------------------------------
stg.MinorSection('Adding steps to Plot: Gibbs - CoNi(100)')
plt.axes(axs[1])

# ---- C.hN + H.hC -> CH.hN
stg.Plot.RxStep([CN100_ChN.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                  CN10R21_i.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_G, Name="CN100/ {C.hN}+2*H2 -> {C.hN+H.hC}+(3/2)H2",
                 Hover=HoverList, Color=CoNiColor1, **LineProps100, StepSpan=.2)
# CN/R21 C.h+H.f->CH.h
stg.Plot.RxStepTS([CN10R21_i.Gibbs(**GibbsOpts), CN10R21_d.Gibbs(**GibbsOpts), CN10R21_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_G, Name='CN/R21: C.hN + H.hC -> CH.hN',
                   Hover=HoverList, Color=CoNiColor1, **LineProps100)

# ---- CH->CH2
# Jump C/ R21 -> R9
stg.Plot.RxStep([CN10R21_f.Gibbs(**GibbsOpts) + (3. / 2.) * H2.Gibbs(**GibbsOpts),
                  CN10R9_i.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_G, Name='CN/{CH.hN}+H(3/2)2->{CH.hN+h.hC}+H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps100)
# CN/R9 CH.hN+H.hC->CH2.hNb
stg.Plot.RxStepTS([CN10R9_i.Gibbs(**GibbsOpts), CN10R9_d.Gibbs(**GibbsOpts), CN10R9_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_G, Name='CN/R9: CH.hN + H.hC -> CH2.hNb',
                   Hover=HoverList, Color=CoNiColor1, **LineProps100)

# ---- CH2->CH3
# Jump C/ R9 -> R10-C
stg.Plot.RxStep([CN10R9_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts),
                  CN10R10tCbC_i.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_G, Name='CN/{CH2.hN}+H2->{CH2.hN+h.hN}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps100)
# CN/R10 tCbC
stg.Plot.RxStepTS([CN10R10tCbC_i.Gibbs(**GibbsOpts),
                    CN10R10tCbC_TS.Gibbs(**GibbsOpts),
                    CN10R10tCbC_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_G, Name='CN/R10-C: CH2.hN + H.hN -> CH3.bC',
                   Hover=HoverList, Color=CoNiColor1, **LineProps100)

# ---- CH3->CH4
# Jump N/ R10 -> R11N (mantiene CH3)
stg.Plot.RxStep([CN10R10tCbC_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  CN10R11N_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_G, Name='CN/{CH3.bC}+(1/2)H2->{CH3.bC+h.hN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps100)
# CN10/R11N: CH3btC + H.h -> CH4.g
stg.Plot.RxStepTS([CN10R11N_i.Gibbs(**GibbsOpts), CN10R11N_TS.Gibbs(**GibbsOpts), CN10R11N_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_G, Name='CN/R11N: CH3bC + H.h -> CH4.g',
                   Hover=HoverList, Color=CoNiColor1, **LineProps100)
# ---- Physisorption
stg.Plot.RxStep([CN10R11N_f.Gibbs(**GibbsOpts), CN100.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_G, Name='CN/{}CH4.gf->{}+CH4',
                 Hover=HoverList, StepSpan=.4, Color=CoNiColor1, **LineProps100)

# -------------------------------- Ramification

# ---- CH2->CH3

# Jump C/ R9 -> R10-N
RefCN100_G_tail2 = RefCN100_G.branch(Step=4)
stg.Plot.RxStep([CN10R9_f.Gibbs(**GibbsOpts) + H2.Gibbs(**GibbsOpts),
                  CN10R10tN_i.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_G_tail2, Name='CN/{CH2.hN}+H2->{CH2.hN+h.hN}+(1/2)H2',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps100)
# CN/R10 tN
stg.Plot.RxStepTS([CN10R10tN_i.Gibbs(**GibbsOpts), CN10R10tN_TS.Gibbs(**GibbsOpts), CN10R10tN_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_G_tail2, Name='CN/R10-N: CH2.hN + H.hC -> CH3.bN',
                   Hover=HoverList, Color=CoNiColor1, StepSpan=1., **LineProps100)

# ---- CH3->CH4

# Jump C/ R10 -> R11C (rota CH3)
stg.Plot.RxStep([CN10R10tN_f.Gibbs(**GibbsOpts) + .5 * H2.Gibbs(**GibbsOpts),
                  CN10R11C_i.Gibbs(**GibbsOpts)],
                 Ref=RefCN100_G_tail2, Name='{CH3.bC}+(1/2)H2->{CH3.bN(rot)+H.hN}',
                 Hover=HoverList, StepSpan=.2, Color=CoNiColor1, **LineProps100)
# CN10/R11C: CH3btN + Hh -> CH4.g
stg.Plot.RxStepTS([CN10R11C_i.Gibbs(**GibbsOpts), CN10R11C_TS.Gibbs(**GibbsOpts), CN10R11C_f.Gibbs(**GibbsOpts)],
                   Ref=RefCN100_G_tail2, Name='CN/R11C: CH3bC + H.h -> CH4.g',
                   Hover=HoverList, Color=CoNiColor1, **LineProps100)

# Check full plot
if ShowGlobal_G:
    RefCN_G_full = RefCN100_G.branch(Step=0)
    stg.Plot.RxStep([CN100_ChN.Gibbs(**GibbsOpts) + 2 * H2.Gibbs(**GibbsOpts),
                      CN100.Gibbs(**GibbsOpts) + CH4_g.Gibbs(**GibbsOpts)],
                     Ref=RefCN_G_full, Name="CN10/{C.hN}+2*H2 -> {}+CH4",
                     Hover=HoverList, Color="lime", StepSpan=4.4, **LineProps100)
    RefCN_G_full.PlotExtend(Until=11., Color="lime", **LineProps100)

# ------------------------------------------------------------------------------------------------ Ending subplot

stg.Plot.ActivateHover(HoverList, fig)
Ley = [Line2D([0], [0], color="k", linewidth=3, linestyle=(0,(1,1)), alpha=1.),
       Line2D([0], [0], color="r", linewidth=3, linestyle='solid', alpha=1.)]
plt.axes(axs[0])
plt.ylabel("Free Gibbs Energy (kJ/mol)")
# Invisible heigh adjust
plt.scatter([0., 0.],[200, -150], alpha=0.)
# Lefft plot
plt.tick_params(axis="y", direction="in")
# other plots
for iax in axs[1:]:
    plt.axes(iax)
    plt.tick_params(axis="y", direction="inout", length=6.)
# all plots
for iax in axs:
    plt.axes(iax)
    plt.axhline(y=0., color="k", alpha=.8, linewidth=1.2)
    plt.xlabel(f"Reaction coordinate $\longrightarrow$")
    iax.set_xticks([])
    # Legend
    plt.legend(Ley, ["(111)", "(100)"],
               prop={'size': 8, 'weight':'bold'}, loc='lower center', handlelength=4, framealpha=0., ncol=2)

plt.savefig("./EnergyProfile_Gibbs_CHx_raw.png", dpi=180)
plt.show()
