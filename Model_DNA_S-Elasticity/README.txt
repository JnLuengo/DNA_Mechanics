Execute as:
python ModelPrediction.py file_with_sequences.txt

file_with_sequences.txt must contain a single column, no spaces, with any amount of sequences of any length.

Output is S, error, of all sequences contained in file_with_sequences.txt, in the same order.

Errors are raised if:
	(i) A sequence contains characters other than A, T, C, G
	(ii) No input file is given, or if file does not exist.
	(iii) A sequence has 1 bp, or if it finds a blank space.

Example input: 'ExampleSeq.txt'

Code efficiency was tested with 1000000 random DNA sequences of 100 bps -> Time: 1m19.319s in 1 CPU
