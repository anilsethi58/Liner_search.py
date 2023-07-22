def search(arr, N, x):
  
    for i in range(0, N):
      
        if (arr[i] == x):
            return i
    return -1
  
  
if __name__ == "__main__":
  
    arr = [2, 3, 4, 10, 40,23,55,65,77,100,91,38]
  
    x=int(input("Enter the number from the list : "))
  
    N = len(arr)
  
    #  call the function
  
    output = search(arr, N, x)
    if(output == -1):
      
        print("Element is not present in array")
      
    else:
      
        print("Element is present at index",output)
