# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:26:38 2020

@author: asgun
"""

from qiskit import *

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr,cr)

circuit.iden(qr[0])
circuit.x(qr[1])

circuit.h(qr[0])
circuit.h(qr[1])



circuit.barrier()

#Caixa Preta
#Função f(x) == 0
#Faz nada, identidade


#Função f(x) == 1
#1 qubit identidade, 2 qubit NOT
#circuit.iden(qr[0])
#circuit.x(qr[1])

##Função f(0) == 0 e f(1) == 1
#CNOT, primeiro qbit como controle
#circuit.cnot(qr[0],qr[1])

#Função f(0) == 1 e f(1) == 0
#NOT, CNOT, NOT
circuit.x(qr[0])
circuit.iden(qr[1])

circuit.cnot(qr[0],qr[1])

circuit.x(qr[0])
circuit.iden(qr[1])


circuit.barrier()

#Fim da caixa-preta
#Desfaz o circuito
circuit.h(qr[0])
circuit.iden(qr[1])


#Mede
circuit.measure(qr,cr)

print(circuit)


simulator = Aer.get_backend('qasm_simulator')

result = execute(circuit, backend=simulator).result()
print(result)
#Mostrar histograma dos resultados
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))



