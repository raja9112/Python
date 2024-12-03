# !/bin/bash

# new_array=()

# new_array[0]="Raja"
# new_array[1]="RN"

# echo ${new_array[0]}
# echo ${new_array[1]}

# # To print all elements
# echo ${new_array[@]}

# # To print number of elements in array
# echo ${#new_array[@]}

# # Looping through array
# for fruit in ${new_array[@]}; do
#     echo $fruit
# done

# Method 2
# for fruit in "${new_array[@]}"
# do
#     echo $fruit
# done

# Associate Array
# declare -A associate_arr
# associate_arr=([Name]="Rajarajan", [Age]=21)

# echo ${associate_arr[Name]}
# echo ${associate_arr[Age]}
# echo ${#associate_arr[@]}
# echo ${associate_arr[@]}

# # looping through asociate array
# # For associate array include !
# for key in ${!associate_arr[@]}; do
#     echo "$Key => ${associate_arr[$key]}"
# done

# # Operators and if else
# #!/bin/bash
# a=5
# b=10

# if [[ $a -lt 10 && $b -gt 15 ]]; then
#     echo "Both conditions are true"
# else
#     echo "At least one condition is false"
# fi

# File test operators

#!/bin/bash

# file="testfile.txt"

# if [ -e $file ]; then
#     echo "File exists"
# else
#     echo "File does not exist"
# fi

# if [ -r $file ]; then
#     echo "File is readable"
# fi

# if [ -w $file ]; then
#     echo "File is writable"
# fi

# While loop
# a=5
# while [ $a -ne 0 ]; do
#     echo $a
#     a=$((a - 1))
# done

# Until loop

#!/bin/bash

# counter=1
# until [ $counter -gt 5 ]
# do
#     echo "Counter: $counter"
#     ((counter++))
# done

# Select loop

# select option in "option 1" "option 2" "quit"; do
#     case $option in
#     "option 1")
#         echo "option 1"
#         ;;
#     "option 2")
#         echo "option 2"
#         ;;
#     "quit")
#         echo "quit"
#         ;;
#     *)
#         echo "Invalid choice"
#         ;;
#     esac
# done

# a=0
# while [ "$a" -lt 10 ]    # this is loop1
# do
#    b="$a"
#    while [ "$b" -ge 0 ]  # this is loop2
#    do
#       echo -n "$b "
#       b=`expr $b - 1`
#    done
#    echo
#    a=`expr $a + 1`
# done

# This will produce the following result. It is important to note how echo -n works here. Here -n option lets echo avoid printing a new line character.


# File substitution

#!/bin/bash

for file in *.txt
do
    echo "Found file: $file
done
