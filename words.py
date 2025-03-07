season = input("What is your favourite season: ")

season_list = ["summer", "winter", "autumn", "spring"]

if season.lower().strip() in season_list:
    print("That is a valid season")
else:
    print("That is not a valid season.")

book = input("What is the first book in the Bible?\na) Genesis\nb) Exodus\nc) Numbers\nd) Leviticus\n>>")