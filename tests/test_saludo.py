def saludar(nombres):
    return f"Hola {nombres}"


def test_saludar_01():
    assert saludar("Ana") == "Hola Ana soy yo desde mi laptop"