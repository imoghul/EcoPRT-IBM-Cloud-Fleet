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

class IMUData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.AxCalib = null;
      this.AyCalib = null;
      this.AzCalib = null;
      this.Ax = null;
      this.Ay = null;
      this.Az = null;
      this.AxRaw = null;
      this.AyRaw = null;
      this.AzRaw = null;
      this.Vx = null;
      this.Vy = null;
      this.Vz = null;
      this.Gx = null;
      this.Gy = null;
      this.Gz = null;
      this.currTime = null;
    }
    else {
      if (initObj.hasOwnProperty('AxCalib')) {
        this.AxCalib = initObj.AxCalib
      }
      else {
        this.AxCalib = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('AyCalib')) {
        this.AyCalib = initObj.AyCalib
      }
      else {
        this.AyCalib = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('AzCalib')) {
        this.AzCalib = initObj.AzCalib
      }
      else {
        this.AzCalib = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Ax')) {
        this.Ax = initObj.Ax
      }
      else {
        this.Ax = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Ay')) {
        this.Ay = initObj.Ay
      }
      else {
        this.Ay = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Az')) {
        this.Az = initObj.Az
      }
      else {
        this.Az = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('AxRaw')) {
        this.AxRaw = initObj.AxRaw
      }
      else {
        this.AxRaw = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('AyRaw')) {
        this.AyRaw = initObj.AyRaw
      }
      else {
        this.AyRaw = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('AzRaw')) {
        this.AzRaw = initObj.AzRaw
      }
      else {
        this.AzRaw = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Vx')) {
        this.Vx = initObj.Vx
      }
      else {
        this.Vx = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Vy')) {
        this.Vy = initObj.Vy
      }
      else {
        this.Vy = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Vz')) {
        this.Vz = initObj.Vz
      }
      else {
        this.Vz = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Gx')) {
        this.Gx = initObj.Gx
      }
      else {
        this.Gx = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Gy')) {
        this.Gy = initObj.Gy
      }
      else {
        this.Gy = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('Gz')) {
        this.Gz = initObj.Gz
      }
      else {
        this.Gz = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('currTime')) {
        this.currTime = initObj.currTime
      }
      else {
        this.currTime = new std_msgs.msg.Float64();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IMUData
    // Serialize message field [AxCalib]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.AxCalib, buffer, bufferOffset);
    // Serialize message field [AyCalib]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.AyCalib, buffer, bufferOffset);
    // Serialize message field [AzCalib]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.AzCalib, buffer, bufferOffset);
    // Serialize message field [Ax]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Ax, buffer, bufferOffset);
    // Serialize message field [Ay]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Ay, buffer, bufferOffset);
    // Serialize message field [Az]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Az, buffer, bufferOffset);
    // Serialize message field [AxRaw]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.AxRaw, buffer, bufferOffset);
    // Serialize message field [AyRaw]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.AyRaw, buffer, bufferOffset);
    // Serialize message field [AzRaw]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.AzRaw, buffer, bufferOffset);
    // Serialize message field [Vx]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Vx, buffer, bufferOffset);
    // Serialize message field [Vy]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Vy, buffer, bufferOffset);
    // Serialize message field [Vz]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Vz, buffer, bufferOffset);
    // Serialize message field [Gx]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Gx, buffer, bufferOffset);
    // Serialize message field [Gy]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Gy, buffer, bufferOffset);
    // Serialize message field [Gz]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.Gz, buffer, bufferOffset);
    // Serialize message field [currTime]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.currTime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IMUData
    let len;
    let data = new IMUData(null);
    // Deserialize message field [AxCalib]
    data.AxCalib = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [AyCalib]
    data.AyCalib = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [AzCalib]
    data.AzCalib = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Ax]
    data.Ax = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Ay]
    data.Ay = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Az]
    data.Az = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [AxRaw]
    data.AxRaw = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [AyRaw]
    data.AyRaw = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [AzRaw]
    data.AzRaw = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Vx]
    data.Vx = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Vy]
    data.Vy = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Vz]
    data.Vz = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Gx]
    data.Gx = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Gy]
    data.Gy = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [Gz]
    data.Gz = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [currTime]
    data.currTime = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 128;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensors/IMUData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e854ee703c7cc2b23f6a5df92872cf41';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Float64 AxCalib
    std_msgs/Float64 AyCalib
    std_msgs/Float64 AzCalib
    std_msgs/Float64 Ax
    std_msgs/Float64 Ay
    std_msgs/Float64 Az
    std_msgs/Float64 AxRaw
    std_msgs/Float64 AyRaw
    std_msgs/Float64 AzRaw
    std_msgs/Float64 Vx
    std_msgs/Float64 Vy
    std_msgs/Float64 Vz
    std_msgs/Float64 Gx
    std_msgs/Float64 Gy
    std_msgs/Float64 Gz
    std_msgs/Float64 currTime
    
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
    const resolved = new IMUData(null);
    if (msg.AxCalib !== undefined) {
      resolved.AxCalib = std_msgs.msg.Float64.Resolve(msg.AxCalib)
    }
    else {
      resolved.AxCalib = new std_msgs.msg.Float64()
    }

    if (msg.AyCalib !== undefined) {
      resolved.AyCalib = std_msgs.msg.Float64.Resolve(msg.AyCalib)
    }
    else {
      resolved.AyCalib = new std_msgs.msg.Float64()
    }

    if (msg.AzCalib !== undefined) {
      resolved.AzCalib = std_msgs.msg.Float64.Resolve(msg.AzCalib)
    }
    else {
      resolved.AzCalib = new std_msgs.msg.Float64()
    }

    if (msg.Ax !== undefined) {
      resolved.Ax = std_msgs.msg.Float64.Resolve(msg.Ax)
    }
    else {
      resolved.Ax = new std_msgs.msg.Float64()
    }

    if (msg.Ay !== undefined) {
      resolved.Ay = std_msgs.msg.Float64.Resolve(msg.Ay)
    }
    else {
      resolved.Ay = new std_msgs.msg.Float64()
    }

    if (msg.Az !== undefined) {
      resolved.Az = std_msgs.msg.Float64.Resolve(msg.Az)
    }
    else {
      resolved.Az = new std_msgs.msg.Float64()
    }

    if (msg.AxRaw !== undefined) {
      resolved.AxRaw = std_msgs.msg.Float64.Resolve(msg.AxRaw)
    }
    else {
      resolved.AxRaw = new std_msgs.msg.Float64()
    }

    if (msg.AyRaw !== undefined) {
      resolved.AyRaw = std_msgs.msg.Float64.Resolve(msg.AyRaw)
    }
    else {
      resolved.AyRaw = new std_msgs.msg.Float64()
    }

    if (msg.AzRaw !== undefined) {
      resolved.AzRaw = std_msgs.msg.Float64.Resolve(msg.AzRaw)
    }
    else {
      resolved.AzRaw = new std_msgs.msg.Float64()
    }

    if (msg.Vx !== undefined) {
      resolved.Vx = std_msgs.msg.Float64.Resolve(msg.Vx)
    }
    else {
      resolved.Vx = new std_msgs.msg.Float64()
    }

    if (msg.Vy !== undefined) {
      resolved.Vy = std_msgs.msg.Float64.Resolve(msg.Vy)
    }
    else {
      resolved.Vy = new std_msgs.msg.Float64()
    }

    if (msg.Vz !== undefined) {
      resolved.Vz = std_msgs.msg.Float64.Resolve(msg.Vz)
    }
    else {
      resolved.Vz = new std_msgs.msg.Float64()
    }

    if (msg.Gx !== undefined) {
      resolved.Gx = std_msgs.msg.Float64.Resolve(msg.Gx)
    }
    else {
      resolved.Gx = new std_msgs.msg.Float64()
    }

    if (msg.Gy !== undefined) {
      resolved.Gy = std_msgs.msg.Float64.Resolve(msg.Gy)
    }
    else {
      resolved.Gy = new std_msgs.msg.Float64()
    }

    if (msg.Gz !== undefined) {
      resolved.Gz = std_msgs.msg.Float64.Resolve(msg.Gz)
    }
    else {
      resolved.Gz = new std_msgs.msg.Float64()
    }

    if (msg.currTime !== undefined) {
      resolved.currTime = std_msgs.msg.Float64.Resolve(msg.currTime)
    }
    else {
      resolved.currTime = new std_msgs.msg.Float64()
    }

    return resolved;
    }
};

module.exports = IMUData;
