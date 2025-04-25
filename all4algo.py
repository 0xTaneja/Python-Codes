from collections import deque
def fcfs_non(processes):
    print(f"First Come First Serve Non Preemptive")

    processes.sort(key=lambda x:x[1])
    time = 0
    total_tat = 0
    total_wt = 0 
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        pid,bt,at = p
        if time<at:
            time = at
        ct = time + bt
        tat = ct - at
        wt = tat - bt

        total_tat+=tat
        total_wt+=wt
        time = ct

        print(f"\t{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        n= len(processes)
        print(f"\nAverage Waiting Time: {total_wt/n:.2f}")
        print(f"Average Turnaround Time: {total_tat/n:.2f}")


def sjf_non(processes):
    print(f"Shortest Job First Algorithm")
    
    processes.sort(key=lambda x : x[1])
    time = 0
    total_tat = 0
    total_wt = 0
    completed = []

    print("PID\tAT\tBT\tCT\tTAT\tWT")
    while len(completed) < len(processes):
        ready = [p for p in processes if p not in completed and p[1]<=time]
        if ready:
            shortest = min (ready,key=lambda x : x[2])
            pid,at,bt = shortest
            ct = time + bt
            tat = ct - at
            wt = tat - bt

            total_tat+=tat
            total_wt+=wt
            time = ct
            completed.append(shortest)

            print(f"\t{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        else :
            time +=1
    n=len(processes)
    print(f"Average Turnaround Time:{total_tat/n:.2f}")
    print(f"Average Waiting Time:{total_wt/n:.2f}")

def round_robin_preempt(processes,time_quantum):
    print(f"Round Robin Algorithm")
    time = 0

    remaining_time = {}
    queue=deque()
    arrived = set()
    completed = {}
    for pid,at,bt in processes:
        remaining_time[pid]=bt
    
    processes.sort(key=lambda x:x[1])
    queue.append(processes[0][0])
    arrived.append(processes[0][0])

    while queue:
        pid = queue.popleft()
        at = next(p[1] for p in processes if p[0] == pid)
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
            completed[pid]=time
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

def Priority_non(processes):
    print(f"Priority Scheduling Non Preemptive")
    processes.sort(key=lambda x:x[1])
    time = 0
    total_tat=0
    total_wt=0
    completed = []
    print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")
    while len(completed)<len(processes):
        ready = [p for p in processes if p not in completed and p[1]<=time]
        if ready:
            next_process = min (ready,key=lambda x : x[3])
            pid,at,bt,pr = next_process
            ct = time + bt
            tat = ct - at
            wt = tat - bt

            total_tat+=tat
            total_wt+=wt
            time = ct
            completed.append(next_process)

            print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        else:
            time+=1
    n=len(processes)
    print(f"Average Turn Around Time : {total_tat/n:.2f}")
    print(f"Average Waiting Time : {total_wt/n:.2f}")


