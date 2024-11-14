class MT:
    def __init__(self, states, initial_state, final_state, alphabet, tape_alphabet, function):
        self.states = states #Estados
        self.initial_state = initial_state #Estado inicial
        self.final_state = final_state #Estado final
        self.alphabet = alphabet #Alfabeto de entrada
        self.tape_alphabet = tape_alphabet #Alfabeto de la cinta
        self.function = function #Funcion de transicion

        # Tape Configuration
        self.headPosition = 0 #Posicion del cabezal actual
        self.tape = [] #La cinta que es la palabra de entrada
        self.currentState = initial_state #Estado actual

        self.error = ""

    def initializeTape(self, simulation_string):
        self.word = simulation_string
        self.tape = list(simulation_string)
        self.currentState = self.initial_state
        self.headPosition = 0

    def moveTape(self):
        if self.headPosition < 0:
            self.error = "Error: Head position is less than 0"
            return False
        
        if self.headPosition >= len(self.tape):
            self.tape.append("B")
        
        currentTapeSymbol = self.tape[self.headPosition]
        if (self.currentState, currentTapeSymbol) not in self.function:
            self.error = "Error: No function defined for the current state and tape symbol"
            return False
        nextState, nextTapeSymbol, tapeDisplacement = self.function[(self.currentState, currentTapeSymbol)]
        self.tape[self.headPosition] = nextTapeSymbol
        if tapeDisplacement == "R":
            self.headPosition += 1
        elif tapeDisplacement == "L":
            self.headPosition -= 1
        self.currentState = nextState
        return True
        

    def printCurrentTape(self):
        #Despues de move se podria llamar a esta funcion
        pass

    def simulateMT(self):
        while self.currentState != self.final_state and self.headPosition < len(self.word):
            if(self.moveTape() == False):
                #Aqui tambien deberia de ir porque si falla debe mostrar la ultima parte que fallo
                break
            #Pienso que podria ir aqui imprimir
