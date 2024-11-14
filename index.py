# import yaml

# # Cargar el archivo YAML
# with open("MT/example.yml", "r") as file:
#     data = yaml.safe_load(file)

# # Guardar datos en variables
# q_states = data.get("q_states", {})




# simulation_strings = data.get("simulation_strings", [])




# q_list = q_states.get("q_list", [])
# initial_state = q_states.get("initial", "")
# final_state = q_states.get("final", "")

# alphabet = data.get("alphabet", [])
# tape_alphabet = data.get("tape_alphabet", [])

# delta = data.get("delta", [])
# function = {}
# for params in delta:
#     # print((params["params"]["initial_state"], params["params"]["tape_input"]))
#     function[(params["params"]["initial_state"], params["params"]["tape_input"])] = (params["output"]["final_state"], params["output"]["tape_output"], params["output"]["tape_displacement"])







# # Mostrar el contenido de las variables
# print("q_list:", q_list)
# print("initial_state:", initial_state)
# print("final_state:", final_state)
# print("alphabet:", alphabet)
# print("tape_alphabet:", tape_alphabet)
# print("delta:", delta)
# print("simulation_strings:", simulation_strings)
# print("function:", function)

from Reader import Reader
from MT import MT

reader = Reader("MT/example.yml")
reader.print_data()

mt = MT(reader.states, reader.initial_state, reader.final_state, reader.alphabet, reader.tape_alphabet, reader.function)

mt.initializeTape("01")
mt.simulateMT()

if mt.error:
    print(mt.error)
    print("Simulation failed")
else:
    print("Simulation successful")

