# solution: we got
# K -> M    O -> Q      E -> G
# All word +2 to break this secret code

# capion "g fmnc" = "i hope"
# url "map" = "ocr"


word = ["a","b","c","d","e","f","g","h","i","j","k"
,"l","m","n","o","p","q","r","s","t","u","v","w","x"
,"y","z"]

word_plus = ["c","d","e","f","g","h","i","j","k"
,"l","m","n","o","p","q","r","s","t","u","v","w","x"
,"y","z","a","b"]

def too_many_secret(secrets):
    sentences = []
    secret = list(secrets)

    for x in range(len(secret)):
        if (secret[x] not in word):
            sentences.append(secret[x])
        else:
            before = word.index(secret[x])
            after = word_plus[before]
            sentences.append(after)

    finnaly = ''.join(sentences)
    return finnaly
