#!/usr/bin/env python3
import composition
import crk
import stilde
import sys

if len(sys.argv)!=2:
    raise ValueError("Error: Input required: file name")
filename = sys.argv[1]

with open(filename, "r") as file:
    for sequence in file:
        sequence = sequence.strip()

#Order of composition array is AA, GG, AC, CA, AG, GA, AT, TA, CG, GC
#With alternative steps TT, CC, GT, TG, CT, TC, AT, TA, CG, GC

        composition.checkseq(sequence)
        comp=composition.compcomp(sequence)
        allcr=crk.crook(comp)
        allsl=crk.sumlj(comp)
        allKcr=crk.crstiff(allcr)
        allSt=stilde.estimate(allKcr,allsl,comp)

        #print(allcr)
        #print(allsl)
        #print(allKcr)
        print(allSt[0], allSt[1])

