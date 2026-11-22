COMPLEMENTARY_BASES = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C" 
}

VALID_BASES = {"A", "T", "C", "G"}

STEPS = ["AA","GG","AC","CA","AG","GA","AT","TA","CG","GC"]
ALTSTEPS = ["TT","CC","GT","TG","CT","TC","AT","TA","CG","GC"]

HK = [0.3322,0.3234,0.349006,0.291422,0.33144,0.330882,0.348286,0.281748,0.310609,0.347632]
LK = [0.3548,0.3894,0.353096,0.380861,0.371571,0.364367,0.351759,0.3771,0.373526,0.350717]
    
ERRHK = [5.7783e-05,2.1620e-04,0.000166033,0.000169531,0.000159135,0.000155969,0.000265121,0.000274753,0.000125921,0.000123905]
ERRLK = [8.0188e-05,2.3615e-04,9.34255e-05,0.000100234,0.000165642,0.000177131,9.66957e-05,0.000103368,0.000135781,0.000139226]

# Eq. 2, K_beta = A exp(-k beta) + Kinf, in the order [A, Kinf, k].
# Fit on bin means of all 10-bp fragments of the motif pool (beta bins of 0.02, weights 1/sd^2); reproducible pipeline and
# bootstrap over molecules described in the Supporting Information of the paper.
PARM_KBETA = [92223.73,545.380,10.00410]
# Bootstrap replicates of PARM_KBETA (columns A, Kinf, k); their spread is the parameter uncertainty of K_beta, including the
# strong correlations among A, Kinf and k (corr A-k 0.996).
KBETA_BOOTSTRAP_FILE = "data/kbeta_bootstrap.dat"

# Step compliances 1/k_Q (1/pN), same order as STEPS, fitted with Eq. 2 above (see Supporting Information) on all 10-bp
# fragments; TA has zero compliance (infinitely stiff step in the fit). Errors: asymptotic standard errors of the fit.
CSTEPS = [5.4023683983e-04,1.1170937689e-03,1.0028380316e-03,1.0676414945e-04,8.1566733823e-04,6.3907972520e-04,9.0190030394e-04,0.0000000000e+00,5.6499728801e-04,1.4175228505e-04]
ERRCSTEPS = [1.2e-06,5.0e-06,8.2e-06,8.6e-06,8.1e-06,7.9e-06,1.0e-05,1.1e-05,1.2e-05,1.1e-05]
