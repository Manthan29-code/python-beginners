# singly link list & basic operation on it
class Node:
   def __init__(self,value=None,next_ref=None):
           self.value=value
           self.next_ref=next_ref


class Head:
      def __init__(self,a=None):
            self.head_ref=Node(value=a)
      def insert_at_first(self,a=None):      # to insert data at first position
            if  self.head_ref is not None:
                  te=Node(value=a)
                  te.next_ref=self.head_ref
                  self.head_ref=te
            else:
                  self.head_ref=Node(value=a)
      
      def insert_at_last(self,a):         # to insert data at last position
            temp=self.head_ref
            while temp.next_ref != None:
                temp=temp.next_ref
            temp.next_ref=Node(value=a)
            return     
      def show(self):  
            temp=self.head_ref
            while temp.next_ref != None:
                print(temp.value)
                temp=temp.next_ref
            print(temp.value)    
            return
      def show_list(self):            # this function will return  list of iteam stored in SLL
            list=[]  
            temp=self.head_ref
            while temp.next_ref != None:
                list.append(temp.value)
                temp=temp.next_ref         
            list.append(temp.value)
            return list
             
list=[10,57.9,"Manthan",[3,7.9,"hello"]]                 
H1=Head()
H1.insert_at_first(28)
H1.insert_at_first(78)
for i in list:
  H1.insert_at_last(i)
H1.show()  
item=H1.show_list()     
print(item)           