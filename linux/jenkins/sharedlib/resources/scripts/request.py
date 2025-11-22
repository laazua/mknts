import requests

# 最简单的 GET 请求
response = requests.get('https://www.baidu.com')
print(f"状态码: {response.status_code}")
print(f"响应内容长度: {len(response.text)}")
print(f"编码: {response.encoding}")