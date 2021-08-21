from logging import error
import vk_api
import creds
def auth_handler():
    #2-factor verification
    key = input('Enter authentication code: ')
    return key, True
def main():
    vk_session = vk_api.VkApi(creds.login, creds.password, auth_handler=auth_handler)
    vk_session.auth()
    vk = vk_session.get_api()

    analyze_id = str(-190900168)
    postidlist = vk.wall.get(owner_id=analyze_id, count=1, offset=0)
    idOfPersonComment = str(postidlist['items'][0]['id'])
    response = vk.wall.getComments(owner_id=analyze_id, post_id=idOfPersonComment, count=1, sort='desc', offset=0)
    try:
        textComment = response['items'][0]['text']
        print(idOfPersonComment)
        print(textComment)
    except IndexError:
        print('вы ненужное сообщество. живите с этим.')
if __name__ == '__main__':
    main()