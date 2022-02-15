import os
from pathlib import Path

from mypy import api as mypy_api


def test_mypy_plugin():
    current_dir = Path(__file__).parent
    mypy_target = os.path.join(str(current_dir.absolute()), "dto_test_module.py")
    mypy_config = os.path.join(current_dir.parent.parent.absolute(), "mypy.ini")
    out, err, code = mypy_api.run([mypy_target, "--config-file", mypy_config, "--show-error-codes"])
    assert code == 0
