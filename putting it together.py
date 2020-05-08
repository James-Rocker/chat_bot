from chat_modules import pronouns as p
from chat_modules import questions as q
from chat_modules import keyphrase as k

rules = {'I want (.*)': ['What would it mean if you got {0}',
                         'Why do you want {0}',
                         "What's stopping you from getting {0}"],
         'do you remember (.*)': ['Did you think I would forget {0}',
                                  "Why haven't you been able to forget {0}",
                                  'What about {0}',
                                  'Yes .. and?'],
         'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
         'if (.*)': ["Do you really think it's likely that {0}",
                     'Do you wish that {0}',
                     'What do you think about {0}',
                     'Really--if {0}']}


# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = k.match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = p.replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response


bot_template = "BOT : {0}"
user_template = "USER : {0}"


def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")