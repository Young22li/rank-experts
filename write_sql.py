import mysql.connector
from faker import Faker
import random

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",        
    user="root",    
    password="",
    database="test001",
    port = "3307"
)

cursor = db.cursor()

# Create a Faker object
fake = Faker()

# Predefined skills and locations
skills_list = [
    "Python, Machine Learning, NLP", 
    "Java, Spring Boot, AWS", 
    "C++, Data Structures, Algorithms", 
    "Project Management, Agile, Scrum", 
    "Data Science, SQL, Python", 
    "Cloud Computing, Kubernetes, Docker",
    "Cybersecurity, Penetration Testing, Network Security",
    "Digital Marketing, SEO, Social Media",
    "UI/UX Design, Figma, Adobe XD",
    "Blockchain, Ethereum, Smart Contracts",
    "Finance, Investment Analysis, Portfolio Management",
    "Accounting, Taxation, Financial Reporting",
    "Marketing Strategy, Brand Development, Content Creation",
    "Sales, Negotiation, Customer Relationship Management",
    "Legal Research, Contract Law, Corporate Governance",
    "Healthcare, Medical Research, Patient Care",
    "Nursing, Healthcare Management, Medical Billing",
    "Education, Curriculum Development, E-learning",
    "Supply Chain Management, Logistics, Procurement",
    "Operations Management, Process Optimization, Lean Manufacturing",
    "Human Resources, Talent Acquisition, Employee Relations",
    "Public Speaking, Presentation, Leadership Coaching",
    "Social Work, Counseling, Mental Health",
    "Graphic Design, Typography, Visual Communication",
    "Writing, Editing, Copywriting",
    "Photography, Videography, Post-Production",
    "Construction Management, Architecture, Urban Planning",
    "Real Estate, Property Development, Land Acquisition",
    "Retail Management, Customer Service, Inventory Management",
    "Hospitality Management, Event Planning, Customer Experience",
    "Tourism, Travel Planning, Cultural Exchange",
    "Logistics, Shipping, Freight Management",
    "Agriculture, Crop Management, Sustainability",
    "Energy Management, Renewable Resources, Solar Energy",
    "Aerospace Engineering, Flight Safety, Space Exploration",
    "Automotive Engineering, Vehicle Design, Manufacturing",
    "Fashion Design, Trend Analysis, Textile Innovation",
    "Culinary Arts, Food Safety, Restaurant Management",
    "Art History, Museum Curation, Gallery Management",
    "Music Production, Audio Engineering, Sound Design",
    "Theater Production, Directing, Stage Design",
    "Sports Management, Athlete Development, Event Coordination",
    "Language Translation, Interpretation, Linguistics",
    "Anthropology, Sociology, Cultural Studies"
]

locations_list = [
    "New York", "London", "Berlin", "San Francisco", 
    "Singapore", "Tokyo", "Toronto", "Sydney", "Paris", "Dubai"
]

# Generate and insert 1000 random records
for _ in range(1000):  # Change this if you need a different number of records
    name = fake.name()                           # Generate a random name
    skills = random.choice(skills_list)          # Choose a skill from the predefined list
    experience = random.randint(1, 30)           # Random experience between 1 and 30 years
    location = random.choice(locations_list)     # Choose a location from the predefined list
    
    # Insert data
    sql = "INSERT INTO experts (name, skills, experience, location) VALUES (%s, %s, %s, %s)"
    val = (name, skills, experience, location)
    
    cursor.execute(sql, val)

# Commit and close connection
db.commit()
print("1000 random records have been inserted into the 'experts' table.")

cursor.close()
db.close()