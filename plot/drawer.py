import matplotlib.pyplot as plt
import matplotlib.animation as anim


def draw(g, solve, population, i=2000, ps_list=None):
    figure = plt.figure()
    ax = figure.gca()

    def init(g, ps_list):
        for i in range(len(g)):
            ax.plot(g.node[i]['x'], g.node[i]['y'], "ko", markersize=8)
        if __debug__:
            for i in range(len(g)):
                startx, starty = g.node[i]['x'], g.node[i]['y']
                for j in range(i + 1, len(g)):
                    endx, endy = g.node[j]['x'], g.node[j]['y']
                    ax.plot([startx, endx], [starty, endy], lw=0.05, c='k')
        if ps_list is not None:
            for i in range(len(ps_list) - 1):
                startx = g.node[ps_list[i]]['x']
                starty = g.node[ps_list[i]]['y']
                endx = g.node[ps_list[i + 1]]['x']
                endy = g.node[ps_list[i + 1]]['y']
                ax.plot([startx, endx], [starty, endy], lw=2.5, c='k')
            startx = g.node[ps_list[0]]['x']
            starty = g.node[ps_list[0]]['y']
            endx = g.node[ps_list[len(ps_list) - 1]]['x']
            endy = g.node[ps_list[len(ps_list) - 1]]['y']
            ax.plot([startx, endx], [starty, endy], lw=2.5, c='k')

    def update(i):
        if __debug__:
            print("Update Canvas : " + str(i))
        # Draw Lines
        # Calculate Answers
        plt.cla()
        init(g, ps_list)
        p = solve(g, population)
        for i in range(len(p) - 1):
            startx = g.node[p[i]]['x']
            starty = g.node[p[i]]['y']
            endx = g.node[p[i+1]]['x']
            endy = g.node[p[i+1]]['y']
            ax.plot([startx, endx], [starty, endy], lw=0.25, c='b')
        startx = g.node[p[0]]['x']
        starty = g.node[p[0]]['y']
        endx = g.node[p[len(ps_list) - 1]]['x']
        endy = g.node[p[len(ps_list) - 1]]['y']
        ax.plot([startx, endx], [starty, endy], lw=0.25, c='b')
        figure.canvas.draw()

    animation = anim.FuncAnimation(figure, update, init_func=init(g, ps_list), interval=i)
    print(animation)
    plt.show()

# draw vertical line from (70,100) to (70, 250)
# plt.plot([70, 70], [100, 250], 'k-', lw=2)

# draw diagonal line from (70, 90) to (90, 200)
# plt.plot([70, 90], [90, 200], 'k-')
