import logging
logging.basicConfig(level=logging.DEBUG, filename='console1.log', filemode='w')

result = []

def divider(a, b):
 if a < b:
    print("ValueError")
    logging.critical("ValueError")
    raise ValueError
 if b > 100:
    print("IndexError")
    logging.critical("IndexError")
    raise IndexError
 logging.critical(result)
 print(result)
 return a/b


data = {10: 2, 2: 5, "123": 4, 18: 50, tuple([2, 4, 6]): 15, 8 : 4}
print(data)

for key in data:
 res = divider(data[key], data[key])
 result.append(res)

print(result)