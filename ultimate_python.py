# THE ULTIMATE PYTHON COMPILE

# CHECK PYTHON DIR version
import sys
print(sys.executable)
print(sys.version)
print(sys.version_info)

# BAG OF WORDS (BOW) aka COUNT VECTORIZER
vectorizer = CountVectorizer()
print( vectorizer.fit_transform(corpus).todense() ) #Gives bag of words feature vectors.
print( vectorizer.vocabulary_ )

# PANDAS check if DataFrame has Nan
df['A'].hasnans
