# Intro to Search
# Author: Ubial
# 25 November

import csv

# Introduction to search algorithms
# Search for all songs by "Kendrick"
# Display all the YouTube and TikTok views
# Sort by either YouTube or TikTok views

def main():
    song_name_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15
    artist = "Kendrick Lamar"

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader object
        r = csv.reader(f)

        # go through reader line by line
        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                print(info)

if __name__ == "__main__":
    main()
