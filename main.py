import time
if __name__=='__main__':
    start = time.perf_counter()
    import finite_difference
    finite_difference.first_order_spec()
    finish = time.perf_counter()
    print(f"time taken {finish-start}")


