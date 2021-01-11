"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'orange', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """

    x_coordinate = int((width-40)/len(YEARS)*year_index+20)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # Set list year, ranks rank_draw to store name_data[name] year, rank/rank_draw
    years = []
    ranks = []
    rank_draw = []
    # k is variable to control line color
    k = 0

    # To check lookup_names data year and rank then append to list ranks
    for name in lookup_names:
        j = 0
        years.clear()
        ranks.clear()
        years += name_data[name]

        for i in range(len(YEARS)):
            str_years = str(YEARS[i])
            if str_years == years[j]:
                year = years[j]
                j += 1
                rank = name_data[name][year]
                ranks.append(rank)
                if j == len(years):
                    years.append('')
            else:
                rank = '*'
                ranks.append(rank)

        # assign rank_draw_temp to check the ranks is digit or not then append to rank_draw for drawing
        for rank_draw_temp in ranks:

            if rank_draw_temp.isdigit():
                rank_draw_temp = int(rank_draw_temp)
                rank_draw.append(rank_draw_temp)

            else:
                rank_draw_temp = int(1001)
                rank_draw.append(rank_draw_temp)

        # Draw the line
        for i in range(len(YEARS)-1):
            x = get_x_coordinate(CANVAS_WIDTH, i)
            canvas.create_line(x, (CANVAS_HEIGHT-40)/1000*rank_draw[i]+20, x+80,
                               (CANVAS_HEIGHT-40)/1000*rank_draw[i+1]+20, width=LINE_WIDTH, fill=COLORS[k])
        # show text in the canvas
        for j in range(len(YEARS)):
            x = get_x_coordinate(CANVAS_WIDTH, j)
            canvas.create_text(x + TEXT_DX, (CANVAS_HEIGHT - 40) / 1000 * rank_draw[j] + 20,
                               text=str(name) + ' ' + str(ranks[j]),
                               anchor=tkinter.SW, fill=COLORS[k])
        k += 1
        # clear rank_draw when the previous canvas_line done
        rank_draw.clear()


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
