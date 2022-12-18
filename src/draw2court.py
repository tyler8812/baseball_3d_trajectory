import pdb
import numpy as np
import cv2
import matplotlib
import os

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.animation as animation


def set_saved_video(output_video, size):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 30
    video = cv2.VideoWriter(output_video, fourcc, fps, size)
    return video


def project_points(
    src_points_1,
    src_points_2,
    dst_points,
    dist,
    mtx,
):
    points_view1 = np.array([src_points_1]).astype("float32")
    points_view2 = np.array([src_points_2]).astype("float32")
    dst_points_pnp = np.array([dst_points]).astype("float32")
    # print(dst_points)
    # print(points_view1)
    # print(points_view2)
    retval1, rvec1, tvec1 = cv2.solvePnP(dst_points_pnp, points_view1, mtx, dist)
    r1, _ = cv2.Rodrigues(rvec1)
    retval2, rvec2, tvec2 = cv2.solvePnP(dst_points_pnp, points_view2, mtx, dist)
    r2, _ = cv2.Rodrigues(rvec2)

    # get view1 project to 3d point
    proj_map_1 = np.matmul(mtx, np.concatenate((r1, tvec1), axis=1))
    # get view2 project to 3d point
    proj_map_2 = np.matmul(mtx, np.concatenate((r2, tvec2), axis=1))

    return proj_map_1, proj_map_2


# ball_view1: view 1 ball position
# ball_view2: view 2 ball position
# src_points_1: view 1 target point
# src_points_2: view 2 target point
# dst_points: mapping 3d target point
# dist: distortion coefficients
# mtx: camera_matrix
# is_show:
# re_run: check if gets projection map from both view targets with dst_points
def draw2court(
    target_view1, target_view2, src_points_1, src_points_2, proj_map_1, proj_map_2
):
    """
    view1_ball = [468, 499, 20, 14]
    view2_ball = [1045, 444, 17, 15]

    view1ball = np.array([[468+20*0.5, 499+14*0.5]], dtype=np.float32)
    view2ball = np.array([[1045+17*0.5, 444+15*0.5]], dtype=np.float32) # read img
    """

    # def checkPts(img, pts):
    #     import copy

    #     img = copy.deepcopy(img)
    #     for p in pts:
    #         if p is not None:
    #             print(p)
    #             cv2.circle(img, (int(p[0]), int(p[1])), 10, (0, 255, 255), 2)
    #             cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    #             while 1:
    #                 cv2.imshow("img", img)
    #                 k = cv2.waitKey(0) & 0xFF
    #                 if k == 27:
    #                     break

    points_view1 = np.array(src_points_1).astype("float32")
    points_view2 = np.array(src_points_2).astype("float32")
    target_view1 = np.array(target_view1).astype("float32")
    target_view2 = np.array(target_view2).astype("float32")

    # read img
    points1 = np.concatenate((points_view1, target_view1), axis=0)
    points2 = np.concatenate((points_view2, target_view2), axis=0)

    pts1 = np.transpose(points1)
    pts2 = np.transpose(points2)
    pts4D = cv2.triangulatePoints(proj_map_1, proj_map_2, pts1, pts2)

    pts4D = pts4D[:, :] / pts4D[-1, :]
    x, y, z, w = pts4D
    target = [x[-1], y[-1], z[-1]]

    courtX = x[:-1]
    courtY = y[:-1]
    courtZ = z[:-1]
    court = [courtX, courtY, courtZ]
    return court, target


# draw the court of different balls
def drawCourt(court_category, ax):
    if court_category == "volleyball":
        points = np.array(
            [
                [0, 0, 0],
                [9, 0, 0],
                [0, 6, 0],
                [9, 6, 0],
                [0, 9, 0],
                [9, 9, 0],
                [0, 12, 0],
                [9, 12, 0],
                [0, 18, 0],
                [9, 18, 0],
            ]
        )
        courtedge = [2, 0, 1, 3, 2, 4, 5, 3, 5, 7, 6, 4, 6, 8, 9, 7]
        curves = points[courtedge]

        netpoints = np.array(
            [
                [0, 9, 0],
                [0, 9, 1.24],
                [0, 9, 2.24],
                [9, 9, 0],
                [9, 9, 1.24],
                [9, 9, 2.24],
            ]
        )
        netedge = [0, 1, 2, 5, 4, 1, 4, 3]
        netcurves = netpoints[netedge]

        court = points.T
        courtX, courtY, courtZ = court
        # ax.scatter(courtX, courtY, courtZ, c='b', marker='x')
        # ax.scatter(0, 0, 5, c='w', marker='x')
        ax.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)
        ax.plot(netcurves[:, 0], netcurves[:, 1], netcurves[:, 2], c="k", linewidth=1)

        # ax2D.scatter(courtX, courtY, c='b', marker='x')
        # print(curves.shape)
        ax2D.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)

    elif court_category == "basketball":
        # https://stackoverflow.com/questions/56888248/how-can-i-get-arc-from-a-3d-circle-in-matplotlib
        r = 0.225
        x0 = 1.575
        y0 = 7.5  # To have the tangent at y=0
        z0 = 3.45

        # Theta varies only between pi/2 and 3pi/2. to have a half-circle
        theta = np.linspace(np.pi / 2.0, 6 * np.pi / 2.0, 201)

        # x = np.zeros_like(theta) # x=0
        y = r * np.cos(theta) + y0  # y - y0 = r*cos(theta)
        x = r * np.sin(theta) + x0  # z - z0 = r*sin(theta)
        z = np.zeros_like(theta) + z0  # x=0

        ax.plot(x, y, z, c="k")

        ax.plot((1.2, 1.2), (7.5 - (1.08 / 2), 7.5 + (1.08 / 2)), (2.9, 2.9), c="k")
        ax.plot((1.2, 1.2), (7.5 - (1.08 / 2), 7.5 + (1.08 / 2)), (3.95, 3.95), c="k")
        ax.plot((1.2, 1.2), (7.5 - (1.08 / 2), 7.5 - (1.08 / 2)), (2.9, 3.95), c="k")
        ax.plot((1.2, 1.2), (7.5 + (1.08 / 2), 7.5 + (1.08 / 2)), (2.9, 3.95), c="k")

    elif court_category == "baseball":
        # baseball home base
        # points = np.array(
        #     [
        #         [30.75, 10, 0],
        #         [51.5, 30.26, 0],
        #         [51.5, 50.76, 0],
        #         [10, 50.76, 0],
        #         [10, 30.26, 0],
        #     ]
        # )
        # court_edges = [0, 1, 2, 3, 4, 0]
        # curves = points[court_edges]
        # ax.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)
        # ax2D.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)
        # new bigger home base
        # points = np.array(
        #     [
        #         [30, 237, 0],
        #         [122, 237, 0],
        #         [122, 40, 0],
        #         [30, 40, 0],
        #         [54.5, 151, 0],
        #         [97.5, 151, 0],
        #     ]
        # )
        # court_edges = [0, 1, 2, 3, 0]
        # curves = points[court_edges]
        # ax.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)
        # ax2D.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)
        # court_edges = [4, 5]
        # curves = points[court_edges]
        # ax.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)
        # ax2D.plot(curves[:, 0], curves[:, 1], c="k", linewidth=1)
        # baseball home base

        points = np.array(
            [
                [0, 0, 0],
                [0, 0, 28],
                [0, 35, 28],
                [0, 35, 0],
                [46, 0, 0],
                [46, 0, 28],
                [46, 35, 28],
                [46, 35, 0],
            ]
        )
        court_edges = [0, 1, 2, 3, 0, 4, 5, 6, 7, 4]
        curves = points[court_edges]
        ax.plot(curves[:, 0], curves[:, 1], curves[:, 2], c="k", linewidth=1)
        court_edges = [1, 5]
        curves = points[court_edges]
        ax.plot(curves[:, 0], curves[:, 1], curves[:, 2], c="k", linewidth=1)
        court_edges = [2, 6]
        curves = points[court_edges]
        ax.plot(curves[:, 0], curves[:, 1], curves[:, 2], c="k", linewidth=1)
        court_edges = [3, 7]
        curves = points[court_edges]
        ax.plot(curves[:, 0], curves[:, 1], curves[:, 2], c="k", linewidth=1)
    return ax


def show_3D(
    input_videos,
    court,
    target,
    target_view1,
    target_view2,
    start_frame1,
    start_frame2,
    alpha=0.8,
    add_court=False,
    save_name=None,
    is_set_lim=True,
    court_category="baseball_bat",
):
    if save_name is not None:
        video = set_saved_video(save_name, (2688, 1512))

    court_x, court_y, court_z = court[0], court[1], court[2]
    target_x, target_y, target_z = target[0], target[1], target[2]
    target_frame = target[3]

    # print(input_videos)
    frame_count = 0
    count = 0
    cap = [cv2.VideoCapture(i) for i in input_videos]

    frames = [None] * len(input_videos)
    ret = [None] * len(input_videos)

    # calibrate two view video
    i = 0
    while i < start_frame1:
        cap[0].read()
        i += 1

    i = 0
    while i < start_frame2:
        cap[1].read()
        i += 1

    while True:
        fig = plt.figure(figsize=(19.2, 21.6))
        gs = gridspec.GridSpec(6, 6)
        ax = plt.subplot(gs[:, :], projection="3d")
        ax.view_init(0, -180)
        if is_set_lim:
            ax.set_xlim(-100, 1100)
            ax.set_ylim(-100, 1100)
            ax.set_zlim(-200, 1000)

        ax.set_xlabel("X Label")
        ax.set_ylabel("Y Label")
        ax.set_zlabel("Z Label")

        for i, c in enumerate(cap):
            if c is not None:
                ret[i], frames[i] = c.read()

        if count < target.shape[-1] and frame_count == target_frame[count]:
            count += 1
        ax.scatter(court_x, court_y, court_z, color="r", marker="o", alpha=alpha)
        ax.scatter(
            target_x[:count],
            target_y[:count],
            target_z[:count],
            color="b",
            marker="o",
            alpha=alpha,
        )

        if add_court:
            drawCourt(court_category, ax)

        fig.canvas.draw()
        # convert canvas to image
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep="")
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        # img is rgb, convert to opencv's default bgr
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # draw target onto view1 and view2
        frame1 = draw_target(target_view1[frame_count], frames[0])
        frame2 = draw_target(target_view2[frame_count], frames[1])

        frame_count += 1

        merge_image = cv2.vconcat([frame1, frame2])
        merge_image = cv2.hconcat([merge_image, img])
        resize_size = (int(merge_image.shape[1] * 0.7), int(merge_image.shape[0] * 0.7))
        merge_image = cv2.resize(merge_image, resize_size)
        cv2.imshow("frame", merge_image)
        if save_name is not None:
            video.write(merge_image)
        if cv2.waitKey(1) == ord("q"):
            break
        plt.close(fig)
    if save_name is not None:
        video.release()
    # cap.release()
    cv2.destroyAllWindows()
    return


def draw_target(target_view, frame):
    if target_view != None:
        cv2.circle(
            frame,
            target_view[1],
            8,
            (141, 66, 245),
            -1,
        )
    return frame
