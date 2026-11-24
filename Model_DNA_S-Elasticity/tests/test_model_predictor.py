from pathlib import Path
import io
import subprocess
import sys
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
TESTS = Path(__file__).resolve().parent

def test_prediction():

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "ModelPrediction.py"),
            str(ROOT / "ExampleSeq.txt"),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    actual = np.loadtxt(io.StringIO(result.stdout), ndmin=2)
    expected = np.loadtxt(TESTS / "ExpectedOutput.dat", ndmin=2)

    np.testing.assert_allclose(actual, expected, rtol=1e-9)

