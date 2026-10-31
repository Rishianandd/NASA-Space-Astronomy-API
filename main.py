from nasa_api import get_astronomy_picture

data = get_astronomy_picture()

if data:

    print("\nNASA ASTRONOMY PICTURE OF THE DAY")
    print("----------------------------------")

    # Get the first picture
    picture = data[0] if isinstance(data, list) else data

    print("Title:", picture["title"])
    print("Date:", picture["date"])
    print("\nExplanation:", picture["explanation"])
    print("\nImage URL:", picture["url"])

else:
    print("Unable to retrieve NASA data.")