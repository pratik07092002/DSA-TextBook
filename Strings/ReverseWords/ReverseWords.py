def reverse_words(s: str)-> str:
    words = s.strip().split()
    return " ".join(reversed(words))


answer = reverse_words("Hello my name is")
print(answer)