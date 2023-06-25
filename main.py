from enigma_simulator import EnigmaSimulator

config_file = 'enigma_config.py'  # Nazwa pliku konfiguracyjnego

# Utworzenie instancji symulatora Enigmy
enigma = EnigmaSimulator(config_file)

# Pytanie użytkownika o wiadomość do zaszyfrowania
message = input("Podaj wiadomość do zaszyfrowania: ")

# Szyfrowanie wiadomości
encrypted_message = enigma.encrypt(message)
print('Encrypted message:', encrypted_message)
