import csv #Import csv module

with open ('election_data.csv') as csvfile: #Start csv file handling

    csvreader=csv.reader(csvfile, delimiter=',') #Specify delimiter and variable 
    header=next(csvreader) #Read the header row first

    ballot_list=[]
    counties_list=[]
    candidates_list=[]
    percentage_list=[]
    hola3_list=[]
    i=0
    for i in csvreader:
     ballots=i[0] #column 0 as ballot
     county=i[1] #column 1 as county
     candidate=i[2] #column 2 as candidate
    #print(ballots,county,candidate) 

     ballot_list.append(ballots) #Add to list
     counties_list.append(county) #AAdd to list
     candidates_list.append(candidate) #Add to list 

    count_votes=len(ballot_list)
    #print(count_votes)

    #count_votes=map(int,ballots)
    #print(sum(count_votes))

    ucandidates_list=[] #list of candidates
    ucandidates_list_count=[] #count of votes

    for x in candidates_list:# checks for unique in candidate list
        if x not in ucandidates_list: 
            ucandidates_list.append(x)

    #print(ucandidates_list)    
    #can=len(ucandidates_list) #how many candidates 
    can=0
    #alternative_count_cand=0
    for w in ucandidates_list:#Loop so I dont use the len fuction
        can=can+1
    #print(can)
    for y in range(can):
        
        temp_count=candidates_list.count(ucandidates_list[y])#loop to count how many votes per candidate        
        ucandidates_list_count.append(temp_count)

    for z in range(can):
        temp_perce=ucandidates_list_count[z]/ count_votes#loop to get and asigned the percentage of votes per candidate
        percentage_list.append(temp_perce)
    #print(ucandidates_list_count)  
   # print(percentage_list)  

    max_temp=max(ucandidates_list_count) #gets by candidate the max votes
    max_temp_index=ucandidates_list_count.index(max_temp)#from the max gets the index
    winner= ucandidates_list[max_temp_index]#checks the candidates list and picks the winner given the index of max

   # print(max_temp, max_temp_index,winner)

    print("ELECTION RESULTS")
    print("----------------------------------------")
    print("Total votes:  "+ str(count_votes))
    print("----------------------------------------")
    for xy in range(can):
        hola2=(f"{ucandidates_list[xy]}  {round((percentage_list[xy])*100,2)}% ({ucandidates_list_count[xy]}) ")#gets all the information pertaining a specific candidate
        hola3_list.append(hola2 +'\n') #creates a new list with the compilation of the candidate information
        print(f"{ucandidates_list[xy]}  {round((percentage_list[xy])*100,2)}% ({ucandidates_list_count[xy]}) ")#prints candidate information compiled
    print("========================================") 
    print(f'The winner is: {winner}')


txtfile=f'\
ELECTION RESULTS\n\
----------------------------------------\n\
Total votes:  {str(count_votes)}\n\
----------------------------------------\n\
'
txtfile2=f'\
----------------------------------------\n\
Winner:  {str(winner)}\n\
----------------------------------------\n\
 '

#print(analysis,hola3_list)


file1=open("pypoll_IG.txt","w") #Open or if file 
file1.writelines(txtfile) #Write easy part of the text
file1.writelines(hola3_list) #Write the new list with the print information
file1.writelines(txtfile2) #Write last section
file1.close() #Close 