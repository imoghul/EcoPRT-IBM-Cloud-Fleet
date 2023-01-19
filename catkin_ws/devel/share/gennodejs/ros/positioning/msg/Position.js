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
      this.latitude = null;
      this.longitude = null;
      this.altitude = null;
      this.imu = null;
    }
    else {
      if (initObj.hasOwnProperty('latitude')) {
        this.latitude = initObj.latitude
      }
      else {
        this.latitude = 0.0;
      }
      if (initObj.hasOwnProperty('longitude')) {
        this.longitude = initObj.longitude
      }
      else {
        this.longitude = 0.0;
      }
      if (initObj.hasOwnProperty('altitude')) {
        this.altitude = initObj.altitude
      }
      else {
        this.altitude = 0.0;
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
    // Serialize message field [latitude]
    bufferOffset = _serializer.float64(obj.latitude, buffer, bufferOffset);
    // Serialize message field [longitude]
    bufferOffset = _serializer.float64(obj.longitude, buffer, bufferOffset);
    // Serialize message field [altitude]
    bufferOffset = _serializer.float64(obj.altitude, buffer, bufferOffset);
    // Serialize message field [imu]
    bufferOffset = sensors.msg.IMUData.serialize(obj.imu, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Position
    let len;
    let data = new Position(null);
    // Deserialize message field [latitude]
    data.latitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [longitude]
    data.longitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [altitude]
    data.altitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [imu]
    data.imu = sensors.msg.IMUData.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 200;
  }

  static datatype() {
    // Returns string type for a message object
    return 'positioning/Position';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '26972fc25ce21b0631b32a2b006a1bf4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 latitude
    float64 longitude
    float64 altitude
    sensors/IMUData imu
    
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
    if (msg.latitude !== undefined) {
      resolved.latitude = msg.latitude;
    }
    else {
      resolved.latitude = 0.0
    }

    if (msg.longitude !== undefined) {
      resolved.longitude = msg.longitude;
    }
    else {
      resolved.longitude = 0.0
    }

    if (msg.altitude !== undefined) {
      resolved.altitude = msg.altitude;
    }
    else {
      resolved.altitude = 0.0
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
