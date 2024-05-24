import curses
import time

def draw_ufo_frame(stdscr, frame):
    # Clear screen
    stdscr.clear()

    # Get screen dimensions
    height, width = stdscr.getmaxyx()

    # UFO frames
    ufo_frames = [
        [
            "                                                             ",
            "                         .   *       _.---._  *              ",
            "                                   .'       '.       .       ",
            "                               _.-~===========~-._          *",
            "                           *  (___________________)     .    ",
            "                       .     .      \\_______/    *           "
        ],
        [
            "                        *         .  _.---._          .      ",
            "                              *    .'       '.  .            ",
            "                               _.-~===========~-._ *         ",
            "                           .  (___________________)       *  ",
            "                            *       \\_______/        .       ",
            "                                                             "
        ],
        [
            "                                   *                .        ",
            "                             *       _.---._              *  ",
            "                          .        .'       '.       *       ",
            "                       .       _.-~===========~-._     *     ",
            "                              (___________________)         .",
            "                       *            \\_______/ .              "
        ],
        [
            "                        *         .  _.---._          .      ",
            "                              *    .'       '.  .            ",
            "                               _.-~===========~-._ *         ",
            "                           .  (___________________)       *  ",
            "                            *       \\_______/        .       ",
            "                                                             "
        ]
    ]

    # Determine start position for vertical centering
    start_y = height // 2 - len(ufo_frames[frame]) // 2
    start_x = width // 2 - len(ufo_frames[frame][0]) // 2

    # Draw the selected frame
    for i, line in enumerate(ufo_frames[frame]):
        stdscr.addstr(start_y + i, start_x, line)

    # Refresh the screen to show the frame
    stdscr.refresh()

def main(stdscr):
    # Disable cursor blinking
    curses.curs_set(0)

    # Animation loop
    frame_count = 4
    while True:
        for frame in range(frame_count):
            draw_ufo_frame(stdscr, frame)
            time.sleep(0.5)  # Slower movement

# Initialize the curses application
curses.wrapper(main)
