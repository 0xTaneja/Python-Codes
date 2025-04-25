from collections import deque
def round_robin_preempt(processes,time_quantum):
    print(f"Round Robin Algorithm")

    time = 0
    queue=deque()
    remaining_time ={}
    completion = {}
    arrived = set()

    for pid,at,bt in processes:
        remaining_time[pid]=bt

    processes.sort(key=lambda x:x[1])
    queue.append(processes[0][0])
    arrived.add(processes[0][0])

    while queue:
        pid = queue.popleft()

        at=next(p[1] for p in processes if p[0]==pid)
        if time < at:
            time = at
        run_time = min(time_quantum,remaining_time[pid])
        time+=run_time
        remaining_time[pid]-=run_time

        for p in processes:
            if p[0] not in arrived and p[1]<=time:
                queue.append(p[0])
                arrived.add(p[0])
        if remaining_time[pid]>0:
            queue.append(pid)
        else:
            completion[pid]=time
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    total_tat = 0
    total_wt = 0
    

    for pid,at,bt in processes:
        ct=completion[pid]
        tat = ct - at
        wt = tat- bt
        total_tat+=tat
        total_wt+=wt
        print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
    
    n = len(processes)
    print(f"\nAverage Turnaround Time = {total_tat/n:.2f}")
    print(f"Average Waiting Time = {total_wt/n:.2f}")

processes = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 1],
    ["P4", 3, 2]
]
round_robin_preempt(processes,time_quantum=2)

