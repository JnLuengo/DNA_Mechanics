import sys 
from src.models import Sequence

def main():

    if len(sys.argv)!=2:
        raise ValueError("Error: Input required: file name")
    filename = sys.argv[1]

    with open(filename, "r") as file:
        
        for sequence in file:

            if not sequence:
                continue
            
            sequence = sequence.strip()
            seq = Sequence(sequence)
            seq.validate()
            
            Stilde = seq.prediction_Stilde()
            print(Stilde[0], Stilde[1])

            
if __name__ == "__main__":
    main()