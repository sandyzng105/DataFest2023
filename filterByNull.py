import pandas as pd

posts = pd.read_csv('reorderedPosts.csv', sep=',∞,', engine='python')
posts.to_csv('cleaned.csv')

questions = pd.read_csv('questions.csv')
null = questions[questions['TakenByAttorneyUno'].isna()]
print(len(null))

family = null.loc[null['Category'] == 'Family and Children']
print(len(family))

familyNull = posts[posts['QuestionUno'].isin(family['QuestionUno'])]
print(len(familyNull))

familyNull['PostText'].to_csv('familyNullPosts.csv')

other = null.loc[null['Category'] == 'Other']
print(len(other))

otherNull = posts[posts['QuestionUno'].isin(other['QuestionUno'])]
print(len(otherNull))

otherNull['PostText'].to_csv('otherNullPosts.csv')

#nullPosts.loc[nullPosts['col1'] == value]