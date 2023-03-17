import TEST_CASES
from pachinko import eval_pachinko

def test_empty():
    assert eval_pachinko(TEST_CASES.Test_000) == TEST_CASES.Percentage000

def test_hole():
    assert eval_pachinko(TEST_CASES.Test_00) == TEST_CASES.Percentage00
    
def test_floor():
    assert eval_pachinko(TEST_CASES.Test_01) == TEST_CASES.Percentage01

def test_mountain_in_middle():
    assert eval_pachinko(TEST_CASES.Test_02) == TEST_CASES.Percentage02
    
def test_mountain_at_start():
    assert eval_pachinko(TEST_CASES.Test_03) == TEST_CASES.Percentage03

def test_mountain_at_end():
    assert eval_pachinko(TEST_CASES.Test_04) == TEST_CASES.Percentage04
