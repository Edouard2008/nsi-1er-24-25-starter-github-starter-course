#git add main.py
#git commit -m "Add main Python file"
#git push

import pytest
from main import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
