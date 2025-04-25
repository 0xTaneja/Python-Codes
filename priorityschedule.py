def priority_scheduling_non(processes):
    print(f"\n Priority Scheduling Non Preemptive")

    processes.sort(key=lambda x:x[1])

    time =0
    total_tat =0
    total_wt=0
    completed = []

    print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")
    while len(completed)<len(processes):
        ready = [p for p in processes if p not in completed and p[1]<=time]
        if ready:
            next_process = min(ready,key=lambda x:x[3])
            pid,at,bt,pr = next_process
            ct = time + bt
            tat = ct - at
            wt = tat-bt

            total_tat+=tat
            total_wt+=wt
            time=ct
            completed.append(next_process)

            print(f"{pid}\t{at}\t{bt}\t{pr}\t{ct}\t{tat}\t{wt}")
        else:
            time+=1
    n=len(processes)
    print(f"\n Average turn around time {total_tat/n:.2f}")
    print(f"\n Average Waiting Time {total_wt/n:.2f}")

process_list = [
    ["P1", 0, 5, 2],
    ["P2", 1, 3, 1],
    ["P3", 2, 8, 4],
    ["P4", 3, 6, 3]
]

priority_scheduling_non(process_list)