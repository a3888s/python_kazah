# Тема: Асинхронне програмування в Python
# Модуль asyncio

# Синхроний приклад

# import time
# from datetime import datetime
#
#
# def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print("fun1 завершена")
#
#
# def fun2(x):
#     print(x**2)
#     time.sleep(3)
#     print("fun2 завершена")
#
#
# def main():
#     fun1(4)
#     fun2(4)
#
#
# start = datetime.now()
#
# main()
#
# end = datetime.now()
# print(f"Час виконання {end-start}")

# Асинхронний приклад
# import asyncio  # Це спеціальний модуль для асинхронного програмування в Python
# from datetime import datetime


# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(5)
#     print("fun1 завершено")
#
#
# async def fun2(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print("fun2 завершено")
#
#
# async def fun3(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print("fun3 завершено")
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#     task3 = asyncio.create_task(fun3(4))
#
#     await task1
#     await task2
#
# start = datetime.now()
# asyncio.run(main())
# end = datetime.now()
# print(f"Час виконання: {end-start}")

websites_lists = [
    "https://lalafo.kg/",
    "https://highload.today/",
    "https://www.youtube.com/",
    "https://www.google.com/",
    "https://www.house.kg/snyat",
    "https://www.house.kg/snyat?page=2",
    "https://www.house.kg/snyat?page=3",
    "https://www.house.kg/snyat?page=4",
    "https://www.house.kg/snyat?page=5",
    "https://www.house.kg/snyat?page=6",
    "https://www.house.kg/snyat?page=7",
    "https://www.house.kg/snyat?page=8"
]
#
# import requests
# from datetime import datetime
#
#
# def make_request():
#     for url in websites_lists:
#         response = requests.get(url)
#         print(response.status_code)
#
#
# start = datetime.now()
# make_request()
# end = datetime.now()
# print(end - start)

# import aiohttp
# import asyncio
# from datetime import datetime
#
#
# async def make_async_request():
#     async with aiohttp.ClientSession() as session:
#         for url in websites_lists:
#             response = await session.get(url)
#             print(response.status)
#
# start = datetime.now()
# asyncio.run(make_async_request())
# end = datetime.now()
# print(end - start)









