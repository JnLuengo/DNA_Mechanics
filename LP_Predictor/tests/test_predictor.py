from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
TESTS = Path(__file__).resolve().parent

def test_prediction():

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "Prediction.py"),
            str(ROOT / "TestSequences.txt"),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    with open(TESTS / "ExpectedOutput.dat") as file:
        expected = file.read()
    
    assert result.stdout == expected