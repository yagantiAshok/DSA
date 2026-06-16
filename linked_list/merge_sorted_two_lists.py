

from insert_opeartions import take_input,print_list

list1 = take_input()
list2 = take_input()

def mergeTwoLists(list1, list2):


        if (list1 is None):

            return list2
        
        if (list2 is None):

            return list1

        
        newhead = None
        newtail = None

        while (list1 is not None and list2 is not None):

            if (list1.data < list2.data):

                if (newhead==None):

                    newhead = list1
                    newtail = list1
                
                else:

                    newtail.ref = list1
                    newtail = list1
                
                list1 = list1.ref
            
            else:

                if (newhead==None):

                    newhead = list2
                    newtail = list2
                
                else:

                    newtail.ref = list2
                    newtail = list2
                
                list2 = list2.ref
        
        if (list1 is not None):

            newtail.ref = list1

        if (list2 is not None):

            newtail.ref = list2
        
        return newhead

head = mergeTwoLists(list1,list2)

print_list(head)
