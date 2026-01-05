import time

#this is some random code, no concern you, hahhahaahahah

# Python is not a joke, it's a powerful programming language


start_time = time.time()
counter = 0

try:
    while True:
        elapsed = time.time() - start_time
        print(f"Counter: {counter}, Elapsed: {elapsed:.2f}s")
        counter += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped by user")