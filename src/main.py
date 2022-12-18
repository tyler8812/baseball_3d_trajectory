import turtle
from matplotlib.pyplot import flag


def get_ball_and_remove_outliers(balls, outliers):
    if len(outliers) == 0:
        outliers = balls
        return 0, outliers
    # print(balls)
    for i in reversed(range(len(balls))):
        is_new_ball = True
        for j in range(len(outliers)):
            # new ball
            if (
                abs(balls[i][1][0] - outliers[j][1][0]) <= 10
                and abs(balls[i][1][1] - outliers[j][1][1]) <= 10
            ):
                is_new_ball = False
                break
        if is_new_ball:
            outliers.append(balls[i])
            return i, outliers
    return -1, outliers


def merge(
    frame_skip,
    target_view1,
    target_view2,
    ref_points_view1,
    ref_points_view2,
    calibration,
    input_videos,
    start_frame1,
    start_frame2,
    output_fig=None,
    show=False,
):
    """
    output
        balls_frame_num: e.g., [[x, y ,z, frame number], [x, y ,z, frame number],...]
        court: e.g., [[x1, y1, z1], [x2, y2, z2],...]
    """
    court = None
    target_view1_for_display = []

    target_view2_for_display = []

    frames = zip(target_view1, target_view2)

    target_frame_num = []

    """
    yolo[i]
        list([]) or list([[68, ['44', '973', '36', '30']]])
    detectron
        list([]) or list([(1330, 292), (1264, 430)])
    """
    proj_map_1, proj_map_2 = project_points(
        src_points_1=get_ref_points(ref_points_view1),
        src_points_2=get_ref_points(ref_points_view2),
        dst_points=get_ref_points(),
        dist=np.load(calibration)["dist_coefs"],
        mtx=np.load(calibration)["camera_matrix"],
    )

    view1_outliers = []
    view2_outliers = []
    for frame_num, frame in enumerate(frames):
        if frame_num % frame_skip != 0:
            continue
        view1, view2 = frame
        view1_idx, view1_outliers = get_ball_and_remove_outliers(view1, view1_outliers)
        view2_idx, view2_outliers = get_ball_and_remove_outliers(view2, view2_outliers)

        target_view1_for_display.append(view1[view1_idx] if view1_idx != -1 else None)
        target_view2_for_display.append(view2[view2_idx] if view2_idx != -1 else None)
        # get targets position
        if view1_idx != -1 and view2_idx != -1:
            target_view1 = np.array(
                [[view1[view1_idx][1][0], view1[view1_idx][1][1]]],
                dtype="int",
            )
            target_view2 = np.array(
                [[view2[view2_idx][1][0], view2[view2_idx][1][1]]],
                dtype="int",
            )

            court, target = draw2court(
                target_view1=target_view1,
                target_view2=target_view2,
                src_points_1=get_ref_points(ref_points_view1),
                src_points_2=get_ref_points(ref_points_view2),
                proj_map_1=proj_map_1,
                proj_map_2=proj_map_2,
            )
            target.append(frame_num)
            target_frame_num.append(target)
    target_frame_num = np.array(target_frame_num)
    target = target_frame_num.T
    # If there is no bat, just add court points.
    if target.shape[-1] == 0:
        court = np.array(get_ref_points()).T
        target = None

    print("total target points: %d" % target.shape[-1])
    if show:
        show_3D(
            input_videos,
            court,
            target,
            target_view1_for_display,
            target_view2_for_display,
            start_frame1=start_frame1,
            start_frame2=start_frame2,
            is_set_lim=True,
            add_court=True,
            court_category="baseball",
            save_name=output_fig,
        )
    court = np.array(court).T
    return target_frame_num, court


def get_ref_points(ref_points="dst_points"):

    if ref_points == "dst_points":
        # baseball home plate
        # return [
        #     [30.75, 10, 0],
        #     [51.5, 30.26, 0],
        #     [51.5, 50.76, 0],
        #     [10, 50.76, 0],
        #     [10, 30.26, 0],
        # ]
        # new bigger home plate
        # return [
        #     [30, 237, 0],
        #     [122, 237, 0],
        #     [122, 40, 0],
        #     [30, 40, 0],
        #     [54.5, 151, 0],
        #     [97.5, 151, 0],
        # ]
        return [
            [0, 0, 0],
            [0, 0, 28],
            [0, 35, 28],
            [46, 0, 0],
            [46, 0, 28],
            [46, 35, 28],
        ]
    else:
        return np.load(ref_points, allow_pickle=True)


def handle_multi_balls(view1_balls, view2_balls, prev_view1, prev_view2):
    view1_moving_ball = None
    view2_moving_ball = None

    def calculate_distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    if len(view1_balls) > 0 and len(prev_view1) > 0:
        # get only coordinate
        view1_balls = [v[2] for v in view1_balls]
        prev_view1 = [v[2] for v in prev_view1]

        for ball in view1_balls:
            is_moving = True
            for prev in prev_view1:
                if calculate_distance((ball[0], ball[1]), (prev[0], prev[1])) < 5:
                    is_moving = False
                    break
            if is_moving:
                view1_moving_ball = ball
    if len(view2_balls) > 0 and len(prev_view2) > 0:
        # get only coordinate
        view2_balls = [v[2] for v in view2_balls]
        prev_view2 = [v[2] for v in prev_view2]

        for ball in view2_balls:
            is_moving = True
            for prev in prev_view2:
                if calculate_distance((ball[0], ball[1]), (prev[0], prev[1])) < 5:
                    is_moving = False
                    break
            if is_moving:
                view2_moving_ball = ball
    # print(view1_moving_ball, view2_moving_ball)
    return view1_moving_ball, view2_moving_ball


if __name__ == "__main__":
    from pathlib import Path
    import argparse
    import numpy as np
    from draw2court import draw2court, show_3D, project_points

    parser = argparse.ArgumentParser()
    parser.add_argument("--end_frame1", default=None, help="End frame", type=int)
    parser.add_argument("--start_frame1", default=None, help="Start frame", type=int)
    parser.add_argument("--end_frame2", default=None, help="End frame", type=int)
    parser.add_argument("--start_frame2", default=None, help="Start frame", type=int)
    parser.add_argument("--frame_skip", default=0, help="Start frame", type=int)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--calib_file", type=str)
    parser.add_argument("--ref_points_view1", type=str)
    parser.add_argument("--ref_points_view2", type=str)
    parser.add_argument("--target_view1", type=str)
    parser.add_argument("--target_view2", type=str)
    parser.add_argument("--output_fig", type=str)
    parser.add_argument("--input_videos", type=str, nargs="+")

    args = parser.parse_args()

    end_frame1 = args.end_frame1
    start_frame1 = args.start_frame1
    end_frame2 = args.end_frame2
    start_frame2 = args.start_frame2
    frame_skip = args.frame_skip
    # is_re_run = args.re_run
    ref_points_view1 = args.ref_points_view1
    ref_points_view2 = args.ref_points_view2
    calibration = args.calib_file
    output_fig = args.output_fig
    input_videos = args.input_videos

    FPS = 120

    # load ball point in two views
    target_view1 = np.load(args.target_view1, allow_pickle=True)
    target_view2 = np.load(args.target_view2, allow_pickle=True)

    if start_frame1 is not None:
        # get start and end frame of eachvideo
        target_view1 = target_view1[start_frame1:end_frame1]
        target_view2 = target_view2[start_frame2:end_frame2]

    print("\n-------------------------------------------\n")
    print(f"view1 video: {len(target_view1)} frames")
    print("\n-------------------------------------------\n")
    print(f"view2 video: {len(target_view1)} frames")
    print("\n-------------------------------------------\n")
    balls_frame_num, court = merge(
        frame_skip,
        target_view1,
        target_view2,
        ref_points_view1,
        ref_points_view2,
        calibration,
        input_videos,
        start_frame1,
        start_frame2,
        output_fig=output_fig,
        show=args.show,
    )
