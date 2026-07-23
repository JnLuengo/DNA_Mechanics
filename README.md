# Predictors of DNA Mechanical properties.

---

## Model_DNA_S-Elasticity

**Physical** predictor of DNA **crookedness** and **stretch modulus**.

Clone directory *Model_DNA_S-Elasticity* and run:

```
python3 ModelPrediction.py file_with_sequences.txt
```

- *file_with_sequences.txt* must contain a single column, no spaces, with any amount of sequences of any length.

- *ModelPrediction.py* will ignore empty linesm and raise error if any sequence contains characters other than A, T, C, G.

- Output is S, error, of all sequences contained in *file_with_sequences.txt*, in the same order.

- Code efficiency was tested with 1000000 random DNA sequences of 100 bps -> Time: 1m19.319s in 1 CPU.

- Example input: *'ExampleSeq.txt'*.

---

## LP_Predictor

**Dense neural network** to predict DNA **persistence lentgh** from DNA sequence.

