$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

$VIEW1VIDEO='2022-12-19-10-1.MP4'
$VIEW2VIDEO='2022-12-19-10-2.MP4'
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

python utils/draw_poly_and_fill.py `
--video "./input_file/${VIEW1NAME}/${VIEW1VIDEO}" `
--output "./input_file/${VIEW1NAME}/${VIEW1NAME}_poly.png"

python utils/draw_poly_and_fill.py `
--video "./input_file/${VIEW2NAME}/${VIEW2VIDEO}" `
--output "./input_file/${VIEW2NAME}/${VIEW2NAME}_poly.png"