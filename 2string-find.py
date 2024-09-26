import re


def check_for_a(string):
    matches = re.findall(r"[aA]", string)
    found = len(matches)
    if found == 0:
        return "A letra a não aparece na string."
    else:
        return f"A letra a aparece {found} vez(es)."


if __name__ == "__main__":
    test0 = "Ainda somos os mesmos e vivemos"
    print(check_for_a(test0))
    # Resultado esperado: A letra a aparece 1 vezes.

    test1 = "Eu quero sossego"
    print(check_for_a(test1))
    # Resultado esperado: A letra a não aparece na string.

    test2 = "aaaAAAa"
    print(check_for_a(test2))
    # Resultado esperado: A letra a aparece 7 vezes.
