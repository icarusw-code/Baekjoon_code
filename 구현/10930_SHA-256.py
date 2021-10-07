# 해시 라이브러리를 이용
import hashlib

s = input()
# 바이트 객체를 구함
encoded_data = s.encode()
result = hashlib.sha256(encoded_data).hexdigest()

print(result)
