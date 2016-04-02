from string import punctuation
import string
from build_knn import build_classifier

s = 'Hello world, jiachen!'

trans = {ord(c): None for c in string.punctuation}

word = s.translate(trans)

word = build_classifier.tokenize(word)


print(word)
