import random

responses = {'question': ["I don't know :(", 'you tell me!'],
             'statement': ['tell me more!',
                           'why do you think that?',
                           'how long have you felt this way?',
                           'I find that extremely interesting',
                           'can you back that up?',
                           'oh wow!',
                           ':)']
             }


def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    else:
        return random.choice(responses["statement"])
