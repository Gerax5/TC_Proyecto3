from Reader import Reader
from MT import MT

reader = Reader("MT/example.yml")
reader.printData()

mt = MT(reader.states, reader.initial_state, reader.final_state, reader.alphabet, reader.tape_alphabet, reader.function)

mt.initializeTape("01")
mt.simulateMT()

if mt.error:
    print(mt.error)
    print("Simulation failed")
else:
    print("Simulation successful")

