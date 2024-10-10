# Email Spam Detector

## Overview
A Python application that detects spam in emails using NLP and keyword analysis. It includes a Tkinter-based GUI for users to input email text and addresses for real-time spam prediction.

## Features
- **Keyword Detection**: Identifies spam-related phrases.
- **Sender Email Check**: Verifies common email domains and usernames.
- **Sentiment Analysis**: Uses polarity and subjectivity to assess email content.
- **GUI**: User-friendly interface for easy input and prediction.

## Structure

### Logic Module (`model.py`)
- **Functions**: 
  - `clean_text()`: Cleans email content.
  - `spam_keywords_count()`: Counts spam-related keywords.
  - `check_if_sender_email_is_spam()`: Validates email addresses.
  - `predict()`: Combines all checks to classify emails as spam or not.

### GUI Module (`index.py`)
- **Components**:
  - Input fields for email address and content.
  - Buttons for prediction and clearing input.
  - Displays prediction result with color-coded output.

## Installation
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


3. Run the application:
   ```bash
   python index.py
   ```

## Dependencies
- `nltk`, `TextBlob`, `Tkinter`

## License
Licensed under MIT.