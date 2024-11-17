from Reader import Reader
from MT import MT

reader = Reader("MT/reconocedora.yml")
reader.printData()

mt = MT(reader.states, reader.initial_state, reader.final_state, reader.alphabet, reader.tape_alphabet, reader.function)

for input_string in reader.simulation_strings:
    print(f"\nSimulando cadena: {input_string}")
    mt.initializeTape(input_string)
    
    if mt.simulateMT():
        print(f"Cadena {input_string} aceptada.")
    else:
        print(f"Cadena {input_string} rechazada.")

