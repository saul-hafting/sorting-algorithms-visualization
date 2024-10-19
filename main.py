import pygame
import random
import sys
from button import Button

# pygame setup
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
comparisons = 0

size = 3 # 1 - 300 smaller = larger sorting size
delayTime = 0

rectangleWidth = size
font = pygame.font.Font(None, 74)


random_numbers = [i for i in range(1, 601) if i % size == 0]

random.shuffle(random_numbers)

MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")
MENU_MOUSE_POS = pygame.mouse.get_pos()





def partition(arr, low, high):
    global comparisons

    # choose the rightmost element as pivot
    pivot = arr[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            draw_array_sorting(arr, i, j)
            pygame.display.set_caption("Quick Sort | Comparisons: " + str(comparisons))
            (arr[i], arr[j]) = (arr[j], arr[i])

    # Swap the pivot element with the greater element specified by i
    draw_array_sorting(arr, i+1, high)
    pygame.time.delay(delayTime)
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    # Return the position from where partition is done
    return i + 1

def quick_sort(arr, low, high):
    global comparisons
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)
        
        
        # Recursive call on the left of pivot
        quick_sort(arr, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(arr, pi + 1, high)
        
def bubble_sort(arr):
    global comparisons
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            comparisons += 1
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                draw_array_sorting(arr, i, i+1)
                pygame.display.set_caption("Bubble Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
def selecton_sort(arr):
    global comparisons
    size = len(arr)
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            comparisons += 1
            pygame.time.delay(delayTime)
            draw_array_sorting(arr, ind, min_index)
            pygame.display.set_caption("Selection Sort | Comparisons: " + str(comparisons))
            # select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                
                min_index = j
         # swapping the elements to sort the array
        
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])

def insertion_sort(arr):
    global comparisons
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            comparisons += 1
            draw_array_sorting(arr, j, j+1)
            pygame.display.set_caption("Insertion Sort | Comparisons: " + str(comparisons))
            pygame.time.delay(delayTime)
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
       
def merge(arr, left, mid, right):
    global comparisons
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        comparisons += 1
        draw_array_sorting(arr, k, k)
        pygame.display.set_caption("Merge Sort | Comparisons: " + str(comparisons))
        pygame.time.delay(delayTime)
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        comparisons += 1
        draw_array_sorting(arr, -1, -1)
        pygame.display.set_caption("Merge Sort | Comparisons: " + str(comparisons))
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        comparisons += 1
        draw_array_sorting(arr, -1, -1)
        pygame.display.set_caption("Merge Sort | Comparisons: " + str(comparisons))
        arr[k] = R[j]
        j += 1
        k += 1
      
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
     
def heapify(arr, n, i):
    global comparisons
    
    
     # Initialize largest as root
    largest = i 
    
    #  left index = 2*i + 1
    l = 2 * i + 1 
    
    # right index = 2*i + 2
    r = 2 * i + 2  

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        comparisons += 1
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        comparisons += 1
        largest = r

    # If largest is not root
    if largest != i:
        draw_array_sorting(arr, i, largest)
        pygame.display.set_caption("Heap Sort | Comparisons: " + str(comparisons))
        pygame.time.delay(delayTime)
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    global comparisons
    
    n = len(arr) 

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
      
        # Move root to end
        arr[0], arr[i] = arr[i], arr[0] 

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

     
def draw_array(arr, button, mouse_pos):
    screen.fill("black")
    button.changeColor(mouse_pos)
    button.update(screen)
    k = 0
    for i in arr:
        k += rectangleWidth
        colour = "green"
        if size > 1:
            pygame.draw.rect(screen, colour, (k, height-i, rectangleWidth-1, i))
        else:
            pygame.draw.rect(screen, colour, (k, height-i, rectangleWidth, i))
    pygame.display.flip()

def draw_array_sorting(arr, h1, h2):
    screen.fill("black")
    k = 0
    for i in arr:
        k += rectangleWidth
        colour = "green"
        if h1 != -1 and h2 != -1:
            if i == arr[h1] or i == arr[h2]:
                colour = "red"
        if size > 1:
            pygame.draw.rect(screen, colour, (k, height-i, rectangleWidth-1, i))
        else:
            pygame.draw.rect(screen, colour, (k, height-i, rectangleWidth, i))
    pygame.display.flip()


def quick_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Quick Sort | Comparisons: " + str(comparisons))
    
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        # fill the screen with a color to wipe away anything from last frame
        

        # RENDER YOUR GAME HERE
        
        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            quick_sort(random_numbers, 0, len(random_numbers)-1)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)

        
        
        clock.tick(60)  # limits FPS to 60

def bubble_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Bubble Sort | Comparisons: " + str(comparisons))
    
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()
        
        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            bubble_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)

        
        
        clock.tick(60)  # limits FPS to 60

def selection_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Selection Sort | Comparisons: " + str(comparisons))
    
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()
        
        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            selecton_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)

        
        
        clock.tick(60)  # limits FPS to 60

def insertion_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Insertion Sort | Comparisons: " + str(comparisons))
    
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        # fill the screen with a color to wipe away anything from last frame
        

        # RENDER YOUR GAME HERE
        
        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            insertion_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)

        
        
        clock.tick(60)  # limits FPS to 60
        
def merge_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Merge Sort | Comparisons: " + str(comparisons))
    
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        
        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            merge_sort(random_numbers, 0, len(random_numbers) - 1)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)

        
        
        clock.tick(60)  # limits FPS to 60

def heap_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Heap Sort | Comparisons: " + str(comparisons))
    
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()
        
        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            heap_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)

        
        
        clock.tick(60)  # limits FPS to 60

def shell_sort(arr):
    global comparisons
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                draw_array_sorting(arr, j, j - gap)
                pygame.display.set_caption("Shell Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def shell_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Shell Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            shell_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def cocktail_shaker_sort(arr):
    global comparisons
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Move from left to right
        for i in range(start, end):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                draw_array_sorting(arr, i, i + 1)
                pygame.display.set_caption("Cocktail Shaker Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # Move from right to left
        for i in range(end - 1, start - 1, -1):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                draw_array_sorting(arr, i, i + 1)
                pygame.display.set_caption("Cocktail Shaker Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

def cocktail_shaker_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Cocktail Shaker Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            cocktail_shaker_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def comb_sort(arr):
    global comparisons
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            comparisons += 1
            if arr[i] > arr[i + gap]:
                draw_array_sorting(arr, i, i + gap)
                pygame.display.set_caption("Comb Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

def comb_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Comb Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            comb_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def gnome_sort(arr):
    global comparisons
    index = 0
    n = len(arr)
    while index < n:
        if index == 0:
            index += 1
        comparisons += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            draw_array_sorting(arr, index, index - 1)
            pygame.display.set_caption("Gnome Sort | Comparisons: " + str(comparisons))
            pygame.time.delay(delayTime)
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

def gnome_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Gnome Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            gnome_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def cycle_sort(arr):
    global comparisons
    n = len(arr)
    for cycle_start in range(0, n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            comparisons += 1
            if arr[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        draw_array_sorting(arr, cycle_start, pos)
        pygame.display.set_caption("Cycle Sort | Comparisons: " + str(comparisons))
        pygame.time.delay(delayTime)
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                comparisons += 1
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            draw_array_sorting(arr, cycle_start, pos)
            pygame.display.set_caption("Cycle Sort | Comparisons: " + str(comparisons))
            pygame.time.delay(delayTime)

def cycle_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Cycle Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            cycle_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def odd_even_sort(arr):
    global comparisons
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, n-1, 2):
            comparisons += 1
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
                draw_array_sorting(arr, i, i+1)
                pygame.display.set_caption("Odd-Even Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)
        for i in range(0, n-1, 2):
            comparisons += 1
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
                draw_array_sorting(arr, i, i+1)
                pygame.display.set_caption("Odd-Even Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)

def odd_even_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Odd-Even Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            odd_even_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def flip(arr, i):
    global comparisons
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        pygame.display.set_caption("Pancake Sort | Comparisons: " + str(comparisons))
        pygame.time.delay(delayTime)
        start += 1
        i -= 1

def find_max(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def pancake_sort(arr):
    global comparisons
    n = len(arr)
    curr_size = n
    while curr_size > 1:
        mi = find_max(arr, curr_size)
        if mi != curr_size - 1:
            if mi != 0:
                flip(arr, mi)
                draw_array_sorting(arr, 0, mi)
                pygame.display.set_caption("Pancake Sort | Comparisons: " + str(comparisons))
                pygame.time.delay(delayTime)
            flip(arr, curr_size - 1)
            draw_array_sorting(arr, 0, curr_size - 1)
            pygame.display.set_caption("Pancake Sort | Comparisons: " + str(comparisons))
            pygame.time.delay(delayTime)
        curr_size -= 1
        comparisons += curr_size  # Count comparisons in find_max

def pancake_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Pancake Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            pancake_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def stooge_sort(arr, l, h):
    global comparisons
    if l >= h:
        return

    comparisons += 1
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
        draw_array_sorting(arr, l, h)
        pygame.display.set_caption("Stooge Sort | Comparisons: " + str(comparisons))
        pygame.time.delay(delayTime)

    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge_sort(arr, l, h - t)
        stooge_sort(arr, l + t, h)
        stooge_sort(arr, l, h - t)

def stooge_sort_game():
    global comparisons
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Stooge Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            stooge_sort(random_numbers, 0, len(random_numbers) - 1)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def merge(a, b):
    global comparisons
    c = []
    while len(a) > 0 and len(b) > 0:
        comparisons += 1
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if len(a) > 0:
        c.extend(a)
    else:
        c.extend(b)
    return c

def strand_sort(arr):
    global comparisons
    result = []
    while len(arr) > 0:
        sublist = [arr.pop(0)]
        i = 0
        while i < len(arr):
            comparisons += 1
            if arr[i] > sublist[-1]:
                sublist.append(arr.pop(i))
            else:
                i += 1
            draw_array_sorting(arr + result + sublist, len(arr), len(arr) + len(result) + len(sublist) - 1)
            pygame.display.set_caption("Strand Sort | Comparisons: " + str(comparisons))
            pygame.time.delay(delayTime)
        result = merge(result, sublist)
        draw_array_sorting(arr + result, len(arr), len(arr) + len(result) - 1)
        pygame.display.set_caption("Strand Sort | Comparisons: " + str(comparisons))
        pygame.time.delay(delayTime)
    return result

def strand_sort_game():
    global comparisons, random_numbers
    random.shuffle(random_numbers)
    sorting = True
    pygame.display.set_caption("Strand Sort | Comparisons: " + str(comparisons))
    
    screen.fill("black")
    
    MENU_BUTTON = Button(image=None, pos=(100, 50), 
                            text_input="MENU", font=font, base_color="blue", hovering_color="white")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

        draw_array(random_numbers, MENU_BUTTON, MENU_MOUSE_POS)
        if sorting:
            random_numbers = strand_sort(random_numbers)
            sorting = False
            for i in range(len(random_numbers)):
                draw_array_sorting(random_numbers, i, i)
        
        clock.tick(60)  # limits FPS to 60

def main_menu():
    global comparisons, size
    comparisons = 0
    while True:
        screen.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font.render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 50))

        SIZE_TEXT = font.render(f"Size: {(600//size)}", True, "white")
        SIZE_RECT = SIZE_TEXT.get_rect(center=(300, 550))

        QUICK_SORT_BUTTON = Button(image=None, pos=(85, 150), 
                            text_input="QUICK", font=font, base_color="green", hovering_color="White")
        
        BUBBLE_SORT_BUTTON = Button(image=None, pos=(110, 200), 
                            text_input="BUBBLE", font=font, base_color="green", hovering_color="White")
        
        SELECTION_SORT_BUTTON = Button(image=None, pos=(155, 250), 
                            text_input="SELECTION", font=font, base_color="green", hovering_color="White")
        
        INSERTION_SORT_BUTTON = Button(image=None, pos=(150, 300), 
                            text_input="INSERTION", font=font, base_color="green", hovering_color="White")
        
        MERGE_SORT_BUTTON = Button(image=None, pos=(98, 350), 
                            text_input="MERGE", font=font, base_color="green", hovering_color="White")
        
        HEAP_SORT_BUTTON = Button(image=None, pos=(79, 400), 
                            text_input="HEAP", font=font, base_color="green", hovering_color="White")
        
        SHELL_SORT_BUTTON = Button(image=None, pos=(90, 450), 
                            text_input="SHELL", font=font, base_color="green", hovering_color="White")

        COCKTAIL_SORT_BUTTON = Button(image=None, pos=(135, 500), 
                            text_input="COCKTAIL", font=font, base_color="green", hovering_color="White")

        COMB_SORT_BUTTON = Button(image=None, pos=(85, 550), 
                            text_input="COMB", font=font, base_color="green", hovering_color="White")

        GNOME_SORT_BUTTON = Button(image=None, pos=(500, 150), 
                            text_input="GNOME", font=font, base_color="green", hovering_color="White")

        CYCLE_SORT_BUTTON = Button(image=None, pos=(512, 200), 
                            text_input="CYCLE", font=font, base_color="green", hovering_color="White")

        ODD_EVEN_SORT_BUTTON = Button(image=None, pos=(464, 250), 
                            text_input="ODD-EVEN", font=font, base_color="green", hovering_color="White")

        INCREASE_SIZE_BUTTON = Button(image=None, pos=(170, 550), 
                            text_input="-", font=font, base_color="blue", hovering_color="White")

        DECREASE_SIZE_BUTTON = Button(image=None, pos=(430, 550), 
                            text_input="+", font=font, base_color="blue", hovering_color="White")

        PANCAKE_SORT_BUTTON = Button(image=None, pos=(470, 300), 
                            text_input="PANCAKE", font=font, base_color="green", hovering_color="White")

        STOOGE_SORT_BUTTON = Button(image=None, pos=(490, 350), 
                            text_input="STOOGE", font=font, base_color="green", hovering_color="White")

        STRAND_SORT_BUTTON = Button(image=None, pos=(490, 400), 
                            text_input="STRAND", font=font, base_color="green", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(SIZE_TEXT, SIZE_RECT)

        for button in [QUICK_SORT_BUTTON, BUBBLE_SORT_BUTTON, SELECTION_SORT_BUTTON, 
                       INSERTION_SORT_BUTTON, MERGE_SORT_BUTTON, HEAP_SORT_BUTTON, 
                       SHELL_SORT_BUTTON, COCKTAIL_SORT_BUTTON, COMB_SORT_BUTTON,
                       GNOME_SORT_BUTTON, CYCLE_SORT_BUTTON, ODD_EVEN_SORT_BUTTON,
                       PANCAKE_SORT_BUTTON, STOOGE_SORT_BUTTON, STRAND_SORT_BUTTON,
                       INCREASE_SIZE_BUTTON, DECREASE_SIZE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUICK_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quick_sort_game()
                elif BUBBLE_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    bubble_sort_game()
                elif SELECTION_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    selection_sort_game()
                elif INSERTION_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    insertion_sort_game()
                elif MERGE_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    merge_sort_game() 
                elif HEAP_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    heap_sort_game()
                elif SHELL_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    shell_sort_game()
                elif COCKTAIL_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    cocktail_shaker_sort_game()
                elif COMB_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    comb_sort_game()
                elif GNOME_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    gnome_sort_game()
                elif CYCLE_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    cycle_sort_game()
                elif ODD_EVEN_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    odd_even_sort_game()
                elif PANCAKE_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pancake_sort_game()
                elif STOOGE_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    stooge_sort_game()
                elif STRAND_SORT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    strand_sort_game()
                elif INCREASE_SIZE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    size = min(300, size + 1)
                    update_random_numbers()
                elif DECREASE_SIZE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    size = max(1, size - 1)
                    update_random_numbers()

        pygame.display.update()

def update_random_numbers():
    global random_numbers, rectangleWidth
    random_numbers = [i for i in range(1, 601) if i % size == 0]
    random.shuffle(random_numbers)
    rectangleWidth = size

main_menu()


