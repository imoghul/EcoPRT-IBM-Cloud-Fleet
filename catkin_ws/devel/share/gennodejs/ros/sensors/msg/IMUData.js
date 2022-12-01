// Auto-generated. Do not edit!

// (in-package sensors.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

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
      this.GxCalib = null;
      this.GyCalib = null;
      this.GzCalib = null;
      this.GxRaw = null;
      this.GyRaw = null;
      this.GzRaw = null;
      this.currTime = null;
    }
    else {
      if (initObj.hasOwnProperty('AxCalib')) {
        this.AxCalib = initObj.AxCalib
      }
      else {
        this.AxCalib = 0.0;
      }
      if (initObj.hasOwnProperty('AyCalib')) {
        this.AyCalib = initObj.AyCalib
      }
      else {
        this.AyCalib = 0.0;
      }
      if (initObj.hasOwnProperty('AzCalib')) {
        this.AzCalib = initObj.AzCalib
      }
      else {
        this.AzCalib = 0.0;
      }
      if (initObj.hasOwnProperty('Ax')) {
        this.Ax = initObj.Ax
      }
      else {
        this.Ax = 0.0;
      }
      if (initObj.hasOwnProperty('Ay')) {
        this.Ay = initObj.Ay
      }
      else {
        this.Ay = 0.0;
      }
      if (initObj.hasOwnProperty('Az')) {
        this.Az = initObj.Az
      }
      else {
        this.Az = 0.0;
      }
      if (initObj.hasOwnProperty('AxRaw')) {
        this.AxRaw = initObj.AxRaw
      }
      else {
        this.AxRaw = 0.0;
      }
      if (initObj.hasOwnProperty('AyRaw')) {
        this.AyRaw = initObj.AyRaw
      }
      else {
        this.AyRaw = 0.0;
      }
      if (initObj.hasOwnProperty('AzRaw')) {
        this.AzRaw = initObj.AzRaw
      }
      else {
        this.AzRaw = 0.0;
      }
      if (initObj.hasOwnProperty('Vx')) {
        this.Vx = initObj.Vx
      }
      else {
        this.Vx = 0.0;
      }
      if (initObj.hasOwnProperty('Vy')) {
        this.Vy = initObj.Vy
      }
      else {
        this.Vy = 0.0;
      }
      if (initObj.hasOwnProperty('Vz')) {
        this.Vz = initObj.Vz
      }
      else {
        this.Vz = 0.0;
      }
      if (initObj.hasOwnProperty('Gx')) {
        this.Gx = initObj.Gx
      }
      else {
        this.Gx = 0.0;
      }
      if (initObj.hasOwnProperty('Gy')) {
        this.Gy = initObj.Gy
      }
      else {
        this.Gy = 0.0;
      }
      if (initObj.hasOwnProperty('Gz')) {
        this.Gz = initObj.Gz
      }
      else {
        this.Gz = 0.0;
      }
      if (initObj.hasOwnProperty('GxCalib')) {
        this.GxCalib = initObj.GxCalib
      }
      else {
        this.GxCalib = 0.0;
      }
      if (initObj.hasOwnProperty('GyCalib')) {
        this.GyCalib = initObj.GyCalib
      }
      else {
        this.GyCalib = 0.0;
      }
      if (initObj.hasOwnProperty('GzCalib')) {
        this.GzCalib = initObj.GzCalib
      }
      else {
        this.GzCalib = 0.0;
      }
      if (initObj.hasOwnProperty('GxRaw')) {
        this.GxRaw = initObj.GxRaw
      }
      else {
        this.GxRaw = 0.0;
      }
      if (initObj.hasOwnProperty('GyRaw')) {
        this.GyRaw = initObj.GyRaw
      }
      else {
        this.GyRaw = 0.0;
      }
      if (initObj.hasOwnProperty('GzRaw')) {
        this.GzRaw = initObj.GzRaw
      }
      else {
        this.GzRaw = 0.0;
      }
      if (initObj.hasOwnProperty('currTime')) {
        this.currTime = initObj.currTime
      }
      else {
        this.currTime = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IMUData
    // Serialize message field [AxCalib]
    bufferOffset = _serializer.float64(obj.AxCalib, buffer, bufferOffset);
    // Serialize message field [AyCalib]
    bufferOffset = _serializer.float64(obj.AyCalib, buffer, bufferOffset);
    // Serialize message field [AzCalib]
    bufferOffset = _serializer.float64(obj.AzCalib, buffer, bufferOffset);
    // Serialize message field [Ax]
    bufferOffset = _serializer.float64(obj.Ax, buffer, bufferOffset);
    // Serialize message field [Ay]
    bufferOffset = _serializer.float64(obj.Ay, buffer, bufferOffset);
    // Serialize message field [Az]
    bufferOffset = _serializer.float64(obj.Az, buffer, bufferOffset);
    // Serialize message field [AxRaw]
    bufferOffset = _serializer.float64(obj.AxRaw, buffer, bufferOffset);
    // Serialize message field [AyRaw]
    bufferOffset = _serializer.float64(obj.AyRaw, buffer, bufferOffset);
    // Serialize message field [AzRaw]
    bufferOffset = _serializer.float64(obj.AzRaw, buffer, bufferOffset);
    // Serialize message field [Vx]
    bufferOffset = _serializer.float64(obj.Vx, buffer, bufferOffset);
    // Serialize message field [Vy]
    bufferOffset = _serializer.float64(obj.Vy, buffer, bufferOffset);
    // Serialize message field [Vz]
    bufferOffset = _serializer.float64(obj.Vz, buffer, bufferOffset);
    // Serialize message field [Gx]
    bufferOffset = _serializer.float64(obj.Gx, buffer, bufferOffset);
    // Serialize message field [Gy]
    bufferOffset = _serializer.float64(obj.Gy, buffer, bufferOffset);
    // Serialize message field [Gz]
    bufferOffset = _serializer.float64(obj.Gz, buffer, bufferOffset);
    // Serialize message field [GxCalib]
    bufferOffset = _serializer.float64(obj.GxCalib, buffer, bufferOffset);
    // Serialize message field [GyCalib]
    bufferOffset = _serializer.float64(obj.GyCalib, buffer, bufferOffset);
    // Serialize message field [GzCalib]
    bufferOffset = _serializer.float64(obj.GzCalib, buffer, bufferOffset);
    // Serialize message field [GxRaw]
    bufferOffset = _serializer.float64(obj.GxRaw, buffer, bufferOffset);
    // Serialize message field [GyRaw]
    bufferOffset = _serializer.float64(obj.GyRaw, buffer, bufferOffset);
    // Serialize message field [GzRaw]
    bufferOffset = _serializer.float64(obj.GzRaw, buffer, bufferOffset);
    // Serialize message field [currTime]
    bufferOffset = _serializer.float64(obj.currTime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IMUData
    let len;
    let data = new IMUData(null);
    // Deserialize message field [AxCalib]
    data.AxCalib = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [AyCalib]
    data.AyCalib = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [AzCalib]
    data.AzCalib = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Ax]
    data.Ax = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Ay]
    data.Ay = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Az]
    data.Az = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [AxRaw]
    data.AxRaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [AyRaw]
    data.AyRaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [AzRaw]
    data.AzRaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vx]
    data.Vx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vy]
    data.Vy = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vz]
    data.Vz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Gx]
    data.Gx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Gy]
    data.Gy = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Gz]
    data.Gz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [GxCalib]
    data.GxCalib = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [GyCalib]
    data.GyCalib = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [GzCalib]
    data.GzCalib = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [GxRaw]
    data.GxRaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [GyRaw]
    data.GyRaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [GzRaw]
    data.GzRaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [currTime]
    data.currTime = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 176;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensors/IMUData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6bda55b7f9e6f3956c206b862be8ffbe';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new IMUData(null);
    if (msg.AxCalib !== undefined) {
      resolved.AxCalib = msg.AxCalib;
    }
    else {
      resolved.AxCalib = 0.0
    }

    if (msg.AyCalib !== undefined) {
      resolved.AyCalib = msg.AyCalib;
    }
    else {
      resolved.AyCalib = 0.0
    }

    if (msg.AzCalib !== undefined) {
      resolved.AzCalib = msg.AzCalib;
    }
    else {
      resolved.AzCalib = 0.0
    }

    if (msg.Ax !== undefined) {
      resolved.Ax = msg.Ax;
    }
    else {
      resolved.Ax = 0.0
    }

    if (msg.Ay !== undefined) {
      resolved.Ay = msg.Ay;
    }
    else {
      resolved.Ay = 0.0
    }

    if (msg.Az !== undefined) {
      resolved.Az = msg.Az;
    }
    else {
      resolved.Az = 0.0
    }

    if (msg.AxRaw !== undefined) {
      resolved.AxRaw = msg.AxRaw;
    }
    else {
      resolved.AxRaw = 0.0
    }

    if (msg.AyRaw !== undefined) {
      resolved.AyRaw = msg.AyRaw;
    }
    else {
      resolved.AyRaw = 0.0
    }

    if (msg.AzRaw !== undefined) {
      resolved.AzRaw = msg.AzRaw;
    }
    else {
      resolved.AzRaw = 0.0
    }

    if (msg.Vx !== undefined) {
      resolved.Vx = msg.Vx;
    }
    else {
      resolved.Vx = 0.0
    }

    if (msg.Vy !== undefined) {
      resolved.Vy = msg.Vy;
    }
    else {
      resolved.Vy = 0.0
    }

    if (msg.Vz !== undefined) {
      resolved.Vz = msg.Vz;
    }
    else {
      resolved.Vz = 0.0
    }

    if (msg.Gx !== undefined) {
      resolved.Gx = msg.Gx;
    }
    else {
      resolved.Gx = 0.0
    }

    if (msg.Gy !== undefined) {
      resolved.Gy = msg.Gy;
    }
    else {
      resolved.Gy = 0.0
    }

    if (msg.Gz !== undefined) {
      resolved.Gz = msg.Gz;
    }
    else {
      resolved.Gz = 0.0
    }

    if (msg.GxCalib !== undefined) {
      resolved.GxCalib = msg.GxCalib;
    }
    else {
      resolved.GxCalib = 0.0
    }

    if (msg.GyCalib !== undefined) {
      resolved.GyCalib = msg.GyCalib;
    }
    else {
      resolved.GyCalib = 0.0
    }

    if (msg.GzCalib !== undefined) {
      resolved.GzCalib = msg.GzCalib;
    }
    else {
      resolved.GzCalib = 0.0
    }

    if (msg.GxRaw !== undefined) {
      resolved.GxRaw = msg.GxRaw;
    }
    else {
      resolved.GxRaw = 0.0
    }

    if (msg.GyRaw !== undefined) {
      resolved.GyRaw = msg.GyRaw;
    }
    else {
      resolved.GyRaw = 0.0
    }

    if (msg.GzRaw !== undefined) {
      resolved.GzRaw = msg.GzRaw;
    }
    else {
      resolved.GzRaw = 0.0
    }

    if (msg.currTime !== undefined) {
      resolved.currTime = msg.currTime;
    }
    else {
      resolved.currTime = 0.0
    }

    return resolved;
    }
};

module.exports = IMUData;
