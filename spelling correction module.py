from textblob import TextBlob

blob=TextBlob('Helllo how aree yoou?')

corrected_blob=blob.correct()

print(f'Original text {blob}')
print(f'Corrected text {corrected_blob}')
