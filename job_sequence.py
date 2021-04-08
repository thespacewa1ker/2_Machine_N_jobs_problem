# Here i'm solving using johnson's Algorithm
#User Input : the total number of jobs
jobs = int(input("Enter the Number of Jobs :"))

# Here i'm solving for 2 machines and n jobs
# taking user input of Machine -1 and Machine-2
machine_1 = []
machine_2 = []
# Creating the empty list to store the shortest job of machine-1 and machine-2 
time_1 = []
time_2 = []

for i in range(jobs):
    x = int(input("FOR Machine_1---Enter the job "+str(i+1)+" time duration :"))
    machine_1.append(x)
print("-------------------------------------")
for i in range(jobs):
    x = int(input("FOR Machine_2---Enter the job "+str(i+1)+" time duration :"))
    machine_2.append(x)

for i in range(jobs):
    #Finding the minimum time duration 
    m_1 = min(machine_1)
    m_2 = min(machine_2)

    # Checking which machine has least element 
    # If both machine contains the least element then obtain the maximum differnece and proceed
    if m_2 < m_1:
        m2_index =machine_2.index(m_2)
        time_2.append(m2_index+1)
        machine_1[m2_index] = 10000
        machine_2[m2_index] = 10000
       
    if m_1 == m_2:
        m1_index = machine_1.index(m_1)
        m2_index = machine_2.index(m_2)
        
        m1_max_diff = abs(machine_1[m1_index]-machine_2[m1_index])
        m2_max_diff = abs(machine_1[m2_index]-machine_2[m2_index])
        shortest = max(m1_max_diff,m2_max_diff)
        
        if shortest == m1_max_diff:
            time_1.append(m1_index+1)
            machine_1[m1_index] = 10000
            machine_2[m1_index] = 10000
        else:
            time_2.append(m2_index+1)
            machine_2[m2_index] = 10000
            machine_1[m2_index] = 10000
    
    if m_1 < m_2:
        m1_index = machine_1.index(m_1)
        time_1.append(m1_index+1)
        machine_1[m1_index] = 10000
        machine_2[m1_index] = 10000
    
    

# reversing the machine-2 job sequence and then appending with machine-1 job sequence 
time_2.reverse()
jobs_Sequence = time_1+time_2

for i in jobs_Sequence:
    print("Job-"+str(i) +">",end =" ")



        

        
    


