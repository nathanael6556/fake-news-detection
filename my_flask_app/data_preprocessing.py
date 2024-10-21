import re
import indoNLP.preprocessing

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove all non-alphanumeric characters (keep letters and numbers)
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    
    # Replace numbers with the placeholder <NUMBER>
    text = re.sub(r'\b\d+\b', '<NUMBER>', text)
    
    # Remove HTML tags
    text = indoNLP.preprocessing.remove_html(text)
    
    # Remove URLs
    text = indoNLP.preprocessing.remove_url(text)
    
    # Replace slang words
    text = indoNLP.preprocessing.replace_slang(text)
    
    # Replace word elongations
    text = indoNLP.preprocessing.replace_word_elongation(text)
    
    return text
