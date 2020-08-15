import time


def loading_bar(iteration, total_iterable):
    '''
    progress bar in terminal, call in loop

    Progress: |██████████████████████████████████████████████████| 100.0% Complete

    #params:
        iteration      (required): current value of loop (int)
        total_iterable (required): total length of iterable values (int)
    '''
    prefix="Progress:"
    suffix="Complete"
    length=50
    
    occupied_space = int((length * iteration) // total_iterable)   # number of occupied blocks in bar
    empty_space = length - occupied_space                          # number of remaining space in bar
    percent = iteration / total_iterable * 100                     # percent of completion
    print(prefix + " |" + "█" * occupied_space + "-" * empty_space + "| " + str(round(percent,1)) + "% " + suffix, end="\r")



for i in range(1,71):
    loading_bar(i,70)
    time.sleep(0.1)
print()

