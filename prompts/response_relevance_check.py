'''
Check response relevance

Step 1: Calculate Similarities
Step 2: Vectorize Text
Step 3: Adapt the response
'''
import numpy as np
import spacy

model_spacy = spacy.load("en_core_web_md")

def cosine_similarities(vec1, vec2):
    overlap = np.dot(vec1, vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    cos_sim = overlap / (magnitude1 * magnitude2)
    return cos_sim

def generate_vector(text):
    return model_spacy(text).vector


def is_relevant(response, input, threshold=0.5):
    vectorized_input = generate_vector(input)
    vectorized_response = generate_vector(response)
    similarity = cosine_similarities(vectorized_input, vectorized_response)
    return similarity >= threshold

