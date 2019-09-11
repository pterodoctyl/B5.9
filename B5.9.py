import time

def time_this(NUM_RUNS=10):
    def dec(func_to_run):
        def func(*args, **kwargs):
            avg_time = 0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                func_to_run(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= NUM_RUNS
            fn = func_to_run.__name__
            print("Выполнение заняло %.5f секунд" % avg_time)
        return func
    return dec

    # Тест выполнения
@time_this(NUM_RUNS=10)    
def f():
    for j in range(10000000):
        pass    
f()

class TAIMER:
	def __init__(self, NUM_RUNS=10):
	 	self.NUM_RUNS = NUM_RUNS
	def __call__(self, func):
		def wrap(*args):
			avg_time = 0
			for _ in range(self.NUM_RUNS):
				t0 = time.time()
				func()
				t1 = time.time()
			avg_time += (t1 - t0)
			avg_time /= self.NUM_RUNS
			print("Выполнение заняло %.5f секунд" % avg_time)
		return wrap

T = TAIMER(10)

@T
def fTAIMER():
    for j in range(10000000):
        pass    

fTAIMER()