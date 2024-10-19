from flask import Flask, render_template, request
# import requests

app = Flask(__name__)

# Fungsi sederhana untuk menghitung kebenaran berita (fake news detector)
def calculate_fake_news_percentage(news_text):
    fake_indicators = ['hoax', 'fake', 'scam', 'fraud', 'misleading']
    words = news_text.lower().split()
    
    # Hitung berapa banyak kata dalam berita yang mengindikasikan 'fake news'
    fake_count = sum(1 for word in words if word in fake_indicators)
    
    # Persentase fake news berdasarkan kata-kata indikator
    fake_percentage = (fake_count / len(words)) * 100 if words else 0
    return fake_percentage

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None  # Nilai default untuk result
    fake_percentage = None  # Nilai default untuk persentase fake news
    error_message = None  # Pesan kesalahan jika URL tidak valid atau terjadi error
    
    if request.method == 'POST':
        option = request.form['option']  # Memeriksa apakah user memilih 'URL' atau 'Text'
        
        if option == 'text':  # Jika pengguna memilih input teks
            news_text = request.form['news']
            
            if news_text:  # Cek apakah teks telah diisi
                # Hitung persentase fake news
                fake_percentage = calculate_fake_news_percentage(news_text)
                if fake_percentage > 50:
                    result = 'Fake News Detected'
                else:
                    result = 'News Looks Real'
        
        elif option == 'url':  # Jika pengguna memilih input URL
            url = request.form['news']
            try:
                response = requests.get(url)
                if response.status_code == 200:  # Jika URL valid
                    news_text = response.text  # Mengambil teks dari URL
                    # Hitung persentase fake news
                    fake_percentage = calculate_fake_news_percentage(news_text)
                    if fake_percentage > 50:
                        result = 'Fake News Detected'
                    else:
                        result = 'News Looks Real'
                else:
                    error_message = 'Error fetching the URL. Status code: {}'.format(response.status_code)
            except requests.exceptions.RequestException as e:
                error_message = 'Invalid URL or request error: {}'.format(e)
    
    return render_template('index.html', result=result, fake_percentage=fake_percentage, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
