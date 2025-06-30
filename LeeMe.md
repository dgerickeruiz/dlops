# Creamos entorno

    python -m venv DLOps

# dar permisos

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activamos Ambiente desde la raiz

    .\DLOps\Scripts\activate

# Desactibar Ambiente desde la raiz
    cd .\DLOps\Scripts
    deactivate

# Borrar dataset

    Remove-Item -Path "dataset" -Recurse -Force 

# Ingresa clave de ambiente

    $Env:GOOGLE_APPLICATION_CREDENTIALS = "dlops_key.json"
    
# Ver en que Tag estoy parado

    git describe --tags --always

# Lista todo los tags

    git tag -l 

# Cambiarse de tag

    git checkout tags/v0
