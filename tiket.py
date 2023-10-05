import tkinter as tk

def process_matrix_and_vector():
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = int(matrix_entries[i][j].get())
            row.append(value)
        matrix.append(row)

    vector_result = [min(row) for row in matrix]

    for i in range(n):
        vector_result_text[i].set(vector_result[i])

    # Highlight the smallest repeating elements in each row
    for i, row in enumerate(matrix):
        counts = {}
        for element in row:
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1

        min_element = min(row)
        for j, element in enumerate(row):
            if counts[element] > 1 and element == min_element:
                canvas.itemconfig(matrix_text[i][j], fill='red')
            else:
                canvas.itemconfig(matrix_text[i][j], fill='black')

# Main program
n = int(input())

root = tk.Tk()
root.title("Matrix and Vector Processor")

canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=n)

matrix_entries = [[tk.Entry(root, width=5) for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix_entries[i][j].grid(row=i, column=j + 1)

process_button = tk.Button(root, text="Process", command=process_matrix_and_vector)
process_button.grid(row=n, column=0, columnspan=n + 1)

vector_result_text = [tk.StringVar() for _ in range(n)]
vector_result_labels = [tk.Label(root, textvariable=vector_result_text[i]) for i in range(n)]
for i in range(n):
    vector_result_labels[i].grid(row=i, column=n + 2)

matrix_text = [[canvas.create_text(j * 30 + 15, i * 30 + 15, text="") for j in range(n)] for i in range(n)]

root.mainloop()
