import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import platform

os_name = platform.system()

def make_window_active():
    app.focus_set()

def get_window_top_left_coords(window):

    app_x = window.winfo_x()
    app_y = window.winfo_y()
    top_left_x = app_x + 8
    return top_left_x, app_y

def make_transparent(window, alpha):
    window.attributes("-alpha", alpha)

def on_focus_in(event):
    make_transparent(app, 0.5)

def on_focus_out(event):
    make_transparent(app, 0.3)

def update_app_coordinates():
    x, y = app.winfo_x(), app.winfo_y()
    app_coordinates_label.config(text=f"Grid Position: {x}, {y}")
    app_coordinates_label.after(50, update_app_coordinates)

def click_grid():
    try:
        grid_rows = int(rows_entry.get())
        grid_cols = int(cols_entry.get())
        top_left_x, app_y = get_window_top_left_coords(app)
        width = app.winfo_width()
        height = app.winfo_height()
        grid_cell_width = width / grid_cols
        grid_cell_height = height / grid_rows
        top_left_y = app_y + 2

        app.iconify()

        intersections = []
        if os_name == "Windows":
            top_left_y = app_y + 30
        if os_name == "Darwin":
            top_left_y = app_y + 22
        for row in range(grid_rows + 1):
            for col in range(grid_cols + 1):
                x = top_left_x + col * grid_cell_width
                y = top_left_y + row * grid_cell_height
                intersections.append((x, y))

        pyautogui.moveTo(intersections[0])
        pyautogui.click()

        for intersection in intersections:
            pyautogui.click(intersection[0], intersection[1])

        messagebox.showinfo("Success", "Grid intersections clicked successfully.")
        app.deiconify()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter integer values for all parameters.")

def draw_grid():

    canvas.delete("all")

    try:
        grid_rows = int(rows_entry.get())
        grid_cols = int(cols_entry.get())
        width = app.winfo_width()
        height = app.winfo_height()
        grid_cell_width = width / grid_cols
        grid_cell_height = height / grid_rows

        for row in range(grid_rows + 1):
            for col in range(grid_cols + 1):
                x = col * grid_cell_width
                y = row * grid_cell_height
                canvas.create_line(x, 0, x, height, fill="#3D3024", width="3")
                canvas.create_line(0, y, width, y, fill="#3D3024", width="3")

    finally:
        app.title("CocoaTabs Grid")

def on_closing():
    app.quit()

frame = tk.Tk()
frame.title("CocoaTabs v0.1")
frame.iconbitmap('icon.ico')

style = ttk.Style()
style.configure('TFrame', background='#1a1a1a')
style.configure('TLabel', background="#1a1a1a", foreground='#c9c9c9', font=('Century Gothic', 12), padding=13)
style.configure('TEntry', fieldbackground='#c9c9c9', foreground='#1a1a1a', font=('Arial', 18))
style.configure('TButton', foreground='#1a1a1a', buttonbackground='#1a1a1a', font=('Century Gothic', 12), padding=3)

if __name__ == "__main__":

    app= tk.Tk()
    app.geometry("310x510+800+250")
    app.title("CocoaTabs Grid")
    app.iconbitmap('icon.ico')

    transparency_value = 1
    make_transparent(app, transparency_value)

    app.bind("<FocusIn>", on_focus_in)
    app.bind("<FocusOut>", on_focus_out)

    cwidth = app.winfo_width()
    cheight = app.winfo_height()

    canvas = tk.Canvas(app, width= cheight, height= cheight, bg="#A97F5F")
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.create_line(0, 5, 300, 5, fill="#3D3024", width=10)
    canvas.create_line(0, 105, 300, 105, fill="#3D3024", width=10)
    canvas.create_line(0, 205, 300, 205, fill="#3D3024", width=10)
    canvas.create_line(0, 305, 300, 305, fill="#3D3024", width=10)
    canvas.create_line(0, 405, 300, 405, fill="#3D3024", width=10)
    canvas.create_line(0, 505, 300, 505, fill="#3D3024", width=10)

    canvas.create_line(5, 0, 5, 510, fill="#3D3024", width=10)
    canvas.create_line(105, 0, 105, 510, fill="#3D3024", width=10)
    canvas.create_line(205, 0, 205, 510, fill="#3D3024", width=10)
    canvas.create_line(305, 0, 305, 510, fill="#3D3024", width=10)

frame = ttk.Frame(frame)
frame['padding'] = (13, 13, 13, 13)
frame.grid(row=0, column=0, padx=0, pady=0)

rows_label = ttk.Label(frame, text="Rows:")
rows_label.grid(row=0, column=0, padx=5, pady=5)
rows_entry = ttk.Entry(frame)
rows_entry.grid(row=0, column=1, padx=5, pady=5)

cols_label = ttk.Label(frame, text="Columns:")
cols_label.grid(row=1, column=0, padx=5, pady=5)
cols_entry = ttk.Entry(frame)
cols_entry.grid(row=1, column=1, padx=5, pady=5)

app_coordinates_label = ttk.Label(frame, text="Cursor Position: N/A")
app_coordinates_label.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

close_button = ttk.Button(frame, text="Draw Grid", command=draw_grid)
close_button.grid(row=6, column=0, padx=5, pady=10)

click_button = ttk.Button(frame, text="Click Grid", command=click_grid)
click_button.grid(row=6, column=1, padx=5, pady=10)

close_button = ttk.Button(frame, text="Close App", command=on_closing)
close_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

update_app_coordinates()

app.attributes('-topmost', True)

frame.mainloop()

make_window_active()