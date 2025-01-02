import mysql.connector
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re



# Stopword list
stop_words = set(stopwords.words('english'))

# Function to extract keywords
def extract_keywords(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(f"[{string.punctuation}]", "", text)

    # Tokenize words
    words = word_tokenize(text)

    # Remove stopwords and single characters
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1]

    return " ".join(filtered_words)

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",        
        user="root",    
        password="",
        database="test001",
        port = "3307"
    )

# Function to get expert skills data from the database
def get_expert_skills():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    # Query for expert names and skills data
    cursor.execute("SELECT name, skills FROM experts")
    
    # Fetch all expert names and skill data
    expert_data = cursor.fetchall()
    
    cursor.close()
    db_connection.close()

    return expert_data

# Sample candidate description
candidate_description = input("Enter candidate description: ")
candidate_keywords = extract_keywords(candidate_description)

expert_data = get_expert_skills()  # Returns a list of (expert_name, expert_skills)

# Use TF-IDF vectorizer to convert text
vectorizer = TfidfVectorizer(ngram_range=(1, 2))  # Using bi-grams to enhance contextual understanding

# Combine candidate description and expert skills data
all_texts = [candidate_keywords] + [expert[1] for expert in expert_data]  # Only get expert skills

# Convert text into a TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(all_texts)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

# Create a list of expert names with their corresponding similarity score
expert_similarity_scores = [(expert_data[idx][0], similarity_matrix[0][idx]) for idx in range(len(expert_data))]

# Sort experts by similarity score in descending order
sorted_experts = sorted(expert_similarity_scores, key=lambda x: x[1], reverse=True)

# Output the top 100 experts with the highest similarity scores
top_n = 100  # Set the number of experts to output
for idx, (expert_name, score) in enumerate(sorted_experts[:top_n]):
    print(f"Expert {expert_name} similarity: {score:.4f}")