'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'FFvj8Rd2MYHc3IEN3mUFI5z9g'
MY_CONSUMER_SECRET = 'zt6b03TEqaUjnYj6fWKx52gfDQE5IJ9zR7eRmzo8icTEgiZq0O'
MY_ACCESS_TOKEN_KEY = '4131419173-RMxKSrMYeS2J3vQkThrYomcHUpAUiPXZ5r55T9v'
MY_ACCESS_TOKEN_SECRET = 'dqJwuZX0Ks0ojrwXtCH4AbDDt9cx8ttE9UOThZg2AJ2Qo'

SOURCE_ACCOUNTS = ["scroll_in"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "scroll_ebooks" #The name of the account you're tweeting to.
