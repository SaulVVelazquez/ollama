
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt":"Porque el cielo es azul?",
  "system":"Responde como si fueras Garfield",
  "stream": false
}'

# llama
- *Paso 1 Instalar Ollama*:curl -fsSL https://ollama.com/install.sh | sh 
- *Paso 2 Mostrar lista de comandos*:ollama
- *Paso 4 Correr servidor*:ollama serve
- *Paso 5 Mostrar modelos Descargados*:ollama list

### modelo: tiny o llama
- *Paso 6 Descargar Modelos*:ollama pull tinyollama
- *Pregunta lo que quieras*: ollama run tinyllama [pregunta]
- *Activa modo chat*: ollama run 
# llava 
- *ollama pull llava*
- * ollama run llava*
