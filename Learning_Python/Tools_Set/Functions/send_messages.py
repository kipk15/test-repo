# this should come after profile is created, and its purpose
# is to confirm with the user that they submitted correct info

# probably import profile

def send_messages(messages, name):
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print(f"\n sending {current_message.title()} now")
        sent_messages.append(current_message)
    return(sent_messages)

sent_messages0 = send_messages(messages0[:])
print(sent_messages0)
print (messages0)
greeting = ['Hello', 'Thank you for signing up', 
'Below is a profile we have created for you: ']

greeting = ['Hello', 'Thank you for signing up', 'Below is a profile we have created for you: ']
sent_messages0 = text(greeting[:])
#print(f"{greeting[0]} {formatted_name}, {greeting[1]}.\n{greeting[2]}")