import re
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import os

nltk.data.path.append(os.path.join(os.getcwd(),'nltk_data'))



spam_keywords = [
    "Act now!", "Apply now!", "Call now!", "Don’t hesitate!", "For only", "Get started now",
    "Limited time", "Great offer", "Instant", "Now only", "Offer expires", "Once in a lifetime",
    "Order now", "Order today", "Special promotion", "Urgent", "While supplies last", "Bonus",
    "All new", "Amazing", "Certified", "Congratulations", "Fantastic deal", "For free",
    "Guaranteed", "Outstanding value", "Risk free", "Satisfaction guaranteed", "Free", "Free!",
    "Free trial", "Free consultation", "Free gift", "Free membership", "Free offer", "Free preview",
    "Free sample", "Free quote", "Sign up free today", "Deal", "Giving away", "No obligation",
    "No strings attached", "Offer", "Prize", "Trial", "Unlimited", "What are you waiting for?",
    "Win", "Winner", "You’re a winner!", "Won", "You have been selected", "#1", "100% free",
    "100% satisfied", "50% off", "One hundred percent guaranteed", "Click below", "Click here",
    "Increase sales", "Increase your sales", "Opt in", "Open", "Sale", "Sales", "Subscribe",
    "Chance", "Sample", "Satisfaction", "Solution", "Success", "Cards accepted", "Full refund",
    "Affordable", "Bargain", "Best price", "Cash", "Cash bonus", "Cheap", "Credit", "Discount",
    "For just $", "Lowest price", "Save big money", "Why pay more?", "Buy", "As seen on",
    "Buy direct", "Clearance", "Order", "$$$", "Marketing solutions", "Join millions", "Name brand",
    "No questions asked", "Giving it away", "Best rates", "Compare", "Drastically reduced"
]

common_email_domains = [
    "google.com","apple.com", "amazon.com", "microsoft.com", "google.com",
    "facebook.com", "twitter.com", "linkedin.com", "ibm.com","github.com","snapchat.com"
]

common_usernames = [
    "no_reply",
    "messages-noreply",
    "admin",
    "info",
    "support",
    "contact",
    "sales",
    "marketing",
    "help",
    "service",
    "hr",
    "careers",
    "billing",
    "accounts",
    "no-reply",
    "noreply",
    "notifications",
    "updates",
    "customer.service",
    "team",
    "ceo",
    "cto",
    "cfo",
    "legal",
    "it",
    "devops"
]


def spam_keywords_count(text):
    # Create a pattern for all the words in the list, joined with '|', and escape special characters
    pattern = '|'.join([re.escape(word) for word in spam_keywords])
    
    # Find all occurrences of any keyword (case-insensitive search)
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    # Return the total number of matches
    return len(matches)



# 2. Data Preprocessing
def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'http\S+|www.\S+', '', text)  # Remove URLs
    text = re.sub(r'\S+@\S+', '', text)  # Remove email addresses
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    #remove new line and tab \r\n
    text = re.sub(r'[\r\n]+', '', text)
    text = text.lower()  # Convert to lowercase
    return text

def check_if_sender_email_is_spam(email):
    username, domain = email.split('@')
     # Check if domain is in the list of common domains
    domain_valid = domain.lower() in common_email_domains
    
    # Check if username is in the list of common usernames
    username_valid = username.lower() in common_usernames

    if domain_valid and username_valid:
        return 'not spam'
    else:
        return 'spam'

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

def tokenize_text(text):
    return re.split(r'\W+', text.lower())

def lemmatize_tokens(tokens):
    wordlem = nltk.WordNetLemmatizer()
    return [wordlem.lemmatize(token) for token in tokens]

def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)



def prepare_email_for_model(email):
    cleaned = clean_text(email)
    polarity = get_polarity(cleaned)
    subjectivity = get_subjectivity(cleaned)
    keywords_count = spam_keywords_count(cleaned)
    return polarity,subjectivity,keywords_count
    

def predict(text,email):
    if check_if_sender_email_is_spam(email) == 'spam':
        return 'spam'
    
    polarity,subjectivity,keywords_count = prepare_email_for_model(text)
    print(f"Email address: {email}")
    print(f"Email text: {text}")
    print(f"subjectivity: {subjectivity}")
    print(f"polarity: {polarity}")
    print(f"spam keywords: {keywords_count}")
    prediction = 'not spam'
    if (polarity < 0.5 or subjectivity < 0.5) and (keywords_count > 5):
        prediction = 'spam'
    print(f"Prediction: {prediction}")
    print('############################################################3')
    return prediction