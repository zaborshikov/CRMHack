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
    postidlist = vk.wall.get(owner_id=analyze_id, count=100, offset=0) 
    n = 0
    comments = []
    while n < 5:
        try:
            postid = str(postidlist['items'][n]['id'])
            print(postid)
            response = vk.wall.getComments(owner_id=analyze_id, post_id=postid, count=100, sort='desc', offset=0)
            try:
                textComment = response['items'][0]['text']
                print(textComment)
            except IndexError:
                break
            print(postid)
            n += 1
        except IndexError:
            break
if __name__ == '__main__':
    main()