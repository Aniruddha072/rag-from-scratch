from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded successfully")

#Sample Chunks
chunk_a = "Age limit is 18-25 years"
chunk_b = "Salary is Rs 21,700"
chunk_c = "Applicants must be between 18 and 25 years old"

#User Question
question = "What is the age criteria?"

print("\nGenerating Embeddings...")

question_embedding = model.encode(question)
print("Embedding Length:", len(question_embedding))

print("\nFirst 10 Values:")
print(question_embedding[:10])

chunk_a_embedding = model.encode(chunk_a)
chunk_b_embedding = model.encode(chunk_b)
chunk_c_embedding = model.encode(chunk_c)

#Similarity scores
sim_a = cos_sim(question_embedding, chunk_a_embedding)
sim_b = cos_sim(question_embedding, chunk_b_embedding)
sim_c = cos_sim(question_embedding, chunk_c_embedding)

print("\nQuestion:")
print(question)

print("\nSimilarity Scores:")
print(f"Chunk A: {sim_a.item():.4f}")
print(f"Chunk B: {sim_b.item():.4f}")
print(f"Chunk C: {sim_c.item():.4f}")

scores = {
    "Chunk A": sim_a.item(),
    "Chunk B": sim_b.item(),
    "Chunk C": sim_c.item(),
}

best_match = max(scores, key=scores.get)
print("\nMost Relevant Chunk:")
print(best_match)