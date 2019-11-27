uniEsse3Api
-----------

Codice di interfaccia alla API di Cineca Esse3.


setup
-----

````
pip install git+https://github.com/UniversitaDellaCalabria/uniApi-Esse3.git
````

usage
-----

````
from unie3api.unie3api import uniE3Api

e3 = uniE3Api('https://unical.esse3.cineca.it/e3rest/api', 'TUOTOKEN')
# or
e3 = uniE3Api('https://unical.esse3.cineca.it/e3rest/api',
              username='thatuser', password='thatpass')


# usiamo sempre il codice fiscale come identificativo
e3.carriera('CODICEFISCALEQUI')

# interrogazione se lo studente ha una carriera attiva
# esclude gli studenti a corso singolo
e3.attivo('CODICEFISCALEQUI')
````
