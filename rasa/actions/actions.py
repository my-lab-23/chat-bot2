verde = "Dal punto di vista etimologico, la parola \"verde\" deriva dal latino vir\u012ddis, corradicale del verbo virere, \"essere verde\"."
rosso = "Dal punto di vista etimologico, la parola \"rosso\" deriva dal latino r\u016dssum, corradicale di r\u016dbeum."
giallo = "Dal punto di vista etimologico in italiano la parola giallo deriva dal francese antico jalne a sua volta derivante dal latino g\u0103lb\u012dnum derivato di g\u0103lbus con significato di \u2018verde-giallo\u2019."

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import subprocess
import sys

class ans_etimology(Action):

    def name(self) -> Text:
        return "ans_etimology"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = tracker.get_slot('word')

        if word == 'rosso':
            response = f'{rosso}'
        elif word == 'verde':
            response = f'{verde}'
        elif word == 'giallo':
            response = f'{giallo}'
        else:
            response = 'Non la so.'

        dispatcher.utter_message(response)

        return [SlotSet('word', 'None')]

class ans_run_app(Action):

    def name(self) -> Text:
        return "ans_run_app"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        subprocess.Popen("firefox")
        dispatcher.utter_message("Ho lanciato la volpe.")

        return []

class ans_ave_maria(Action):

    def name(self) -> Text:
        return "ans_ave_maria"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Ave, o Maria, piena di grazia, \
                                  il Signore è con te. \
                                  Tu sei benedetta fra le donne \
                                  e benedetto è il frutto del tuo seno, Gesù. \
                                  Santa Maria, Madre di Dio, \
                                  prega per noi peccatori, \
                                  adesso e nell'ora della nostra morte. \
                                  Amen.")

        return []
