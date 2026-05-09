import ollama

input_text = "In un quartiere molto trafficato, il Comune ha trasformato un vecchio parcheggio abbandonato in un giardino condiviso. Ora gli abitanti possono coltivare piante, leggere all'aperto e partecipare a piccoli incontri sul benessere, creando uno spazio più verde, sociale e rilassante."

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": f"Riassumi questo testo in un solo paragrafo di massimo 255 caratteri. Mantieni un tono naturale, chiaro e rilassante. Rispondi solo con il riassunto:\n\n{input_text}"}
    ],
)

summary = response["message"]["content"]

print("Testo originale:", input_text)
print("Riassunto:", summary)
print("Caratteri:", len(summary))