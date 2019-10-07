from qiskit import Aer, ClassicalRegister, execute, QuantumCircuit, QuantumRegister

q = QuantumRegister(4) # initialize 4 quantum registers (qubits)
c = ClassicalRegister(4) # initialize 4 classical registers to measure the 4 qubits
qc = QuantumCircuit(q, c) # initialize the circuit
backend = Aer.get_backend('qasm_simulator') # modify this line to run this code on a real quantum computer

print("Quantum RPG Character Generator (Partial)") # this is just a proof-of-concept partial generator

attributes = ("STR", "DEX", "INT", "WIS", "CON", "CHA") # someone played Dungeons & Dragons as a kid... might've been me....

i = 0
while i < 4:
    qc.h(q[i]) # put all 4 qubits into superposition states so that each will measure as a 0 or 1 completely at random
    i = i + 1
   
for i in range(6):
    qc.measure(q, c) # collapse the superpositions and get 4 random digits
    m = str(execute(qc, backend, shots=1, memory=True).result().get_memory()) # store the 4 digits in a variable so they can be manipulated
    diceroll = str((int(m[2])*8) + (int(m[3])*4) + (int(m[4])*2) + (int(m[5])*1) + 3) # use the digits as a binary of length 4 and convert it to decimal with a range of 0-15; simulate a 3d6 dice roll by adding 3, giving a range of 3-18
    print(attributes[i] + ": " + diceroll)
