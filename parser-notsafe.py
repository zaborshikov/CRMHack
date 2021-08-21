from logging import error
import vk_api
import creds
vk_session = vk_api.VkApi(creds.login, creds.password)
try:
    vk_session.authorization()
except vk_api.AuthorizationError as error_msg:
    print(error_msg)

vk = vk_session.get_api()

analyze_id = str(-29534144)
postidlist = vk.wall.get(owner_id=analyze_id, count=1, offset=0)
a = str(postidlist['items'][0]['id'])
response = vk.wall.getComments(owner_id=analyze_id, post_id=a, count=1, sort='desc', offset=0)
b = response['items'][0]['text']
print(a)
print(b)