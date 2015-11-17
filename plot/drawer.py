import matplotlib.pyplot as plt
import matplotlib.animation as anim


def draw(point_list, points_solution_list, solve, matrix):
    figure = plt.figure()
    ax = figure.gca()

    def init(point_list, points_solution_list):
        for i in range(len(point_list)):
            ax.plot(point_list[i][0], point_list[i][1], "ko", markersize=8)
        if __debug__:
            for i in range(len(point_list)):
                startx, starty = point_list[i][0], point_list[i][1]
                for j in range(i + 1, len(point_list)):
                    endx, endy = point_list[j][0], point_list[j][1]
                    ax.plot([startx, endx], [starty, endy], lw=0.05, c='k')
        if points_solution_list is not None:
            for i in range(len(points_solution_list) - 1):
                startx = point_list[points_solution_list[i]][0]
                starty = point_list[points_solution_list[i]][1]
                endx = point_list[points_solution_list[i + 1]][0]
                endy = point_list[points_solution_list[i + 1]][1]
                ax.plot([startx, endx], [starty, endy], lw=2.5, c='k')
            startx = point_list[points_solution_list[0]][0]
            starty = point_list[points_solution_list[0]][1]
            endx = point_list[points_solution_list[len(points_solution_list) - 1]][0]
            endy = point_list[points_solution_list[len(points_solution_list) - 1]][1]
            ax.plot([startx, endx], [starty, endy], lw=2.5, c='k')

    def update(i):
        if __debug__:
            print("Update Canvas : " + str(i))

        # Draw Lines
        # Calculate Answers
        plt.cla()
        init(point_list, points_solution_list)

        points = solve(point_list, matrix)
#        for i in points:
#                startx = point_list[points[i]][0]
#                starty = point_list[points[i]][1]
#                endx = point_list[points[i+1][0]]
#                endy = point_list[points[i+1][1]]
#                ax.plot([startx, endx], [starty, endy], lw=2.5, c='k')
#        startx = point_list[points[0]][0]
#        starty = point_list[points[0]][1]
#        endx = point_list[points[len(points_solution_list) - 1]][0]
#        endy = point_list[points[len(points_solution_list) - 1]][1]
#        ax.plot([startx, endx], [starty, endy], lw=2.5, c='k')
                

        figure.canvas.draw()
        return True

    anim.FuncAnimation(figure, update, init_func=init(point_list, points_solution_list))
    plt.show()

# draw vertical line from (70,100) to (70, 250)
# plt.plot([70, 70], [100, 250], 'k-', lw=2)

# draw diagonal line from (70, 90) to (90, 200)
# plt.plot([70, 90], [90, 200], 'k-')
