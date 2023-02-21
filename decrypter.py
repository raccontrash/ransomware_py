import os
import pyaes

## abrir o conteudo criptografado

file_name = 'teste.txt.AMONCRIPT'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## setar a chave de descriptografia

key = b'AMON'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt.data = aes.decrypt(file_data)

## remove o arquivo original
os.remove(file_name)

# cria novo doc orignal
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()