from app import apps

app = apps()

if __name__ == '__main__':
    app.run(debug=True, port=80)