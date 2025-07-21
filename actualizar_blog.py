import os
import subprocess

# Ruta al repositorio donde está blog.html
REPO_DIR = r"C:\Users\PC\Desktop\Nueva carpeta (2)\lebiuclub.github.io"

def actualizar_blog():
    os.chdir(REPO_DIR)

    print("🟡 git add .")
    subprocess.run(["git", "add", "."], shell=True)

    print("🟢 git commit")
    subprocess.run(["git", "commit", "-m", "Actualización automática de blog.html"], shell=True)

    print("🚀 git push")
    resultado = subprocess.run(["git", "push"], shell=True, capture_output=True, text=True)

    if resultado.returncode == 0:
        print("✅ ¡Cambios subidos a GitHub!")
    else:
        print("❌ Error al hacer push:")
        print(resultado.stderr)

if __name__ == "__main__":
    actualizar_blog()
