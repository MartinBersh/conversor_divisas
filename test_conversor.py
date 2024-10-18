import pytest
from conversor import ConversorMonedas
from constantes import TASAS_CAMBIO


@pytest.fixture
def conversor():
    return ConversorMonedas(TASAS_CAMBIO)


def test_conversion_usd_a_eur(conversor):
    assert conversor.convertir(100, 'USD', 'EUR') == 85.0


def test_conversion_eur_a_cop(conversor):
    assert conversor.convertir(50, 'EUR', 'COP') == 23529.41


def test_conversion_btc_a_usd(conversor):
    assert conversor.convertir(0.002, 'BTC', 'USD') == 95.24


def test_conversion_moneda_no_soportada(conversor):
    with pytest.raises(ValueError):
        conversor.convertir(100, 'YEN', 'USD')

def test_valor_no_numerico(conversor):
    with pytest.raises(ValueError):
        conversor.convertir("abc", 'USD', 'COP')
