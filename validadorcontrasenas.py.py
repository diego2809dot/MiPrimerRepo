import getpass
import re

try:
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    if len(contraseña) < 10:
        raise ValueError("Contraseña demasiado corta")
    if not any(char.isdigit() for char in contraseña):
        raise ValueError("Debe contener al menos un número")
    if not re.search(r"[!@#$%^&*()_+=\[{\]};:<>|./?,-]", contraseña):
        raise ValueError("Debe contener al menos un carácter especial")
    print("Contraseña válida.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
