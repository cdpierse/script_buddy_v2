import ast
import json
import re
import unicodedata

import pandas as pd
from bs4 import BeautifulSoup
import csv


class Parser:

    def __init__(self):
        self.script_data = Parser.read('scripts.json')
        self.scene_set = [
            'INT.', 'EXT.', 'I/E.', 'EXTERIOR', 'INTERIOR', 'INSERT' 'CLOSE UP',
            'CLOSE-UP', 'WIDE ANGLE', 'CONTINUED', 'FADE IN',
            'DISSOLVE TO','CUT-TO', 'CUT TO', 'CUT TO BLACK', 'INTERCUT'
        ]
        self.dialogue_whitespace = " " * 15

    def getScriptText(self, df):
        """
        Returns script_text column values
        from a dataframe of script metadata. 

        """
        return df['title'].values, df['script_text'].values

    def getFilmDialogue(self, df=None):

        def IsDialogue(s):
            if s.startswith(self.dialogue_whitespace) or s.startswith("\t"):
                return True
            else:
                return False
        def isAlphaNum(s):
            if any(letter.isalnum() for letter in s):
                return True

        if df is None:
            titles, raw_text = self.getScriptText(self.script_data)
        else:
            titles, raw_text = self.getScriptText(df)

        film_dialogue = {}
        for title, text in zip(titles,raw_text):
            try:
                soup = BeautifulSoup(text[0],features="lxml")
                dialogue = []
                for b_tag in soup.findAll('b'):
                    sibling_lines  = str(b_tag.next_sibling).splitlines()
                    main_string = ""
                    for line in sibling_lines:
                        if IsDialogue(line):
                            line = line.strip()
                            if isAlphaNum(line) and isAlphaNum(main_string):
                                main_string += " " + line + " "
                            else:
                                main_string += line
                    if main_string:
                        dialogue.append(main_string)
                if len(dialogue) == 0:
                    print(f'{title} contains no readable dialogue')
            except:
                print(f'{title} is a bad title')
            
            if len(dialogue) > 100:
                film_dialogue[title] = dialogue
        
        return film_dialogue

    def getSingleFilmDialogue(self, title):
        """
        Gets the dialogue for a single film that matches
        the title parameter.
        """
        df = self.script_data[self.script_data.title == title].copy()
        return self.getFilmDialogue(df)

    def getFilmTitles(self):
        return self.script_data.title.unique()

    @staticmethod
    def read(filename: str) -> pd.DataFrame():
        with open(filename, "r") as f:
            content = f.readlines()
        content = content[1: -2]
        scripts = []
        for line in content:
            scripts.append(ast.literal_eval(line)[0])

        return pd.DataFrame(scripts)

    @staticmethod
    def removeControlCharacters(string):
        """
        Code taken from Alex Quinns response at
        https://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
        """
        return "".join(ch for ch in string if unicodedata.category(ch)[0] != "C")

    def main(self):
        pass


p = Parser()
titles = p.getFilmTitles()
dialogue_dict = p.getFilmDialogue()

with open('mycsvfile.csv','w') as f:
    w = csv.writer(f)
    w.writerows(dialogue_dict.items())