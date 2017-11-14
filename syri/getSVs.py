#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:33:37 2017

@author: goel
"""
import os
import sys
import pandas as pd
from syri.synsearchFunctions import readSVData, getSV, getNotAligned

if __name__ == "__main__":
    if len(sys.argv) != 2:
#        print("Usage: python getSVs.py <path_to_coords_file>")
        sys.exit("Usage: getSVs <path_to_coords_file>")
    if len(sys.argv) == 2:
        fileLocation = sys.argv[1]   
#        fileLocation = "/netscratch/dep_coupland/grp_schneeberger/projects/SynSearch/testRuns/col_ler_Chr/out_m_i90_l100.coords"
    
    cwdPath = os.getcwd()+"/"
#    cwdPath = "/netscratch/dep_coupland/grp_schneeberger/projects/SynSearch/testRuns/col_ler_Chr/"
    coords = pd.read_table(fileLocation, header = None) 
    coords.columns  =   ["aStart","aEnd","bStart","bEnd","aLen","bLen","iden","aDir","bDir","aChr","bChr"]
    aChromo = set(coords["aChr"])
    bChromo = set(coords["bChr"])
    uniChromo = list(aChromo if len(aChromo) < len(bChromo) else bChromo)
    uniChromo.sort()
    ctxout = "ctxOut.txt"
    
    if ctxout not in os.listdir(cwdPath):
        print("No ctx Out file in directory. Exiting.")
        sys.exit()
    allAlignments = readSVData(cwdPath, uniChromo, ctxout)
    mumSNPIn = allAlignments[["aStart","aEnd","bStart","bEnd","aChr","bChr"]].copy()
    mumSNPIn.to_csv(cwdPath+"mumSNPIn.txt",sep="\t",header = False, index = False)
    getSV(cwdPath, allAlignments)
    
    getNotAligned(cwdPath, uniChromo, ctxout)
