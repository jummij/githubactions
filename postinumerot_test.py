# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from postinumerot import multiple_zipcodes, district_is_in_data

#täytyy itse kirjoittaa input...

# testaa löytyykö useampi postinro
def test_helsinki_has_multiple_zipcodes():
    assert multiple_zipcodes('Helsinki') == True

def test_kirkkonummi_has_multiple_zipcodes():
    assert multiple_zipcodes('kirkkonummi') == True

def test_vuorilahti_has_one_zipcode():
    assert multiple_zipcodes('vuorilahti') == False

# Testaa löytyykö aluetta datalistasta

def test_if_helsinki_in_data():
    assert district_is_in_data('Helsinki') == True

def test_if_testikaupunki_in_data():
    assert district_is_in_data('testikaupunki') == False

