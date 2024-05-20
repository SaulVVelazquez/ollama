# ollama
ollama
# paso 1 instalar ollama desde curl
# mostrar lista de comandos ollama
# correr el servidor  ollama serve
# mostrar modelos  ollama  list 
# descargar modelos ollama 
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt":"Porque el cielo es azul?",
  "system":"Responde como si fueras Garfield",
  "stream": false
}'