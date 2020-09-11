# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
from datetime import datetime
ven = ''
date = ''
def dt(x):
    return datetime(x[0], x[1], x[2])
events = [(2020, 7, 5),(2020, 7, 12),(2020, 7, 19), (2020, 8, 2), (2020, 8, 9), (2020, 8, 16), (2020, 8, 30), (2020, 9, 6), (2020, 9, 13), (2020, 9, 27), (2020, 10, 11), (2020, 10, 25), (2020, 11, 1)]
venue = ['Austria', 'Austria', 'Hungary', 'Great Britain', 'Great Britain', 'Spain', 'Belgium', 'Italy Monza', 'Italy Mugello', 'Russia', 'Germany Nurburgring', 'Portugal Portimao', 'Italy Imola']
dates=[]
for i in events:
    dates.append(str(dt(i).strftime('%x')))
now = datetime.now().strftime('%x')
ind = 0
for i in dates:
    if i>=now:
        ven = venue[dates.index(i)]
        date = i
        ind = dates.index(i)
        break

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to the 2020 F1 calendar, what do you want to know ?" + '  sbinnala'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class NextGPIntentHandler(AbstractRequestHandler):
    """Handler for Next GP Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NextGPIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "The next F1 Grand Prix will be on: "+str(date)+' at '+ ven + '. Do you want to know anything else ?'
        # speak_output = 'The full calendar is, '+''.join(list(i+', '+j+'.\n' for i, j in zip(dates,venue)))

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FullCalendarIntentHandler(AbstractRequestHandler):
    """Handler for Full Calendar Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FullCalendarIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # speak_output = "The next Grand Prix will be on: "+str(date)+' at '+ ven + '.'
        speak_output = 'The full calendar is, '+''.join(list(i+', '+j+'.\n' for i, j in zip(dates,venue))) + '. Do you want to know anything else ?'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class RemainIntentHandler(AbstractRequestHandler):
    """Handler for Remain Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RemainIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # speak_output = "The next Grand Prix will be on: "+str(date)+' at '+ ven + '.'
        speak_output = 'The remaining events are , '+''.join(list(i+', '+j+'.\n' for i, j in list(zip(dates,venue))[ind:]))+ '. Do you want to know anything else ?'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class YesIntentHandler(AbstractRequestHandler):
    """Handler for Remain Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # speak_output = "The next Grand Prix will be on: "+str(date)+' at '+ ven + '.'
        speak_output = 'Ok. Tell me.'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class NoIntentHandler(AbstractRequestHandler):
    """Handler for Remain Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # speak_output = "The next Grand Prix will be on: "+str(date)+' at '+ ven + '.'
        speak_output = 'Understandable, have a good day.'

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can ask me about the next Grand Prix ,  all the remaining Grand Prix ,  and the full race calendar "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(NextGPIntentHandler())
sb.add_request_handler(RemainIntentHandler())
sb.add_request_handler(FullCalendarIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()