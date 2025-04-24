def sjf_non(processes):
    print("Shortest Job First Scheduling")
    processes.sort(key=lambda x:x[1])

    time=0
    total_tat=0
    total_wt=0
    completed=[]
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    while len(completed)<len(processes):
        ready =[p for p in processes if p not in completed and p[1]<=time]
        if ready:
            shortest = min(ready,key=lambda x:x[2])
            pid,at,bt = shortest
            ct = time + bt
            tat = ct - at
            wt = tat - bt

            total_tat +=tat
            total_wt +=wt
            time = ct
            completed.append(shortest)

            print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        else:
            time += 1

    n=len(processes)
    print(f"Average Turnaround Time:{total_tat/n:.2f}")
    print(f"Average Waiting Time:{total_wt/n:.2f}")

process_list = [
    ["P1", 0, 5],
    ["P2", 2, 3],
    ["P3", 1, 8],
    ["P4", 4, 6]
]

sjf_non(process_list.copy())    
