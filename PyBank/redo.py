import csv #Import csv module

with open ('budget_data.csv') as csvfile: #Start csv file handling

    csvreader=csv.reader(csvfile, delimiter=',') #Specify delimiter and variable 
    header=next(csvreader) #Read the header row first

    months_list=[]  #creation of variables ans list 
    winloss_list=[]
    winloss_list2=[]
    Change_list=[]
    total_months=0
    total_amount=0
    priorRev=0
    i=0
    max_win=0
    min_win=0

    for i in csvreader:    #loop to read the csv file
        total_months = total_months +1
        total_amount = total_amount+int(i[1])  #capturing total amount
        
        rev_change = int(i[1])-priorRev
        priorRev=int(i[1])
        winloss_list=winloss_list+[rev_change]#capturing in a list the  net loss and win
        months_list=months_list+[i[0]]
    #winloss_list.pop(0)
    winloss_list2= winloss_list[1:]
    #months_list.pop(0)
    #print(winloss_list2,months_list)

    for x in range(total_months-2): #loop to find max win and min loss
       if(winloss_list2[x+1] >max_win):
           max_win=winloss_list2[x+1]
           #print(max_win) 
       if(winloss_list2[x+1] <min_win):
           min_win=winloss_list2[x+1]
    #print(max_win,min_win)   
     #for max_win in winloss_list:
    max_month=winloss_list.index(int(max_win))  #looking at index for max win so we can get the corresponding month
    max_change=months_list[max_month]  
   # print(max_month,months_list[max_month])        

    #for min_win in winloss_list2:
    min_month=winloss_list.index(min_win) #looking at index for min win so we can get the corresponding month
    min_change=months_list[min_month]  
  #  print(min_month,months_list[min_month])
   # print(total_amount,total_months) 

    average=sum(winloss_list2)/(total_months-1)#getting the average
    sum_total2=sum(winloss_list)
    #print(average)

    forthe_txt_file=f'\
    Financial analysis\n\
    ---------------------------------- \n\
    Total months: {str(total_months)}\n\
    Total Amount: $ {str(total_amount)} \n\
    Average Change: $ {str(int(average))}\n\
    Greatest incrrease in profits {str(max_change)} $ {str(int(max_win))}\n\
    reatest Decrease in profits {str(min_change)} $ {str(int(min_win))}\n'

    print(forthe_txt_file)

    file1=open("pybank IG.txt","w") #Open or if file does not exist then create file 
    file1.writelines(forthe_txt_file) 
    file1.close() #Close pybank.txt write mode