def displayConvo(convo):
    if convo.name == 'start':
        return 'start2'
    elif convo.name == "start":
        return None

def getConversation(conversationName, conversations):
    for x in conversations:
        if x.name == conversationName:
            return (x)

def talkToNPC(conversations):
    convo = getConversation ('start', conversations)
    nextConvo = displayConvo(convo)
    while nextConvo != None:
        convo = getConversation (nextConvo, conversations)
        nextConvo = displayConvo(convo)

class convo:
    def __init__(self, name, text, responses):
        self.name = name
        self.text = text
        self.responses = responses

convo1 = convo('start', 'hello', [])
convo2 = convo('start2', 'hello', [])

myConversations = [convo1, convo2]

talkToNPC(myConversations)

        
