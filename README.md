# Predictors of DNA Mechanical properties.

---

## Model_DNA_S-Elasticity

**Physical** predictor of DNA **crookedness** and **stretch modulus**.

Clone directory *Model_DNA_S-Elasticity* and run:

```
python3 ModelPrediction.py file_with_sequences.txt
```

- *file_with_sequences.txt* must contain a single column, no spaces, with any amount of sequences of any length.

- *ModelPrediction.py* will ignore empty lines and raise error if any sequence contains characters other than A, T, C, G.

- Output is S, error, of all sequences contained in *file_with_sequences.txt*, in the same order.

- Code efficiency was tested with 1000000 random DNA sequences of 100 bps -> Time: 1m19.319s in 1 CPU.

- Example input: *'ExampleSeq.txt'*.

---

## LP_Predictor

**Dense neural network** to predict DNA **persistence lentgh** from DNA sequence.

Clone directory *LP_Predictor* and run:

```
python3 Prediction.py file_with_sequences.txt
```

Requires **numpy** and **tensorflow**.

- *file_with_sequences.txt* must contain a single column, no spaces, with any amount of sequences of any length.

- *Prediction.py* will ignore empty lines and raise error if any sequence contains characters other than A, T, C, G.

- Output is input sequence, persistence length, of all sequences contained in *file_with_sequences.txt*, in the same order.

- Example input: *'TestSequences.txt'*.

### Model details

- 31 input features: normalized trimer composition.

- 4 hidden, dense layers with ReLU activation. Neurons: 200 - 100 - 50 - 25.

- Output layer with single neuron and linear activation.
