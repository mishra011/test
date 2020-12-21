# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


#This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


# class ActionSessionStart(Action):
#     def name(self) -> Text:
#         return "action_session_start"

#     @staticmethod
#     def fetch_slots(tracker: Tracker) -> List[EventType]:
#         """Collect slots that contain the user's name and phone number."""

#         slots = []

#         for key in ("name"):
#             value = tracker.get_slot(key)
#             if value is not None:
#                 slots.append(SlotSet(key=key, value=value))

#         return slots

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:

#         # the session should begin with a `session_started` event
#         events = [SessionStarted()]

#         # any slots that should be carried over should come after the
#         # `session_started` event
#         events.extend(self.fetch_slots(tracker))

#         # an `action_listen` should be added at the end as a user message follows
#         events.append(ActionExecuted("action_listen"))

#         return events