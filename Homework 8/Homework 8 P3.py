################
# Author: Andrew Wang
# Date: 11/03/2019
# This programs reads this file and allows user to enter a year which the program will print out the team
#   that won the worlds series that year and how many time they've won since 1903 - 2009
#################
#Main function
def main():
    #Reads the file
    ww_winner = open('WorldSeriesWinners.txt','r')
    line = ww_winner.readlines()
    #Initializing variables
    team = {}
    team_win = set()
    team_win_d = {}
    count = 0

    #Creates a list with new line removed
    for i in range(len(line)):
        line[i] = line[i].rstrip('\n')

    #Creates a dictionary that correspondes year with winning team
    for i in range(len(line) + 2):
        dict_year = i + 1903
        if dict_year == 1904 or dict_year == 1994:
            team[dict_year] = None
            line.insert(i, None)
        else:
            team[dict_year] = line[i]

    #Creates a dictionary that counts how many times each team have won
    team_win.update(line)
    for key in team_win:
        wins = line.count(key)
        team_win_d[key] = wins

    #Allows user to input year
    year = int(input('Enter a year in the range 1903-2009: '))

    #If statement that determines the user inputted year and the winning team of that year
    if year >= 1903 and year <= 2009:
        if year == 1904 or year == 1994:
            print('The world series wasn\'nt played in the year %d' %year)
            
        else: 
            win_team = team.get(year)
            for v in team.values():
                if v == win_team:
                    count += 1
            

            print('The team that won the world series in %d is the %s.' %(year, win_team))
            print('They won the world series %d times.' %count)
        
        
      
    else:
        print('The data for year %d is not included in our database.' %year)

    ww_winner.close()
    
#Calling main function
main()

        
