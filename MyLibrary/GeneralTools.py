import time

def progress_bar(index=1, total=100, start=0.0,information="") -> None:
    """进度条

    :param index: 当前进度
    :type index: int

    :param total: 总进度,循环的次数len(wheel)
    :type total: int

    :param start: 开始时间 start = time.perf_counter()
    :type start: float

    :return: None
    """
    index += 1
    t = 100
    i = int(t * index / total)
    
    finsh = "▓" * i
    need_do = "-" * (t - i)
    progress = (i / t) * 100
    dur = time.perf_counter() - start
    info = ""
    if information:
        info = " --提示："+ information
    print("\r{:^3.0f}%[{}->{}]{:.2f}s{}".format(progress, finsh, need_do, dur, info), end="")