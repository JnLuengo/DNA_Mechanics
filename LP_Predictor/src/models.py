from config import VALID_BASES, COMPLEMENTARY_BASES, TRIMERS, LP_MEAN, LP_STD
from tensorflow.keras.models import load_model
import numpy as np
from pathlib import Path

class Sequence:
    """
    Represents a DNA sequence and provides methods to compute sequence
    composition and predict structural and mechanical properties based on
    step-based physical models.

    Parameters
    ----------
    sequence : str
        DNA sequence composed the bases: A, T, C, G.
    """

    ROOT = Path(__file__).resolve().parent.parent
    model = load_model(ROOT / "final_model_ANN.keras")

    def __init__(self, sequence):
        """
        Initialize a Sequence object.

        Parameters
        ----------
        sequence : str
            DNA sequence.
        """
        self.sequence = sequence


    def validate(self):
        """
        Checks that DNA sequence contains only valid bases.

        Raises
        ------
        ValueError
            If the sequence contains characters other than A, T, C, G, 
            or corresponding lower cases. 
        """

        sequence = self.sequence
        if any (base.upper() not in VALID_BASES for base in sequence):
            raise ValueError("Invalid DNA sequence. Bases must be A, T, C or G.")


    def composition(self):
        """
        Computes trimer (trinucleotide) composition of the DNA sequence.

        List of possible trimers provided in TRIMERS (list).
        Reverse-complement equivalent trimers are counted together.

        Returns
        -------
        list of int
            List containing the occurrence count of each trimer in
            the order defined by TRIMERS.
        """
    
        sequence = self.sequence.upper()
        comp = [0]*32

        for i in range(len(sequence)-2):
            motif=sequence[i:i+3]

            for k in range(32):
                altmotif = ''.join([COMPLEMENTARY_BASES.get(base) for base in motif[::-1]])
                if motif==TRIMERS[k] or altmotif==TRIMERS[k]:
                    comp[k]+=1
        return comp


    def prediction_LP(self):
        """
                Uses model loaded as class attribute to compute prediction of LP.

                Calls method composition() and prepares input features to perform
                model predictions.
                Reverses LP normalization using LP_MEAN and LP_STD.
        
                Returns
                -------
                float
                    Predicted persistence length (LP) in units of nm.    
        """

        comp = self.composition()

        X_sample = [x / sum(comp) for x in comp[:31]]
        X_sample = np.array([X_sample], dtype=np.float64)

        y_pred = Sequence.model.predict(X_sample, verbose=0)[0][0]

        return y_pred*LP_STD + LP_MEAN