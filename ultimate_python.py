# THE ULTIMATE PYTHON COMPILE

# CHECK PYTHON DIR version
import sys
print(sys.executable)
print(sys.version)
print(sys.version_info)

# BAG OF WORDS (BOW) aka COUNT VECTORIZER
vectorizer = CountVectorizer()
print( vectorizer.fit_transform(corpus).todense() )
print( vectorizer.vocabulary_ )
