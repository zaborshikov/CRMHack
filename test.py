from flask_restful import Api
import dotn 
import creds
print(dotn.Api.create("fmproducts"))
# result = creds.vk.groups.getById(group_ids="fmproducts", group_id="fmproducts")
# # print(result)
# id_company = str(result[0]['id'])
# print(id_company)
# # shortname = creds.vk.groups.getById(group_ids="fmproducts", group_id="fmproducts")
# # print(dotn.Api.create("fmproducts"))
# # import creds
# # analyze_id = str(-190900168)
# # postidlist = creds.vk.wall.get(owner_id=analyze_id, count=100, offset=0) 
# # postid = postidlist['items'][0]['id']
# # print(postid)