from computeindex import *
import glob
import sys, argparse, csv
import time
import pandas as p


outfileAllDataIndexTime= 'resultAnalysis.csv'
outfileIndex= 'resultAnalysis_indexes.csv'

f = open(outfileAllDataIndexTime, "w")
f.write("FILENAME,"
        "RPDlep,RPDlepT,"+
        "RPDlea,RPDleaT,"+
        "RPDlepr,RPDleprT,"+
        "RDPgep,RDPgepT,"+
        "RDPgea,RDPgeaT,"+
        "RDPgepr,RDPgeprT,"+
        "trendRPDlep,trendRPDlepT,"+
        "trendRPDlea,trendRPDleaT,"+
        "trendRPDlepr,trendRPDleprT,"+
        "trendRDPgep,trendRDPgepT,"+
        "trendRDPgea,trendRDPgeaT,"+
        "trendRDPgepr,trendRDPgeprT"+
        "\n")
f.close()


f = open(outfileIndex, "w")
f.write("FILENAME,"
        "RPDlep,trendRPDlep,"+
        "RPDlea,trendRPDlea,"+
        "RPDlepr,trendRPDlepr,"+
        "RDPgep,trendRDPgep,"+
        "RDPgea,trendRDPgea,"+
        "RDPgepr,trendRDPgepr,"+
        "\n")
f.close()

#dir_paths = ['02_csv_header/logistica_degrado_0_rndvalue.101_npoints.4_nbinomial.20.csv',
#               '02_csv_header/logistica_degrado_0_flip_rndvalue.801_npoints.100_nbinomial.100.csv']

#dir_paths = ['02_csv_header/logistica_degrado_1_rndvalue.1_npoints.20_nbinomial.20_cangle.0.01.csv']
#dir_paths = ['02_csv_header/logistica_degrado_0_flip*','02_csv_header/logistica_degrado_0_rnd*',
#             '02_csv_header/logistica_degrado_1_flip*','02_csv_header/logistica_degrado_1_rnd*',
#             '02_csv_header/logistica_degrado_2_flip*','02_csv_header/logistica_degrado_2_rnd*']
dir_paths = ['02_csv_header/*csv']


bigTot=len(dir_paths)
bigTotExecution=0
for searchPath in dir_paths:
    res = glob.glob(searchPath)
    fileTot=len(res)
    fileTotExecution=0
    bigTotExecution=bigTotExecution+1
    # firstFile=True
    for fin in res:
        #    if firstFile:
        fileTotExecution=fileTotExecution+1
        print(str(bigTotExecution) +"/" + str(bigTot) + " -- " + str(fileTotExecution) +"/" +
              str(fileTot) + " -- " + fin)
        firstFile=False
        df = p.read_csv(fin)
        df2 = df[['TREND']]

        trendRPDlepTi =round(time.time() * 1000)
        trendRPDlepIndex=RPDlep(df2.values)
        trendRPDlepIndex=trendRPDlepIndex[0]
        trendRPDlepTs = round(time.time() * 1000)
        trendRPDlepT=trendRPDlepTs-trendRPDlepTi

        trendRPDleaTi =round(time.time() * 1000)
        trendRPDleaIndex=RPDlea(df2.values)
        trendRPDleaIndex=trendRPDleaIndex[0]
        trendRPDleaTs = round(time.time() * 1000)
        trendRPDleaT=trendRPDleaTs-trendRPDleaTi

        trendRPDleprTi =round(time.time() * 1000)
        trendRPDleprIndex=RPDlepr(df2.values)
        trendRPDleprIndex=trendRPDleprIndex[0]
        trendRPDleprTs = round(time.time() * 1000)
        trendRPDleprT=trendRPDleprTs-trendRPDleprTi

        trendRDPgepTi =round(time.time() * 1000)
        trendRDPgepIndex=RDPgep(df2.values)
        trendRDPgepIndex=trendRDPgepIndex[0]
        trendRDPgepTs = round(time.time() * 1000)
        trendRDPgepT = trendRDPgepTs - trendRDPgepTi

        trendRDPgeaTi =round(time.time() * 1000)
        trendRDPgeaIndex=RDPgea(df2.values)
        trendRDPgeaIndex=trendRDPgeaIndex[0]
        trendRDPgeaTs = round(time.time() * 1000)
        trendRDPgeaT = trendRDPgeaTs - trendRDPgeaTi


        trendRDPgeprTi =round(time.time() * 1000)
        trendRDPgeprIndex=RDPgepr(df2.values)
        trendRDPgeprIndex=trendRDPgeprIndex[0]
        trendRDPgeprTs = round(time.time() * 1000)
        trendRDPgeprT = trendRDPgeprTs - trendRDPgeprTi

        #fileTotExecution = fileTotExecution + 1
        #print(str(bigTotExecution) + "/" + str(bigTot) + " -- " + str(fileTotExecution) + "/" + str(fileTot) + " -- " + fin)
        df = p.read_csv(fin)
        df2 = df[['RESULT']]
        RPDlepTi = round(time.time() * 1000)
        RPDlepIndex = RPDlep(df2.values)
        RPDlepIndex=RPDlepIndex[0]
        RPDlepTs = round(time.time() * 1000)
        RPDlepT = RPDlepTs - RPDlepTi

        RPDleaTi = round(time.time() * 1000)
        RPDleaIndex = RPDlea(df2.values)
        RPDleaIndex=RPDleaIndex[0]
        RPDleaTs = round(time.time() * 1000)
        RPDleaT = RPDleaTs - RPDleaTi

        RPDleprTi = round(time.time() * 1000)
        RPDleprIndex = RPDlepr(df2.values)
        RPDleprIndex=RPDleprIndex[0]
        RPDleprTs = round(time.time() * 1000)
        RPDleprT = RPDleprTs - RPDleprTi

        RDPgepTi = round(time.time() * 1000)
        RDPgepIndex= RDPgep(df2.values)
        RDPgepIndex=RDPgepIndex[0]
        RDPgepTs = round(time.time() * 1000)
        RDPgepT = RDPgepTs - RDPgepTi

        RDPgeaTi = round(time.time() * 1000)
        RDPgeaIndex = RDPgea(df2.values)
        RDPgeaIndex=RDPgeaIndex[0]
        RDPgeaTs = round(time.time() * 1000)
        RDPgeaT = RDPgeaTs - RDPgeaTi

        RDPgeprTi = round(time.time() * 1000)
        RDPgeprIndex = RDPgepr(df2.values)
        RDPgeprIndex=RDPgeprIndex[0]
        RDPgeprTs = round(time.time() * 1000)
        RDPgeprT = RDPgeprTs - RDPgeprTi

        f = open(outfileAllDataIndexTime, "a")
        f.write(fin + "," +
                str(RPDlepIndex) + "," + str(RPDlepT) + ","  +
                str(RPDleaIndex) + "," + str(RPDleaT) + "," +
                str(RPDleprIndex) + "," +str(RPDleprT) + "," +
                str(RDPgepIndex)+","+str(RDPgepT)+","+
                str(RDPgeaIndex)+","+str(RDPgeaT)+"," +
                str(RDPgeprIndex)+","+str(RDPgeprT)+"," +
                str(trendRPDlepIndex)+","+str(trendRPDlepT)+","+
                str(trendRPDleaIndex)+","+str(trendRPDleaT)+","+
                str(trendRPDleprIndex)+","+str(trendRPDleprT)+","+
                str(trendRDPgepIndex)+","+str(trendRDPgepT)+","+
                str(trendRDPgeaIndex)+","+str(trendRDPgeaT)+","+
                str(trendRDPgeprIndex)+","+str(trendRDPgeprT)+
                "\n" )
        f.close()
        f = open(outfileIndex, "a")
        f.write(fin + "," +
                str(round(RPDlepIndex,2)) + "," + str(round(trendRPDlepIndex,2)) + ","  +
                str(round(RPDleaIndex,2)) + "," + str(round(trendRPDleaIndex,2)) + "," +
                str(round(RPDleprIndex,2)) + "," +str(round(trendRPDleprIndex,2)) + "," +
                str(round(RDPgepIndex,2))+","+str(round(trendRDPgepIndex,2))+","+
                str(round(RDPgeaIndex,2))+","+str(round(trendRDPgeaIndex,2))+"," +
                str(round(RDPgeprIndex,2))+","+str(round(trendRDPgeprIndex,2))+"," +
                "\n" )
        f.close()



