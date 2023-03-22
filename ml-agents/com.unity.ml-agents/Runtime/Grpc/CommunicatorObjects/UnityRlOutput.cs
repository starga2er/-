// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: mlagents_envs/communicator_objects/unity_rl_output.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Unity.MLAgents.CommunicatorObjects {

  /// <summary>Holder for reflection information generated from mlagents_envs/communicator_objects/unity_rl_output.proto</summary>
  internal static partial class UnityRlOutputReflection {

    #region Descriptor
    /// <summary>File descriptor for mlagents_envs/communicator_objects/unity_rl_output.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static UnityRlOutputReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CjhtbGFnZW50c19lbnZzL2NvbW11bmljYXRvcl9vYmplY3RzL3VuaXR5X3Js",
            "X291dHB1dC5wcm90bxIUY29tbXVuaWNhdG9yX29iamVjdHMaM21sYWdlbnRz",
            "X2VudnMvY29tbXVuaWNhdG9yX29iamVjdHMvYWdlbnRfaW5mby5wcm90byK5",
            "AgoSVW5pdHlSTE91dHB1dFByb3RvEkwKCmFnZW50SW5mb3MYAiADKAsyOC5j",
            "b21tdW5pY2F0b3Jfb2JqZWN0cy5Vbml0eVJMT3V0cHV0UHJvdG8uQWdlbnRJ",
            "bmZvc0VudHJ5EhQKDHNpZGVfY2hhbm5lbBgDIAEoDBpJChJMaXN0QWdlbnRJ",
            "bmZvUHJvdG8SMwoFdmFsdWUYASADKAsyJC5jb21tdW5pY2F0b3Jfb2JqZWN0",
            "cy5BZ2VudEluZm9Qcm90bxpuCg9BZ2VudEluZm9zRW50cnkSCwoDa2V5GAEg",
            "ASgJEkoKBXZhbHVlGAIgASgLMjsuY29tbXVuaWNhdG9yX29iamVjdHMuVW5p",
            "dHlSTE91dHB1dFByb3RvLkxpc3RBZ2VudEluZm9Qcm90bzoCOAFKBAgBEAJC",
            "JaoCIlVuaXR5Lk1MQWdlbnRzLkNvbW11bmljYXRvck9iamVjdHNiBnByb3Rv",
            "Mw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Unity.MLAgents.CommunicatorObjects.AgentInfoReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto), global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Parser, new[]{ "AgentInfos", "SideChannel" }, null, null, new pbr::GeneratedClrTypeInfo[] { new pbr::GeneratedClrTypeInfo(typeof(global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto), global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto.Parser, new[]{ "Value" }, null, null, null),
            null, })
          }));
    }
    #endregion

  }
  #region Messages
  internal sealed partial class UnityRLOutputProto : pb::IMessage<UnityRLOutputProto> {
    private static readonly pb::MessageParser<UnityRLOutputProto> _parser = new pb::MessageParser<UnityRLOutputProto>(() => new UnityRLOutputProto());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<UnityRLOutputProto> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Unity.MLAgents.CommunicatorObjects.UnityRlOutputReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public UnityRLOutputProto() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public UnityRLOutputProto(UnityRLOutputProto other) : this() {
      agentInfos_ = other.agentInfos_.Clone();
      sideChannel_ = other.sideChannel_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public UnityRLOutputProto Clone() {
      return new UnityRLOutputProto(this);
    }

    /// <summary>Field number for the "agentInfos" field.</summary>
    public const int AgentInfosFieldNumber = 2;
    private static readonly pbc::MapField<string, global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto>.Codec _map_agentInfos_codec
        = new pbc::MapField<string, global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto>.Codec(pb::FieldCodec.ForString(10), pb::FieldCodec.ForMessage(18, global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto.Parser), 18);
    private readonly pbc::MapField<string, global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto> agentInfos_ = new pbc::MapField<string, global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pbc::MapField<string, global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Types.ListAgentInfoProto> AgentInfos {
      get { return agentInfos_; }
    }

    /// <summary>Field number for the "side_channel" field.</summary>
    public const int SideChannelFieldNumber = 3;
    private pb::ByteString sideChannel_ = pb::ByteString.Empty;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pb::ByteString SideChannel {
      get { return sideChannel_; }
      set {
        sideChannel_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as UnityRLOutputProto);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(UnityRLOutputProto other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!AgentInfos.Equals(other.AgentInfos)) return false;
      if (SideChannel != other.SideChannel) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= AgentInfos.GetHashCode();
      if (SideChannel.Length != 0) hash ^= SideChannel.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      agentInfos_.WriteTo(output, _map_agentInfos_codec);
      if (SideChannel.Length != 0) {
        output.WriteRawTag(26);
        output.WriteBytes(SideChannel);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      size += agentInfos_.CalculateSize(_map_agentInfos_codec);
      if (SideChannel.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeBytesSize(SideChannel);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(UnityRLOutputProto other) {
      if (other == null) {
        return;
      }
      agentInfos_.Add(other.agentInfos_);
      if (other.SideChannel.Length != 0) {
        SideChannel = other.SideChannel;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 18: {
            agentInfos_.AddEntriesFrom(input, _map_agentInfos_codec);
            break;
          }
          case 26: {
            SideChannel = input.ReadBytes();
            break;
          }
        }
      }
    }

    #region Nested types
    /// <summary>Container for nested types declared in the UnityRLOutputProto message type.</summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static partial class Types {
      internal sealed partial class ListAgentInfoProto : pb::IMessage<ListAgentInfoProto> {
        private static readonly pb::MessageParser<ListAgentInfoProto> _parser = new pb::MessageParser<ListAgentInfoProto>(() => new ListAgentInfoProto());
        private pb::UnknownFieldSet _unknownFields;
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public static pb::MessageParser<ListAgentInfoProto> Parser { get { return _parser; } }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public static pbr::MessageDescriptor Descriptor {
          get { return global::Unity.MLAgents.CommunicatorObjects.UnityRLOutputProto.Descriptor.NestedTypes[0]; }
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        pbr::MessageDescriptor pb::IMessage.Descriptor {
          get { return Descriptor; }
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public ListAgentInfoProto() {
          OnConstruction();
        }

        partial void OnConstruction();

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public ListAgentInfoProto(ListAgentInfoProto other) : this() {
          value_ = other.value_.Clone();
          _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public ListAgentInfoProto Clone() {
          return new ListAgentInfoProto(this);
        }

        /// <summary>Field number for the "value" field.</summary>
        public const int ValueFieldNumber = 1;
        private static readonly pb::FieldCodec<global::Unity.MLAgents.CommunicatorObjects.AgentInfoProto> _repeated_value_codec
            = pb::FieldCodec.ForMessage(10, global::Unity.MLAgents.CommunicatorObjects.AgentInfoProto.Parser);
        private readonly pbc::RepeatedField<global::Unity.MLAgents.CommunicatorObjects.AgentInfoProto> value_ = new pbc::RepeatedField<global::Unity.MLAgents.CommunicatorObjects.AgentInfoProto>();
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public pbc::RepeatedField<global::Unity.MLAgents.CommunicatorObjects.AgentInfoProto> Value {
          get { return value_; }
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public override bool Equals(object other) {
          return Equals(other as ListAgentInfoProto);
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public bool Equals(ListAgentInfoProto other) {
          if (ReferenceEquals(other, null)) {
            return false;
          }
          if (ReferenceEquals(other, this)) {
            return true;
          }
          if(!value_.Equals(other.value_)) return false;
          return Equals(_unknownFields, other._unknownFields);
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public override int GetHashCode() {
          int hash = 1;
          hash ^= value_.GetHashCode();
          if (_unknownFields != null) {
            hash ^= _unknownFields.GetHashCode();
          }
          return hash;
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public override string ToString() {
          return pb::JsonFormatter.ToDiagnosticString(this);
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public void WriteTo(pb::CodedOutputStream output) {
          value_.WriteTo(output, _repeated_value_codec);
          if (_unknownFields != null) {
            _unknownFields.WriteTo(output);
          }
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public int CalculateSize() {
          int size = 0;
          size += value_.CalculateSize(_repeated_value_codec);
          if (_unknownFields != null) {
            size += _unknownFields.CalculateSize();
          }
          return size;
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public void MergeFrom(ListAgentInfoProto other) {
          if (other == null) {
            return;
          }
          value_.Add(other.value_);
          _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
        }

        [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
        public void MergeFrom(pb::CodedInputStream input) {
          uint tag;
          while ((tag = input.ReadTag()) != 0) {
            switch(tag) {
              default:
                _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
                break;
              case 10: {
                value_.AddEntriesFrom(input, _repeated_value_codec);
                break;
              }
            }
          }
        }

      }

    }
    #endregion

  }

  #endregion

}

#endregion Designer generated code
