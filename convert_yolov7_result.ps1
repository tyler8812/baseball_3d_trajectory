$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

$VIEW1VIDEO='2022-11-22-6-1.MP4'
$VIEW2VIDEO='2022-11-22-6-2.MP4'
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

echo "Convert yolov7 result from ${VIEW1VIDEO} and delete some outliers......"
python utils/convert_yolov7_result.py `
--input_folder "./runs/detect/${VIEW1NAME}/labels" `
--output "./input_file/${VIEW1NAME}/labels.npy" `
--input_video "./runs/detect/${VIEW1NAME}/${VIEW1VIDEO}" `
--video_name $VIEW1NAME `
--view 1

echo "Convert yolov7 result from ${VIEW2VIDEO} and delete some outliers......"
python utils/convert_yolov7_result.py `
--input_folder "./runs/detect/${VIEW2NAME}/labels" `
--output "./input_file/${VIEW2NAME}/labels.npy" `
--input_video "./runs/detect/${VIEW2NAME}/${VIEW2VIDEO}" `
--video_name $VIEW2NAME `
--view 2