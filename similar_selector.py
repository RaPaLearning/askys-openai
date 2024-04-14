import json
from numpy import dot
from numpy.linalg import norm
from scipy.spatial import distance


def cosine_similarity(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def cosine_distance(a, b):
    return distance.cosine(a, b)


def cosine_similarities(text_embedding, question_embeddings):
    cos_similarities = list(map(lambda q_emb: cosine_similarity(q_emb, text_embedding), question_embeddings))
    print('cosine similarities for each question:')
    # the last question is out of context, so its cosine similarity must be least
    print(cos_similarities)


def cosine_distances(text_embedding, question_embeddings):
    cos_distances = list(map(lambda q_emb: cosine_distance(q_emb, text_embedding), question_embeddings))
    print('cosine distances for each question:')
    # the last question is out of context, so its cosine distance must be most
    print(cos_distances)


embeddings_filename = 'embeddings.json'
print(f'reading embeddings from: {embeddings_filename}')
with open(embeddings_filename, 'r') as f:
    embeddings = json.load(f)
    cosine_similarities(embeddings['text_embedding'], embeddings['question_embeddings'])
    cosine_distances(embeddings['text_embedding'], embeddings['question_embeddings'])
