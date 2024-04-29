# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mindsdb.microservices_grpc.db.common_pb2 as common__pb2
import mindsdb.microservices_grpc.db.db_pb2 as db__pb2


class DBServiceStub(object):
    """// Represents server ouput without
    // data. like 'OK' or 'ERROR'
    message StatusResponse {
    bool success = 1;
    string error_message = 2;
    }

    // Represents server output with
    // some data inside. SELECT result for instance
    message Response {
    string type = 1;
    bytes data_frame = 2;
    int32 query = 3;
    int32 error_code = 4;
    string error_message = 5;
    }

    Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.unary_unary(
                '/DBService/Connect',
                request_serializer=db__pb2.HandlerContext.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )
        self.CheckConnection = channel.unary_unary(
                '/DBService/CheckConnection',
                request_serializer=db__pb2.HandlerContext.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/DBService/Disconnect',
                request_serializer=db__pb2.HandlerContext.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )
        self.NativeQuery = channel.unary_unary(
                '/DBService/NativeQuery',
                request_serializer=db__pb2.NativeQueryContext.SerializeToString,
                response_deserializer=common__pb2.Response.FromString,
                )
        self.BinaryQuery = channel.unary_unary(
                '/DBService/BinaryQuery',
                request_serializer=db__pb2.BinaryQueryContext.SerializeToString,
                response_deserializer=common__pb2.Response.FromString,
                )
        self.GetTables = channel.unary_unary(
                '/DBService/GetTables',
                request_serializer=db__pb2.HandlerContext.SerializeToString,
                response_deserializer=common__pb2.Response.FromString,
                )
        self.GetColumns = channel.unary_unary(
                '/DBService/GetColumns',
                request_serializer=db__pb2.ColumnsContext.SerializeToString,
                response_deserializer=common__pb2.Response.FromString,
                )


class DBServiceServicer(object):
    """// Represents server ouput without
    // data. like 'OK' or 'ERROR'
    message StatusResponse {
    bool success = 1;
    string error_message = 2;
    }

    // Represents server output with
    // some data inside. SELECT result for instance
    message Response {
    string type = 1;
    bytes data_frame = 2;
    int32 query = 3;
    int32 error_code = 4;
    string error_message = 5;
    }

    Interface exported by the server.
    """

    def Connect(self, request, context):
        """A simple RPC.

        Establish connection to the specified database

        by creating an appropriate type of Handler instance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckConnection(self, request, context):
        """A simple RPC.

        Check connection to the specified database

        by creating an appropriate type of Handler instance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """A simple RPC.

        Drop the connection to the specified database

        by creating an appropriate type of Handler instance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NativeQuery(self, request, context):
        """A simple RPC.

        Execute native query (string) and returns the result

        wrapped into Response object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BinaryQuery(self, request, context):
        """A simple RPC.

        Execute query (object) and returns the result

        wrapped into Response object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTables(self, request, context):
        """A simple RPC.

        Performs 'get_tables' request and returns the result

        wrapped into Response object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetColumns(self, request, context):
        """A simple RPC.

        Performs 'get_columns' request and returns the result

        wrapped into Response object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=db__pb2.HandlerContext.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
            'CheckConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckConnection,
                    request_deserializer=db__pb2.HandlerContext.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=db__pb2.HandlerContext.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
            'NativeQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.NativeQuery,
                    request_deserializer=db__pb2.NativeQueryContext.FromString,
                    response_serializer=common__pb2.Response.SerializeToString,
            ),
            'BinaryQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.BinaryQuery,
                    request_deserializer=db__pb2.BinaryQueryContext.FromString,
                    response_serializer=common__pb2.Response.SerializeToString,
            ),
            'GetTables': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTables,
                    request_deserializer=db__pb2.HandlerContext.FromString,
                    response_serializer=common__pb2.Response.SerializeToString,
            ),
            'GetColumns': grpc.unary_unary_rpc_method_handler(
                    servicer.GetColumns,
                    request_deserializer=db__pb2.ColumnsContext.FromString,
                    response_serializer=common__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DBService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBService(object):
    """// Represents server ouput without
    // data. like 'OK' or 'ERROR'
    message StatusResponse {
    bool success = 1;
    string error_message = 2;
    }

    // Represents server output with
    // some data inside. SELECT result for instance
    message Response {
    string type = 1;
    bytes data_frame = 2;
    int32 query = 3;
    int32 error_code = 4;
    string error_message = 5;
    }

    Interface exported by the server.
    """

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBService/Connect',
            db__pb2.HandlerContext.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBService/CheckConnection',
            db__pb2.HandlerContext.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBService/Disconnect',
            db__pb2.HandlerContext.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NativeQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBService/NativeQuery',
            db__pb2.NativeQueryContext.SerializeToString,
            common__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BinaryQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBService/BinaryQuery',
            db__pb2.BinaryQueryContext.SerializeToString,
            common__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBService/GetTables',
            db__pb2.HandlerContext.SerializeToString,
            common__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetColumns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBService/GetColumns',
            db__pb2.ColumnsContext.SerializeToString,
            common__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
