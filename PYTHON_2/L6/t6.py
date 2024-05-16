from urllib3 import encode_multipart_formdata
import json
from dotenv import load_dotenv

import os
shared_dir = os.path.abspath('./SHARED')

import sys
sys.path.append(shared_dir)

import task_util


def extract_name(text):
  system_prompt = 'Dostaniesz fragment tekstu. Twoim zadaniem jest identyfikacja podmiotu, najlepiej imienia osoboy, której mowa. Zwróć imię w formacie JSON w polu "name"'
  resp = task_util.get_oai_answer(text, system_prompt)
  print(resp)
  return json.loads(resp)['name']

if __name__ == "__main__":
  load_dotenv()
 
  task, token = task_util.get_task('inprompt')
  input = task['input']
  question = task['question']
  name = extract_name(question)
  input = task['input']
  filtered = [s for s in input if name in s]
  print('FILTERED:', filtered)
 
  system_prompt = """Poniżej masz podane informacje o osobie. Odpowiesz na zadane pytanie tylko na podstawie dostarczonych informacji (kontekstu).
  Dbasz o to, aby odpowiedź była zgodna z kontekstem w 100%. Nie dodajesz niczego, czego nie ma w kontekście.
  Jeśli nie potrafisz znaleźć informacji w kontekście na zadane pytanie odpowiadasz: Brak informacji.
  ###
  """ + '.'.join(filtered)
  
  print(system_prompt)
  print(question)
  resp = task_util.get_oai_answer(question, system_prompt)
  print(resp)
  #task_util.submit_task(resp, token)
  
  