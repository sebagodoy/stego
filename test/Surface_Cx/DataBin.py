# This is a IDERx bin file, it contains the models used for other computations
#   NAME:          Cx
#   Last Edited:   21-jun-2022
#   Notes:
#       Energías necesarias para cálculos de Cx en superficies
#       Nivel de precisión convergencia geom PREC, luego cómputo AccCore, para Bader y DDEC

# Load module
from IDERx import ItemClasses as Model
from IDERx.Params import eV2kJpmol
from IDERx.Plot import RxStep as prx
from IDERx.Plot import Align_Rx_Ticks as fixax
from IDERx.Plot import RxRef as refrx
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D

C_gas = Model.Gas(Name="C.gas", G_ID='0', Acc='E7', E0=-1.26572903, dipolE0=0.)

# Ni(100)  ------------------------------------------------------------------------------------------------------
N10 = Model.CleanSurf(Name='N10', G_ID="k384", Acc='E6G001', E0=-291.86035891, dipolE0=0.02888413)
N10_AC = Model.CleanSurf(Name='N10.Ac', G_ID="2730", Acc='Ac.E7G001', E0=-291.83856508, dipolE0=0.02686400)

N10_C1_h_Ac = Model.AdsSurf(Name='N10.C1.h', G_ID="k40", Acc='Ac.E6G002', E0=-300.89096721, dipolE0=0.03188079)
N10_C2_1_Ac = Model.AdsSurf(Name='N10.C2.1', G_ID="k39", Acc='Ac.E6G002', E0=-307.84546297, dipolE0=0.04887185)
N10_C3_1_Ac = Model.AdsSurf(Name='N10.C3.1', G_ID="k37", Acc='Ac.E6G002', E0=-314.47128470, dipolE0=0.04336959)
N10_C4_1_Ac = Model.AdsSurf(Name='N10.C4.1', G_ID="k43", Acc='Ac.E6G002', E0=-324.51508335, dipolE0=0.03310696)

N10_C1_h = Model.AdsSurf(Name='N10.C1.h', G_ID="1786", Acc='E6G002', E0=-300.91532256, dipolE0=0.03402243)
N10_C2_1 = Model.AdsSurf(Name='N10.C2.1', G_ID="k28", Acc='E6G002', E0=-307.87109881, dipolE0=0.05145535)
N10_C3_1 = Model.AdsSurf(Name='N10.C3.1.ring', G_ID="k35", Acc='E6G002', E0=-314.49778451, dipolE0=0.04583623)
N10_C3_2 = Model.AdsSurf(Name='N10.C3.2', G_ID="k50", Acc='E6G002', E0=-317.04825803, dipolE0=0.03811805)
N10_C4_1 = Model.AdsSurf(Name='N10.C4.1', G_ID="k42", Acc='E6G002', E0=-324.54178722, dipolE0=0.03516097)
N10_C5_2 = Model.AdsSurf(Name='N10.C5.2-angle', G_ID="k47", Acc='E6G002', E0=-332.61877607, dipolE0=0.03532789)
N10_C5_1 = Model.AdsSurf(Name='N10.C5.2', G_ID="k77", Acc='E6G002', E0=-333.61766323, dipolE0=0.03626420)

# Ni(111)  ------------------------------------------------------------------------------------------------------
N11 = Model.CleanSurf(Name='N11', G_ID="1812", Acc="E6G001", E0=-298.23685034, dipolE0=0.08464490)
N11_Ac = Model.CleanSurf(Name='N11.Ac', G_ID="2719", Acc="E7G001", E0=-298.21906475, dipolE0=0.07967661)

N11_C1_h = Model.AdsSurf(Name='N11.C1.h', G_ID='1897', Acc='E6G002', E0=-305.97119766, dipolE0=0.10239186)
N11_C2_h = Model.AdsSurf(Name='N11.C2.h', G_ID='k99', Acc='E6G002', E0=-314.14457552, dipolE0=0.11574089)
N11_C3_h = Model.AdsSurf(Name='N11.C3.h', G_ID='k103', Acc='E6G002', E0=-322.15438191, dipolE0=0.09967583)
N11_C4_h = Model.AdsSurf(Name='N11.C4.h', G_ID='k105', Acc='E6G002', E0=-330.38100711, dipolE0=0.09602473)
N11_C5_h = Model.AdsSurf(Name='N11.C5.h', G_ID='k101', Acc='E6G002', E0=-338.37267234, dipolE0=0.08685297)

# Co(100)  ------------------------------------------------------------------------------------------------------
# C10 = Model.CleanSurf(Name="C10", G_ID=445, Acc="E5G005", E0=-387.61323262)
C10 = Model.CleanSurf(Name="C10", G_ID='k339', Acc="E6G002", E0=-387.67035442, dipolE0=0.00005354)
C10_Ac = Model.CleanSurf(Name="C10.Ac", G_ID=2731, Acc="E7G001.Ac", E0=-387.58288278, dipolE0=0.04428590)

C10_C1_h = Model.AdsSurf(Name='C10.C1.h', G_ID=1787, Acc='E6G001', E0=-396.49207873, dipolE0=0.05551126)
C10_C2_1 = Model.AdsSurf(Name='C10.C2.1', G_ID="k51", Acc='E6G002', E0=-403.63434413, dipolE0=0.07677805)
C10_C3_1 = Model.AdsSurf(Name='C10.C3.1', G_ID="k53", Acc='E6G002', E0=-412.71708667, dipolE0=0.06321049)
C10_C4_1 = Model.AdsSurf(Name='C10.C4.1', G_ID="k55", Acc='E6G002', E0=-420.23037344, dipolE0=0.06691070)
C10_C5_1 = Model.AdsSurf(Name='C10.C5.1', G_ID="k57", Acc='E6G002', E0=-429.34747965, dipolE0=0.06538243)

# Co(111)  ------------------------------------------------------------------------------------------------------
C11 = Model.CleanSurf(Name="C11", G_ID="1809", Acc="E6G001", E0=-395.91283095, dipolE0=0.07322467)
C11_Ac = Model.CleanSurf(Name="C11.Ac", G_ID="2722", Acc="E7G001.Ac", E0=-395.87360142, dipolE0=0.06921275)

C11_C1_h = Model.AdsSurf(Name='C11.C1.h', G_ID='1926', Acc='E6G002', E0=-403.66326927, dipolE0=0.08299258)
C11_C2_h = Model.AdsSurf(Name='C11.C2.h', G_ID='k84', Acc='E6G002', E0=-411.92881384, dipolE0=0.09829902)
C11_C3_h = Model.AdsSurf(Name='C11.C3.h', G_ID='k87', Acc='E6G002', E0=-420.04459573, dipolE0=0.08417886)
C11_C4_h = Model.AdsSurf(Name='C11.C4.h', G_ID='k89', Acc='E6G002', E0=-428.22107248, dipolE0=0.08319192)
C11_C5_h = Model.AdsSurf(Name='C11.C5.h', G_ID='k97', Acc='E6G002', E0=-436.30217392, dipolE0=0.07813765)

# CoNi(100)  ----------------------------------------------------------------------------------------------------
CN10 = Model.CleanSurf(Name="CN10", G_ID=1783, Acc="E6G001", E0=-339.92495377, dipolE0=0.01142035)
CN10_Ac = Model.CleanSurf(Name="CN10.Ac", G_ID=2736, Acc="E7G001-Ac", E0=-339.89196827, dipolE0=0.01078257)

CN10_C1_hN = Model.AdsSurf(Name="CN10.C1.hN", G_ID=1784, Acc="E6G002", E0=-348.69773036, dipolE0=0.01619079)
CN10_C2_hN = Model.AdsSurf(Name="CN10.C2.hN", G_ID="k58", Acc="E6G002", E0=-356.15102747, dipolE0=0.02670676)
CN10_C3_hN = Model.AdsSurf(Name="CN10.C3.hN", G_ID="k60", Acc="E6G002", E0=-364.88058230, dipolE0=0.01960657)
CN10_C4_hN = Model.AdsSurf(Name="CN10.C4.hN", G_ID="k66", Acc="E6G002", E0=-372.39018645, dipolE0=0.01977503)
CN10_C5_hN = Model.AdsSurf(Name="CN10.C5.hN", G_ID="k74", Acc="E6G001", E0=-381.47736027, dipolE0=0.01898612)

# CoNi(111)  ----------------------------------------------------------------------------------------------------
CN11 = Model.CleanSurf(Name="CN11", G_ID="1813", Acc="E6G001", E0=-346.99558518, dipolE0=0.11304503)
CN11_Ac = Model.CleanSurf(Name="CN11.Ac", G_ID="2723", Acc="E7G001.Ac", E0=-346.96734829, dipolE0=0.10674556)

CN11_C1_hN = Model.AdsSurf(Name='CN11.C1.hN', G_ID='1945', Acc='E6G002', E0=-354.74895445, dipolE0=0.12609037)
CN11_C2_hN = Model.AdsSurf(Name='CN11.C2.hN', G_ID='k107', Acc='E6G002', E0=-362.90703410, dipolE0=0.14047628)
CN11_C3_hN = Model.AdsSurf(Name='CN11.C3.hN', G_ID='k110', Acc='E6G002', E0=-370.68947782, dipolE0=0.12335593)
CN11_C4_hN = Model.AdsSurf(Name='CN11.C4.hN', G_ID='k109', Acc='E6G002', E0=-379.13603386, dipolE0=0.11951823)
CN11_C5_hN = Model.AdsSurf(Name='CN11.C5.hN', G_ID='k111', Acc='E6G002', E0=-387.28906017, dipolE0=0.11637611)

CN11_C2t_hN = Model.AdsSurf(Name='CN11.C2t.hN', G_ID='k108', Acc='E6G002', E0=-363.00233328, dipolE0=0.14046175)
CN11_C3t_hN = Model.AdsSurf(Name='CN11.C3t.hN', G_ID='k112', Acc='E6G002', E0=-370.89760711, dipolE0=0.12287377)
CN11_C4t_hN = Model.AdsSurf(Name='CN11.C4t.hN', G_ID='k113', Acc='E6G002', E0=-379.14753243, dipolE0=0.12020599)
CN11_C5t_hN = Model.AdsSurf(Name='CN11.C5t.hN', G_ID='k114', Acc='E6G002', E0=-387.19774310, dipolE0=0.11233208)




# ----------------------------------------------------------------------------------------------------------------------




fig, axs = plt.subplots(2,5)
plt.subplots_adjust(left=0.05, right=.95, top=.95, bottom=.05)



# ......................................................................................................................
# Plot  direct values ...............................................................................................[0]
# {Cx}
plt.axes(axs[0][0])
plt.title("Direct values")
# Ni(100)
plt.scatter([i for i in range(4)], [N10_C1_h_Ac.E0, N10_C2_1_Ac.E0, N10_C3_1_Ac.E0, N10_C4_1_Ac.E0],
         marker='o', color='purple', label="Ni(100)-Ac")
plt.scatter([i for i in range(5)], [N10_C1_h.E0, N10_C2_1.E0, N10_C3_1.E0, N10_C4_1.E0, N10_C5_2.E0],
         marker='x', color='purple', label="Ni(100)")
plt.scatter([2, 4], [N10_C3_2.E0, N10_C5_1.E0], marker='+', color='purple')
# Co(100)
plt.scatter([i for i in range(5)], [C10_C1_h.E0, C10_C2_1.E0, C10_C3_1.E0, C10_C4_1.E0, C10_C5_1.E0],
         marker='x',color='g', label="Co(100)")
# CoNi(100)
plt.scatter([i for i in range(5)], [CN10_C1_hN.E0, CN10_C2_hN.E0, CN10_C3_hN.E0, CN10_C4_hN.E0, CN10_C5_hN.E0],
         marker='x',color='b', label="CoNi(100)")
plt.legend()

# ........................................................
plt.axes(axs[1][0])
plt.title("Direct values")
# Ni(111)
plt.scatter([i for i in range(5)], [N11_C1_h.E0, N11_C2_h.E0, N11_C3_h.E0, N11_C4_h.E0, N11_C5_h.E0],
         marker='x',color='purple', label="Ni(111)")
# Co(111)
plt.scatter([i for i in range(5)], [C11_C1_h.E0, C11_C2_h.E0, C11_C3_h.E0, C11_C4_h.E0, C11_C5_h.E0],
         marker='x',color='g', label="Co(111)")
# CoNi(111)-Line
plt.scatter([i for i in range(5)], [CN11_C1_hN.E0, CN11_C2_hN.E0, CN11_C3_hN.E0, CN11_C4_hN.E0, CN11_C5_hN.E0],
         marker='x',color='b', label="CoNi(111)-line")
# CoNi(111)-trans
plt.scatter([i for i in range(3)], [CN11_C1_hN.E0, CN11_C2t_hN.E0, CN11_C3t_hN.E0],
         marker='x',color='r', label="CoNi(111)-trans")


plt.legend()

# ......................................................................................................................
# Plot  from C gas ..................................................................................................[1]
# {Cx} + C(5-x) - {} - 5C
plt.axes(axs[0][1])
plt.title("From C gas")
# Ni(100)
plt.plot([i for i in range(1,6)], [1*N10_C1_h.E0 + 4*C_gas.E0 - N10.E0 - 5*C_gas.E0,
                                   1*N10_C2_1.E0 + 3*C_gas.E0 - N10.E0 - 5*C_gas.E0,
                                   1*N10_C3_2.E0 + 2*C_gas.E0 - N10.E0 - 5*C_gas.E0,
                                   1*N10_C4_1.E0 + 1*C_gas.E0 - N10.E0 - 5*C_gas.E0,
                                   1*N10_C5_1.E0 + 0*C_gas.E0 - N10.E0 - 5*C_gas.E0],
         marker='x', color='purple', label="Ni(100)")
plt.scatter([2], [1*N10_C3_1.E0 + 2*C_gas.E0 - N10.E0 - 5*C_gas.E0], marker="o", color='purple')
plt.scatter([4], [1*N10_C5_2.E0 + 0*C_gas.E0 - N10.E0 - 5*C_gas.E0], marker="o", color='purple')
# Co(100)
plt.plot([i for i in range(1,6)], [1*C10_C1_h.E0 + 4*C_gas.E0 - C10.E0 - 5*C_gas.E0,
                                   1*C10_C2_1.E0 + 3*C_gas.E0 - C10.E0 - 5*C_gas.E0,
                                   1*C10_C3_1.E0 + 2*C_gas.E0 - C10.E0 - 5*C_gas.E0,
                                   1*C10_C4_1.E0 + 1*C_gas.E0 - C10.E0 - 5*C_gas.E0,
                                   1*C10_C5_1.E0 + 0*C_gas.E0 - C10.E0 - 5*C_gas.E0],
         marker='x', color='g', label="Co(100)")
# CoNi(100)
plt.plot([i for i in range(1,6)], [1*CN10_C1_hN.E0 + 4*C_gas.E0 - CN10.E0 - 5*C_gas.E0,
                                   1*CN10_C2_hN.E0 + 3*C_gas.E0 - CN10.E0 - 5*C_gas.E0,
                                   1*CN10_C3_hN.E0 + 2*C_gas.E0 - CN10.E0 - 5*C_gas.E0,
                                   1*CN10_C4_hN.E0 + 1*C_gas.E0 - CN10.E0 - 5*C_gas.E0,
                                   1*CN10_C5_hN.E0 + 0*C_gas.E0 - CN10.E0 - 5*C_gas.E0
                                   ],
         marker='x', color='b', label="CoNi(100)")

plt.legend()


plt.axes(axs[1][1])
plt.title("From C gas")
# Ni(111)
plt.plot([i for i in range(1,6)], [1*N11_C1_h.E0 + 4*C_gas.E0 - N11.E0 - 5*C_gas.E0,
                                   1*N11_C2_h.E0 + 3*C_gas.E0 - N11.E0 - 5*C_gas.E0,
                                   1*N11_C3_h.E0 + 2*C_gas.E0 - N11.E0 - 5*C_gas.E0,
                                   1*N11_C4_h.E0 + 1*C_gas.E0 - N11.E0 - 5*C_gas.E0,
                                   1*N11_C5_h.E0 + 0*C_gas.E0 - N11.E0 - 5*C_gas.E0],
         marker='x', color='purple', label="Ni(111)")
# Co(111)
plt.plot([i for i in range(1,6)], [1*C11_C1_h.E0 + 4*C_gas.E0 - C11.E0 - 5*C_gas.E0,
                                   1*C11_C2_h.E0 + 3*C_gas.E0 - C11.E0 - 5*C_gas.E0,
                                   1*C11_C3_h.E0 + 2*C_gas.E0 - C11.E0 - 5*C_gas.E0,
                                   1*C11_C4_h.E0 + 1*C_gas.E0 - C11.E0 - 5*C_gas.E0,
                                   1*C11_C5_h.E0 + 0*C_gas.E0 - C11.E0 - 5*C_gas.E0],
         marker='x', color='green', label="Co(111)")
# CoNi(111)
plt.plot([i for i in range(1,6)], [1*CN11_C1_hN.E0 + 4*C_gas.E0 - CN11.E0 - 5*C_gas.E0,
                                   1*CN11_C2_hN.E0 + 3*C_gas.E0 - CN11.E0 - 5*C_gas.E0,
                                   1*CN11_C3_hN.E0 + 2*C_gas.E0 - CN11.E0 - 5*C_gas.E0,
                                   1*CN11_C4_hN.E0 + 1*C_gas.E0 - CN11.E0 - 5*C_gas.E0,
                                   1*CN11_C5_hN.E0 + 0*C_gas.E0 - CN11.E0 - 5*C_gas.E0],
         marker='x', color='blue', label="CoNi(111)")


# Plot desde C en sup values ...........................................................................................
# {Cx} + (5-x){C} + (x-1){} - 5{C}
plt.axes(axs[0][2])
plt.title("Desde *C surf")
# Ni(100)
# plt.plot([i for i in range(1,5)], [4*N10_C1_h_Ac.E0                               - 4*N10_C1_h_Ac.E0,
#                                    2*N10_C1_h_Ac.E0 +   N10_C2_1_Ac.E0 +   N10.E0 - 4*N10_C1_h_Ac.E0,
#                                    1*N10_C1_h_Ac.E0 +   N10_C3_1_Ac.E0 + 2*N10.E0 - 4*N10_C1_h_Ac.E0,
#                                                         N10_C4_1_Ac.E0 + 3*N10.E0 - 4*N10_C1_h_Ac.E0],
#          marker='x', color='purple', label="Ni(100)-Ac")

plt.plot([i for i in range(1,6)], [5*N10_C1_h.E0                            - 5*N10_C1_h.E0,
                                   3*N10_C1_h.E0 +   N10_C2_1.E0 +   N10.E0 - 5*N10_C1_h.E0,
                                   2*N10_C1_h.E0 +   N10_C3_2.E0 + 2*N10.E0 - 5*N10_C1_h.E0,
                                     N10_C1_h.E0 +   N10_C4_1.E0 + 3*N10.E0 - 5*N10_C1_h.E0,
                                                     N10_C5_1.E0 + 4*N10.E0 - 5*N10_C1_h.E0],
         marker='o', color='purple', label="Ni(100)")
# plt.plot(3, 2*N10_C1_h.E0 +   N10_C3_1.E0 + 2*N10.E0 - 5*N10_C1_h.E0, marker='+', color='purple')

# Co(100)
plt.plot([i for i in range(1,6)], [5*C10_C1_h.E0                               - 5*C10_C1_h.E0,
                                   3*C10_C1_h.E0 +   C10_C2_1.E0 +   C10_Ac.E0 - 5*C10_C1_h.E0,
                                   2*C10_C1_h.E0 +   C10_C3_1.E0 + 2*C10_Ac.E0 - 5*C10_C1_h.E0,
                                     C10_C1_h.E0 +   C10_C4_1.E0 + 3*C10_Ac.E0 - 5*C10_C1_h.E0,
                                                     C10_C5_1.E0 + 4*C10_Ac.E0 - 5*C10_C1_h.E0],
         marker='o', color='g', label="Co(100)")

# CoNi(100)
plt.plot([i for i in range(1,6)], [5*CN10_C1_hN.E0                               - 5*CN10_C1_hN.E0,
                                   3*CN10_C1_hN.E0 +   CN10_C2_hN.E0 +   CN10.E0 - 5*CN10_C1_hN.E0,
                                   2*CN10_C1_hN.E0 +   CN10_C3_hN.E0 + 2*CN10.E0 - 5*CN10_C1_hN.E0,
                                   1*CN10_C1_hN.E0 +   CN10_C4_hN.E0 + 3*CN10.E0 - 5*CN10_C1_hN.E0,
                                                       CN10_C5_hN.E0 + 4*CN10.E0 - 5*CN10_C1_hN.E0
                                   ],
         marker='x', color='b', label="CoNi(100)")

plt.legend()

plt.axes(axs[1][2])
plt.title("Desde *C surf")
# Ni(111)
plt.plot([i for i in range(1,6)], [5*N11_C1_h.E0                            - 5*N11_C1_h.E0,
                                   3*N11_C1_h.E0 +   N11_C2_h.E0 +   N11.E0 - 5*N11_C1_h.E0,
                                   2*N11_C1_h.E0 +   N11_C3_h.E0 + 2*N11.E0 - 5*N11_C1_h.E0,
                                     N11_C1_h.E0 +   N11_C4_h.E0 + 3*N11.E0 - 5*N11_C1_h.E0,
                                                     N11_C5_h.E0 + 4*N11.E0 - 5*N11_C1_h.E0],
         marker='x', color='purple', label="Ni(111)")

# Co(111)
plt.plot([i for i in range(1,6)], [5*C11_C1_h.E0                            - 5*C11_C1_h.E0,
                                   3*C11_C1_h.E0 +   C11_C2_h.E0 +   C11.E0 - 5*C11_C1_h.E0,
                                   2*C11_C1_h.E0 +   C11_C3_h.E0 + 2*C11.E0 - 5*C11_C1_h.E0,
                                     C11_C1_h.E0 +   C11_C4_h.E0 + 3*C11.E0 - 5*C11_C1_h.E0,
                                                     C11_C5_h.E0 + 4*C11.E0 - 5*C11_C1_h.E0],
         marker='x', color='green', label="Co(111)")
# CoNi(111)
plt.plot([i for i in range(1,6)], [5*CN11_C1_hN.E0                               - 5*CN11_C1_hN.E0,
                                   3*CN11_C1_hN.E0 +   CN11_C2_hN.E0 +   CN11.E0 - 5*CN11_C1_hN.E0,
                                   2*CN11_C1_hN.E0 +   CN11_C3_hN.E0 + 2*CN11.E0 - 5*CN11_C1_hN.E0,
                                     CN11_C1_hN.E0 +   CN11_C4_hN.E0 + 3*CN11.E0 - 5*CN11_C1_hN.E0,
                                                       CN11_C5_hN.E0 + 4*CN11.E0 - 5*CN11_C1_hN.E0],
         marker='x', color='blue', label="CoNi(111)")



# Plot stepwise .....................................................................................................[3]
# {Cx} + (5-x){C} + (x-1){} - ( {C(x-1)} + (5-x-1){C} + (x-2){} )
plt.axes(axs[0][3])
plt.title("Steepwise")
# Ni(100)
plt.plot([i for i in range(1,6)],
         [5*N10_C1_h.E0                            - 5*N10_C1_h.E0,
          3*N10_C1_h.E0 +   N10_C2_1.E0 +   N10.E0 - 5*N10_C1_h.E0,
          2*N10_C1_h.E0 +   N10_C3_2.E0 + 2*N10.E0 - (3*N10_C1_h.E0 +   N10_C2_1.E0 +   N10.E0),
            N10_C1_h.E0 +   N10_C4_1.E0 + 3*N10.E0 - (2*N10_C1_h.E0 +   N10_C3_2.E0 + 2*N10.E0),
            N10_C5_2.E0 + 4*N10.E0                  - ( N10_C1_h.E0 +   N10_C4_1.E0 + 3*N10.E0)],
         marker='o', color='purple', label="Ni(100)")

# Co(100)
plt.plot([i for i in range(1,6)],
         [5*C10_C1_h.E0                               - 5*C10_C1_h.E0,
          3*C10_C1_h.E0 +   C10_C2_1.E0 +   C10_Ac.E0 - 5*C10_C1_h.E0,
          2*C10_C1_h.E0 +   C10_C3_1.E0 + 2*C10_Ac.E0 - (3*C10_C1_h.E0 +   C10_C2_1.E0 +   C10_Ac.E0),
            C10_C1_h.E0 +   C10_C4_1.E0 + 3*C10_Ac.E0 - (2*C10_C1_h.E0 +   C10_C3_1.E0 + 2*C10_Ac.E0),
            C10_C5_1.E0                 + 4*C10_Ac.E0 - (  C10_C1_h.E0 +   C10_C4_1.E0 + 3*C10_Ac.E0)],
         marker='o', color='g', label="Co(100)")
plt.legend()

# Plot profile from C gas ...........................................................................................[4]
plt.axes(axs[0][4])
plt.title("Direct values(100)")
# Ni(100)
N10Ref = refrx(0,((4*N10.E0 + 4*C_gas.E0)-(4*N10_C1_h.E0))*eV2kJpmol)
# N10Ref = refrx(0,0)
prx([5*N10.E0 + 5*C_gas.E0      ,   5*N10_C1_h.E0],         Ref=N10Ref, Color='purple')
prx([2*N10_C1_h.E0              ,   N10_C2_1.E0 + N10.E0],  Ref=N10Ref, Color='purple')
prx([N10_C2_1.E0 + N10_C1_h.E0  ,   N10_C3_2.E0 + N10.E0],  Ref=N10Ref, Color='purple')
prx([N10_C3_2.E0 + N10_C1_h.E0  ,   N10_C4_1.E0 + N10.E0],  Ref=N10Ref, Color='purple')
prx([N10_C4_1.E0 + N10_C1_h.E0  ,   N10_C5_1.E0 + N10.E0],  Ref=N10Ref, Color='purple')

# Co(100)
C10Ref = refrx(0,((4*C10.E0 + 4*C_gas.E0)-(4*C10_C1_h.E0))*eV2kJpmol)
# C10Ref = refrx(0,0)
prx([5*C10.E0 + 5*C_gas.E0,     5*C10_C1_h.E0], Name="C10: 5{}+5C -> 5{C}", Ref=C10Ref, Color="g")
prx([2*C10_C1_h.E0,             C10_C2_1.E0 + C10.E0], Name="C10: {C}+{C} -> {C2}+{}", Ref=C10Ref, Color='g')
prx([C10_C2_1.E0+C10_C1_h.E0,   C10_C3_1.E0 + C10.E0], Name='C10: {C2}+{C} -> {C3}+{}', Ref=C10Ref, Color='g')
prx([C10_C3_1.E0+C10_C1_h.E0,   C10_C4_1.E0 + C10.E0], Name='C10: {C3}+{C} -> {C4}+{}', Ref=C10Ref, Color='g')
prx([C10_C4_1.E0+C10_C1_h.E0,   C10_C5_1.E0 + C10.E0], Name='C10: {C4}+{C} -> {C5}+{}', Ref=C10Ref, Color='g')

# CoNi(100)
CN10Ref = refrx(0,((4*CN10.E0 + 4*C_gas.E0)-(4*CN10_C1_hN.E0))*eV2kJpmol)
# CN10Ref = refrx(0,0)
prx([5*CN10.E0 + 5*C_gas.E0,        5*CN10_C1_hN.E0], Name="CN10: 5{}+5C -> 5{C}", Ref=CN10Ref, Color="b")
prx([2*CN10_C1_hN.E0,               CN10_C2_hN.E0 + CN10.E0], Name="CN10: {C}+{C} -> {C2}+{}", Ref=CN10Ref, Color='b')
prx([CN10_C2_hN.E0+CN10_C1_hN.E0,   CN10_C3_hN.E0 + CN10.E0], Name='CN10: {C2}+{C} -> {C3}+{}', Ref=CN10Ref, Color='b')
prx([CN10_C3_hN.E0+CN10_C1_hN.E0,   CN10_C4_hN.E0 + CN10.E0], Name='CN10: {C3}+{C} -> {C4}+{}', Ref=CN10Ref, Color='b')
prx([CN10_C4_hN.E0+CN10_C1_hN.E0,   CN10_C5_hN.E0 + CN10.E0], Name='CN10: {C4}+{C} -> {C5}+{}', Ref=CN10Ref, Color='b')


# Plot profile from C gas ...........................................................................................[4]
plt.axes(axs[1][4])
plt.title("Direct values(111)")
# Ni(111)
N11Ref = refrx(0,((4*N11.E0 + 4*C_gas.E0)-(4*N11_C1_h.E0))*eV2kJpmol)
# N11Ref = refrx(0,0)
prx([5*N11.E0 + 5*C_gas.E0      ,   5*N11_C1_h.E0],         Ref=N11Ref, Color='purple')
prx([2*N11_C1_h.E0              ,   N11_C2_h.E0 + N11.E0],  Ref=N11Ref, Color='purple')
prx([N11_C2_h.E0 + N11_C1_h.E0  ,   N11_C3_h.E0 + N11.E0],  Ref=N11Ref, Color='purple')
prx([N11_C3_h.E0 + N11_C1_h.E0  ,   N11_C4_h.E0 + N11.E0],  Ref=N11Ref, Color='purple')
prx([N11_C4_h.E0 + N11_C1_h.E0  ,   N11_C5_h.E0 + N11.E0],  Ref=N11Ref, Color='purple')

# Co(111)
C11Ref = refrx(0,((4*C11.E0 + 4*C_gas.E0)-(4*C11_C1_h.E0))*eV2kJpmol)
# C11Ref = refrx(0,0)
prx([5*C11.E0 + 5*C_gas.E0      ,   5*C11_C1_h.E0],         Ref=C11Ref, Color='g')
prx([2*C11_C1_h.E0              ,   C11_C2_h.E0 + C11.E0],  Ref=C11Ref, Color='g')
prx([C11_C2_h.E0 + C11_C1_h.E0  ,   C11_C3_h.E0 + C11.E0],  Ref=C11Ref, Color='g')
prx([C11_C3_h.E0 + C11_C1_h.E0  ,   C11_C4_h.E0 + C11.E0],  Ref=C11Ref, Color='g')
prx([C11_C4_h.E0 + C11_C1_h.E0  ,   C11_C5_h.E0 + C11.E0],  Ref=C11Ref, Color='g')

# CoNi(111)
CN11Ref = refrx(0,((4*CN11.E0 + 4*C_gas.E0)-(4*CN11_C1_hN.E0))*eV2kJpmol)
# CN11Ref = refrx(0,0)
prx([5*CN11.E0 + 5*C_gas.E0         ,   5*CN11_C1_hN.E0],         Ref=CN11Ref, Color='b')
prx([2*CN11_C1_hN.E0                ,   CN11_C2_hN.E0 + CN11.E0],  Ref=CN11Ref, Color='b')
prx([CN11_C2_hN.E0 + CN11_C1_hN.E0  ,   CN11_C3_hN.E0 + CN11.E0],  Ref=CN11Ref, Color='b')
prx([CN11_C3_hN.E0 + CN11_C1_hN.E0  ,   CN11_C4_hN.E0 + CN11.E0],  Ref=CN11Ref, Color='b')
prx([CN11_C4_hN.E0 + CN11_C1_hN.E0  ,   CN11_C5_hN.E0 + CN11.E0],  Ref=CN11Ref, Color='b')






CustomLegend = [Line2D([0], [0], color="purple", lw=1., linestyle="solid"),
                Line2D([0], [0], color="green", lw=1., linestyle="solid"),
                Line2D([0], [0], color="blue", lw=1., linestyle="solid")]
# axs[0][4].legend(CustomLegend, ["Ni(100)", "Co(100)", "CoNi(100)"], loc = "upper left",
#               facecolor='white', edgecolor="white", framealpha=1., prop={'size':10})


plt.axes(axs[0][4])
plt.xlim([1,11])
plt.axes(plt.gca()).set_xticks([2,4,6,8,10])
plt.axes(plt.gca()).get_xaxis().set_ticklabels([])

plt.ylim([-800, -700])
plt.axes(plt.gca()).set_yticks([i for i in range(-800, -399, 100)])
print(plt.yticks())
plt.grid()


plt.axes(axs[1][4])
plt.xlim([1,11])
plt.axes(plt.gca()).set_xticks([2,4,6,8,10])
plt.axes(plt.gca()).get_xaxis().set_ticklabels([])

plt.ylim([-680, -580])
plt.axes(plt.gca()).set_yticks([i for i in range(-800, -599, 50)])
print(plt.yticks())
plt.grid()

plt.savefig('/home/seba/Thesis/IDERx/test/Surface_Cx/C_all_chain_raw.png', bbox_inches='tight')
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

fig, axs = plt.subplots(1, 2, figsize=(6,5))
plt.subplots_adjust(left=0.15, right=.95, top=.92, bottom=.10, wspace=.25)

PropsNi = {'LineStyle':'solid', 'LineWidth':1.4, 'AlphaLines':1., 'Color':'purple'}
PropsCo = {'LineStyle':'dashed', 'LineWidth':1.4, 'AlphaLines':1., 'Color':'green'}
PropsCN = {'LineStyle':'dashdot', 'LineWidth':1.4, 'AlphaLines':1., 'Color':'blue'}
PropsCNt = {'LineStyle':'dotted', 'LineWidth':1.4, 'AlphaLines':1., 'Color':'red'}

plt.axes(axs[1])
plt.title("Direct values(100)")
# Ni(100)
N10Ref = refrx(2,((N10_C1_h.E0)-(N10.E0 + C_gas.E0))*eV2kJpmol)
# N10Ref = refrx(0,((4*N10.E0 + 4*C_gas.E0)-(4*N10_C1_h.E0))*eV2kJpmol)
# N10Ref = refrx(0,0)
# prx([5*N10.E0 + 5*C_gas.E0      ,   5*N10_C1_h.E0],         Ref=N10Ref, **PropsNi)
prx([2*N10_C1_h.E0              ,   N10_C2_1.E0 + N10.E0],  Ref=N10Ref, **PropsNi)
prx([N10_C2_1.E0 + N10_C1_h.E0  ,   N10_C3_2.E0 + N10.E0],  Ref=N10Ref, **PropsNi)
prx([N10_C3_2.E0 + N10_C1_h.E0  ,   N10_C4_1.E0 + N10.E0],  Ref=N10Ref, **PropsNi)
prx([N10_C4_1.E0 + N10_C1_h.E0  ,   N10_C5_1.E0 + N10.E0],  Ref=N10Ref, **PropsNi)

# Co(100)
C10Ref = refrx(2,((C10_C1_h.E0)-(C10.E0 + C_gas.E0))*eV2kJpmol)
# C10Ref = refrx(0,((4*C10.E0 + 4*C_gas.E0)-(4*C10_C1_h.E0))*eV2kJpmol)
# C10Ref = refrx(0,0)
# prx([5*C10.E0 + 5*C_gas.E0,     5*C10_C1_h.E0], Name="C10: 5{}+5C -> 5{C}", Ref=C10Ref, **PropsCo)
prx([2*C10_C1_h.E0,             C10_C2_1.E0 + C10.E0], Name="C10: {C}+{C} -> {C2}+{}", Ref=C10Ref, **PropsCo)
prx([C10_C2_1.E0+C10_C1_h.E0,   C10_C3_1.E0 + C10.E0], Name='C10: {C2}+{C} -> {C3}+{}', Ref=C10Ref, **PropsCo)
prx([C10_C3_1.E0+C10_C1_h.E0,   C10_C4_1.E0 + C10.E0], Name='C10: {C3}+{C} -> {C4}+{}', Ref=C10Ref, **PropsCo)
prx([C10_C4_1.E0+C10_C1_h.E0,   C10_C5_1.E0 + C10.E0], Name='C10: {C4}+{C} -> {C5}+{}', Ref=C10Ref, **PropsCo)

# CoNi(100)
CN10Ref = refrx(2,((CN10_C1_hN.E0)-(CN10.E0 + C_gas.E0))*eV2kJpmol)
# CN10Ref = refrx(0,((4*CN10.E0 + 4*C_gas.E0)-(4*CN10_C1_hN.E0))*eV2kJpmol)
# CN10Ref = refrx(0,0)
# prx([5*CN10.E0 + 5*C_gas.E0,        5*CN10_C1_hN.E0], Name="CN10: 5{}+5C -> 5{C}", Ref=CN10Ref, **PropsCN)
prx([2*CN10_C1_hN.E0,               CN10_C2_hN.E0 + CN10.E0], Name="CN10: {C}+{C} -> {C2}+{}", Ref=CN10Ref, **PropsCN)
prx([CN10_C2_hN.E0+CN10_C1_hN.E0,   CN10_C3_hN.E0 + CN10.E0], Name='CN10: {C2}+{C} -> {C3}+{}', Ref=CN10Ref, **PropsCN)
prx([CN10_C3_hN.E0+CN10_C1_hN.E0,   CN10_C4_hN.E0 + CN10.E0], Name='CN10: {C3}+{C} -> {C4}+{}', Ref=CN10Ref, **PropsCN)
prx([CN10_C4_hN.E0+CN10_C1_hN.E0,   CN10_C5_hN.E0 + CN10.E0], Name='CN10: {C4}+{C} -> {C5}+{}', Ref=CN10Ref, **PropsCN)


# Plot profile from C gas ...........................................................................................[4]
plt.axes(axs[0])
plt.title("Direct values(111)")
# Ni(111)
N11Ref = refrx(2,((N11_C1_h.E0)-(N11.E0 + C_gas.E0))*eV2kJpmol)
# N11Ref = refrx(0,((4*N11.E0 + 4*C_gas.E0)-(4*N11_C1_h.E0))*eV2kJpmol)
# N11Ref = refrx(0,0)
# prx([5*N11.E0 + 5*C_gas.E0      ,   5*N11_C1_h.E0],         Ref=N11Ref, **PropsNi)
prx([2*N11_C1_h.E0              ,   N11_C2_h.E0 + N11.E0],  Ref=N11Ref, **PropsNi)
prx([N11_C2_h.E0 + N11_C1_h.E0  ,   N11_C3_h.E0 + N11.E0],  Ref=N11Ref, **PropsNi)
prx([N11_C3_h.E0 + N11_C1_h.E0  ,   N11_C4_h.E0 + N11.E0],  Ref=N11Ref, **PropsNi)
prx([N11_C4_h.E0 + N11_C1_h.E0  ,   N11_C5_h.E0 + N11.E0],  Ref=N11Ref, **PropsNi)

# Co(111)
C11Ref = refrx(2,((C11_C1_h.E0)-(C11.E0 + C_gas.E0))*eV2kJpmol)
# C11Ref = refrx(0,((4*C11.E0 + 4*C_gas.E0)-(4*C11_C1_h.E0))*eV2kJpmol)
# C11Ref = refrx(0,0)
# prx([5*C11.E0 + 5*C_gas.E0      ,   5*C11_C1_h.E0],         Ref=C11Ref, **PropsCo)
prx([2*C11_C1_h.E0              ,   C11_C2_h.E0 + C11.E0],  Ref=C11Ref, **PropsCo)
prx([C11_C2_h.E0 + C11_C1_h.E0  ,   C11_C3_h.E0 + C11.E0],  Ref=C11Ref, **PropsCo)
prx([C11_C3_h.E0 + C11_C1_h.E0  ,   C11_C4_h.E0 + C11.E0],  Ref=C11Ref, **PropsCo)
prx([C11_C4_h.E0 + C11_C1_h.E0  ,   C11_C5_h.E0 + C11.E0],  Ref=C11Ref, **PropsCo)

# CoNi(111)
CN11Ref = refrx(2,((CN11_C1_hN.E0)-(CN11.E0 + C_gas.E0))*eV2kJpmol)
# CN11Ref = refrx(0,((4*CN11.E0 + 4*C_gas.E0)-(4*CN11_C1_hN.E0))*eV2kJpmol)
# CN11Ref = refrx(0,0)
# prx([5*CN11.E0 + 5*C_gas.E0         ,   5*CN11_C1_hN.E0],         Ref=CN11Ref, **PropsCN)
prx([2*CN11_C1_hN.E0                ,   CN11_C2_hN.E0 + CN11.E0],  Ref=CN11Ref, **PropsCN)
prx([CN11_C2_hN.E0 + CN11_C1_hN.E0  ,   CN11_C3_hN.E0 + CN11.E0],  Ref=CN11Ref, **PropsCN)
prx([CN11_C3_hN.E0 + CN11_C1_hN.E0  ,   CN11_C4_hN.E0 + CN11.E0],  Ref=CN11Ref, **PropsCN)
prx([CN11_C4_hN.E0 + CN11_C1_hN.E0  ,   CN11_C5_hN.E0 + CN11.E0],  Ref=CN11Ref, **PropsCN)

# CoNi(111) - trans
CN11tRef = refrx(2,((CN11_C1_hN.E0)-(CN11.E0 + C_gas.E0))*eV2kJpmol)
# CN11Ref = refrx(0,((4*CN11.E0 + 4*C_gas.E0)-(4*CN11_C1_hN.E0))*eV2kJpmol)
# CN11Ref = refrx(0,0)
# prx([5*CN11.E0 + 5*C_gas.E0         ,   5*CN11_C1_hN.E0],         Ref=CN11Ref, **PropsCN)
prx([2*CN11_C1_hN.E0                ,   CN11_C2t_hN.E0 + CN11.E0],  Ref=CN11tRef, **PropsCNt)
prx([CN11_C2t_hN.E0 + CN11_C1_hN.E0  ,   CN11_C3t_hN.E0 + CN11.E0],  Ref=CN11tRef, **PropsCNt)
prx([CN11_C3t_hN.E0 + CN11_C1_hN.E0  ,   CN11_C4t_hN.E0 + CN11.E0],  Ref=CN11tRef, **PropsCNt)
prx([CN11_C4t_hN.E0 + CN11_C1_hN.E0  ,   CN11_C5t_hN.E0 + CN11.E0],  Ref=CN11tRef, **PropsCNt)


CustomLegend = [Line2D([0], [0], color="purple", lw=1.5, linestyle="solid"),
                Line2D([0], [0], color="green", lw=1.5, linestyle="dashed"),
                Line2D([0], [0], color="blue", lw=1.5, linestyle="dashdot"),
                Line2D([0], [0], color="red", lw=1.5, linestyle="dotted")]



plt.axes(axs[1])
plt.axes(plt.gca()).set_xticks([2,4,6,8,10])
plt.ylim([-840, -380])
# plt.axes(plt.gca()).set_yticks([i for i in range(-800, -399, 100)])
plt.gca().legend(CustomLegend, ["Ni(100)", "Co(100)", "NiCo(100)"],
                 loc = "lower right", facecolor='white', edgecolor="white", framealpha=1., handlelength=4,
                 prop={'size':8}, bbox_to_anchor=(1.,.05))

plt.axes(axs[0])
plt.ylabel("Energy (kJ/mol)", fontsize=12)
plt.axes(plt.gca()).set_xticks([2,4,6,8,10])
plt.ylim([-840, -380])
# plt.axes(plt.gca()).set_yticks([i for i in range(-800, -499, 100)])
plt.gca().legend(CustomLegend, ["Ni(111)", "Co(111)", "NiCo(111)-l", "NiCo(100)-t"],
                 loc = "lower left", facecolor='white', edgecolor="white", framealpha=1., handlelength=4,
                 prop={'size':8}, bbox_to_anchor=(.0,.05))


labeldict = {1:'b) (100)', 0:'a) (111)'}
for k in range(2):
    plt.axes(axs[k])
    plt.xlim([1.5, 10.5])
    plt.grid()
    plt.xlabel(r"$*C_x + *C\longrightarrow *C_{x+1}+*$", fontweight='bold', fontsize = 12)
    plt.axes(plt.gca()).get_xaxis().set_ticklabels([])
    plt.gca().tick_params(axis='both', which='major', labelsize=10)
    for i in range(1,5):
        plt.annotate(r'x='+str(i), xy=[i, i],xytext=[i*2+1, 0.02],
                         xycoords=('data', 'axes fraction'), textcoords=('data', 'axes fraction'),
                         ha='center', va='center', size=10, color='k', fontweight='bold',
                         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=.0))
    plt.annotate(labeldict[k], xy=[i, i], xytext=[.08, 0.95],
                 xycoords='axes fraction', textcoords='axes fraction',
                 ha='left', va='center', size=10, color='k', fontweight='bold', fontsize=12,
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec='k', lw=0., alpha=1.0))



# plt.savefig('/home/seba/Thesis/Graphics/C_chain_raw.png', bbox_inches='tight')
plt.savefig('/home/seba/Thesis/IDERx/test/Surface_Cx/C_chain_raw.png', bbox_inches='tight')




plt.show()