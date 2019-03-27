Introdução


    https://periodicos.utfpr.edu.br/recit/article/view/4330/Leandro

Algoritmo incial que executa uma soma das entradas e dos pesos e depois executa a step function.

em Python

````py
entradas = [-1,7,5]
pesos = [0.8,0.1,0]

def soma(entradas, pesos):
    soma = 0
    for index in range(3):
        soma += entradas[index] * pesos[index]
    return soma

somaTotal = soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

resultado = stepFunction(somaTotal)
````

em JS

````js
const entradas = [-1,7,5]
const pesos = [0.8,0.1,0]

const func1 = (entradas, pesos) => (somado) => console.log('to aqui')

const haveSameLength = (entradas, pesos) => if(entradas.lenght === pesos.lenght) : true ? false
executeSoma = (entradas , pesos ) => haveSameLength(entradas, pesos) => console.log()

soma = (entradas, pesos) => executeSoma(entradas, pesos) 

````

