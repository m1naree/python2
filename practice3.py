from googletrans import Translator

translator = Translator()

sentence= input =("책을 읽으며 인상 깊었던 구절을 적어주세요:")
result1 = translator.translate(sentence,'en')
result2 = translator.translate(sentence,'de')


print("===========번역 결과==========")
print("입력어 ko: ")
print("번역어 1- en: ", result1)
print("번역어 2- de: ", result2)
print("==============================")