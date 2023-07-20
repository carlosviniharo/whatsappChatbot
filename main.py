from flask import Flask, request, Response
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def chatbot():

    incoming_msg = str(request.values.get("Body", "")).lower()
    response = MessagingResponse()
    q = incoming_msg
    result = []
    for i in search(q, num_results=3):
        result.append(i)

    msg = response.message(f"--- Results for '{incoming_msg}' ---")
    #for res in result:
    msg = response.message(result[1])
    print(Response(str(response), mimetype="application/xml"))
    return Response(str(response), mimetype="application/xml")


if __name__ == '__main__':
    app.run()
