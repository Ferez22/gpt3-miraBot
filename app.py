from flask import Flask, request, session
from twilio.twiml.messaging_response import messaging_response
from miraBot import ask, append_interaction_to_chat_log

app = Flask(__name__)
# if conversation becomes weird, change secret key
app.config['SECRET_KEY'] = '89djhf9lhkd93'

@app.route('/miraBot', methos=["POST"])
def mira():
    incoming_msg = resquest.values['Body']
    chast_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, 
                                                        chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)