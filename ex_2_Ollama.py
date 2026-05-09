import ollama

input_text = "Mi chiamo Elena Bardi, ho 34 anni e lavoro come progettista di esperienze benessere. Collaboro con spazi che uniscono comunità, natura e rilassamento, creando percorsi dedicati al benessere delle persone, tra giardini sensoriali, aree relax e ambienti armoniosi."

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": f"Estrai nome, età e professione da questo testo. Rispondi solo in questo formato: Nome, Età, Professione.\n\n{input_text}"}
    ],
)

print("Testo inserito:", input_text)
print("Dettagli estratti:")
print(response["message"]["content"])