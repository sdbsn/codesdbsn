# Code SDBSN

Ce dépôt contient le code source pour le projet SDBSN.

## Structure du projet

- `src/` - Code source principal
- `tests/` - Tests unitaires
- `docs/` - Documentation

## Prérequis

- Python 3.8+
- Git

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/sdbsn/codesdbsn.git
cd codesdbsn
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
```

3. Activez l'environnement virtuel :
- Sur Windows :
```bash
venv\Scripts\activate
```

4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

5. Lancez l'application :
```bash
python -m src.app
```

L'application sera accessible à l'adresse http://localhost:5000

## Structure du projet

```
codesdbsn/
├── src/              # Code source
│   ├── __init__.py   # Module principal
│   └── app.py        # Application Flask
├── tests/            # Tests unitaires
├── docs/            # Documentation
├── requirements.txt  # Dépendances Python
└── setup.py         # Configuration du package
