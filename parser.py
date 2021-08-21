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
    analyze_id = str(-190900168)
    postidlist = vk.wall.get(owner_id=analyze_id, count=100, offset=0) 
    n = 0
    m = 0
    commentsEmoji = []
    posts = []
    while n < 101:
        m = 0
        try:
            postid = str(postidlist['items'][n]['id'])
            response = vk.wall.getComments(owner_id=analyze_id, post_id=postid, count=100, sort='desc', offset=0)
            while m < 101:
                try:
                    textComment = response['items'][m]['text']
                    commentsEmoji.insert(m, textComment)
                    m += 1
                except IndexError:
                    break
            posts.insert(n, postid)
            n += 1
        except IndexError:
            break

    
    # comments = [word if word != "👍" else 'Класс!' for word in commentsEmoji]
    # comments = [word if word != "🙃" else 'Прикольно' for word in commentsEmoji]
    # comments = [word if word != "🤨" else 'Что?' for word in commentsEmoji]
    # comments = [word if word != "👌" else 'Хорошо!' for word in commentsEmoji]
    # comments = [word if word != "🤷" else 'Не знаю...' for word in commentsEmoji]
    # comments = [word if word != "🤞" else 'Будем надеяться' for word in commentsEmoji]
    # comments = [word if word != "🔥" else 'Супер!' for word in commentsEmoji]

    # print(comments)    
    for i in commentsEmoji:
        return(ai.analyze([i]))
    # print(ai.analyze(comments))
    # return(comments, posts)
    # return(comments, posts)



if __name__ == '__main__':
    print(main())