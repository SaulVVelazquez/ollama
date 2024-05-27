import json
import requests

# NOTE: ollama debe estar en funcionamiento para que esto funcione; inicia la aplicación o ejecuta `ollama serve`
model = "llama3"  # TODO: actualiza esto con el nombre del modelo que desees usar


def chat(messages):
    r = requests.post(
        "http://0.0.0.0:11434/api/chat",
        json={"model": model, "messages": messages, "stream": True},
    )
    r.raise_for_status()
    output = ""

    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            # la respuesta se transmite un token a la vez, imprímelo a medida que lo recibimos
            print(content, end="", flush=True)

        if body.get("done", False):
            message["content"] = output
            return message


def main():
    messages = []

    while True:
        user_input = input("Ingresa una indicación: ")
        if not user_input:
            exit()
        print()
        messages.append({"role": "user", "content": user_input})
        message = chat(messages)
        messages.append(message)
        print("\n\n")


if __name__ == "__main__":
    main()
