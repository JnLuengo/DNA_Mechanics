import math
from config import VALID_BASES, COMPLEMENTARY_BASES, STEPS, HK, LK, ERRHK, ERRLK
from config import PARM_KBETA, ERRPARM_KBETA, KSTEPS, ERRKSTEPS

class Sequence:
    
    def __init__(self, sequence):
        self.sequence = sequence


    def validate(self):

        sequence = self.sequence
        if any (base.upper() not in VALID_BASES for base in sequence):
            raise ValueError("Invalid DNA sequence. Bases must be A, T, C or G.")


    def composition(self):
    
        sequence = self.sequence.upper()
        comp = [0]*10

        for i in range(len(sequence)-1):
            motif=sequence[i:i+2]

            for k in range(10):
                altmotif = ''.join([COMPLEMENTARY_BASES.get(base) for base in motif[::-1]])
                if motif==STEPS[k] or altmotif==STEPS[k]:
                    comp[k]+=1
        return comp


    def prediction_crookedness(self):
        
        comp = self.composition()
        num = 0
        den = 0
        errnum = 0
        errden = 0

        for k in range(10):
            num += comp[k]*HK[k]
            den += comp[k]*LK[k]
            errnum += (comp[k]*ERRHK[k])**2
            errden += (comp[k]*ERRLK[k])**2

        errnum = math.sqrt(errnum)
        errden = math.sqrt(errden)
        errcr = (1/math.sqrt(1-(num/den)**2)/den*errnum)**2
        errcr += (num/math.sqrt(1-(num/den)**2)/den**2*errden)**2
        
        errcr = math.sqrt(errcr)
        cr = math.acos(num/den)
        allcr = [cr, errcr]

        return allcr


    def prediction_sumlj(self):
        
        comp = self.composition()
        slj=0
        errslj=0

        for k in range(10):
            slj += comp[k]*LK[k]
            errslj += (comp[k]*ERRLK[k])**2

        errslj = math.sqrt(errslj)
        allslj = [slj, errslj]

        return allslj


    def prediction_Kbeta(self):

        allcr = self.prediction_crookedness()

        Kcr = PARM_KBETA[0]*math.exp(-PARM_KBETA[2]*allcr[0]) +  PARM_KBETA[1]

        errKcr = ERRPARM_KBETA[1]**2 + (math.exp(-PARM_KBETA[2]*allcr[0])*ERRPARM_KBETA[0])**2
        errKcr += (PARM_KBETA[0]*allcr[0]*math.exp(-PARM_KBETA[2]*allcr[0])*ERRPARM_KBETA[2])**2 + (PARM_KBETA[0]*PARM_KBETA[2]*math.exp(-PARM_KBETA[2]*allcr[0])*allcr[1])**2
        errKcr = math.sqrt(errKcr)

        allKcr = [Kcr, errKcr]

        return allKcr


    def prediction_Stilde(self):

        comp = self.composition()
        allKcr = self.prediction_Kbeta()
        allsl = self.prediction_sumlj()
        suminv = 0
        errinv = 0

        for k in range(10):
            suminv += comp[k]*(1/KSTEPS[k])
            errinv += (comp[k]*ERRKSTEPS[k]/KSTEPS[k]**2)**2

        errinv = math.sqrt(errinv)

        St = (1/allKcr[0]) + (0.1/allsl[0])*suminv
        St = 1/St

        errSt = (St**2/allKcr[0]**2*allKcr[1])**2 + (0.01*St**2/allsl[0]**2*suminv*10*allsl[1])**2 + (0.1*St**2/allsl[0]*errinv)**2
        errSt = math.sqrt(errSt)

        allSt = [St,errSt]

        return allSt