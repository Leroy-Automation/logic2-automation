# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from saleae.grpc import saleae_pb2 as saleae_dot_grpc_dot_saleae__pb2


class ManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDevices = channel.unary_unary(
                '/saleae.automation.Manager/GetDevices',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.GetDevicesRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.GetDevicesReply.FromString,
                )
        self.StartCapture = channel.unary_unary(
                '/saleae.automation.Manager/StartCapture',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.StartCaptureRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.StartCaptureReply.FromString,
                )
        self.StopCapture = channel.unary_unary(
                '/saleae.automation.Manager/StopCapture',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.StopCaptureRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.StopCaptureReply.FromString,
                )
        self.LoadCapture = channel.unary_unary(
                '/saleae.automation.Manager/LoadCapture',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.LoadCaptureRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.LoadCaptureReply.FromString,
                )
        self.SaveCapture = channel.unary_unary(
                '/saleae.automation.Manager/SaveCapture',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.SaveCaptureRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.SaveCaptureReply.FromString,
                )
        self.CloseCapture = channel.unary_unary(
                '/saleae.automation.Manager/CloseCapture',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.CloseCaptureRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.CloseCaptureReply.FromString,
                )
        self.ExportRawDataCsv = channel.unary_unary(
                '/saleae.automation.Manager/ExportRawDataCsv',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataCsvRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataCsvReply.FromString,
                )
        self.ExportRawDataBinary = channel.unary_unary(
                '/saleae.automation.Manager/ExportRawDataBinary',
                request_serializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataBinaryRequest.SerializeToString,
                response_deserializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataBinaryReply.FromString,
                )


class ManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDevices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartCapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopCapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadCapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveCapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseCapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportRawDataCsv(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportRawDataBinary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevices,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.GetDevicesRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.GetDevicesReply.SerializeToString,
            ),
            'StartCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.StartCapture,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.StartCaptureRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.StartCaptureReply.SerializeToString,
            ),
            'StopCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.StopCapture,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.StopCaptureRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.StopCaptureReply.SerializeToString,
            ),
            'LoadCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadCapture,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.LoadCaptureRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.LoadCaptureReply.SerializeToString,
            ),
            'SaveCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveCapture,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.SaveCaptureRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.SaveCaptureReply.SerializeToString,
            ),
            'CloseCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseCapture,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.CloseCaptureRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.CloseCaptureReply.SerializeToString,
            ),
            'ExportRawDataCsv': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportRawDataCsv,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataCsvRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataCsvReply.SerializeToString,
            ),
            'ExportRawDataBinary': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportRawDataBinary,
                    request_deserializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataBinaryRequest.FromString,
                    response_serializer=saleae_dot_grpc_dot_saleae__pb2.ExportRawDataBinaryReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'saleae.automation.Manager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Manager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/GetDevices',
            saleae_dot_grpc_dot_saleae__pb2.GetDevicesRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.GetDevicesReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartCapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/StartCapture',
            saleae_dot_grpc_dot_saleae__pb2.StartCaptureRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.StartCaptureReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopCapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/StopCapture',
            saleae_dot_grpc_dot_saleae__pb2.StopCaptureRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.StopCaptureReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadCapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/LoadCapture',
            saleae_dot_grpc_dot_saleae__pb2.LoadCaptureRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.LoadCaptureReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveCapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/SaveCapture',
            saleae_dot_grpc_dot_saleae__pb2.SaveCaptureRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.SaveCaptureReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseCapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/CloseCapture',
            saleae_dot_grpc_dot_saleae__pb2.CloseCaptureRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.CloseCaptureReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportRawDataCsv(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/ExportRawDataCsv',
            saleae_dot_grpc_dot_saleae__pb2.ExportRawDataCsvRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.ExportRawDataCsvReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportRawDataBinary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saleae.automation.Manager/ExportRawDataBinary',
            saleae_dot_grpc_dot_saleae__pb2.ExportRawDataBinaryRequest.SerializeToString,
            saleae_dot_grpc_dot_saleae__pb2.ExportRawDataBinaryReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
