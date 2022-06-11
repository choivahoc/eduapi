from flask import jsonify, abort
from application.extensions import action_logger


class ResponseTemplate(object):

    def __init__(self, code, message, log_args=None):
        self.stt_code = code
        self.res_message = message

        if log_args:
            self.service_name = log_args['service_name']
            self.source_file = log_args['source_file']
            self.username = log_args['username']
            self.obj_target = log_args['obj_target']
            self.args = log_args['args']
            self.start_time = log_args['start_time']
            self.print_log = True
        else:
            self.print_log = False

    def return_response(self):
        if self.stt_code == 200:
            if self.print_log:
                action_logger.info('POST',
                                   ServiceCode=self.service_name,
                                   Source=self.source_file,
                                   UserName=self.username,
                                   Object=self.obj_target,
                                   RequestContent=self.args,
                                   ResponseStatus=0,
                                   ResponseContent=self.res_message,
                                   StartTime=self.start_time)
            return jsonify(self.res_message)
        else:
            if self.print_log:
                action_logger.info('POST',
                                   ServiceCode=self.service_name,
                                   Source=self.source_file,
                                   UserName=self.username,
                                   Object=self.obj_target,
                                   RequestContent=self.args,
                                   ResponseStatus=1,
                                   ResponseContent=self.res_message,
                                   ErrorCode=self.stt_code,
                                   StartTime=self.start_time)
            return abort(self.stt_code, self.res_message)

    def print(self):
        return {
            'code': self.stt_code,
            'message': self.res_message
        }
