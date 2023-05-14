import requests
import json

base_url = "https://petstore.swagger.io/v2/pet"
header = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {
      "id": 45679875678,
      "category": {
        "id": 5468798,
        "name": "Dogs"
      },
      "name": "Bobik",
      "photoUrls": [
        "http://kartinka.ru/bobik.jpg"
      ],
      "tags": [
        {
          "id": 93254,
          "name": "my_pet"
        }
      ],
      "status": "available"
    }


# Тип запроса Get, проверяем что нового питомца нет
print("GET запрос")
res_get = requests.get(f"{base_url}/{data['id']}", headers=header)
print("Код ответа:", res_get.status_code)
print(res_get.json())


# Тип запроса Post, добавляем нового питомца
print("POST запрос")
res_post = requests.post(base_url, headers=header, data=json.dumps(data))
print("Код ответа:", res_post.status_code)
print(res_post.json())


# Тип запроса Put, изменяем имя питомца
print("PUT запрос")
data["name"] = "Barbos"
res_put = requests.put(base_url, headers=header, data=json.dumps(data))
print("Код ответа:", res_put.status_code)
print(res_put.json())


# Тип запроса Delete, удаляем добавленного питомца
print("DELETE запрос")
res_delete = requests.delete(f"{base_url}/{data['id']}", headers=header)
print("Код ответа:", res_delete.status_code)
print(res_delete.json())