import creds
import ai
import db


def main():
    analyze_shrtnm = input()
    analyze_id = db.Database.create(analyze_shrtnm)
    postidlist = creds.vk.wall.get(owner_id=analyze_id, count=100, offset=0) 
    n = 0
    m = 0
    commentsEmoji = []
    posts = []
    while n < 5:
        m = 0
        try:
            postid = str(postidlist['items'][n]['id'])
            response = creds.vk.wall.getComments(owner_id=analyze_id, post_id=postid, count=100, sort='desc', offset=0)
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

    

    print(commentsEmoji)   
    
    for i in commentsEmoji:
        print(ai.analyze([i], analyze_id))

if __name__ == '__main__':
    print(main())