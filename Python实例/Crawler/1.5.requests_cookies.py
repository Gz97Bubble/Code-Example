# coding:utf-8
import requests

url = 'https://github.com/g1320832596z'

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

# 构建cookie字典
temp = '_octo=GH1.1.278547650.1597412471; _ga=GA1.2.2145867146.1597412591; tz=Asia%2FShanghai; _device_id=9d3760b6814fb6c16ee7f54c653790dd; has_recent_activity=1; user_session=xOg44w-2bNjHNq8oPbAqArj_kEAf0Pe0o47LMQKw3M8WAmoM; __Host-user_session_same_site=xOg44w-2bNjHNq8oPbAqArj_kEAf0Pe0o47LMQKw3M8WAmoM; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=g1320832596z; _gh_sess=wUbQvSWD1b90AzpC7j6cCXT3o%2BT8pConC9Xo4nzfvqihC9BHFMiezsR71Lewg3SA5l9%2Bp39RJmoAjyG4zpbZ4xnBwvpfJ2JH%2FZKtM846gndNl5ucdtJwQDHeqLvJqydVsADXqcVBdXd%2Bqd4ZIEmj%2FmSRaoCGHAhC9iZzI7S7VaQUVmrAgXOi7rrEQ0OuuoY9eA7GbIAxyYCSsiEjhx%2FWX2jwOlUzE72HQKgsesNeMQHLtLsrxwKlpVeqpi%2FY3u1hBPKkwtichEkhM2cfXuGDCnAKOvW6kCOwN3asidOL62OZTAgJHGW3EBFbEc0tnHD0akIS7XDDO8%2F%2B6XKhqbTBAtca8MwGdU1fOsLmm%2BaIh1VmDOX8LRPRTkS6S3etWlziS5r1j4MN24HZnv87nEm7TkZ40jllqgrqFf1bK3CfxcxU54mIZoIEVSpI%2F7nY8Iw4MXMhsSFEuwLvGg%2FUqvxte0M6c1Zz1G7WDimq9mA6ZvcWXt4jlI%2FvoJLAfiu3jfPjmhLW3OhATwY6oti6sMf0FatF1iIfv9V5lzK1vGZ9ZK5KsmxOF6FT%2FQ5FsJOi6R46Hdw9cslqVRM3kw1QUlssmP8iC%2BhTTW00xaZIy5aen3jL8TnR3Q63MjBN4nlSI2GH5uH6c7PG8%2F01KB5%2BZ%2FifLjMFjgJ%2FHkXO0t4VioHKZNzstFQHMbbmiEzsO7aEj7bEqqmyBI52j0a1gFCYl4jVERDBKr9h9HAJzzoTFsd559maIiLlprJ2yQwH0UNVQMUEvG%2B92HlYKFMZJ2nkT4sRMkoyi1W%2F91nbVWyPMJkrsANKCnVUcTUm1KtGeif4zN7UXYGdOYUSf9rNmexAF%2BonNmLsQ%2BX%2BVKTy--QHYjhhwM8KaUnoEw--n9wvk9tDDIwNXAotHo3g%2Bg%3D%3D'

# 稳妥方案
cookie_list = temp.split('; ')

cookies = {cookie.split('=')[0]: cookie.split('=')[-1]for cookie in cookie_list}
# cookies = {}
# for cookie in cookie_list:
#     cookies[cookie.split('=')[0]] = cookie.split('=')[-1]

print(cookies)

response = requests.get(url, headers=headers, cookies=cookies)

with open("github_with_cookies3_.html", 'wb') as f:
    f.write(response.content)