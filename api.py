from fastapi import FastAPI
import io
from starlette.responses import StreamingResponse
import requests

app = FastAPI(
    title="App",
    description="FAST API calls",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }, )


@app.get("/home")
def home(name: str):
    return "Welcome Home! " + name


@app.get("/plot-iris")
def plot_iris():
    """This is to Plot Iris!"""
    import pandas as pd
    import matplotlib.pyplot as plt

    url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")

    return StreamingResponse(file, media_type="image/jpeg")


@app.get("/lena")
def lena():
    resp = requests.get("https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png")
    file = io.BytesIO(resp.content)
    return StreamingResponse(file, media_type="image/jpeg")
