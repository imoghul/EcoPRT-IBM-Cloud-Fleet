// Auto-generated. Do not edit!

// (in-package positioning.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensors = _finder('sensors');

//-----------------------------------------------------------

class Position {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.gps = null;
      this.imu = null;
    }
    else {
      if (initObj.hasOwnProperty('gps')) {
        this.gps = initObj.gps
      }
      else {
        this.gps = new sensors.msg.GPSData();
      }
      if (initObj.hasOwnProperty('imu')) {
        this.imu = initObj.imu
      }
      else {
        this.imu = new sensors.msg.IMUData();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Position
    // Serialize message field [gps]
    bufferOffset = sensors.msg.GPSData.serialize(obj.gps, buffer, bufferOffset);
    // Serialize message field [imu]
    bufferOffset = sensors.msg.IMUData.serialize(obj.imu, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Position
    let len;
    let data = new Position(null);
    // Deserialize message field [gps]
    data.gps = sensors.msg.GPSData.deserialize(buffer, bufferOffset);
    // Deserialize message field [imu]
    data.imu = sensors.msg.IMUData.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensors.msg.GPSData.getMessageSize(object.gps);
    return length + 176;
  }

  static datatype() {
    // Returns string type for a message object
    return 'positioning/Position';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6fb7f457c11907847ca6763dd0bb7aad';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    sensors/GPSData gps
    sensors/IMUData imu
    
    ================================================================================
    MSG: sensors/GPSData
    string time
    float64 lat
    float64 long
    
    ================================================================================
    MSG: sensors/IMUData
    float64 AxCalib
    float64 AyCalib
    float64 AzCalib
    float64 Ax
    float64 Ay
    float64 Az
    float64 AxRaw
    float64 AyRaw
    float64 AzRaw
    float64 Vx
    float64 Vy
    float64 Vz
    float64 Gx
    float64 Gy
    float64 Gz
    float64 GxCalib
    float64 GyCalib
    float64 GzCalib
    float64 GxRaw
    float64 GyRaw
    float64 GzRaw
    float64 currTime
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Position(null);
    if (msg.gps !== undefined) {
      resolved.gps = sensors.msg.GPSData.Resolve(msg.gps)
    }
    else {
      resolved.gps = new sensors.msg.GPSData()
    }

    if (msg.imu !== undefined) {
      resolved.imu = sensors.msg.IMUData.Resolve(msg.imu)
    }
    else {
      resolved.imu = new sensors.msg.IMUData()
    }

    return resolved;
    }
};

module.exports = Position;
