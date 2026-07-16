import math

def estimate(allKcr,allsl,comp):

    allkstep = [1906.26,923.638,1037.41,13914.2,1311.59,1593.17,1185.21,4.06903e+07,1905.72,7899.67]
    errkstep = [4.423,4.285,8.86,1674.0,14.08,20.2,14.13,1.801e+10,42.33,675.7]

    suminv = 0
    errinv = 0

    for k in range(10):
        suminv += comp[k]*(1/allkstep[k])
        errinv += (comp[k]*errkstep[k]/allkstep[k]**2)**2

    errinv = math.sqrt(errinv)

    St = (1/allKcr[0]) + (0.1/allsl[0])*suminv
    St = 1/St

    errSt = (St**2/allKcr[0]**2*allKcr[1])**2 + (0.01*St**2/allsl[0]**2*suminv*10*allsl[1])**2 + (0.1*St**2/allsl[0]*errinv)**2
    errSt = math.sqrt(errSt)

    allSt = [St,errSt]

    return(allSt)
