import ollama

data = {
    "name": "Marta Verde",
    "age": 37,
    "city": "Trento",
    "profession": "designer di spazi naturali per il benessere",
}


response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": f"Trasforma questi dati in una descrizione naturale, breve e armoniosa. Parla di società, natura e rilassamento senza inventare dati nuovi. Rispondi solo con la descrizione:\n\n{data}"}
    ],
)

print("Dati:", data)
print("Descrizione:")
print(response["message"]["content"])