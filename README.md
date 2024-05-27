# bd91

## Descargar y istalar ollama}

curl -fsSL https://ollama.com/install.sh | sh

## Correr el server ollama 

ollama serve

##  lISTA DE OLLAMA

ollama list

## Descargar tinyllama
ollama pull tinyllama

ollama pull llama2 




FROM llama3

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
"""


# CREAR MODELO
cd Models
ollama create example -f Modelfile