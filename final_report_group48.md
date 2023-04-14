# Introduction: 
### After looking for possible topics of interest for the project, our group decided to focus on music. In particular we wanted to know what factors contribute to the popularity of music. Knowing that people have different tastes, we were curious about what kinds of trends and influences we could discover after analyzing a musical dataset. Initially our broad guiding question was: “What factors make music popular? In line with this inquiry, our chosen data set was one that provided a list of songs and their scores in regards to different musical features like popularity,  accousticness, and loudness. 

# Exploratory Data Analysis: 
### The purpose of the EDA was to gain useful insights into our dataset in order to mold more refined and specific questions. We each took a slightly different approach even with our initial questions but found similar trends. One common question was whether there is a distinct musical feature that most correlates to or perhaps “causes” popularity. The basic correlation and scatter plots we constructed showed that this was not the case. As can be seen below, none of the features had a strong correlation with popularity. Through this we discovered that there isn’t a one to one causal relationship between the features and popularity, meaning we’d have to look further to find how they possibly interact. 

# Person 1: Alvin:
# Question 1 + Results: Is there a combination of elements that is only prevalent amongst the most popular songs?

![Loudness of Top 15 Songs](/images/alvin1.png)

![Pairplot](/images/alvin2.png)

### This bar plot is one of several. It shows the top 15 popular songs (listed most to least popular), and their loudness scores. The most significant implication of this graph is that the feature of loudness (similarly to the other tested features) doesn’t have a specific correlation with popularity. Even among the top 15, there is a distribution where some of the top songs in this list have high loudness, but also some of the lower rated songs in this list have high loudness as well. For example Kryptonite which is 14th has a higher loudness rating than Billie Jean, but lower popularity. The fact that this occurs with the other features shows that neither one or a combination of elements are necessarily only prevalent in the most popular songs. The pair plot similarly shows that the features do not have high or low ratings for only high or low popularity. For most features there are popular songs with high and low scores, and unpopular songs with the same. 


# Question 2 + Results: Are there musical features that contribute to the popularity of certain genres and not others? 

![Pairplot](/images/alvin2.png)

![Violin Plot](/images/alvin3.png)

### The approach I took to analyzing how the different genres interact with the different factors was to look at both distribution and quantity. The violin plot helps to identify the most popular genres and the distribution of popularity, which helps when looking at the pairplot to pay attention to the most popular genres and how their features relate to popularity. Rock songs which are the most prevalent seem to also have the least noticeable trend. For each factor, apart from loudness and acoustic-ness (danceability, energy, speechiness, temp, audio valence, loudness_energy and energy duration), rock and pop songs are distributed widely, having both high and low ratings in these factors and popularity across the board. In contrast hip hop and hard rock  seem to cluster in more of these categories. For acousticness, the hard rock songs all have below average acoustic-ness but are still popular, implying that this factor isn't impactful in their popularity. For loudness however, all hard rock and hip hop songs have above average scores and are highly popular, signifying that they are popular because of the factor of loudness. Loudness and energy seem to have similar impact in the popularity of pop songs. 

### Therefore, it can be said that thus far I know that hard rock, hip hop and pop songs are the most popular within my chosen sample size. The factors that most influence their popularity seem to be loudness and energy. The impact of loudness and energy is strengthened by the fact that the combined loundness_energy scores for these two genres are high along with their popularity.


# Person 2: Tobi Ogunbote 

# Research Question 1:

# Are songs with repeated verses or choruses considered more catchy or popular than songs without?

### I could not go through every song and check the ones that had repeated verses or choruses, that would take too long. The closest thing that I could find to back up this question was the variable “speechiness” which means the presence of spoken words in a track. The closer to 1.0, the more spoken words in the song. 

![Scatterplot](/images/tobi1.png)

### Figure 1. Scatterplot of speechiness and song popularity. This Scatterplot portrays how the speechiness of the songs in my dataset have correlation to the popularity of the song. Most songs in this dataset have a speechiness of less than 0.5 meaning they do not have many spoken words. At first I believed that the more words in a song, the more popular it is. Although, in this dataset, the songs with less words are the more popular ones. This is seen in the graph (the big clump of dots near the popularity of 60-80). Another thing seen here is the outlier (the one dot at the far right of the graph) that has a lot of words and is not that popular. This scatterplot helped me answer my question but not my main research question. 


# Research Question 2: 

# Are there specific genres of music that are more popular than others?

![Bar Graph](/images/tobi2.png)

### Figure 2. Bar graph depicting average song popularity in relation to the genres. In this graph, it shows the average song popularity of each genre and the most popular songs are Reggae, Metal, Pop and Hip-Hop. Average meaning the mean of the most and least popular songs put together. According to the graph, Reggae, Metal, Pop and Hip Hop are the most popular songs in this dataset. The least popular songs in this dataset are Son Cubaro, Bolero and Latin Pop. This occurred because there was only 1 song for each of these genres. I believe that if these genres had more songs in them, they would have a higher popularity. This graph still answers my question that there are genres that individuals find more popular than others in a set of songs. 

![Bar plot](/images/tobi3.png)

### Figure 3. Bar plot of song popularity with certain genres. This final graph is a box plot to better showcase the 4 most popular genres (Reggae, Metal, Pop and Hip-Hop). The plot for Hip-Hop is quite tall which means there is a big discrepancy in most popular and least popular songs. With this plot we can assume that most Hip-Hop songs in the dataset are not popular (since the upper quartile is shorter) but that some of them are popular, but the non-popular songs outweigh the popular ones. Taking a look at Reggae plot, it is very short meaning most Reggae songs in this set are popular. This might also be a bit inaccurate because there were only 3 songs in this dataset with the genre Reggae. This can be improved if there were more songs with this specific genre in the dataset to give a more accurate picture. The pop genre has a medium sized plot with a lot more popular songs than non popular songs. The Metal plot is just 1 line because there is only 1 song so this does not give a proper correlation of the data.

### In conclusion from all these plots and according to my modified dataset, Hip-Hop, Reggae and Pop are the most popular genres. Which means there are certain genres that make a song more popular. If that was not the case then all the genres would have had the same number. 


# Person 3: Annabelle 


# Question 1: What musical elements are most associated with each other and how are they related to music popularity? Are the trends consistent across the top and least popular songs?


# Figure 1: Correlation Heatmap between elements

![Corr Plot](/images/anna1.png)

# Figure 2 (Left) : Correlation between Musical Elements and  Popularity Score (Top 50 Songs)

![Corr Plot](/images/anna2.png)

# Figure 3 (Right): Correlation between Musical Elements and  Popularity Score (Bottom 50 Songs)

![Corr Plot](/images/anna3.png)



# Results:
### The results of my analysis showed that we the two elements that were most associated with each other are loudness and energy. The heatmap above shows that the two elements had a a strong positive correlation of  0.75 . I also found by comparing the popularity scores of each individual song to song popularity that audio valence and danceability had the strongest relationship to popularity.  Even though the each of the elements individually were not particularly correlated with song popularity, the aggregate elements loud_energy_prod had the  second highest correlation to popularity in the top 50 songs as shown in Figure 2. This positive correlation suggests that as loudness and energy both increase in a song, the song is associated with a higher popularity score. . These results are inconsistent in the bottom 50 songs however as song duration , audio valence and the aggregate element vale_dance_prod had the strongest relationship with popularity as shown in Figure 3. The negative correlation between the elements  and popularity suggests that among the least popular songs, higher audio valence and vale_dance_prod is associated with a lower popularity score. 


# Question 2: What musical features are most important to the song popularities of the most popular genres within this dataset?

# Figure 4: Average Song Popularity by Genre

![Popularity](/images/anna4.png)

# Figure 5: Most important features by most popular genre

![Genre](/images/anna5.png)

# Results:

### As identified by the mean popularity score of each genre, the most popular genres in my sample are Trap, Hip Hop and Pop Rock respectively.

### Trap: Based on the results above, energy and audio valence seem to be the most important musical features to the song popularity of trap music. This is seen in the correlation data generated in line 516, where energy and audio valence are shown to have correlations to popularity of -0.587341 and -0.552183, respectively. The importance of energy here can likely be explained by the fact that trap music tends to have a heavier emphasis on delivery, which is one of the elements of a song that can bring about the most energy. Additionally, the importance of audio valence can be explained by the presence of acoustically appealing elements in trap, such as synth, which often evokes feelings of euphoria.

### Hip Hop: Based on the results above, instrumentalness and danceability seem to be the most important musical features to the song popularity of the Hip Hop genre. This is seen in the correlation data generated in line 556, where instrumentalness and danceability are shown to have correlations to popularity of -0.597227 and 0.415569, respectively. The importance of instrumentalness here can likely be explained by the fact that hip hop music tends to have a heavier emphasis on the beats, which is where the instrumentation exists. The importance of danceability here also follows, as beats provide the rhythm for dance.

### Pop Rock: Based on the results above, song duration and loud_energy_prod seem to be the most important musical features to the song popularity in the Pop Rock genre. This is seen in the correlation data generated in line 558, where song duration and loud_energy_prod are shown to have correlations to popularity of -0.588488 and 0.536797, respectively. The importance of song duration here can likely be explained by the fact that Pop Rock songs tend to be more radio friendly, which would come with specific time retraints for artists seeking such a platform. The importance of loud_energy_prod can be explained by the fact that Pop rock is a genre that often emphasizes catchy melodies, memorable hooks, and sing-along choruses, and the use of loudness and energy can help to amplify these qualities and make the music more engaging and exciting. Loudness in particular can create a sense of power and urgency, and can be used to create contrast between softer and louder sections of a song, adding to its dynamic range.



# Summary/Conclusion: 
### While we all took slightly different approaches to the question of music and popularity, there is a common conclusion. While we initially thought that there may be broad general trends that show which features specifically correlate or match up with popularity, the relationships that exist are more complex and are compartmentalized. After subsetting data, these relationships are much easier to see. For example by subsetting according to genre, we found that for different genres, different features correlated with popularity levels. This makes sense logically as music is not homogenous. People have different music tastes which may align with the idea of genres. It then is reasonable that within these genres, certain traits of music are more preferred than others








