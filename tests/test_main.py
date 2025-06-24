import sys
sys.path.append('/home/scjmorris/projects/pickleball/pycleball/')
from main import main
from page_objects.dashboard import Dashboard


def test_main():
    main()
    assert 1 == 1
