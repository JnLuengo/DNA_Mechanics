import sys
from tensorflow.keras.models import load_model
import numpy as np
from pathlib import Path

lp_mean = 57.092876401100135
lp_std = 7.27999126659362

if len(sys.argv) < 2:
    print("Error: no input file")
    sys.exit(1)

filename = sys.argv[1]

# Load model
ROOT = Path(__file__).resolve().parent
model = load_model(ROOT / "final_model_ANN.keras")
#print(model.summary()) # Model summary

postrims = ["AAA", "AAC", "AAG", "AAT", "ACA", "ACC", "ACG", "ACT", "AGA", "AGC", "AGG", 
            "ATA", "ATC", "ATG", "CAA", "CAC", "CAG", "CCA", "CCC", "CCG", "CGA", "CGC", 
            "CTA", "CTC", "GAA", "GAC", "GCA", "GCC", "GGA", "GTA", "TAA", "TCA"] # Possible trimers
alttrims = ["TTT", "GTT", "CTT", "ATT", "TGT", "GGT", "CGT", "AGT", "TCT", "GCT", "CCT", 
            "TAT", "GAT", "CAT", "TTG", "GTG", "CTG", "TGG", "GGG", "CGG", "TCG", "GCG", 
            "TAG", "GAG", "TTC", "GTC", "TGC", "GGC", "TCC", "TAC", "TTA", "TGA"] # Alternative trimers

valid_bases = {"A", "C", "G", "T"} # set of valid bases

with open(filename, "r") as f:
    for line in f:
        sequence = line.strip()

        if not sequence:
            continue  #skip empty lines

        if any(base not in valid_bases for base in sequence): # ckech whether all bases in valid_bases
            print(f"Error: invalid base found in sequence {line}.") # end if non-valid character is found
            sys.exit(1)

        trimcomp = [0]*32 # content list
        seqlength = len(sequence)

        for i in range(seqlength-2):
            trim=sequence[i:i+3] # go through all trimers

            for k in range(32):
                if trim==postrims[k] or trim==alttrims[k]:
                    trimcomp[k]+=1 # assign trimer to content list

        normalization = sum(trimcomp)
        X_sample = [x / normalization for x in trimcomp[:31]] # normalized 31 features expected by the model
        X_sample = np.array([X_sample], dtype=np.float64) # correct format
        y_pred = model.predict(X_sample, verbose=0)[0][0]

        print(sequence, y_pred*lp_std+lp_mean) # output sequence, prediction
