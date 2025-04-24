def fcfs_non(processes):
    print(f"Fcfc Scheduling")
    processes.sort(key=lambda x:x[1])
    time =0
    total_wt=0
    total_tat=0
    
    print(f"PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        pid,at,bt = p 
        if time < at:
            time = at
        ct=time+bt
        tat=ct-at
        wt=tat-bt

        total_wt+=wt
        total_tat+=tat
        time=ct

        print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

        n=len(processes);
        print(f"\nAverage Waiting Time: {total_wt/n:.2f}")
        print(f"Average Turnaround Time: {total_tat/n:.2f}")
        
process_list = [
    ("P1",0,5),
    ("P2",2,3),
    ("P3",1,8),
    ("P4",4,6),
]
fcfs_non(process_list.copy())