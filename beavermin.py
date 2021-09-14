from gurobipy import *

m = Model('wakingbeaver')
##set X vairables to be binary
citylist = ['cm', 'ic', 'ms','pn','wb','b','a','ot','ah','d','p','ls','ss','ps']
lmarketlist = ['cm', 'pn','wb','a','ls']
yearlist = [2022,2023,2024,2025,2026,2027,2028,2029,2030,2031]

## Calculate the sumX of each city in all year
## Set a dictionary to store value of each city's sumX in all year into different SumX
x = m.addVars(citylist,yearlist, vtype=GRB.BINARY)
sumX = {}
for j in range (0,14):
    sumX[citylist[j]] = 0
    value = 0
    for i in range(0,10):
        value =  value + x[citylist[j],yearlist[i]]
    sumX[citylist[j]] = value


##set the coefficient (the total market share of each city) as variables for future changes
##mst represent market share in total
mstcm = 0.06
mstic = 0.028
mstms = 0.04
mstpn = 0.06
mstwb = 0.045
mstb = 0.028
msta = 0.06
mstot = 0.05
mstah = 0.05
mstd = 0.024
mstp = 0.035
mstls = 0.075
mstss = 0.045
mstps = 0.03

##msp represent market share in primary market for each city
mspcm = 0.04
mspic = 0.02
mspms = 0.03
msppn = 0.04
mspwb = 0.03
mspb = 0.02
mspa = 0.04
mspot = 0.03
mspah = 0.03
mspd = 0.02
mspp = 0.025
mspls = 0.05
mspss = 0.03
mspps = 0.025

##mss represent market share in primary market for each city
msscm = 0.02
mssic = 0.008
mssms = 0.01
msspn = 0.02
msswb = 0.015
mssb = 0.008
mssa = 0.02
mssot = 0.02
mssah = 0.02
mssd = 0.004
mssp = 0.01
mssls = 0.025
mssss = 0.015
mssps = 0.005



sum_city_allyear = 0
for j in range (0,14):
    sum_city_allyear = sum_city_allyear + sumX[citylist[j]]


##Objective Value setting
m.setObjective(sum_city_allyear , sense = GRB.MINIMIZE)

##Constraints
##Primary market share grows in 2022(3%)
##msp means primary market share
##mss means secondary market share

m.addConstr(mspcm *x['cm',2022] + mspic *x['ic',2022] + mspms *x['ms',2022] + msppn *x['pn',2022]
+ mspwb *x['wb',2022] + mspb *x['b',2022] + mspa * x['a',2022] + mspot *x['ot',2022] + mspah *x['ah',2022]
+ mspd *x['d',2022] + mspp *x['p',2022] + mspls *x['ls',2022] + mspss *x['ss',2022] + mspps *x['ps',2022] == 0.03)

priGrowth22 = mspcm *x['cm',2022] + mspic *x['ic',2022] + mspms *x['ms',2022] + msppn *x['pn',2022]
+ mspwb *x['wb',2022] + mspb *x['b',2022] + mspa * x['a',2022] + mspot *x['ot',2022] + mspah *x['ah',2022]
+ mspd *x['d',2022] + mspp *x['p',2022] + mspls *x['ls',2022] + mspss *x['ss',2022] + mspps *x['ps',2022]

m.addConstr(msscm *x['cm',2022] + mssic *x['ic',2022] + mssms *x['ms',2022] + msspn *x['pn',2022]
+ msswb *x['wb',2022] + mssb *x['b',2022] + mssa * x['a',2022] + mssot *x['ot',2022] + mssah *x['ah',2022]
+ mssd *x['d',2022] + mssp *x['p',2022] + mssls *x['ls',2022] + mssss *x['ss',2022] + mssps *x['ps',2022] == 0.02)

secGrowth22 = msscm *x['cm',2022] + mssic *x['ic',2022] + mssms *x['ms',2022] + msspn *x['pn',2022]
+ msswb *x['wb',2022] + mssb *x['b',2022] + mssa * x['a',2022] + mssot *x['ot',2022] + mssah *x['ah',2022]
+ mssd *x['d',2022] + mssp *x['p',2022] + mssls *x['ls',2022] + mssss *x['ss',2022] + mssps *x['ps',2022]

##Primary market share grows in 2023-2031(10%-16%):

m.addConstr(mspcm *sumX['cm'] + mspic *sumX['ic'] + mspms *sumX['ms'] + msppn *sumX['pn']
+ mspwb *sumX['wb'] + mspb *sumX['b'] + mspa *sumX['a'] + mspot *sumX['ot'] + mspah *sumX['ah']
+ mspd *sumX['d'] + mspp *sumX['p'] + mspls *sumX['ls'] + mspss *sumX['ss'] + mspps *sumX['ps'] - 0.03 >= 0.1)

m.addConstr(mspcm *sumX['cm'] + mspic *sumX['ic'] + mspms *sumX['ms'] + msppn *sumX['pn']
+ mspwb *sumX['wb'] + mspb *sumX['b'] + mspa *sumX['a'] + mspot *sumX['ot'] + mspah *sumX['ah']
+ mspd *sumX['d'] + mspp *sumX['p'] + mspls *sumX['ls'] + mspss *sumX['ss'] + mspps *sumX['ps'] - 0.03 <= 0.16)

##Secondary market share grows in 2023-2031(6%-9%):
m.addConstr(msscm *sumX['cm'] + mssic *sumX['ic'] + mssms *sumX['ms'] + msspn *sumX['pn']
+ msswb *sumX['wb'] + mssb *sumX['b'] + mssa *sumX['a'] + mssot *sumX['ot'] + mssah *sumX['ah']
+ mssd *sumX['d'] + mssp *sumX['p'] + mssls *sumX['ls'] + mssss *sumX['ss'] + mssps *sumX['ps'] - 0.02 >= 0.06)

m.addConstr(msscm *sumX['cm'] + mssic *sumX['ic'] + mssms *sumX['ms'] + msspn *sumX['pn']
+ msswb *sumX['wb'] + mssb *sumX['b'] + mssa *sumX['a'] + mssot *sumX['ot'] + mssah *sumX['ah']
+ mssd *sumX['d'] + mssp *sumX['p'] + mssls *sumX['ls'] + mssss *sumX['ss'] + mssps *sumX['ps'] - 0.02 <= 0.09)

# ##Regional market share:
# total_market_share = mstcm *sumX['cm'] + mstic *sumX['ic'] + mstms *sumX['ms'] + mstpn *sumX['pn']
# + mstwb *sumX['wb'] + mstb *sumX['b'] + msta *sumX['a'] + mstot *sumX['ot'] + mstah *sumX['ah']
# + mstd *sumX['d'] + mstp *sumX['p'] + mstls *sumX['ls'] + mstss *sumX['ss'] + mstps *sumX['ps']
#
# ##mid-west
# m.addConstr(mstcm *sumX['cm'] + mstic *sumX['ic'] + mstms *sumX['ms'] >= total_market_share * 0.18)
# m.addConstr(mstcm *sumX['cm'] + mstic *sumX['ic'] + mstms *sumX['ms'] <= total_market_share * 0.22)
#
# # ##mid-atlantic
# m.addConstr(mstpn *sumX['pn']  >= total_market_share * 0.045)
# m.addConstr(mstpn *sumX['pn']  <= total_market_share * 0.055)
#
# # ##Northeast
# # m.addConstr(mstpn *sumX['pn'] + mstwb *sumX['wb'] + mstb *sumX['b'] >= total_market_share * 0.135)
# # m.addConstr(mstpn *sumX['pn'] + mstwb *sumX['wb'] + mstb *sumX['b'] <= total_market_share * 0.165)
#
# # ##Southeast
# # m.addConstr(msta *sumX['a'] + mstot *sumX['ot'] >= total_market_share * 0.225)
# # m.addConstr(msta *sumX['a'] + mstot *sumX['ot'] <= total_market_share * 0.275)
#
# # ##Southwest
# m.addConstr(mstah *sumX['ah'] + mstd *sumX['d'] + mstp *sumX['p'] >= total_market_share * 0.18)
# m.addConstr(mstah *sumX['ah'] + mstd *sumX['d'] + mstp *sumX['p'] <= total_market_share * 0.22)
#
# ##West
# m.addConstr(mstls *sumX['ls'] + mstss *sumX['ss'] + mstps *sumX['ps'] >= total_market_share * 0.135)
# m.addConstr(mstls *sumX['ls'] + mstss *sumX['ss'] + mstps *sumX['ps'] <= total_market_share * 0.165)

##General Constraints
m.addConstrs(x.sum('*',i) == 1 for i in range (2022,2024))
m.addConstrs(x.sum('*',i) <= 2 for i in range (2024,2032))
m.addConstrs(x[citylist[i],2022]+ x[citylist[i],2023] + x[citylist[i],2024] + x[citylist[i],2025]
+ x[citylist[i],2026] + x[citylist[i],2027] + x[citylist[i],2028] + x[citylist[i],2029] + x[citylist[i],2030]
+ x[citylist[i],2031] <= 1 for i in range(0,14))
m.addConstrs(x.sum(lmarketlist,i) <= 1 for i in yearlist)


m.optimize()

for i in range(0,10):
    for j in range(0,14):
        print(str(yearlist[i]) + '  ' + str(citylist[j]) + '  ' + str(x[citylist[j], yearlist[i]]))

print('Obj: %g' % m.objVal)








































































##
