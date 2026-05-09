import ollama

input_text = "Nel nuovo parco di quartiere, le persone possono camminare tra gli alberi, leggere sulle panchine e partecipare a piccoli incontri dedicati al benessere. Lo spazio è nato per unire natura, relax e vita sociale."

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": f"Crea 3 domande di comprensione semplici su questo testo. Rispondi solo con le domande numerate:\n\n{input_text}"}
    ],
)

print("Testo:", input_text)
print("Domande:")
print(response["message"]["content"])