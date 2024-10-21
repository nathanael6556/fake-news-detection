from flask import Flask, render_template, request
import model_evaluation
import data_preprocessing


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    y_percent = 0  # Inisialisasi y_percent dengan nilai default
    y_status = None

    if request.method == 'POST':
        news_text = request.form['news']
        
        if news_text: 
            news_text = data_preprocessing.clean_text(news_text)
            
            y_pred, y_status = model_evaluation.vote(news_text)
            
            if len(y_pred) > 0:  # Pastikan bahwa y_pred tidak kosong
                y_percent = (sum(y_pred) / 7) * 100  # Hitung persentase
            
            if sum(y_pred) / len(y_pred) > 0.5:
                result = 'Fake News Detected'
            else:
                result = 'News Looks Real'
    
    return render_template('index.html', result=result, y_percent=y_percent, y_status=y_status) 

if __name__ == '__main__':
    app.run(debug=True)
