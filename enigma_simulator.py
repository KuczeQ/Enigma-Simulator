import importlib
import string

class EnigmaSimulator:
    def __init__(self, config_file):
        self.rotors = []
        self.reflector = []
        self.initial_positions = []
        self.current_positions = []

        # Wczytanie pliku konfiguracyjnego
        config_module = importlib.import_module(config_file.replace('.py', ''))
        self.rotors = config_module.rotors
        self.reflector = config_module.reflector
        self.initial_positions = config_module.initial_positions
        self.current_positions = config_module.current_positions

    def encrypt(self, message):
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                char = char.upper()  # Konwersja na dużą literę
                encrypted_char = self.process_char(char)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def process_char(self, char):
        self.rotate_rotors()

        char_index = string.ascii_uppercase.index(char)
        for i in range(len(self.rotors)):
            char_index = (char_index + self.current_positions[i]) % 26
            char_index = self.rotors[i][char_index]
            char_index = (char_index - self.current_positions[i]) % 26

        char_index = self.reflector[char_index]

        for i in range(len(self.rotors) - 1, -1, -1):
            char_index = (char_index + self.current_positions[i]) % 26
            char_index = self.rotors[i].index(char_index)
            char_index = (char_index - self.current_positions[i]) % 26

        encrypted_char = string.ascii_uppercase[char_index]
        return encrypted_char

    def rotate_rotors(self):
        self.current_positions[0] = (self.current_positions[0] + 1) % 26

        for i in range(len(self.rotors) - 1):
            if (self.current_positions[i] + 1) % 26 == self.initial_positions[i + 1]:
                self.current_positions[i + 1] = (self.current_positions[i + 1] + 1) % 26
            else:
                break
