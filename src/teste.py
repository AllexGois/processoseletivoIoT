print("=== TESTE SIMPLES ===")
print("Se aparecer isso, o MicroPython está funcionando!")

import time
print("Import time: OK")

try:
    import machine
    print("Import machine: OK")
except ImportError as e:
    print(f"Import machine: ERRO - {e}")

try:
    import network
    print("Import network: OK")
except ImportError as e:
    print(f"Import network: ERRO - {e}")

print("=== FIM DO TESTE ===")