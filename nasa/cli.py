from nasa import get_today_picture


def main():
    print("Connecting to NASA API...")

    data = get_today_picture()

    if not data:
        print("Unable to retrieve NASA data.")
        return

    print("\nNASA ASTRONOMY PICTURE OF THE DAY")
    print("----------------------------------")
    print("Title:", data.get("title"))
    print("Date:", data.get("date"))
    print("\nExplanation:", data.get("explanation"))
    print("\nImage URL:", data.get("hdurl", data.get("url")))


if __name__ == "__main__":
    main()