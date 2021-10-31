# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionIndiadeaths(Action):

    def name(self) -> Text:
        return "action_deaths_india"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses=requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        data=responses["data"]
        date=data[-1]["day"]
        total=data[-1]["summary"]["deaths"]
        message="Number of Deaths in India due to covid is " + str(total)+"as of "+str(date)



        dispatcher.utter_message(message)

        return []


class ActionIndiacases(Action):

    def name(self) -> Text:
        return "action_cases_india"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses=requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        data=responses["data"]
        date=data[-1]["day"]
        cases=data[-1]["summary"]["total"]
        print(cases)
        message="Number of Deaths in India due to covid is " + str(cases)+"as of "+str(date)



        dispatcher.utter_message(message)

        return []


class ActionStatecases(Action):

    def name(self) -> Text:
        return "action_cases_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        message="enter a valid state name"
        entities=tracker.latest_message['entities']
        for e in entities:
            if e['entity']=='state':
                state=e['value']
            # if e['entity']=='type':
            #     type=e['value']


        for data in responses["data"][-1]["regional"]:
            if data["loc"] == state.title():
                message = " number of active cases in " + state.title() + " is " + str(data["totalConfirmed"])
        # else:
        #     for data in responses["data"][-1]["regional"]:
        #         if data["loc"] == state.title():
        #             message = " number of active cases in " + state.title() + " is " + str(data["deaths"])

        dispatcher.utter_message(message)

        return []

class ActionStatedeaths(Action):

    def name(self) -> Text:
        return "action_deaths_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        message="enter a valid state name"
        entities=tracker.latest_message['entities']
        for e in entities:
            if e['entity']=='state':
                state=e['value']

        for data in responses["data"][-1]["regional"]:
            if data["loc"]==state.title():
                message=" number of active cases in "+ data["loc"].title() + " is "+str(data["deaths"])

        dispatcher.utter_message(message)

        return []


class ActionIndiacasestime(Action):

    def name(self) -> Text:
        return "action_cases_india_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses=requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        entities = tracker.latest_message['entities']
        message="enter the right time"
        for e in entities:
            if e['entity']=='time':
                time=e['value']
        data=responses["data"]
        for date in data:
            if date["day"]==time.partition("T")[0]:
                # cases=data[time]["summary"]["total"]
                message = "Number of cases in India due to covid is " + str(date["summary"]["total"]) + " on " + str(time)

        dispatcher.utter_message(message)

        return []



class ActionIndiacasestime(Action):

    def name(self) -> Text:
        return "action_deaths_india_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses=requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        message="enter the right time"
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity']=='time':
                time=e['value']
        data=responses["data"]
        for date in data:
            if date["day"]==time.partition("T")[0]:
                # cases=data[time]["summary"]["total"]
                message = "Number of Deaths in India due to covid is " + str(date["summary"]["deaths"]) + " on " + str(time)

        dispatcher.utter_message(message)

        return []


class ActionStatedeathstime(Action):

    def name(self) -> Text:
        return "action_deaths_state_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        message="enter a valid state name"
        entities=tracker.latest_message['entities']
        for e in entities:
            if e['entity']=='state':
                state=e['value']
            if e['entity']=='time':
                time=e['value']

        for data in responses["data"]:
            if data["day"]==time.partition("T")[0]:
                for location in data["regional"]:
                    if location["loc"]==state.title():
                        message = " number of deaths in " + location["loc"].title() + " is " + str(location["deaths"])


        dispatcher.utter_message(message)

        return []


class ActionStatecasestime(Action):

    def name(self) -> Text:
        return "action_cases_state_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        message = "enter a valid state name"
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'state':
                state = e['value']
            elif e['entity'] == 'time':
                time = e['value']

        for data in responses["data"]:
            if data["day"] == time.partition("T")[0]:
                for location in data["regional"]:
                    if location["loc"] == state.title():
                        message = " number of active cases in " + location["loc"].title() + " is " + str(
                            location["totalConfirmed"])

        dispatcher.utter_message(message)

        return []
