import requests as req
# pic and pdf
# img
# url= 'https://tw.appledaily.com/resizer/x7sCreHQDDSnhoPg4uXPPUl0mMI=/760x570/filters:quality(100)/cloudfront-ap-northeast-1.images.arcpublishing.com/appledaily/WUI6UYEANBBMZOV3Z5OHDNDLSY.png'
# r=req.get(url)
#
# with open('123.jpeg', mode='wb') as file:
#     file.write(r.content)

# url= 'https://www.lib.ntu.edu.tw/doc/cl/etdsguide.pdf'
# r=req.get(url)
#
# with open('123.pdf', mode='wb') as file:
#     file.write(r.content)

# httpbin
url='https://httpbin.org/get'
params= {
    'page' :2,
    'count' :5
}
r=req.get(url,params=params)


print(r.text)