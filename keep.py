from flask import Flask, request
from threading import Thread
app = Flask(" ")

def search_function(section, number):
    # استبدل هذا بالدالة الحقيقية التي لديك 
    return f"تم البحث في القسم {section} باستخدام الرقم {number}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        section = request.form.get('section')
        number = request.form.get('number')
        result = search_function(section, number)
        return f'''
            <html>
            <head>
                <title>علاماتي - النتائج</title>
                <style>
                    body {{
                        background: linear-gradient(to right, #FFFFFF, #87CEFA);
                        font-family: Arial, sans-serif;
                    }}
                    .result {{
                        margin: 0 auto;
                        width: 200px;
                        padding: 20px;
                        border: 1px solid #ccc;
                        background: #fff;
                        border-radius: 10px;
                    }}
                    .button {{
                        display: flex;
                        justify-content: center;
                        margin-top: 20px;
                    }}
                </style>
            </head>
            <body>
                <div class="result">
                    {result}
                </div>
                <div class="button">
                    <button onclick="window.history.back();">رجوع</button>
                </div>
            </body>
            </html>
            '''
    else:
        return '''
            <html>
            <head>
                <title>علاماتي</title>
                <style>
                    body {
                        background: linear-gradient(to right, #FFFFFF, #87CEFA);
                        font-family: Arial, sans-serif;
                    }
                    form {
                        margin: 0 auto;
                        width: 200px;
                        padding: 20px;
                        border: 1px solid #ccc;
                        background: #fff;
                        border-radius: 10px;
                    }
                    .button {
                        display: flex;
                        justify-content: center;
                        margin-top: 20px;
                    }
                </style>
            </head>
            <body>
                <form method="POST">
                <h1>علاماتي</h1>
                الرجاء اختيار القسم:<br>
                <input type="radio" name="section" value="arabic.csv"> عربي<br>
                <input type="radio" name="section" value="english.csv"> انكليزي<br>
                <input type="radio" name="section" value="3"> فرنسي<br>

                الرجاء إدخال الرقم:<br>
                <input type="text" name="number"><br>
                <div class="button">
                    <input type="submit" value="بحث">
                </div>
                </form>
            </body>
            </html>
            '''

def run():
    app.run(host="0.0.0.0", port=8080)

def keep():
    t = Thread(target=run)
    t.start()
if __name__ == '__main__':
    keep()
