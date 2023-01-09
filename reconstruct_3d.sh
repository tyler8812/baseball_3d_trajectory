VIEW1NAME='2022-12-19-8-1'
VIEW2NAME='2022-12-19-8-2'
VIEW1VIDEO="$VIEW1NAME.MP4"
VIEW2VIDEO="$VIEW2NAME.MP4"


python src/main.py \
--target_view1 "input_file/$VIEW1NAME/labels.npy" \
--target_view2 "input_file/$VIEW2NAME/labels.npy" \
--ref_points_view1 "input_file/$VIEW1NAME/${VIEW1NAME}_coordinate.npy" \
--ref_points_view2 "input_file/$VIEW2NAME/${VIEW2NAME}_coordinate.npy" \
--mask_view1 "input_file/$VIEW1NAME/${VIEW1NAME}_poly.png" \
--mask_view2 "input_file/$VIEW2NAME/${VIEW2NAME}_poly.png" \
--calib_file "input_file/calib.npz" \
--start_frame1 0 \
--end_frame1 780 \
--start_frame2 0 \
--end_frame2 780 \
--frame_skip 1 \
--show \
--input_videos "./input_file/${VIEW1NAME}/${VIEW1VIDEO}" "./input_file/${VIEW2NAME}/${VIEW2VIDEO}" \
--output_fig "output/$VIEW1NAME.mp4"