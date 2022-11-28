# Database for the

import stego.items as Model

# ----------------------------------------------------------------------------------------------------------------------
# Molecular information from RPBE-DFT and reference (McQuarrie & Simon)

# WARNING: CH4 freqs from McQuarrie & Simon
CH4_g = Model.Gas(Name='CH4', E0=-24.03491563, dipolE0=0.,
                  Acc='Full', TS=False, G_ID='CH4.gas_Local_UltraHighRes_Box15',
                  F_ID='freqs from McQuarrie & Simon',
                  # FreqR=[2898.29495187837, 1515.1757782002, 1515.1757782002, 3002.55016597471, 3002.55016597471,
                  #        3002.55016597471, 1299.71500240109, 1299.71500240109, 1299.71500240109],
                  FreqR=[3088.351691, 3086.406086, 3080.600334, 2967.887746, 1519.931601, 1516.585642,
                         1296.27073, 1295.587467, 1291.591103],
                  Geometry='Poliatomic', Mass=16.04,
                  RotT=[7.54, 7.54, 7.54], RotSymNum=12)

# WARNING: CH4 freqs from McQuarrie & Simon
H2 = Model.Gas(Name='H2-gas',
               G_ID=0, E0=-6.98503949, dipolE0=0., Acc='E7G001', TS=False,
               F_ID=0, FreqR=[4354.140143],
               Geometry='Diatomic homonuclear', Mass=2.0,
               RotT=85.3, RotSymNum=2)

# WARNING: CO Rot T from McQuarrie & Simon
CO = Model.Gas(Name="CO",
                G_ID='CO.gas_Local_UltraHighRes', E0=-14.42576166, dipolE0=0.00000721, Acc="E7G0.01/", TS=False,
                F_ID='My own', FreqR=[2104.300781],
                Geometry='Diatomic heteronuclear', Mass=28.01,
                RotT=2.77, RotSymNum=1)

CO2 = Model.Gas(Name='CO2',
                G_ID='local:CO2.gas_Local_UltraHighRes',
                E0=-22.26736244, Acc='E7G0.01/', TS=False, dipol=0.,
                F_ID='McQuarrie', FreqR=[2346.518228, 1306.083546, 627.736721, 627.259647],
                Geometry='Diatomic homonuclear', Mass=44.01,
                RotT=0.561, RotSymNum=2)

H2O = Model.Gas(Name='H2O',
                G_ID='ads',
                E0=-14.14745554,Acc='E7G001', TS=False, dipolE0=0.00126900,
                F_ID='McQuarrie',
                Geometry='Poliatomic', Mass=18.00, FreqR=[3833.413608, 3721.047191, 1597.447164],
                RotT=[40.1, 20.9, 13.4], RotSymNum=2)

# ----------------------------------------------------------------------------------------------------------------------
# Parameters for the Shomate equation

NH3_NIST	= {	'A':19.99563,'B':49.77119,'C':-15.37599,'D':1.921168,'E':0.189174,'F':-53.30667,
				'G':203.8591,'H':-45.89806,'H0f':-45.90,'S0f':192.77}

H2_NIST		= {	'A':33.066178,'B':-11.363417,'C':11.432816,'D':-2.772874,'E':-0.158558,'F':-9.980797,
				'G':172.707974,'H':0.,'H0f':0.,'S0f':130.68}

H2O_NIST 	= { 'A':30.09200, 'B':6.832514, 'C':6.793435, 'D':-2.534480, 'E':0.082139, 'F':-250.8810,
				'G':223.3967, 'H':-241.8264, 'H0f':-241.83, 'S0f':188.84}

CO2_NIST	= { 'A':24.99735, 'B':55.18696, 'C':-33.69137, 'D':7.948387, 'E':-0.136638, 'F':-403.6075,
				'G':228.2431, 'H':-393.5224, 'H0f':-393.52, 'S0f':213.79}

CO_NIST 	= { 'A':25.56759, 'B':6.096130, 'C':4.054656, 'D':-2.671301, 'E':0.131021, 'F':-118.0089,
			   'G':227.3665, 'H':-110.5271, 'H0f':-110.53, 'S0f':197.66}

CH4_NIST 	= { 'A':-0.703029, 'B':108.4773, 'C':-42.52157, 'D':5.862788, 'E':0.678565, 'F':-76.84376,
				'G':158.7163, 'H':-74.87310, 'H0f':-74.6, 'S0f':186.25}

N2_NIST_low	= { 'A':28.98641, 'B':1.853978, 'C':-9.647459, 'D':16.63537, 'E':0.000117, 'F':-8.671914,
				   'G':226.4168,'H':0.,'H0f':0.,'S0f':191.61}