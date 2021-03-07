import csv

selectedThemeFile = r'Themes\discord.csv'

theme = []

with open(str(selectedThemeFile)) as themeInput:
    themeReader = csv.reader(themeInput)
    for row in themeReader:
        theme.append(row)
        
print(theme)