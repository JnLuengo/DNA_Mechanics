import sys 
from src.models import Sequence

def main():
    """
    Receives file path, validates the existence of the file,
    the reads DNA sequences as lines. For each DNA sequence,
    validates that it contains only valid characters (A, T, C, G),
    then executes prediction of the effective DNA stretch modulus.

    Raises
    ----------
    ValueError:
        If filename is not received as input.
        Or if sequence contains invalid characters.

    Returns
    ----------
    List of float
        Two-element list containing predicted effective stretch modulus 
        and its error.
    """

    if len(sys.argv)!=2:
        raise ValueError("Error: Input required: file name")
    filename = sys.argv[1]

    try:

        with open(filename, "r") as file:
        
            for sequence in file:

                if not sequence:
                    continue
            
                sequence = sequence.strip()
                seq = Sequence(sequence)
                seq.validate()
            
                Stilde = seq.prediction_Stilde()
                print(Stilde[0], Stilde[1])

    except FileNotFoundError:

        print(f"File {filename} does not exist.")

    except IsADirectoryError:

        print(f"The path {filename} is a directory.")

            
if __name__ == "__main__":
    main()