import time

def progress_bar(index, total, start):
    """
    进度条
    index: 当前进度
    total: 总进度
    start: 开始时间 start = time.perf_counter()
    """
    index += 1
    t = 100
    i = int(t * index / total)
    
    finsh = "▓" * i
    need_do = "-" * (t - i)
    progress = (i / t) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")