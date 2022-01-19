import subprocess
import sys

from Driver import Driver

if __name__ == "__main__":
    if "-t" in sys.argv:
        subprocess.call(
            ["coverage", "run", "-m", "unittest", "LogicTests.py"])
        subprocess.call(["coverage", "report"])
        if "-g" in sys.argv:
            subprocess(["coverage", "run", "-m", "unittest", "GUITests.py"])
        subprocess.call(["coverage", "report"])
    elif "-l" in sys.argv:
        subprocess.call(["pylama", "."])
    else:
        Driver()
