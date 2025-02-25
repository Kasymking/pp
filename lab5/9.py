import re

text = "HelloWorldAiIsAmazing"

pattern = '(?<=[a-z])(?=[A-Z])' # Вставляем пробел только между строчной и заглавной буквой
result = re.sub(pattern, ' ', text)

print(result)