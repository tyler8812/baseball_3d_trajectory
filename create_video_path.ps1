$FOLDERPATH=$PSScriptRoot

cd ${FOLDERPATH}
echo "Entering ${FOLDERPATH}......"
./env/Scripts/activate

# single video
$VIEW1VIDEO="2022-11-22-4s5-1.MP4"
$VIEW2VIDEO="2022-11-22-4s5-2.MP4"
$VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
$VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

mkdir input_file
mkdir output
mkdir "input_file/$VIEW1NAME"
mkdir "input_file/$VIEW2NAME"

Copy "video/${VIEW1VIDEO}" "input_file/$VIEW1NAME"
Copy "video/${VIEW2VIDEO}" "input_file/$VIEW2NAME"

# multi video
# for ($num1 = 1 ; $num1 -le 4 ; $num1++){  
#     if ($num1 -eq 3){
#         continue;
#     } 
#     for ($num = 1 ; $num -le 3 ; $num++){  
#         $VIEW1VIDEO="2022-11-22-${num1}s${num}-1.MP4"
#         $VIEW2VIDEO="2022-11-22-${num1}s${num}-2.MP4"
#         $VIEW1NAME=$VIEW1VIDEO.Split('.')[0]
#         $VIEW2NAME=$VIEW2VIDEO.Split('.')[0]

#         mkdir input_file
#         mkdir output
#         mkdir "input_file/$VIEW1NAME"
#         mkdir "input_file/$VIEW2NAME"

#         Copy "video/${VIEW1VIDEO}" "input_file/$VIEW1NAME"
#         Copy "video/${VIEW2VIDEO}" "input_file/$VIEW2NAME"
#     }
# }