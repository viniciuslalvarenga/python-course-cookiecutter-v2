"""
Este e um arquivo de configuracao do pytest para testes.

Sempre que um arquivo chamado conftest.py e encontrado em um diretorio de testes,
o pytest o utiliza para configurar fixtures e hooks que serao aplicados aos testes.
"""

import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
# Nao necessario precisava do resolve() ele so nao deixa aparecer o ../
THIS_DIR_PARENT = (THIS_DIR / "../").resolve()

# tick to solve import from project.py
sys.path.insert(0, str(THIS_DIR_PARENT))

# carregamento automático de plugins do pytest
# tests.fixtures.exemple_fixture funciona com import path para resolver imports
pytest_plugins = ["tests.fixtures.exemple_fixture"]
