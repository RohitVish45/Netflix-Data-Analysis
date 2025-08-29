# Import necessary libraries

import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset

df = pd.read_csv("netflix_titles.csv")

# Drop unnecessary columns to simplify analysis

df.drop(columns=['cast','director','duration','date_added','description','show_id'],inplace=True)
print(df.columns)

# Drop rows with missing values to ensure clean data

df.dropna(subset=['type','release_year','title','country','rating','listed_in'],inplace=True)


# Count the number of Movies and TV Shows

value_count = df['type'].value_counts()


# Create a bar chart comparing Movies and TV Shows

plt.bar(value_count.index.tolist(), value_count.values.tolist(), color=['blue','green'], label='Movies VS TV Shows', width=0.8)
plt.title("Movies V/S TV Shows")
plt.xlabel("Type of Content")
plt.ylabel("Count")
plt.legend()
plt.savefig('Movies_VS_TV_Shows.png', dpi=300, bbox_inches='tight')
plt.show()

# Count the distribution of content ratings

rating_count = df['rating'].value_counts()

# for getting a different colour for different slice
cmap = plt.get_cmap('Set3')
color = [cmap(i) for i in range(len(rating_count))]

# Create a pie chart to visualize the percentage of each content rating

plt.pie(rating_count, labels=rating_count.index.tolist(), colors=color, autopct='%1.1f%%')
plt.title('Percentage of Content Rating')
plt.legend()
plt.savefig('content_rating.png', dpi=300, bbox_inches='tight')
plt.show()

# Count titles by country

country_count = df['country'].value_counts().head(10)

# Create a bar chart showing top 10 countries with the most content

plt.bar(country_count.index.tolist(), country_count.values.tolist(), label='Country_with_most_content', color = ['skyblue', 'orange', 'green', 'red', 'purple', 'gold', 'pink', 'cyan', 'magenta', 'lime'], width=0.8)
plt.title('Top 10 Countries with most content')
plt.xlabel('Countries')
plt.xticks(rotation=45)
plt.ylabel('No of Content')
plt.legend()
plt.savefig('Country_with_most_content.png', dpi=300, bbox_inches='tight')
plt.show()

# Count the number of titles released each year

year_count = df['release_year'].value_counts().sort_index()

# Create a line chart showing content released by year

plt.plot(year_count.index.tolist(), year_count.values.tolist(), color='r',marker='o', label='Content released by year', linewidth=2)
plt.title('Content Released by Year')
plt.xlabel('Years')
plt.ylabel('No of Content by each year')
plt.legend()
plt.savefig('content_released_by_year.png', dpi=300, bbox_inches='tight')
plt.show()

genres_count = df['listed_in'].value_counts().head(10)


# Visualize the top 10 genres from the 'listed_in' column

plt.pie(genres_count, labels=genres_count.index.tolist(), autopct='%1.1f%%', colors=['skyblue', 'orange', 'green', 'red', 'purple', 'gold', 'pink', 'cyan', 'magenta', 'lime'])
plt.title("Top 10 genres")
plt.legend('upper left')
plt.savefig('Top_10_genres.png', dpi=300, bbox_inches='tight')
plt.show()
