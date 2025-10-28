from __future__ import annotations
import random
import string
from typing import Final

DEFAULT_LENGTH: Final[int] = 12
SYMBOLS: Final[str] = "!@#$%&*()-_=+[]{};:,.<>/?"

# Constrói o conjunto de caracteres (charset) a ser usado na geração de senhas.
def build_charset(use_lower: bool = True,
                  use_upper: bool = True,
                  use_digits: bool = True,
                  use_symbols: bool = True) -> str:
    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += SYMBOLS
    if not charset:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
    return charset

# Gera uma senha aleatória com base no charset configurado.
def generate_password(length: int = DEFAULT_LENGTH,
                      use_lower: bool = True,
                      use_upper: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = True) -> str:
    if length < 1:
        raise ValueError("length deve ser >= 1")

    charset = build_charset(use_lower, use_upper, use_digits, use_symbols)
    system_random = random.SystemRandom()
    password_chars = [system_random.choice(charset) for _ in range(length)]
    return ''.join(password_chars)