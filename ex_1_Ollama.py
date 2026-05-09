import ollama

input_text = "Questa poltrona è realizzata in tessuto beige chiaro, con una seduta morbida e una struttura elegante in legno."

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": f"Traduci tra italiano e inglese in modo naturale. Rispondi solo con la traduzione:\n\n{input_text}"}
    ],
)

print("Testo inserito:", input_text)
print("Traduzione:", response["message"]["content"])