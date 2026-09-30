def isHappy(n): 
   occur_num = []
   
   # base case
   if(n==1):
      return True

   while(n>0):
      total = 0
      while(n > 0):
            digit = n % 10  # get last digit
            total = total + (digit * digit)
            n = n//10   # remove last digit

      if(total not in occur_num):
            occur_num.append(total)
      else:
            return False

      if(total == 1):
            return True

      n = total   # if above conditions fail
   return False
   
if __name__ == "__main__": 
   sample0_output = isHappy(19) 
   sample1_output = isHappy(2) 
   with open("/app/bind_mount/output.txt", "w") as f: 
      f.write(f"19: {sample0_output}\n") 
      f.write(f"2: {sample1_output}\n") 
   print("Results saved to /app/bind_mount/output.txt")