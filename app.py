from flask import Flask

app = Flask(__name__)

stores=[
    {
        "name":"mystore",
        "items":[
            {"name":"chair","price":1234}
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores":stores}