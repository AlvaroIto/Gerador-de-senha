"""CLI para gerador de senhas."""
from __future__ import annotations
import argparse
import sys
from generator import generate_password

#cria um parser de argumentos usando argparse e retorna um objeto contendo as opções fornecidas pelo usuário.
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gerador de Senhas CLI")
    parser.add_argument("--length", "-l", type=int, default=12, help="Comprimento da senha")
    parser.add_argument("--no-upper", action="store_true", help="Não incluir letras maiúsculas")
    parser.add_argument("--no-lower", action="store_true", help="Não incluir letras minúsculas")
    parser.add_argument("--no-digits", action="store_true", help="Não incluir dígitos")
    parser.add_argument("--no-symbols", action="store_true", help="Não incluir símbolos")
    parser.add_argument("--save", "-s", metavar="FILE", help="Salvar a senha gerada em FILE (append)")
    return parser.parse_args()

def main() -> int:
    args = parse_args()
    try:
        password = generate_password(
            length=args.length,
            use_lower=not args.no_lower,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols
        )
    except ValueError as e:
        print(f"Erro: {e}", file=sys.stderr)
        return 1

    print(password)

    # salva a senha em um arquivo
    if args.save:
        with open(args.save, "a", encoding="utf-8") as f:
            f.write(password + "\n")
        print(f"Senha salva em {args.save}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
