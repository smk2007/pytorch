"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___DeviceTypeProto = DeviceTypeProto
class _DeviceTypeProto(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeviceTypeProto], type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    PROTO_CPU = DeviceTypeProto.V(0)
    PROTO_CUDA = DeviceTypeProto.V(1)
    PROTO_MKLDNN = DeviceTypeProto.V(2)
    PROTO_OPENGL = DeviceTypeProto.V(3)
    PROTO_OPENCL = DeviceTypeProto.V(4)
    PROTO_IDEEP = DeviceTypeProto.V(5)
    PROTO_HIP = DeviceTypeProto.V(6)
    PROTO_FPGA = DeviceTypeProto.V(7)
    PROTO_ORT = DeviceTypeProto.V(8)
    PROTO_XLA = DeviceTypeProto.V(9)
    PROTO_MPS = DeviceTypeProto.V(10)
    PROTO_DML = DeviceTypeProto.V(11)
    PROTO_COMPILE_TIME_MAX_DEVICE_TYPES = DeviceTypeProto.V(12)
class DeviceTypeProto(metaclass=_DeviceTypeProto):
    V = typing.NewType('V', int)
PROTO_CPU = DeviceTypeProto.V(0)
PROTO_CUDA = DeviceTypeProto.V(1)
PROTO_MKLDNN = DeviceTypeProto.V(2)
PROTO_OPENGL = DeviceTypeProto.V(3)
PROTO_OPENCL = DeviceTypeProto.V(4)
PROTO_IDEEP = DeviceTypeProto.V(5)
PROTO_HIP = DeviceTypeProto.V(6)
PROTO_FPGA = DeviceTypeProto.V(7)
PROTO_ORT = DeviceTypeProto.V(8)
PROTO_XLA = DeviceTypeProto.V(9)
PROTO_MPS = DeviceTypeProto.V(10)
PROTO_DML = DeviceTypeProto.V(11)
PROTO_COMPILE_TIME_MAX_DEVICE_TYPES = DeviceTypeProto.V(12)

class TensorProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _DataType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DataType], type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNDEFINED = TensorProto.DataType.V(0)
        FLOAT = TensorProto.DataType.V(1)
        INT32 = TensorProto.DataType.V(2)
        BYTE = TensorProto.DataType.V(3)
        STRING = TensorProto.DataType.V(4)
        BOOL = TensorProto.DataType.V(5)
        UINT8 = TensorProto.DataType.V(6)
        INT8 = TensorProto.DataType.V(7)
        UINT16 = TensorProto.DataType.V(8)
        INT16 = TensorProto.DataType.V(9)
        INT64 = TensorProto.DataType.V(10)
        FLOAT16 = TensorProto.DataType.V(12)
        DOUBLE = TensorProto.DataType.V(13)
        ZERO_COLLISION_HASH = TensorProto.DataType.V(14)
        REBATCHING_BUFFER = TensorProto.DataType.V(15)
    class DataType(metaclass=_DataType):
        V = typing.NewType('V', int)
    UNDEFINED = TensorProto.DataType.V(0)
    FLOAT = TensorProto.DataType.V(1)
    INT32 = TensorProto.DataType.V(2)
    BYTE = TensorProto.DataType.V(3)
    STRING = TensorProto.DataType.V(4)
    BOOL = TensorProto.DataType.V(5)
    UINT8 = TensorProto.DataType.V(6)
    INT8 = TensorProto.DataType.V(7)
    UINT16 = TensorProto.DataType.V(8)
    INT16 = TensorProto.DataType.V(9)
    INT64 = TensorProto.DataType.V(10)
    FLOAT16 = TensorProto.DataType.V(12)
    DOUBLE = TensorProto.DataType.V(13)
    ZERO_COLLISION_HASH = TensorProto.DataType.V(14)
    REBATCHING_BUFFER = TensorProto.DataType.V(15)

    class _SerializationFormat(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SerializationFormat], type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        FMT_PROTOBUF = TensorProto.SerializationFormat.V(0)
        FMT_BFLOAT16 = TensorProto.SerializationFormat.V(1)
    class SerializationFormat(metaclass=_SerializationFormat):
        V = typing.NewType('V', int)
    FMT_PROTOBUF = TensorProto.SerializationFormat.V(0)
    FMT_BFLOAT16 = TensorProto.SerializationFormat.V(1)

    class Segment(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        BEGIN_FIELD_NUMBER: int
        END_FIELD_NUMBER: int
        begin: int = ...
        end: int = ...

        def __init__(self,
            *,
            begin : typing.Optional[int] = ...,
            end : typing.Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"begin",b"begin",u"end",b"end"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"begin",b"begin",u"end",b"end"]) -> None: ...

    DIMS_FIELD_NUMBER: int
    DATA_TYPE_FIELD_NUMBER: int
    DATA_FORMAT_FIELD_NUMBER: int
    FLOAT_DATA_FIELD_NUMBER: int
    INT32_DATA_FIELD_NUMBER: int
    BYTE_DATA_FIELD_NUMBER: int
    STRING_DATA_FIELD_NUMBER: int
    DOUBLE_DATA_FIELD_NUMBER: int
    INT64_DATA_FIELD_NUMBER: int
    RAW_DATA_FIELD_NUMBER: int
    NAME_FIELD_NUMBER: int
    DEVICE_DETAIL_FIELD_NUMBER: int
    SEGMENT_FIELD_NUMBER: int
    dims: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    data_type: global___TensorProto.DataType = ...
    data_format: int = ...
    float_data: google.protobuf.internal.containers.RepeatedScalarFieldContainer[float] = ...
    int32_data: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    byte_data: bytes = ...
    string_data: google.protobuf.internal.containers.RepeatedScalarFieldContainer[bytes] = ...
    double_data: google.protobuf.internal.containers.RepeatedScalarFieldContainer[float] = ...
    int64_data: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    raw_data: bytes = ...
    name: typing.Text = ...

    @property
    def device_detail(self) -> global___DeviceOption: ...

    @property
    def segment(self) -> global___TensorProto.Segment: ...

    def __init__(self,
        *,
        dims : typing.Optional[typing.Iterable[int]] = ...,
        data_type : typing.Optional[global___TensorProto.DataType] = ...,
        data_format : typing.Optional[int] = ...,
        float_data : typing.Optional[typing.Iterable[float]] = ...,
        int32_data : typing.Optional[typing.Iterable[int]] = ...,
        byte_data : typing.Optional[bytes] = ...,
        string_data : typing.Optional[typing.Iterable[bytes]] = ...,
        double_data : typing.Optional[typing.Iterable[float]] = ...,
        int64_data : typing.Optional[typing.Iterable[int]] = ...,
        raw_data : typing.Optional[bytes] = ...,
        name : typing.Optional[typing.Text] = ...,
        device_detail : typing.Optional[global___DeviceOption] = ...,
        segment : typing.Optional[global___TensorProto.Segment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"byte_data",b"byte_data",u"data_format",b"data_format",u"data_type",b"data_type",u"device_detail",b"device_detail",u"name",b"name",u"raw_data",b"raw_data",u"segment",b"segment"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"byte_data",b"byte_data",u"data_format",b"data_format",u"data_type",b"data_type",u"device_detail",b"device_detail",u"dims",b"dims",u"double_data",b"double_data",u"float_data",b"float_data",u"int32_data",b"int32_data",u"int64_data",b"int64_data",u"name",b"name",u"raw_data",b"raw_data",u"segment",b"segment",u"string_data",b"string_data"]) -> None: ...
global___TensorProto = TensorProto

class QTensorProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DIMS_FIELD_NUMBER: int
    PRECISION_FIELD_NUMBER: int
    SCALE_FIELD_NUMBER: int
    BIAS_FIELD_NUMBER: int
    IS_SIGNED_FIELD_NUMBER: int
    DATA_FIELD_NUMBER: int
    NAME_FIELD_NUMBER: int
    DATA_TYPE_FIELD_NUMBER: int
    SCALES_FIELD_NUMBER: int
    BIASES_FIELD_NUMBER: int
    AXIS_FIELD_NUMBER: int
    IS_MULTIPARAM_FIELD_NUMBER: int
    dims: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    precision: int = ...
    scale: float = ...
    bias: float = ...
    is_signed: bool = ...
    data: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    name: typing.Text = ...
    data_type: global___TensorProto.DataType = ...
    scales: google.protobuf.internal.containers.RepeatedScalarFieldContainer[float] = ...
    biases: google.protobuf.internal.containers.RepeatedScalarFieldContainer[float] = ...
    axis: int = ...
    is_multiparam: bool = ...

    def __init__(self,
        *,
        dims : typing.Optional[typing.Iterable[int]] = ...,
        precision : typing.Optional[int] = ...,
        scale : typing.Optional[float] = ...,
        bias : typing.Optional[float] = ...,
        is_signed : typing.Optional[bool] = ...,
        data : typing.Optional[typing.Iterable[int]] = ...,
        name : typing.Optional[typing.Text] = ...,
        data_type : typing.Optional[global___TensorProto.DataType] = ...,
        scales : typing.Optional[typing.Iterable[float]] = ...,
        biases : typing.Optional[typing.Iterable[float]] = ...,
        axis : typing.Optional[int] = ...,
        is_multiparam : typing.Optional[bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"axis",b"axis",u"bias",b"bias",u"data_type",b"data_type",u"is_multiparam",b"is_multiparam",u"is_signed",b"is_signed",u"name",b"name",u"precision",b"precision",u"scale",b"scale"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"axis",b"axis",u"bias",b"bias",u"biases",b"biases",u"data",b"data",u"data_type",b"data_type",u"dims",b"dims",u"is_multiparam",b"is_multiparam",u"is_signed",b"is_signed",u"name",b"name",u"precision",b"precision",u"scale",b"scale",u"scales",b"scales"]) -> None: ...
global___QTensorProto = QTensorProto

class TensorProtos(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROTOS_FIELD_NUMBER: int

    @property
    def protos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorProto]: ...

    def __init__(self,
        *,
        protos : typing.Optional[typing.Iterable[global___TensorProto]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"protos",b"protos"]) -> None: ...
global___TensorProtos = TensorProtos

class TensorShape(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DIMS_FIELD_NUMBER: int
    DATA_TYPE_FIELD_NUMBER: int
    UNKNOWN_DIMS_FIELD_NUMBER: int
    UNKNOWN_SHAPE_FIELD_NUMBER: int
    NAME_FIELD_NUMBER: int
    dims: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    data_type: global___TensorProto.DataType = ...
    unknown_dims: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    unknown_shape: bool = ...
    name: typing.Text = ...

    def __init__(self,
        *,
        dims : typing.Optional[typing.Iterable[int]] = ...,
        data_type : typing.Optional[global___TensorProto.DataType] = ...,
        unknown_dims : typing.Optional[typing.Iterable[int]] = ...,
        unknown_shape : typing.Optional[bool] = ...,
        name : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"data_type",b"data_type",u"name",b"name",u"unknown_shape",b"unknown_shape"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data_type",b"data_type",u"dims",b"dims",u"name",b"name",u"unknown_dims",b"unknown_dims",u"unknown_shape",b"unknown_shape"]) -> None: ...
global___TensorShape = TensorShape

class TensorShapes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SHAPES_FIELD_NUMBER: int

    @property
    def shapes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorShape]: ...

    def __init__(self,
        *,
        shapes : typing.Optional[typing.Iterable[global___TensorShape]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"shapes",b"shapes"]) -> None: ...
global___TensorShapes = TensorShapes

class TensorBoundShape(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _DimType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DimType], type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNKNOWN = TensorBoundShape.DimType.V(0)
        CONSTANT = TensorBoundShape.DimType.V(1)
        BATCH = TensorBoundShape.DimType.V(2)
        BATCH_OF_FEATURE_MAX = TensorBoundShape.DimType.V(3)
        BATCH_OF_FEATURE_MAX_DEFAULT = TensorBoundShape.DimType.V(4)
        FEATURE_MAX = TensorBoundShape.DimType.V(5)
        FEATURE_MAX_DEFAULT = TensorBoundShape.DimType.V(6)
    class DimType(metaclass=_DimType):
        V = typing.NewType('V', int)
    UNKNOWN = TensorBoundShape.DimType.V(0)
    CONSTANT = TensorBoundShape.DimType.V(1)
    BATCH = TensorBoundShape.DimType.V(2)
    BATCH_OF_FEATURE_MAX = TensorBoundShape.DimType.V(3)
    BATCH_OF_FEATURE_MAX_DEFAULT = TensorBoundShape.DimType.V(4)
    FEATURE_MAX = TensorBoundShape.DimType.V(5)
    FEATURE_MAX_DEFAULT = TensorBoundShape.DimType.V(6)

    SHAPE_FIELD_NUMBER: int
    DIM_TYPE_FIELD_NUMBER: int
    NAME_FIELD_NUMBER: int
    SHAPE_IS_FINAL_FIELD_NUMBER: int
    dim_type: google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___TensorBoundShape.DimType] = ...
    name: typing.Text = ...
    shape_is_final: bool = ...

    @property
    def shape(self) -> global___TensorShape: ...

    def __init__(self,
        *,
        shape : typing.Optional[global___TensorShape] = ...,
        dim_type : typing.Optional[typing.Iterable[global___TensorBoundShape.DimType]] = ...,
        name : typing.Optional[typing.Text] = ...,
        shape_is_final : typing.Optional[bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"name",b"name",u"shape",b"shape",u"shape_is_final",b"shape_is_final"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dim_type",b"dim_type",u"name",b"name",u"shape",b"shape",u"shape_is_final",b"shape_is_final"]) -> None: ...
global___TensorBoundShape = TensorBoundShape

class TensorBoundShapes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SHAPES_FIELD_NUMBER: int
    MAX_BATCH_SIZE_FIELD_NUMBER: int
    MAX_FEATURE_LEN_FIELD_NUMBER: int
    max_batch_size: int = ...
    max_feature_len: int = ...

    @property
    def shapes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorBoundShape]: ...

    def __init__(self,
        *,
        shapes : typing.Optional[typing.Iterable[global___TensorBoundShape]] = ...,
        max_batch_size : typing.Optional[int] = ...,
        max_feature_len : typing.Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"max_batch_size",b"max_batch_size",u"max_feature_len",b"max_feature_len"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"max_batch_size",b"max_batch_size",u"max_feature_len",b"max_feature_len",u"shapes",b"shapes"]) -> None: ...
global___TensorBoundShapes = TensorBoundShapes

class AOTConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_BATCH_SIZE_FIELD_NUMBER: int
    MAX_SEQ_SIZE_FIELD_NUMBER: int
    IN_BATCH_BROADCAST_FIELD_NUMBER: int
    ONNXIFI_BLACKLIST_OPS_FIELD_NUMBER: int
    ONNXIFI_MIN_OPS_FIELD_NUMBER: int
    max_batch_size: int = ...
    max_seq_size: int = ...
    in_batch_broadcast: bool = ...
    onnxifi_blacklist_ops: typing.Text = ...
    onnxifi_min_ops: int = ...

    def __init__(self,
        *,
        max_batch_size : typing.Optional[int] = ...,
        max_seq_size : typing.Optional[int] = ...,
        in_batch_broadcast : typing.Optional[bool] = ...,
        onnxifi_blacklist_ops : typing.Optional[typing.Text] = ...,
        onnxifi_min_ops : typing.Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"in_batch_broadcast",b"in_batch_broadcast",u"max_batch_size",b"max_batch_size",u"max_seq_size",b"max_seq_size",u"onnxifi_blacklist_ops",b"onnxifi_blacklist_ops",u"onnxifi_min_ops",b"onnxifi_min_ops"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"in_batch_broadcast",b"in_batch_broadcast",u"max_batch_size",b"max_batch_size",u"max_seq_size",b"max_seq_size",u"onnxifi_blacklist_ops",b"onnxifi_blacklist_ops",u"onnxifi_min_ops",b"onnxifi_min_ops"]) -> None: ...
global___AOTConfig = AOTConfig

class Argument(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: int
    F_FIELD_NUMBER: int
    I_FIELD_NUMBER: int
    S_FIELD_NUMBER: int
    T_FIELD_NUMBER: int
    N_FIELD_NUMBER: int
    FLOATS_FIELD_NUMBER: int
    INTS_FIELD_NUMBER: int
    STRINGS_FIELD_NUMBER: int
    TENSORS_FIELD_NUMBER: int
    NETS_FIELD_NUMBER: int
    QTENSORS_FIELD_NUMBER: int
    name: typing.Text = ...
    f: float = ...
    i: int = ...
    s: bytes = ...
    floats: google.protobuf.internal.containers.RepeatedScalarFieldContainer[float] = ...
    ints: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    strings: google.protobuf.internal.containers.RepeatedScalarFieldContainer[bytes] = ...

    @property
    def t(self) -> global___TensorProto: ...

    @property
    def n(self) -> global___NetDef: ...

    @property
    def tensors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorProto]: ...

    @property
    def nets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetDef]: ...

    @property
    def qtensors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QTensorProto]: ...

    def __init__(self,
        *,
        name : typing.Optional[typing.Text] = ...,
        f : typing.Optional[float] = ...,
        i : typing.Optional[int] = ...,
        s : typing.Optional[bytes] = ...,
        t : typing.Optional[global___TensorProto] = ...,
        n : typing.Optional[global___NetDef] = ...,
        floats : typing.Optional[typing.Iterable[float]] = ...,
        ints : typing.Optional[typing.Iterable[int]] = ...,
        strings : typing.Optional[typing.Iterable[bytes]] = ...,
        tensors : typing.Optional[typing.Iterable[global___TensorProto]] = ...,
        nets : typing.Optional[typing.Iterable[global___NetDef]] = ...,
        qtensors : typing.Optional[typing.Iterable[global___QTensorProto]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"f",b"f",u"i",b"i",u"n",b"n",u"name",b"name",u"s",b"s",u"t",b"t"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"f",b"f",u"floats",b"floats",u"i",b"i",u"ints",b"ints",u"n",b"n",u"name",b"name",u"nets",b"nets",u"qtensors",b"qtensors",u"s",b"s",u"strings",b"strings",u"t",b"t",u"tensors",b"tensors"]) -> None: ...
global___Argument = Argument

class DeviceOption(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_TYPE_FIELD_NUMBER: int
    DEVICE_ID_FIELD_NUMBER: int
    RANDOM_SEED_FIELD_NUMBER: int
    NODE_NAME_FIELD_NUMBER: int
    NUMA_NODE_ID_FIELD_NUMBER: int
    EXTRA_INFO_FIELD_NUMBER: int
    device_type: int = ...
    device_id: int = ...
    random_seed: int = ...
    node_name: typing.Text = ...
    numa_node_id: int = ...
    extra_info: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    def __init__(self,
        *,
        device_type : typing.Optional[int] = ...,
        device_id : typing.Optional[int] = ...,
        random_seed : typing.Optional[int] = ...,
        node_name : typing.Optional[typing.Text] = ...,
        numa_node_id : typing.Optional[int] = ...,
        extra_info : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_id",b"device_id",u"device_type",b"device_type",u"node_name",b"node_name",u"numa_node_id",b"numa_node_id",u"random_seed",b"random_seed"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_id",b"device_id",u"device_type",b"device_type",u"extra_info",b"extra_info",u"node_name",b"node_name",u"numa_node_id",b"numa_node_id",u"random_seed",b"random_seed"]) -> None: ...
global___DeviceOption = DeviceOption

class OperatorDef(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INPUT_FIELD_NUMBER: int
    OUTPUT_FIELD_NUMBER: int
    NAME_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    ARG_FIELD_NUMBER: int
    DEVICE_OPTION_FIELD_NUMBER: int
    ENGINE_FIELD_NUMBER: int
    CONTROL_INPUT_FIELD_NUMBER: int
    IS_GRADIENT_OP_FIELD_NUMBER: int
    DEBUG_INFO_FIELD_NUMBER: int
    DOMAIN_FIELD_NUMBER: int
    OP_VERSION_FIELD_NUMBER: int
    input: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
    output: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
    name: typing.Text = ...
    type: typing.Text = ...
    engine: typing.Text = ...
    control_input: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
    is_gradient_op: bool = ...
    debug_info: typing.Text = ...
    domain: typing.Text = ...
    op_version: int = ...

    @property
    def arg(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Argument]: ...

    @property
    def device_option(self) -> global___DeviceOption: ...

    def __init__(self,
        *,
        input : typing.Optional[typing.Iterable[typing.Text]] = ...,
        output : typing.Optional[typing.Iterable[typing.Text]] = ...,
        name : typing.Optional[typing.Text] = ...,
        type : typing.Optional[typing.Text] = ...,
        arg : typing.Optional[typing.Iterable[global___Argument]] = ...,
        device_option : typing.Optional[global___DeviceOption] = ...,
        engine : typing.Optional[typing.Text] = ...,
        control_input : typing.Optional[typing.Iterable[typing.Text]] = ...,
        is_gradient_op : typing.Optional[bool] = ...,
        debug_info : typing.Optional[typing.Text] = ...,
        domain : typing.Optional[typing.Text] = ...,
        op_version : typing.Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"debug_info",b"debug_info",u"device_option",b"device_option",u"domain",b"domain",u"engine",b"engine",u"is_gradient_op",b"is_gradient_op",u"name",b"name",u"op_version",b"op_version",u"type",b"type"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"arg",b"arg",u"control_input",b"control_input",u"debug_info",b"debug_info",u"device_option",b"device_option",u"domain",b"domain",u"engine",b"engine",u"input",b"input",u"is_gradient_op",b"is_gradient_op",u"name",b"name",u"op_version",b"op_version",u"output",b"output",u"type",b"type"]) -> None: ...
global___OperatorDef = OperatorDef

class MapFieldEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: int
    VAL_FIELD_NUMBER: int
    key: typing.Text = ...
    val: typing.Text = ...

    def __init__(self,
        *,
        key : typing.Optional[typing.Text] = ...,
        val : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"key",b"key",u"val",b"val"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"val",b"val"]) -> None: ...
global___MapFieldEntry = MapFieldEntry

class BackendOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BACKEND_NAME_FIELD_NUMBER: int
    OPTION_FIELD_NUMBER: int
    backend_name: typing.Text = ...

    @property
    def option(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MapFieldEntry]: ...

    def __init__(self,
        *,
        backend_name : typing.Optional[typing.Text] = ...,
        option : typing.Optional[typing.Iterable[global___MapFieldEntry]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"backend_name",b"backend_name"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"backend_name",b"backend_name",u"option",b"option"]) -> None: ...
global___BackendOptions = BackendOptions

class PartitionInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: int
    DEVICE_ID_FIELD_NUMBER: int
    EXTRA_INFO_FIELD_NUMBER: int
    BACKEND_OPTIONS_FIELD_NUMBER: int
    name: typing.Text = ...
    device_id: google.protobuf.internal.containers.RepeatedScalarFieldContainer[int] = ...
    extra_info: typing.Text = ...

    @property
    def backend_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackendOptions]: ...

    def __init__(self,
        *,
        name : typing.Optional[typing.Text] = ...,
        device_id : typing.Optional[typing.Iterable[int]] = ...,
        extra_info : typing.Optional[typing.Text] = ...,
        backend_options : typing.Optional[typing.Iterable[global___BackendOptions]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"extra_info",b"extra_info",u"name",b"name"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"backend_options",b"backend_options",u"device_id",b"device_id",u"extra_info",b"extra_info",u"name",b"name"]) -> None: ...
global___PartitionInfo = PartitionInfo

class NetDef(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: int
    OP_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    NUM_WORKERS_FIELD_NUMBER: int
    DEVICE_OPTION_FIELD_NUMBER: int
    ARG_FIELD_NUMBER: int
    EXTERNAL_INPUT_FIELD_NUMBER: int
    EXTERNAL_OUTPUT_FIELD_NUMBER: int
    PARTITION_INFO_FIELD_NUMBER: int
    name: typing.Text = ...
    type: typing.Text = ...
    num_workers: int = ...
    external_input: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
    external_output: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    @property
    def op(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OperatorDef]: ...

    @property
    def device_option(self) -> global___DeviceOption: ...

    @property
    def arg(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Argument]: ...

    @property
    def partition_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PartitionInfo]: ...

    def __init__(self,
        *,
        name : typing.Optional[typing.Text] = ...,
        op : typing.Optional[typing.Iterable[global___OperatorDef]] = ...,
        type : typing.Optional[typing.Text] = ...,
        num_workers : typing.Optional[int] = ...,
        device_option : typing.Optional[global___DeviceOption] = ...,
        arg : typing.Optional[typing.Iterable[global___Argument]] = ...,
        external_input : typing.Optional[typing.Iterable[typing.Text]] = ...,
        external_output : typing.Optional[typing.Iterable[typing.Text]] = ...,
        partition_info : typing.Optional[typing.Iterable[global___PartitionInfo]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_option",b"device_option",u"name",b"name",u"num_workers",b"num_workers",u"type",b"type"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"arg",b"arg",u"device_option",b"device_option",u"external_input",b"external_input",u"external_output",b"external_output",u"name",b"name",u"num_workers",b"num_workers",u"op",b"op",u"partition_info",b"partition_info",u"type",b"type"]) -> None: ...
global___NetDef = NetDef

class ExecutionStep(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: int
    SUBSTEP_FIELD_NUMBER: int
    NETWORK_FIELD_NUMBER: int
    NUM_ITER_FIELD_NUMBER: int
    CRITERIA_NETWORK_FIELD_NUMBER: int
    REPORT_NET_FIELD_NUMBER: int
    REPORT_INTERVAL_FIELD_NUMBER: int
    RUN_EVERY_MS_FIELD_NUMBER: int
    CONCURRENT_SUBSTEPS_FIELD_NUMBER: int
    SHOULD_STOP_BLOB_FIELD_NUMBER: int
    ONLY_ONCE_FIELD_NUMBER: int
    CREATE_WORKSPACE_FIELD_NUMBER: int
    NUM_CONCURRENT_INSTANCES_FIELD_NUMBER: int
    name: typing.Text = ...
    network: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
    num_iter: int = ...
    criteria_network: typing.Text = ...
    report_net: typing.Text = ...
    report_interval: int = ...
    run_every_ms: int = ...
    concurrent_substeps: bool = ...
    should_stop_blob: typing.Text = ...
    only_once: bool = ...
    create_workspace: bool = ...
    num_concurrent_instances: int = ...

    @property
    def substep(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExecutionStep]: ...

    def __init__(self,
        *,
        name : typing.Optional[typing.Text] = ...,
        substep : typing.Optional[typing.Iterable[global___ExecutionStep]] = ...,
        network : typing.Optional[typing.Iterable[typing.Text]] = ...,
        num_iter : typing.Optional[int] = ...,
        criteria_network : typing.Optional[typing.Text] = ...,
        report_net : typing.Optional[typing.Text] = ...,
        report_interval : typing.Optional[int] = ...,
        run_every_ms : typing.Optional[int] = ...,
        concurrent_substeps : typing.Optional[bool] = ...,
        should_stop_blob : typing.Optional[typing.Text] = ...,
        only_once : typing.Optional[bool] = ...,
        create_workspace : typing.Optional[bool] = ...,
        num_concurrent_instances : typing.Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"concurrent_substeps",b"concurrent_substeps",u"create_workspace",b"create_workspace",u"criteria_network",b"criteria_network",u"name",b"name",u"num_concurrent_instances",b"num_concurrent_instances",u"num_iter",b"num_iter",u"only_once",b"only_once",u"report_interval",b"report_interval",u"report_net",b"report_net",u"run_every_ms",b"run_every_ms",u"should_stop_blob",b"should_stop_blob"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"concurrent_substeps",b"concurrent_substeps",u"create_workspace",b"create_workspace",u"criteria_network",b"criteria_network",u"name",b"name",u"network",b"network",u"num_concurrent_instances",b"num_concurrent_instances",u"num_iter",b"num_iter",u"only_once",b"only_once",u"report_interval",b"report_interval",u"report_net",b"report_net",u"run_every_ms",b"run_every_ms",u"should_stop_blob",b"should_stop_blob",u"substep",b"substep"]) -> None: ...
global___ExecutionStep = ExecutionStep

class PlanDef(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: int
    NETWORK_FIELD_NUMBER: int
    EXECUTION_STEP_FIELD_NUMBER: int
    name: typing.Text = ...

    @property
    def network(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetDef]: ...

    @property
    def execution_step(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExecutionStep]: ...

    def __init__(self,
        *,
        name : typing.Optional[typing.Text] = ...,
        network : typing.Optional[typing.Iterable[global___NetDef]] = ...,
        execution_step : typing.Optional[typing.Iterable[global___ExecutionStep]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"name",b"name"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"execution_step",b"execution_step",u"name",b"name",u"network",b"network"]) -> None: ...
global___PlanDef = PlanDef

class BlobProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    TENSOR_FIELD_NUMBER: int
    CONTENT_FIELD_NUMBER: int
    QTENSOR_FIELD_NUMBER: int
    CONTENT_NUM_CHUNKS_FIELD_NUMBER: int
    CONTENT_CHUNK_ID_FIELD_NUMBER: int
    name: typing.Text = ...
    type: typing.Text = ...
    content: bytes = ...
    content_num_chunks: int = ...
    content_chunk_id: int = ...

    @property
    def tensor(self) -> global___TensorProto: ...

    @property
    def qtensor(self) -> global___QTensorProto: ...

    def __init__(self,
        *,
        name : typing.Optional[typing.Text] = ...,
        type : typing.Optional[typing.Text] = ...,
        tensor : typing.Optional[global___TensorProto] = ...,
        content : typing.Optional[bytes] = ...,
        qtensor : typing.Optional[global___QTensorProto] = ...,
        content_num_chunks : typing.Optional[int] = ...,
        content_chunk_id : typing.Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"content",b"content",u"content_chunk_id",b"content_chunk_id",u"content_num_chunks",b"content_num_chunks",u"name",b"name",u"qtensor",b"qtensor",u"tensor",b"tensor",u"type",b"type"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"content",b"content",u"content_chunk_id",b"content_chunk_id",u"content_num_chunks",b"content_num_chunks",u"name",b"name",u"qtensor",b"qtensor",u"tensor",b"tensor",u"type",b"type"]) -> None: ...
global___BlobProto = BlobProto

class DBReaderProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: int
    SOURCE_FIELD_NUMBER: int
    DB_TYPE_FIELD_NUMBER: int
    KEY_FIELD_NUMBER: int
    name: typing.Text = ...
    source: typing.Text = ...
    db_type: typing.Text = ...
    key: typing.Text = ...

    def __init__(self,
        *,
        name : typing.Optional[typing.Text] = ...,
        source : typing.Optional[typing.Text] = ...,
        db_type : typing.Optional[typing.Text] = ...,
        key : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"db_type",b"db_type",u"key",b"key",u"name",b"name",u"source",b"source"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"db_type",b"db_type",u"key",b"key",u"name",b"name",u"source",b"source"]) -> None: ...
global___DBReaderProto = DBReaderProto

class BlobSerializationOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FloatFormat(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FloatFormat], type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        FLOAT_DEFAULT = BlobSerializationOptions.FloatFormat.V(0)
        FLOAT_PROTOBUF = BlobSerializationOptions.FloatFormat.V(1)
        FLOAT_BFLOAT16 = BlobSerializationOptions.FloatFormat.V(2)
    class FloatFormat(metaclass=_FloatFormat):
        V = typing.NewType('V', int)
    FLOAT_DEFAULT = BlobSerializationOptions.FloatFormat.V(0)
    FLOAT_PROTOBUF = BlobSerializationOptions.FloatFormat.V(1)
    FLOAT_BFLOAT16 = BlobSerializationOptions.FloatFormat.V(2)

    BLOB_NAME_REGEX_FIELD_NUMBER: int
    CHUNK_SIZE_FIELD_NUMBER: int
    FLOAT_FORMAT_FIELD_NUMBER: int
    blob_name_regex: typing.Text = ...
    chunk_size: int = ...
    float_format: global___BlobSerializationOptions.FloatFormat = ...

    def __init__(self,
        *,
        blob_name_regex : typing.Optional[typing.Text] = ...,
        chunk_size : typing.Optional[int] = ...,
        float_format : typing.Optional[global___BlobSerializationOptions.FloatFormat] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"blob_name_regex",b"blob_name_regex",u"chunk_size",b"chunk_size",u"float_format",b"float_format"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"blob_name_regex",b"blob_name_regex",u"chunk_size",b"chunk_size",u"float_format",b"float_format"]) -> None: ...
global___BlobSerializationOptions = BlobSerializationOptions

class SerializationOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OPTIONS_FIELD_NUMBER: int

    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BlobSerializationOptions]: ...

    def __init__(self,
        *,
        options : typing.Optional[typing.Iterable[global___BlobSerializationOptions]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"options",b"options"]) -> None: ...
global___SerializationOptions = SerializationOptions

DeviceType = int

# These are freedom-patched into caffe2_pb2 in caffe2/proto/__init__.py
CPU: int = DeviceType.PROTO_CPU
CUDA: int = DeviceType.PROTO_CUDA
MKLDNN: int = DeviceType.PROTO_MKLDNN
OPENGL: int = DeviceType.PROTO_OPENGL
OPENCL: int = DeviceType.PROTO_OPENCL
IDEEP: int = DeviceType.PROTO_IDEEP
HIP: int = DeviceType.PROTO_HIP
COMPILE_TIME_MAX_DEVICE_TYPES: int = DeviceType.PROTO_COMPILE_TIME_MAX_DEVICE_TYPES
