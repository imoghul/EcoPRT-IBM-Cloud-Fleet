// Auto-generated. Do not edit!

// (in-package sensors.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class GPSData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.time = null;
      this.lat = null;
      this.long = null;
    }
    else {
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('lat')) {
        this.lat = initObj.lat
      }
      else {
        this.lat = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('long')) {
        this.long = initObj.long
      }
      else {
        this.long = new std_msgs.msg.Float64();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GPSData
    // Serialize message field [time]
    bufferOffset = std_msgs.msg.String.serialize(obj.time, buffer, bufferOffset);
    // Serialize message field [lat]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.lat, buffer, bufferOffset);
    // Serialize message field [long]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.long, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GPSData
    let len;
    let data = new GPSData(null);
    // Deserialize message field [time]
    data.time = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [lat]
    data.lat = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [long]
    data.long = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.String.getMessageSize(object.time);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensors/GPSData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '127d8146da420293b29d277551a452ba';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/String time
    std_msgs/Float64 lat
    std_msgs/Float64 long
    
    ================================================================================
    MSG: std_msgs/String
    string data
    
    ================================================================================
    MSG: std_msgs/Float64
    float64 data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GPSData(null);
    if (msg.time !== undefined) {
      resolved.time = std_msgs.msg.String.Resolve(msg.time)
    }
    else {
      resolved.time = new std_msgs.msg.String()
    }

    if (msg.lat !== undefined) {
      resolved.lat = std_msgs.msg.Float64.Resolve(msg.lat)
    }
    else {
      resolved.lat = new std_msgs.msg.Float64()
    }

    if (msg.long !== undefined) {
      resolved.long = std_msgs.msg.Float64.Resolve(msg.long)
    }
    else {
      resolved.long = new std_msgs.msg.Float64()
    }

    return resolved;
    }
};

module.exports = GPSData;
