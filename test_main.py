import subprocess
import sys


def test_abc_quantity_shows_error():
    result = subprocess.run(
        [sys.executable, "main.py"],
        input="2\ndarya\ntea\nabc\n5\n",
        capture_output=True,
        text=True,
    )
    assert "must be a number" in result.stdout