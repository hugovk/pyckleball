import os
import sys
sys.path.append('/home/scjmorris/projects/pickleball/pycleball/')
from main import main

def test_main():
    main()
    assert 1 == 1
