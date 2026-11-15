import pandas as pd

df = pd.read_csv("cfb.csv")

season = int(input("Which season would you like to analyze? "))
season_data = df[df["Season"] == season]

if season_data.empty:

    print(f"Data for season of {season} not found.")
else:
    categories = { #create empty lists
        "10 or more wins:": [],
        "8-9 wins:": [],
        "6-7 wins:": [],
        "Fewer than 6 wins:": [],
    }

    for _, row in season_data.iterrows(): #building team categories
        team = row["Team"]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins:"].append(team)
        elif wins >= 8:
            categories["8-9 wins:"].append(team)
        elif wins >= 6:
            categories["6-7 wins:"].append(team)
        else:
            categories["Fewer than 6 wins:"].append(team)
#printing the results
    print(f"College football results for season of {season}:")
    for category, teams in categories.items():
        print(category)
        if teams:#notice nested loop to read both category then rows
            for team in teams:
                print(team)
        else:
            print("None")