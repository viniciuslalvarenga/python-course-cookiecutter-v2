"""Constantes usadas nos testes."""

from pathlib import Path

THIS_DIR = Path(__file__).parent
# Nao necessario precisava do resolve() ele so nao deixa aparecer o ../
PROJECT_DIR = (THIS_DIR / "../").resolve()
