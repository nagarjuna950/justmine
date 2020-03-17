
import os
import requests
from rasa_sdk import Action, Tracker
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union, Optional 

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class MoodIdentifier(Action):
    def name(self) -> Text:
        return 'action_mood_identifier'

    def run(self, dispatcher, tracker, domain):
        intent =  tracker.latest_message['intent'].get('name')
        text = tracker.latest_message.get("text")
        print(intent)
        print(text)
        print(type(intent))
        if text=='1star':
            dispatcher.utter_template("utter_q2_one_apo1",tracker)
            dispatcher.utter_template("utter_q2_one_apo2",tracker)
            dispatcher.utter_template("utter_q2_one_a",tracker)                 
        elif text=='2star':
            dispatcher.utter_template("utter_q2_two_apo1",tracker)
            dispatcher.utter_template("utter_q2_two_apo2",tracker)
            dispatcher.utter_template("utter_q2_two_a",tracker)         
        elif text=='3star':
            dispatcher.utter_template("utter_q2_three_apo1",tracker)
            dispatcher.utter_template("utter_q2_three_apo2",tracker)
            dispatcher.utter_template("utter_q2_three_a",tracker)       
        elif text=='4star':
            dispatcher.utter_template("utter_q2_four_apo1",tracker)
            dispatcher.utter_template("utter_q2_four_apo2",tracker)
            dispatcher.utter_template("utter_q2_four_a",tracker)         
        elif text=='5star':
            dispatcher.utter_template("utter_q2_five_apo1",tracker)
            dispatcher.utter_template("utter_q2_five_apo2",tracker)
            dispatcher.utter_template("utter_q2_five_a",tracker)       
        return[]

class MoodIdentifier(Action):
    def name(self) -> Text:
        return 'action_mood_identifier6'

    def run(self, dispatcher, tracker, domain):
        intent =  tracker.latest_message['intent'].get('name')
        print(intent)
        print(type(intent))
        if intent in "mood_happy":
            dispatcher.utter_template("utter_q7",tracker)
        else:
            dispatcher.utter_template("utter_thankyou1",tracker)
        return[]

class MoodIdentifier(Action):
    def name(self) -> Text:
        return 'action_mood_identifier7'

    def run(self, dispatcher, tracker, domain):
        intent =  tracker.latest_message['intent'].get('name')
        print(intent)
        print(type(intent))
        if intent in "mood_happy":
            dispatcher.utter_template("utter_thankyou",tracker)
            dispatcher.utter_template("utter_thankyou1",tracker)
        else:
            dispatcher.utter_template("utter_thankyou1",tracker)
        return[]



class Feedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "feedback_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["opt","opt1"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            
            "opt": [self.from_entity(entity="opt"), self.from_text()],
            "opt1": [self.from_entity(entity="opt1"), self.from_text()],

           
            
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_submit", tracker)
        return []

class Feedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "feedback_form3"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feedback3"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            
            "feedback3": [self.from_entity(entity="feedback3"), self.from_text()],
            
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_submit", tracker)
        return []
        
class Feedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "feedback_form5"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feedback5"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            
            "feedback5": [self.from_entity(entity="feedback5"), self.from_text()],
            
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_submit", tracker)
        return []
          
class Feedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "feedback_form4"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feedback4"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            
            "feedback4": [self.from_entity(entity="feedback4"), self.from_text()],
            
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_submit", tracker)
        return []
          





        
          






