import json
import requests

# NOTA: ollama debe estar en funcionamiento para que esto funcione; inicia la aplicación o ejecuta `ollama serve`
model = 'stablelm-zephyr'  # TODO: actualiza esto con el nombre del modelo que desees usar

def generate(prompt, context):
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        # la respuesta se transmite un token a la vez, imprímelo a medida que lo recibimos
        print(response_part, end='', flush=True)

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return body['context']

def main():
    context = []  # el contexto almacena un historial de conversación, puedes usarlo para que el modelo sea más consciente del contexto
    while True:
        user_input = input("Ingresa una indicación: ")
        if not user_input:
            exit()
        print()
        context = generate(user_input, context)
        print()

if __name__ == "__main__":
    main()
