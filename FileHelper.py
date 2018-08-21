#coding=utf8
import itchat, time


itchat.auto_login(hotReload=True)



itchat.send((u'你好，现在是 %s' % time.asctime( time.localtime(time.time()) )), toUserName='filehelper')

for num in range(1, 10):
	#name后填微信备注即可
	users = itchat.search_friends(name = u'境由心生')
	#获取对方UserName
	#print(users[0]['UserName'])
	itchat.send((u'你好，现在是 %s' % time.asctime( time.localtime(time.time()) )), users[0]['UserName'])
	print('123');
	time.sleep(5)



# SINCERE_WISH = u'祝%s新年快乐！'
# REAL_SINCERE_WISH = u'祝%s新年快乐！！'

# def send_wishes():
#     friendList = itchat.get_friends(update=True)[1:]
#     for friend in friendList:
#         # 如果不是演示目的，把下面的方法改为itchat.send即可
#         print(SINCERE_WISH % (friend['DisplayName']
#             or friend['NickName']), friend['UserName'])
#         time.sleep(.5)

# def send_special_wishes(chatroomName='wishgroup'):
#     itchat.get_chatrooms(update=True)
#     chatrooms = itchat.search_chatrooms(name=chatroomName)
#     if chatrooms is None:
#         print(u'没有找到群聊：' + chatroomName)
#     else:
#         chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
#         for friend in chatroom['MemberList']:
#             friend = itchat.search_friends(userName=friend['UserName'])
#             # 如果不是演示目的，把下面的方法改为itchat.send即可
#             print(REAL_SINCERE_WISH % (friend['DisplayName']
#                 or friend['NickName']), friend['UserName'])
#             time.sleep(.5)

# send_wishes()
# send_special_wishes()