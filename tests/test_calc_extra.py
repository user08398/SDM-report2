import pytest
from calc_mul import calc  # ← 実際のモジュール名に置き換える

# 有効ケース
def test_valid_small():
    assert calc(1, 1) == 1

def test_valid_large():
    assert calc(999, 999) == 999 * 999

# 境界値
def test_boundary_low_high():
    assert calc(1, 999) == 1 * 999
    assert calc(2, 998) == 2 * 998

# 範囲外（無効）
def test_out_of_range():
    assert calc(0, 5) == -1
    assert calc(1000, 1) == -1
    assert calc(1, 1000) == -1

# 型エラー・非整数
def test_string_input():
    assert calc("12", 3) == -1

def test_mixed_string():
    assert calc("12a", 3) == -1

def test_float_input():
    assert calc(3.0, 2.0) == -1

def test_none_input():
    assert calc(None, 5) == -1