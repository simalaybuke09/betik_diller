from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t0= time.perf_counter() 
        result=func(*args,**kwargs)
        total_time=time.perf_counter()-t0
        print(f"total_time: {total_time:.4f} s") # Süre formatı hatalıydı
        return result
    return wrapper


def required_column(requireds: set[str]):
    def deco(func):
        @wraps(func)
        def wrapper(rows, *args,**kwargs):
            if not rows:
                return func(rows, *args, **kwargs) 
                
            # İlk satırdaki anahtarları alma
            keys = set(rows[0].keys()) # hata
            missing = requireds - keys
            if missing:
                raise ValueError(f"Eksik kolonlar: {missing}. Zorunlu: {requireds}")
            return func(rows,*args,**kwargs)
        return wrapper
    return deco