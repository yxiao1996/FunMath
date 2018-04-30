fib_sum = 0
left = 0
right = 1
new = left + right
while(new <= 4000000):
    if new % 2 == 0:
        fib_sum += new
    left = right
    right = new
    new = left + right
print fib_sum