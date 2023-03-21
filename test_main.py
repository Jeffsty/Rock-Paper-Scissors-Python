import main
import pytest

def main():
    test_compare_weapons()

def test_compare_weapons():
    assert main.compare_weapons("It's a draw") == True