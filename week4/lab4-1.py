def outer():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print(f"Inner count: {count}")
    increment() # Inner count: 1
    increment() # Inner count: 2
    print(f"Outer count: {count}") # Outer count: 2
outer()
