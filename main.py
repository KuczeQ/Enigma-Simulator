from enigma_simulator import EnigmaSimulator

config_file = 'enigma_config.py' 

enigma = EnigmaSimulator(config_file)

message = input("Enter the message to be encrypted: ")

encrypted_message = enigma.encrypt(message)
print('Encrypted message:', encrypted_message)
