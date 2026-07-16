def checkseq(seq):
    bases = ["A", "T", "C", "G"]

    for bp in seq:
        if bp not in bases:
            raise ValueError("Invalid DNA sequence. One or more bases not A, T, C or G.")
    return seq


def compcomp(seq):
    comp = [0]*10
    arrsteps = ["AA","GG","AC","CA","AG","GA","AT","TA","CG","GC"]
    altsteps = ["TT","CC","GT","TG","CT","TC","AT","TA","CG","GC"]

    seqlength=len(seq)
    for i in range(seqlength-1):
        step=seq[i:i+2]

        for k in range(10):
            if step==arrsteps[k] or step==altsteps[k]:
                comp[k]+=1

    return comp
