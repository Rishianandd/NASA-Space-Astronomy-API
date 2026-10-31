from nasa_api import get_today_picture

data = get_today_picture()

if data:
    print("\nNASA ASTRONOMY PICTURE OF THE DAY")
    print("----------------------------------")

    print("Title:", data["title"])
    print("Date:", data["date"])
    print("\nExplanation:", data["explanation"])
    print("\nImage URL:", data.get("hdurl", data.get("url")))

else:
    print("Unable to retrieve NASA data.")