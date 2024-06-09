
import sys

class USvisaException(Exception):
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__()
        self.error_details=error_details
        self.error_message= USvisaException.get_error_message(error_message=error_message,
                                                              error_details=self.error_details)
    
    @staticmethod
    def get_error_message(error_message:Exception,error_details:sys):
        _,__,exc_tb=error_details.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        line_number=exc_tb.tb_lineno
        
        complete_error_message=f""" 
        Exception occurred in script 
            file name : {file_name}
            line number : {line_number}
            error message : {str(error_message)}
        """
        
        return complete_error_message
        
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return self.error_message