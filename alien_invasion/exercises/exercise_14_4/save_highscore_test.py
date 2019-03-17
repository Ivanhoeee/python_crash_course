
def save_score_username(filename, score, username): 
	if score > 0: 
		with open(filename, 'a') as file_object: 
			file_object.write('\n' + username + "," +  str(score))

filename = 'highscores.txt'		
score = 2
save_score_username(filename, 50, "ivan") 		

def load_highscore(filename): 
	# load the highest score in file
	import pandas as pd
	df_scores = pd.read_csv(filename, header = 0)
	# find highscore
	highscore = df_scores['Score'].values.max()
	return highscore
	
print(load_highscore('highscores.txt'))

