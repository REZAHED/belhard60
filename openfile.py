import menu
import os
import json
class OpenFile:

    @staticmethod
    def opening_read(self):
        with open(self, 'r', encoding='utf-8-sig') as file:
            return file.read()


    @staticmethod
    def opening_json(self):

        if os.path.getsize('dictionary.json') !=0:
            with open(self, 'r', encoding='utf-8-sig') as file:
                return json.load(file)
        else:
            print("я здесь")

