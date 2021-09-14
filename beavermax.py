from gurobipy import *

m = Model('wakingbeaver')
##set X vairables to be binary
citylist = ['cm', 'ic', 'ms','pn','wb','b','a','ot','ah','d','p','ls','ss','ps']
lmarketlist = ['cm', 'pn','wb','a','ls']
yearlist = [2022,2023,2024,2025,2026,2027,2028,2029,2030,2031]

x = m.addVars(citylist,yearlist,vtype=GRB.BINARY)

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


##Objective Value setting
m.setObjective(mstcm *x.sum('cm','*') + mstic *x.sum('ic','*') + mstms *x.sum('ms','*') + mstpn *x.sum('pn','*')
+ mstwb *x.sum('wb','*') + mstb *x.sum('b','*') + msta *x.sum('a','*') + mstot *x.sum('ot','*') + mstah *x.sum('ah','*')
+ mstd *x.sum('d','*') + mstp *x.sum('p','*') + mstls *x.sum('ls','*') + mstss *x.sum('ss','*') + mstps *x.sum('ps','*') , sense = GRB.MAXIMIZE)

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

m.addConstr(mspcm *x.sum('cm','*') + mspic *x.sum('ic','*') + mspms *x.sum('ms','*') + msppn *x.sum('pn','*')
+ mspwb *x.sum('wb','*') + mspb *x.sum('b','*') + mspa *x.sum('a','*') + mspot *x.sum('ot','*') + mspah *x.sum('ah','*')
+ mspd *x.sum('d','*') + mspp *x.sum('p','*') + mspls *x.sum('ls','*') + mspss *x.sum('ss','*') + mspps *x.sum('ps','*') -0.03 >= 0.1)

m.addConstr(mspcm *x.sum('cm','*') + mspic *x.sum('ic','*') + mspms *x.sum('ms','*') + msppn *x.sum('pn','*')
+ mspwb *x.sum('wb','*') + mspb *x.sum('b','*') + mspa *x.sum('a','*') + mspot *x.sum('ot','*') + mspah *x.sum('ah','*')
+ mspd *x.sum('d','*') + mspp *x.sum('p','*') + mspls *x.sum('ls','*') + mspss *x.sum('ss','*') + mspps *x.sum('ps','*') -0.03 <= 0.16)

##Secondary market share grows in 2023-2031(6%-9%):
m.addConstr(msscm *x.sum('cm','*') + mssic *x.sum('ic','*') + mssms *x.sum('ms','*') + msspn *x.sum('pn','*')
+ msswb *x.sum('wb','*') + mssb *x.sum('b','*') + mssa *x.sum('a','*') + mssot *x.sum('ot','*') + mssah *x.sum('ah','*')
+ mssd *x.sum('d','*') + mssp *x.sum('p','*') + mssls *x.sum('ls','*') + mssss *x.sum('ss','*') + mssps *x.sum('ps','*')  -0.02 >= 0.06)

m.addConstr(msscm *x.sum('cm','*') + mssic *x.sum('ic','*') + mssms *x.sum('ms','*') + msspn *x.sum('pn','*')
+ msswb *x.sum('wb','*') + mssb *x.sum('b','*') + mssa *x.sum('a','*') + mssot *x.sum('ot','*') + mssah *x.sum('ah','*')
+ mssd *x.sum('d','*') + mssp *x.sum('p','*') + mssls *x.sum('ls','*') + mssss *x.sum('ss','*') + mssps *x.sum('ps','*')  -0.02 <= 0.09)

# # ##Regional market share:
# total_market_share = mstcm *x.sum('cm','*') + mstic *x.sum('ic','*') + mstms *x.sum('ms','*') + mstpn *x.sum('pn','*')
# + mstwb *x.sum('wb','*') + mstb *x.sum('b','*') + msta *x.sum('a','*') + mstot *x.sum('ot','*') + mstah *x.sum('ah','*')
# + mstd *x.sum('d','*') + mstp *x.sum('p','*') + mstls *x.sum('ls','*') + mstss *x.sum('ss','*') + mstps *x.sum('ps','*')
#
# # ##mid-west
# m.addConstr(mstcm *x.sum('cm','*') + mstic *x.sum('ic','*') + mstms *x.sum('ms','*') >= total_market_share * 0.18)
# m.addConstr(mstcm *x.sum('cm','*') + mstic *x.sum('ic','*') + mstms *x.sum('ms','*') <= total_market_share * 0.22)
#
# # # ##mid-atlantic
# m.addConstr(mstpn *x.sum('pn','*')  >= total_market_share * 0.045)
# m.addConstr(mstpn *x.sum('pn','*')  <= total_market_share * 0.055)
#
# # ##Northeast
# m.addConstr( mstwb *x.sum('wb','*') + mstb *x.sum('b','*') >= total_market_share * 0.135)
# m.addConstr( mstwb *x.sum('wb','*') + mstb *x.sum('b','*') <= total_market_share * 0.165)
#
# # # ##Southeast
# m.addConstr(msta *x.sum('a','*') + mstot *x.sum('ot','*') >= total_market_share * 0.225)
# m.addConstr(msta *x.sum('a','*') + mstot *x.sum('ot','*') <= total_market_share * 0.275)
#
# # # ##Southwest
# m.addConstr(mstah *x.sum('ah','*') + mstd *x.sum('d','*') + mstp *x.sum('p','*') >= total_market_share * 0.18)
# # m.addConstr(mstah *x.sum('ah','*') + mstd *x.sum('d','*') + mstp *x.sum('p','*') <= total_market_share * 0.22)
#
# # ##West
# m.addConstr(mstls *x.sum('ls','*') + mstss *x.sum('ss','*') + mstps *x.sum('ps','*') >= total_market_share * 0.135)
# # m.addConstr(mstls *x.sum('ls','*') + mstss *x.sum('ss','*') + mstps *x.sum('ps','*') <= total_market_share * 0.165)
#


##General Constraints
m.addConstrs(x.sum('*',i) == 1 for i in range (2022,2024))
m.addConstrs(x.sum('*',i) <= 2 for i in range (2024,2032))
m.addConstrs(x.sum(i,'*') <= 1 for i in citylist)
m.addConstrs(x.sum(lmarketlist,i) <= 1 for i in yearlist)


m.optimize()

for i in range(0,10):
    for j in range(0,14):
        print(str(yearlist[i]) + '  ' + str(citylist[j]) + '  ' + str(x[citylist[j], yearlist[i]]))

print('Obj: %g' % m.objVal)
# valuecity_allyear = {}
# for j in range(0,14):
#     value = 0
#     for i in range(1,10):
#         value = value + x[citylist[j],yearlist[i]].getAttr('x')
#     valuecity_allyear[citylist[j]] = value
# total_market_share = mstp *valuecity_allyear['p'] + mstls *valuecity_allyear['ls'] + mstss *valuecity_allyear['ss'] + mstps *valuecity_allyear['ps']
# print(valuecity_allyear)
# print(mstls *valuecity_allyear['ls'] + mstss *valuecity_allyear['ss'] + mstps *valuecity_allyear['ps'])
#
# print( total_market_share )





































































##
