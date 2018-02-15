tweet = "I love Hamid!"
lengthOfTheTweet = len(tweet)
print(tweet)
maximumAmountOfCharactersForTweet = 280
if len(tweet) <= maximumAmountOfCharactersForTweet:
    print('Your tweet is {} characters and you have {} remaining characters left to use.'.format(len(tweet), maximumAmountOfCharactersForTweet-len(tweet)))
elif len(tweet) > maximumAmountOfCharactersForTweet:
    print('Your tweet is {} characters, and too long to post. Please reduce the number of characters by at least {} in order to post your tweet.'.format(len(tweet), len(tweet)-maximumAmountOfCharactersForTweet))
