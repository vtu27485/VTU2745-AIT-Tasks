facts = {
    "sun": "The Sun is a star",
    "earth": "Earth is a planet",
    "moon": "The Moon revolves around Earth",
    "python": "Python is a programming language"
}

query = input("Enter a fact name: ").lower()

if query in facts:
    print(facts[query])
else:
    print("Fact not found")


"""
INPUT:
Enter a fact name: earth

OUTPUT:
Earth is a planet
"""
