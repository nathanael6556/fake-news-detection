from flask import Flask, render_template, request
import model_evaluation
import data_preprocessing

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    fake_percentage = None
    real_percentage = None

    if request.method == 'POST':
        news_text = request.form['news']  # Get the news text input from the form
        
        if news_text:  # Ensure that text has been entered
            news_text = data_preprocessing.clean_text(news_text)
            
            # 'vote' returns a tuple (y_pred, y_status), so unpack them
            y_pred, y_status = model_evaluation.vote(news_text)
            
            fake_percentage = (sum(y_pred) / len(y_pred)) * 100  # Calculate fake news probability
            real_percentage = 100 - fake_percentage  # Calculate real news percentage
            
            if fake_percentage > 50:
                result = 'Fake News Detected'
            else:
                result = 'News Looks Real'
    
    # Pass real_percentage and fake_percentage to the template
    return render_template('index.html', result=result, real_percentage=real_percentage, fake_percentage=fake_percentage)

if __name__ == '__main__':
    app.run(debug=True)
