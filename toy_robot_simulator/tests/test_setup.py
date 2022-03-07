import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["TEST_ENABLED"] = "True"
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)