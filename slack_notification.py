from slacker import Slacker


def lambda_handler(event=None, context=None):
    slack = Slacker("")
    if slack.api.test().successful:
        print(f"Connected to {slack.team.info().body['team']['name']}.")
    else:
        print('Try Again!')
    channels = ['tejasupport','devopsdiscussion']
    # Post a message
    for ch in channels:
        slack.chat.post_message(channel='{}'.format(ch),
                        text='Have a great day! on another channel',
                        username='Python Test')