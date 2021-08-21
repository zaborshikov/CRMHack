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
    # n = 0
    # m = 0
    # for i in postsGroup:
    # while n < 10:
    #     idOfPost = str(['items'][0]['id'])
    #     while m < 10:
    #         response = vk.wall.getComments(owner_id=analyze_id, post_id=idOfPost, count=m, sort='desc', offset=0)
    #         try:
    #             textComment = response['items'][m]['text']
    #             print(textComment)
    #             print(idOfPost)
    #         except IndexError:
    #             pass
    #         m += 1
    #     n += 1


    # postidlist = vk.wall.get(owner_id=analyze_id, count=1, offset=0)
    # idOfPost = str(postidlist['items'][0]['id'])
    # response = vk.wall.getComments(owner_id=analyze_id, post_id=idOfPost, count=1, sort='desc', offset=0)
    # idOfPersonComment = str(idOfPost['items'][0]['id'])

    postidlist = vk.wall.get(owner_id=analyze_id, count=100, offset=0) #получаем последний пост со стены
    n = 0
    m = 0
    while n < 101:
        try:
            postid = str(postidlist['items'][n]['id'])
            print(postid)
            response = vk.wall.getComments(owner_id=analyze_id, post_id=postid, count=100, sort='desc', offset=0) #Получаем последний комментарий в последнем посте со стены
            while m < 101:
                try:
                    textComment = response['items'][m]['text']
                    print(textComment)
                    m += 1
                except IndexError:
                    break
            print(postid)
            n += 1
        except IndexError:
            break
    # postid = str(postidlist['items'][1]['id']) #получаем id поста в виде цифры и записываем
    # print(postsGroup)\
    # except IndexError:
    #     print('вы ненужное сообщество. живите с этим.')
if __name__ == '__main__':
    main()