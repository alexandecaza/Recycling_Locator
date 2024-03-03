
from sc_google_maps_api import ScrapeitCloudClient
from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)


@app.route('/info')
def info_page():
    return render_template('info.html')



@app.route('/', methods=['POST',"GET"])
def get_locations():

    if request.method =='POST':
        city = request.form.get('location' )
    else:
        city = request.args.get('location', 'Greensboro')
    locations = []

    



    if city:
        client = ScrapeitCloudClient(api_key='640e6b80-5cca-4e41-bf98-e8819568c5ac')

        response = client.scrape(
            params={
                "keyword": f"recycling in {city}",
                "country": "US",
                "domain": "com"
            }
        )

        data=response.json()

        print("Number of locations:", len(data["scrapingResult"]["locals"]))


        for local in data["scrapingResult"]["locals"]:
            location = {"Title": local.get("title", "No title available"),
            "Address": local.get("address", "No address available"),
            "rating":local.get('rating',"No rating available"),
            "Service_options": local.get("serviceOptions", "No service options available"),
            "phone":local.get('phone',"No phone number available"),

            }
            locations.append(location)
     
    return render_template("index.html",locations=locations)
if __name__ == '__main__':
    app.run(debug=True) 