$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

$VIEW1VIDEO='2022-11-22-6-1.MP4'
$VIEW2VIDEO='2022-11-22-6-2.MP4'
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

mkdir input_file
mkdir output
mkdir "input_file/$VIEW1NAME"
mkdir "input_file/$VIEW2NAME"

Copy "video/${VIEW1VIDEO}" "input_file/$VIEW1NAME"
Copy "video/${VIEW2VIDEO}" "input_file/$VIEW2NAME"