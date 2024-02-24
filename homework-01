import typing as tp
import pathlib
import threading
import time

T = tp.TypeVar("T")

def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    return [values[i:i+n] for i in range(0, len(values), n)]

def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)

def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    return group(digits, 9)

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row, _ = pos
    return grid[row]

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    _, col = pos
    return [grid[i][col] for i in range(len(grid))]

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row, col = pos
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    return [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]

def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    empty_pos = find_empty_positions(grid)
    if not empty_pos:
        return grid
    row, col = empty_pos
    possible_values = find_possible_values(grid, (row, col))
    for value in possible_values:
        grid[row][col] = value
        if solve(grid):
            return grid
        grid[row][col] = '.'
    return None

def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for i in range(9):
        for j in range(9):
            if grid[i][j] == '.':
                return (i, j)
    return None

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    row_values = get_row(grid, pos)
    col_values = get_col(grid, pos)
    block_values = get_block(grid, pos)
    existing_values = set(row_values + col_values + block_values)
    possible_values = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - existing_values
    return possible_values

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    def is_valid(arr: tp.List[str]) -> bool:
        arr = [x for x in arr if x != '.']
        return len(arr) == len(set(arr))
    
    for i in range(9):
        if not is_valid(get_row(solution, (i, 0))) or not is_valid(get_col(solution, (0, i))) or not is_valid(get_block(solution, (i // 3 * 3, (i % 3) * 3))):
            return False
    return True

def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    grid = [['.' for _ in range(9)] for _ in range(9)]
    # Generate Sudoku with N filled elements
    return grid

def solve_with_threading(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f"{filename}: {end-start}")

if __name__ == "__main__":
    puzzle_files = [r"C:\Users\Artem\PycharmProjects\pythonProject1\puzzle1.txt",
                    r"C:\Users\Artem\PycharmProjects\pythonProject1\puzzle2.txt",
                    r"C:\Users\Artem\PycharmProjects\pythonProject1\puzzle3.txt"]
    
    threads = []
    for filename in puzzle_files:
        t = threading.Thread(target=solve_with_threading, args=(filename,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
