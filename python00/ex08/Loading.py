import sys
import time
import shutil

def ft_tqdm(lst: range) -> None:
    """
        Prints a dynamically updating progressbar everytime a value is requested
    """

    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        progress = i + 1
        percent = (progress / total) * 100

        elapsed_time = time.time() - start_time
        if progress > 0:
            rate = progress / elapsed_time
            eta = (total - progress) / rate if rate > 0 else 0
        else:
            rate = 0
            eta = 0
        
        bar_length = shutil.get_terminal_size().columns - 40
        filled = int((progress / total) * bar_length)
        bar = '█' * filled + '▌' * (1 if filled < bar_length and progress < total else 0)
        bar = bar.ljust(bar_length)

        sys.stdout.write(f'\r{percent:3.0f}%|{bar}| {progress}/{total} '
                        f'[{elapsed_time:02.0f}:{elapsed_time%60:02.0f}<{eta//60:02.0f}:{eta%60:02.0f}, '
                        f'{rate:.1f}it/s]')
        sys.stdout.flush()
        
        yield item
    
    print()