import sys
import time
import os


def ft_tqdm(iterable):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(iterable)
    start_time = time.time()

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    for index, item in enumerate(iterable):
        yield item
        percent_complete = (index + 1) / total
        elapsed_time = time.time() - start_time
        eta = (elapsed_time / (index + 1)) * (total - index - 1)

        # Formatting elapsed time and ETA
        elapsed_formatted = (
            f'{int(elapsed_time // 60):02}:{int(elapsed_time % 60):02}'
        )
        eta_formatted = f'{int(eta // 60):02}:{int(eta % 60):02}'
        rate = (index + 1) / elapsed_time if elapsed_time > 0 else 0

        # Prefix
        prefix = f'{percent_complete * 100:3.0f}%|'

        # Postfix
        ratio = f'{index + 1}/{total}'
        timer = f'{elapsed_formatted}<{eta_formatted}'
        ips = f'{rate:.2f}it/s'
        postfix = f'| {ratio} [{timer}, {ips}]'

        # Calculate available space for the bar
        available_space = terminal_width - len(prefix) - len(postfix)
        filled_length = int(available_space * percent_complete)
        bar = '█' * filled_length + ' ' * (available_space - filled_length)

        sys.stdout.write(f'\r{prefix}{bar}{postfix}')
        sys.stdout.flush()

    print()


def main():
    pass


if __name__ == "__main__":
    main()
