def saludar(nombres):
    return f"Hola {nombres}"


def test_saludar():
    assert saludar("Ana") == "Hola Ana"!