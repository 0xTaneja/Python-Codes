memoryBlocks = {
    "M1":100,
    "M2":500,
    "M3":200,
    "M4":300,
    "M5":600
}

process = {}

def display_blocks():
    print("\n Current Block Status")
    for block,size in memoryBlocks.items():
        print(f"{block}:{size} KB")

while True:
    print("\n Choose Allocation Method")
    print("\n 1.First Fit")
    print("\n 2.Best Fit")
    choice = input("Enter your choice (1,2) : ")
    
    pname = input("Enter process name : ")
    try:
        req=int(input("Enter memory required"));
    except ValueError:
        print("Invalid memory input. Try again.")
        continue
    allocated = False
    if choice == "1":
        for block in memoryBlocks:
            if memoryBlocks[block]>=req:
                memoryBlocks[block]-=req
                process[pname]=block
                print(f"✅ Process {pname} allocated to Memory Block {block} [First Fit]")
                allocated = True
                break
        if not allocated:
            print(f"No suitable Memory Block Found")
    elif choice == "2":
        best_block = None
        min_space = float('inf')
        for block in memoryBlocks:
            space_left = memoryBlocks[block] - req;
            if space_left>=0 and space_left<min_space:
                best_block = block
                min_space = space_left
        if best_block:
            memoryBlocks[best_block]-=req
            process[pname]=best_block
            print(f"Process {pname} allocated to Memory Block {best_block} [Best Fit]")
            allocated = True

        else:
            print("❌ No suitable memory block found.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        continue
    
    display_blocks()
    cont = input("\nDo you want to allocate another process? (y/n): ").lower()
    if cont != 'y':
        break

print(f"Final Allocation Summart")
for p,b in process.items():
    print(f"Process {p} -> Block {b}");

