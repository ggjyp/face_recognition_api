基于百度AI的人脸识别小实验
=======

## 实验环境
- python 3.5

## 实验效果
简单的整合了百度AI官网给出的人脸识别相关API，官方的示例代码是基于Python2.7环境下开发的，而这个项目使用的开发环境是Python3.5

实现的具体API有：

- 获取access_token
- 人脸注册
- 用户查询
- 获取用户组的用户列表
- 删除用户
- 人脸识别

实验时使用两张我自己的不同照片，一张用来注册，一张用来识别。 测试结果的置信度为93.88，这是一个可以接收的结果(一般置信度高于80即可认为是同一个人)

## 如何使用
1. 确保你的python版本是3.5
2. 将```getAccessToken```方法中的```client_id```和```client_secret```替换为你自己的百度云应用信息

## ToDo
这只是个调用接口的小实验，具体应用场景需要由移动设备或嵌入式设备作为图片的输入，同时需要搭建后台管理网站方便管理人脸信息
