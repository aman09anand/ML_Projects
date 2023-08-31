import sys 
'''
sys module in python provides various functions and variables that are used ti manipulate different parts of the python runtime enviroments.
'''

def error_message_deatil(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomerException(Exception):
    def __init__(self,error_message,error_detail=error_detail):
        super().__init__(error_message)
        self.error_message=error_message_deatil(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message