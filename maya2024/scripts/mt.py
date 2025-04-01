import marshal
with open("c:/Arts and Spells/Metapipe Studio 3.0.0/data/" + 'mt-42.mtp', 'rb') as file:
    serialized_code = file.read()
mt = marshal.loads(serialized_code)