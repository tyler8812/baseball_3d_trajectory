$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

$VIEW1VIDEO='2022-11-22-6-1.MP4'
$VIEW2VIDEO='2022-11-22-6-2.MP4'
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

python src/main.py `
--target_view1 "input_file/$VIEW1NAME/labels.npy" `
--target_view2 "input_file/$VIEW2NAME/labels.npy" `
--ref_points_view1 "input_file/$VIEW1NAME/${VIEW1NAME}_coordinate.npy" `
--ref_points_view2 "input_file/$VIEW2NAME/${VIEW2NAME}_coordinate.npy" `
--calib_file "input_file/calib.npz" `
--start_frame1 25 `
--end_frame1 100 `
--start_frame2 38 `
--end_frame2 113 `
--frame_skip 1 `
--show `
--input_videos "./input_file/${VIEW1NAME}/${VIEW1VIDEO}" "./input_file/${VIEW2NAME}/${VIEW2VIDEO}" `
--output_fig "output/$VIEW1NAME.mp4"