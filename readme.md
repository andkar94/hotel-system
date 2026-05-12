## Uruchamianie
1. Stwórz wirtualne środowisko w python (python -m venv myvenv)
2. Aktywuj środowisko (myvenv\Scripts\activate.bat)
3. Zainstaluj zależności (pip install -r requirements.txt)

Start serwera -> 
```
python manage.py runserver
```

### Migracje po zmianach w bazie danych:

```
python manage.py makemigrations members
```

```
python manage.py migrate
```