# DeutschProblem
Implementação do problema de Deutsch no Qiskit


Neste artigo, vamos escrever uma rotina no Qiskit que simula o problema de Deutsch.

O circuito tem a finalidade de descobrir se uma função desconhecida é pura ou balanceada, com uma chamada à caixa-preta (Uf).

![](https://informacaoquantica.files.wordpress.com/2020/04/deutsch00.png)

O artigo anterior mostra como simular a caixa-preta do problema de Deutsch. Aqui, vamos utilizar direto o resultado já obtido.

O circuito

Vamos montar o circuito no Qiskit.

Este terá dois qubits e dois bits clássicos.

from qiskit import *

qr = QuantumRegister(2)

cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr,cr)

A seguir, vamos inserir uma porta NOT no qubit 1 (lembre-se de que o Qiskit é base 0). A porta NOT serve para o qubit ficar no estado |1>.

O operador identidade no qubit 0 é para deixar explícito que não estamos fazendo nada com ele.

circuit.iden(qr[0])

circuit.x(qr[1])

A seguir, aplicar uma porta Hadamard em cada qubit

circuit.h(qr[0])

circuit.h(qr[1])

O comando “barrier” serve apenas para criar uma barra horizontal, para separar visualmente os elementos do circuito.

circuit.barrier()

Dentro da caixa-preta, temos quatro possibilidades.

Vamos deixar colocar a princípio a função f(x) == 0, que equivale a não fazer nada.

#Caixa Preta

#Função f(x) == 0

#Faz nada, identidade

circuit.barrier()

O circuito após a caixa-preta é um Hadamard no primeiro qubit:

#Fim da caixa-preta

#Desfaz o circuito

circuit.h(qr[0])

circuit.iden(qr[1])

![](https://informacaoquantica.files.wordpress.com/2020/04/diagrama0.jpg)

E, depois, medir o circuito.

circuit.measure(qr,cr)

Comandos de execução e visualização.

print(circuit)

simulator = Aer.get_backend('qasm_simulator')

result = execute(circuit, backend=simulator).result()

print(result)

#Mostrar histograma dos resultados

from qiskit.tools.visualization import plot_histogram

plot_histogram(result.get_counts(circuit))

Para o primeiro circuito, (f(x) == 0), o resultado é dado por:
![](https://informacaoquantica.files.wordpress.com/2020/04/circuito0.png)

Lembre-se que a ordem de leitura do Qiskit é de baixo para cima. Portanto, o qubit 0 terá sempre valor |0>, enquanto o qubit 1 pode ser |0> ou |1>.

Para simular f(x) == 1, uso um NOT no segundo qubit
![](https://informacaoquantica.files.wordpress.com/2020/04/diagrama1-1.jpg)

#Função f(x) == 1

#1 qubit identidade, 2o qubit NOT

circuit.iden(qr[0])

circuit.x(qr[1])

Resultado:

![](https://informacaoquantica.files.wordpress.com/2020/04/circuito1.png)

Novamente, o qubit 0 terá sempre valor |0>. Ou seja, se o primeiro qubit for zero, a função será pura (ou seja, ou f(x) == 0 ou f(x) == 1), conforme dita a teoria sobre o assunto.

Para simular f(0) == 0 e f(1) == 1, utilizo uma porta CNOT na caixa-preta.
![](https://informacaoquantica.files.wordpress.com/2020/04/diagrama2.jpg)

 #Função f(0) == 0 e f(1) == 1

#CNOT, primeiro qbit como controle

#circuit.cnot(qr[0],qr[1])

Resultado:
![](https://informacaoquantica.files.wordpress.com/2020/04/circuito2-1.png)

O qubit 0 terá sempre valor |1>. Lembrando que o Qiskit mostra valores de baixo para cima.

Finalmente, para f(0) == 1 e f(1) == 0, é o circuito mais complicado NOT – CNOT – NOT.
![](https://informacaoquantica.files.wordpress.com/2020/04/diagrama3.jpg)

#Função f(0) == 1 e f(1) == 0

circuit.x(qr[0])

circuit.iden(qr[1])

circuit.cnot(qr[0],qr[1])

circuit.x(qr[0])

circuit.iden(qr[1])

Resultado:
![](https://informacaoquantica.files.wordpress.com/2020/04/circuito3-1.png)


O qubit 0 terá sempre valor |1>, ou seja, se a função for balanceada, o primeiro qubit terá valor |1>, e está de acordo com a teoria.

Conclusão:

Este artigo mostra uma forma de simular o circuito do problema de Deutsch para as 4 funções possíveis.

O problema de Deutsch é interessante por demonstrar vários conceitos de circuitos quânticos. Entretanto, além do problema não ter valor prático, também pode ser simulado classicamente com a mesma eficiência.


Link para download do código:

https://github.com/asgunzi/DeutschProblem

https://informacaoquantica.wordpress.com/2020/04/22/a-caixa-preta-do-problema-de-deutsch
