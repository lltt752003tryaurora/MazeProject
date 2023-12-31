import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import sys

sys.path.append("./Algorithms")
from dfs import dfs
from bfs import bfs
from ucs import ucs


def find_path(algorithm, filename):
    with open(filename, "r") as f:
        maze = f.readlines()[1:]  # Bỏ qua dòng đầu tiên
        maze = [line.strip() for line in maze]

    start_position = None
    end_position = None

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "S":
                start_position = (x, y)
            elif maze[y][x] == "E":
                end_position = (x, y)

    if not start_position or not end_position:
        return None

    path = algorithm(maze, start_position, end_position)
    return path


def draw_path_on_maze(maze, path):
    rows = len(maze)
    cols = len(maze[0])

    # Tạo bản đồ màu tùy chỉnh
    cmap = mcolors.ListedColormap(
        ["black", "white", "red", "yellow", "purple", "cyan", "lightblue"]
    )

    # Tạo hình vẽ và điều chỉnh kích thước
    fig, ax = plt.subplots(figsize=(cols, rows))

    # Tạo một ma trận màu xanh biển cho các ô trống
    colored_maze = [[6 if cell != "x" else 0 for cell in row] for row in maze]

    # Vẽ bản đồ mê cung
    ax.imshow(colored_maze, cmap=cmap, origin="upper")

    # Vẽ đường đi nếu có
    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_x, path_y, color="red", linewidth=2)

    # Tìm vị trí của điểm bắt đầu (S) và điểm kết thúc (E)
    start = None
    end = None
    for y in range(rows):
        for x in range(cols):
            if maze[y][x] == "S":
                start = (x, y)
            elif maze[y][x] == "E":
                end = (x, y)

    # Tô màu điểm đầu (màu vàng) và điểm cuối (màu tím)
    if start:
        start_x, start_y = start
        ax.plot(start_x, start_y, marker="o", markersize=10, color="yellow")
    if end:
        end_x, end_y = end
        ax.plot(end_x, end_y, marker="o", markersize=10, color="purple")

    # ax.set_title("DFS")

    # Loại bỏ trục và hiển thị
    ax.axis("off")
    plt.show()


# Sử dụng hàm find_path:
idInput = 1
filename = f"./MapTest/MapNotPrize/input{idInput}.txt"  # Đổi tên file tương ứng với file bản đồ của bạn


path = find_path(ucs, filename)

with open(f"./MapTest/MapNotPrize/input{idInput}.txt", "r") as file:
    # Đọc toàn bộ nội dung file và loại bỏ dòng đầu tiên
    lines = file.readlines()[1:]

# Lưu dữ liệu còn lại vào biến mảng maze
maze = [line.strip() for line in lines]

# In ra để kiểm tra
for line in maze:
    print(line)

maze_colors = []
for row in maze:
    maze_colors.append([0 if cell == "x" else 1 for cell in row])

draw_path_on_maze(maze, path)
