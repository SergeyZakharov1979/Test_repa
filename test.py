s = "[2025-07-03 14:20:01] INFO: User 'alex' logged in"
# stop_list = '0123456789-:[]'
# status_and_mess = ''.join([symb for symb in s if symb not in stop_list])
# status, *message = status_and_mess.split()
# message = ' '.join(message)

# print(status, message)

status, message = s[s.find(']') + 1:].split(':')
print(status, message, sep='\n')
