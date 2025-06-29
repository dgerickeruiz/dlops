# Creamos entorno

    python -m venv DLOps

# Dar permisos

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activamos Ambiente desde la raiz

    .\DLOps\Scripts\activate

# Desactibar Ambiente desde la raiz

    cd .\DLOps\Scripts
    deactivate

# Definir variables de entorno para FireBase

    $Env:GOOGLE_APPLICATION_CREDENTIALS = "dlops_key.json"