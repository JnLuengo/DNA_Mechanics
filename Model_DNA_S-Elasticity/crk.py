import math

def crook(comp):
    
    num=0
    den=0

    errnum=0
    errden=0

    hk = [0.3322,0.3234,0.349006,0.291422,0.33144,0.330882,0.348286,0.281748,0.310609,0.347632]
    lk = [0.3548,0.3894,0.353096,0.380861,0.371571,0.364367,0.351759,0.3771,0.373526,0.350717]
    
    errhk = [5.7783e-05,2.1620e-04,0.000166033,0.000169531,0.000159135,0.000155969,0.000265121,0.000274753,0.000125921,0.000123905]
    errlk = [8.0188e-05,2.3615e-04,9.34255e-05,0.000100234,0.000165642,0.000177131,9.66957e-05,0.000103368,0.000135781,0.000139226]

    for k in range(10):
        num+=comp[k]*hk[k]
        den+=comp[k]*lk[k]

        errnum+=(comp[k]*errhk[k])**2
        errden+=(comp[k]*errlk[k])**2

    errnum=math.sqrt(errnum)
    errden=math.sqrt(errden)

    errcr=(1/math.sqrt(1-(num/den)**2)/den*errnum)**2 + (num/math.sqrt(1-(num/den)**2)/den**2*errden)**2
    errcr=math.sqrt(errcr)

    cr=math.acos(num/den)

    allcr=[cr,errcr]

    return(allcr)

def sumlj(comp):

    slj=0
    errslj=0

    lk = [0.3548,0.3894,0.353096,0.380861,0.371571,0.364367,0.351759,0.3771,0.373526,0.350717]
    errlk = [8.0188e-05,2.3615e-04,9.34255e-05,0.000100234,0.000165642,0.000177131,9.66957e-05,0.000103368,0.000135781,0.000139226]

    for k in range(10):
        slj+=comp[k]*lk[k]
        errslj+=(comp[k]*errlk[k])**2

    errslj=math.sqrt(errslj)
    allslj=[slj,errslj]

    return(allslj)

def crstiff(allcr):

    parm = [93570.6794686375,552.761190029697,10.1023666203498]
    errparm = [12637.7076391763,31.9078788108333,0.38856779860459]

    Kcr = parm[0]*math.exp(-parm[2]*allcr[0]) +  parm[1]

    errKcr = errparm[1]**2 + (math.exp(-parm[2]*allcr[0])*errparm[0])**2
    errKcr += (parm[0]*allcr[0]*math.exp(-parm[2]*allcr[0])*errparm[2])**2 + (parm[0]*parm[2]*math.exp(-parm[2]*allcr[0])*allcr[1])**2
    errKcr = math.sqrt(errKcr)
    allKcr=[Kcr,errKcr]

    return(allKcr)
