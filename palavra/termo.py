from dataclasses import dataclass
from enum import Enum, auto
from typing import Sequence, Tuple
from unidecode import unidecode

class Feedback(Enum):
    '''Enumeração para os tipos de feedback de uma tentativa.'''
    CORRECT_POSITION = auto()
    WRONG_POSITION = auto()
    INCORRECT = auto()

def count_frequencies(values):
    '''Conta a frequência de cada valor na lista fornecida.'''
    frequencies = {}
    
    for value in values:
        frequencies[value] = frequencies.get(value, 0) + 1
    return frequencies

@dataclass
class Result:
    def __init__(self, win, feedback):
        self.win = win
        self.feedback = feedback

    def to_dict(self):
        '''Converte o resultado em um dicionário para ser serializável em JSON.''' 
        return {
            "win": self.win, 
            "feedback": [(letter, feedback.name) for letter, feedback in self.feedback]
        }

class InvalidAttempt(Exception):
    '''Exceção para tentativas inválidas.'''
    pass

@dataclass
class Termo:
    '''Classe principal do jogo Termo.'''
    target_word: str
    valid_words: set
    normalized_target_word: str = None
    normalized_valid_words: set = None

    def __post_init__(self):
        '''Normaliza a palavra alvo e a lista de palavras válidas.'''
        self.normalized_target_word = unidecode(self.target_word).lower()

        self.normalized_valid_words = set(map(
            lambda word: unidecode(word).lower(),
            self.valid_words,
        ))

    def _generate_feedback(self, guess: str):
        '''Gera feedback para uma tentativa de palavra.'''
        if len(guess) != len(self.target_word):
            raise InvalidAttempt('Tentativa inválida: tamanho incorreto')

        for index, char in enumerate(guess):
            if char == self.normalized_target_word[index]:
                yield self.target_word[index], Feedback.CORRECT_POSITION

            elif char in self.normalized_target_word:
                yield char, Feedback.WRONG_POSITION
            
            else:
                yield char, Feedback.INCORRECT

    def get_feedback(self, guess: str):
        '''Obtém o feedback detalhado para a palavra fornecida.'''
        feedback = list(self._generate_feedback(guess))
        target_word_freq = count_frequencies(self.target_word)

        feedback_freq = count_frequencies(map(
            lambda pair: pair[0],
            filter(lambda pair: pair[1] == Feedback.CORRECT_POSITION, feedback)
        ))

        for char, freq in target_word_freq.items():
            if feedback_freq.get(char, 0) >= freq:

                incorrect_indexes = map(lambda pair: pair[0], filter(
                    lambda pair: pair[1][0] == char and pair[1][1] == Feedback.WRONG_POSITION,
                    enumerate(feedback),
                ))
                
                for index in incorrect_indexes:
                    feedback[index] = (feedback[index][0], Feedback.INCORRECT)
        
        return feedback

    def test_guess(self, guess: str) -> Result:
        '''Testa uma palavra e retorna o resultado.'''
        normalized_guess = unidecode(guess).lower()

        if normalized_guess not in self.normalized_valid_words:
            raise InvalidAttempt('Tentativa inválida: palavra não permitida')

        return Result(
            win=self.normalized_target_word == normalized_guess,
            feedback=self.get_feedback(normalized_guess),
        )
