from app import myapp_obj

app = myapp_obj  # Flask will detect this as the app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
