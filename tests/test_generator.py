# tests/test_generator.py
from src.generator import generate_password, SYMBOLS

def test_length():
    p = generate_password(length=20)
    assert len(p) == 20

def test_only_lower():
    p = generate_password(use_lower=True, use_digits=False, use_symbols=False, use_upper=False)
    assert all(ch.islower() for ch in p)

def test_only_upper():
    p = generate_password(use_upper=True, use_lower=False, use_digits=False, use_symbols=False)
    assert all(ch.isupper() for ch in p)

def test_only_digits():
    p = generate_password(use_digits=True, use_upper=False, use_lower=False, use_symbols=False)
    assert all(ch.isdigit() for ch in p)

def test_only_symbols():
    p = generate_password(use_symbols=True, use_digits=False, use_upper=False, use_lower=False)
    assert all(ch in SYMBOLS for ch in p)
