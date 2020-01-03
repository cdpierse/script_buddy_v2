import ast
import json
import re
import unicodedata

import pandas as pd


class Parser:

    def __init__(self):
        self.script_data = Parser.read('scripts.json')
    
    def getScriptText(self,df):
        return df['script_text'].values
    

    def getFilmDialogue(self,df=None):
        if df is None:
            raw_text = self.getScriptText(self.script_data)
        else:
            raw_text = self.getScriptText(df)[0][0]

        return raw_text

    def getSingleFilmDialogue(self,title):
        df = self.script_data[self.script_data.title == title].copy()
        return self.getFilmDialogue(df)


    @staticmethod
    def read(filename : str) -> pd.DataFrame():
        with open(filename,"r") as f:
                content = f.readlines()
        content = content[1 : -2]
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
        return "".join(ch for ch in string if unicodedata.category(ch)[0]!="C")

    
    def main(self):
        pass

p = Parser()
print(p.getSingleFilmDialogue("Joker"))
