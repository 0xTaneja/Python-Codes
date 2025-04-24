memoryBlocks = {
    "M1":100,
    "M2":500,
    "M3":200,
    "M4":300,
    "M5":600
}

process = {} 
current = 0

def display_blocks():
    print(f"Current Block Status:")
    for block,size in memoryBlocks.items():
        print(f"{block}:{size} KB")
blockList = list(memoryBlocks)


while True:
    print("Choose Allocation Method :")
    print("1.Next Fit")
    print("2.Worst Fit")
    choice = input("Enter your choice (1/2):")

    pname = input("Enter Process Name")

    try:
        req = int(input("Enter Required Memory"))
    except ValueError:
        print("Errorenous Input")
        continue
    
    allocated = False

    if choice == "1":
        n = len(blockList)
        checked = 0
        while checked < n:
            i = current % n 
            block = blockList[i]
            if memoryBlocks[block] >= req:
                memoryBlocks[block] -= req
                process[pname]=block
                print(f"✅ Process {pname} allocated to Memory Block {block} [Next Fit]")
                current = (i+1)%n
                allocated = True
                break
            current = (current + 1) % n
            checked += 1
        if not allocated :
            print(f"No Suitable Memory Block Found")
    elif choice == "2":
        worstBlock = None
        max_space = float('-inf')
        for block in memoryBlocks:
            space_left = memoryBlocks[block] - req
            if space_left >=0 and space_left > max_space:
                worstBlock = block
                max_space = space_left
        if worstBlock :
            memoryBlocks[worstBlock] -= req
            process[pname] = worstBlock
            print(f"✅ Process {pname} allocated to Memory Block {worstBlock} [Worst Fit]")
        else :
            print(f"No SUitable Block FOund")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        continue
    
    display_blocks()

    cont = input ("Do You wish to allocate another block [Y/N]");
    if cont !='Y':
        break

print("\n📋 Final Process Allocations:")
for p, b in process.items():
    print(f"Process {p} → Block {b}")



