from logging import error
import vk_api
import creds
import ai


def auth_handler():
    #2-factor verification
    key = input('Enter authentication code: ')
    return key, True


def main():
    vk_session = vk_api.VkApi(creds.login, creds.password, auth_handler=auth_handler)
    vk_session.auth()
    vk = vk_session.get_api()
    vk_link = str(-190900168)
    postidlist = vk.wall.get(owner_id=vk_link, count=100, offset=0) 
    n = 0
    m = 0
    commentsEmoji = []
    posts = []
    while n < 5:
        m = 0
        try:
            postid = str(postidlist['items'][n]['id'])
            response = vk.wall.getComments(owner_id=vk_link, post_id=postid, count=100, sort='desc', offset=0)
            while m < 5:
                try:
                    if 'text' not in response['items'][m]:
                        break
                    textComment = response['items'][m]['text']
                    commentsEmoji.insert(m, textComment)
                    m += 1
                except IndexError:
                    break
            posts.insert(n, postid)
            n += 1
        except IndexError:
            break

    for i in commentsEmoji:
        print(ai.analyze([i]))

if __name__ == '__main__':
    print(main())