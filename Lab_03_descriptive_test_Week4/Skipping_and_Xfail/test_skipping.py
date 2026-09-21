import os
import sys
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert False

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_needs_modern_python():
    assert True

@pytest.mark.skipif(not os.path.exists("/etc/hosts"), reason="No hosts file")
def test_hosts_file():
    assert os.path.exists("/etc/hosts")
