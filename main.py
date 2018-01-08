# encoding:utf-8
import requests
import json
import base64

# 获取access_token
def getAccessToken():
    #请求参数
    client_id = '[替换为你的百度API Key]'
    client_secret = '[替换为你的百度Secret Key]'
    grant_type = 'client_credentials'

    request_url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': grant_type}
    r = requests.get(url=request_url, params=params)
    access_token = json.loads(r.text)['access_token']
    return access_token

###############################################################
# 人脸库管理
###############################################################

#人脸注册
def registerUserFace(uid, group_id, image, user_info):
    print('开始人脸注册')
    request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/add"
    f = open(image, 'rb')
    # 参数images：图像base64编码
    img = base64.b64encode(f.read())

    params = {'access_token': getAccessToken()}
    data = {"group_id": group_id, "image": img, "uid": uid, "user_info": user_info}
    r = requests.post(url=request_url, params=params, data=data)
    print(user_info,'注册成功')
    return json.loads(r.text)

# 用户信息查询
def getUserInfo(uid):
    print('开始用户信息查询')
    request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/get"
    params = {'access_token': getAccessToken()}
    data = {"uid": uid}
    r = requests.post(url=request_url, params=params, data=data)
    return json.loads(r.text)

# 组列表查询
def getGroupList():
    print('开始组列表查询')
    request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/getlist"
    params = {'access_token': getAccessToken()}
    r = requests.post(url=request_url, params=params,data='')
    return json.loads(r.text)

# 组内用户列表查询
def getGroupUsers(group_id):
    print('开始组内用户列表查询')
    request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/getlist"
    params = {'access_token': getAccessToken()}
    data = {'group_id': group_id}
    r = requests.post(url=request_url, params=params, data= data)
    return json.loads(r.text)

def deleteUser(uid):
    print('开始删除用户')
    request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/delete"
    params = {'access_token': getAccessToken()}
    data = {'uid': uid}
    r = requests.post(url=request_url, params=params, data=data)
    return json.loads(r.text)

###############################################################
# 人脸识别
###############################################################
def face_recognition(image, group_id):
    print('开始人脸识别')
    request_url = "https://aip.baidubce.com/rest/2.0/face/v2/identify"
    f = open(image, 'rb')
    # 参数images：图像base64编码
    img = base64.b64encode(f.read())

    params = {'access_token': getAccessToken()}
    data = {"group_id": group_id, "image": img}
    r = requests.post(url=request_url, params=params, data=data)
    return json.loads(r.text)

###############################################################
# 主程序
###############################################################
uid = 'jyp'
group_id = str('normal_group')
image = str('face_lib/rick.jpg') #注册用
test_image = str('face_lib/rick_test.jpg') #识别用
user_info = str('rick jiang')

# 人脸注册
# ret = registerUserFace(uid, group_id, image, user_info)

# 用户查询
# ret = getUserInfo(uid)

# 获取用户组的用户列表
# ret = getGroupUsers(group_id)

# 删除用户
# ret = deleteUser(uid)

# 人脸识别
ret = face_recognition(test_image, group_id)

print(ret)