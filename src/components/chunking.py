import re
from collections import Counter
import math

def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    return float(numerator) / denominator

def create_embedding(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def semantic_chunking(text, similarity_threshold=0.5):
    chunks = []
    sentences = re.split(r'\n\s*\n', text.strip())
    current_chunk = sentences.pop(0)
    current_embedding = create_embedding(current_chunk)
    count = 0
    while sentences:
        sentence_embedding = create_embedding(sentences[count])
        similarity = cosine_similarity(current_embedding, sentence_embedding)
        

        if similarity >= similarity_threshold:
            current_chunk += " " + sentences[count]
            sentences.pop(count)
            count -= 1
        else:
            count += 1
        
        if count == len(sentences):
            current_chunk = sentences.pop(0)
            current_embedding = create_embedding(current_chunk)
            count = 0
            chunks.append(current_chunk)
    
    return chunks