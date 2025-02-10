from autocorrect import Speller

spell = Speller(lang='en')

def correct_sentence(text):
    return spell(text)
