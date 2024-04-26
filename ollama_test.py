import ollama, sys

user_message = sys.argv[1]

stream = ollama.chat(model='llama3', messages=[{'role':'user', 'content':user_message}], stream=True)

for chunk in stream:
	print(chunk['message']['content'], end='', flush=True)
print('')
print('')
