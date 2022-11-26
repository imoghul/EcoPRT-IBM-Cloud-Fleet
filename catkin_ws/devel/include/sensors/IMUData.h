// Generated by gencpp from file sensors/IMUData.msg
// DO NOT EDIT!


#ifndef SENSORS_MESSAGE_IMUDATA_H
#define SENSORS_MESSAGE_IMUDATA_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Float64.h>

namespace sensors
{
template <class ContainerAllocator>
struct IMUData_
{
  typedef IMUData_<ContainerAllocator> Type;

  IMUData_()
    : AxCalib()
    , AyCalib()
    , AzCalib()
    , Ax()
    , Ay()
    , Az()
    , AxRaw()
    , AyRaw()
    , AzRaw()
    , Vx()
    , Vy()
    , Vz()
    , Gx()
    , Gy()
    , Gz()
    , currTime()  {
    }
  IMUData_(const ContainerAllocator& _alloc)
    : AxCalib(_alloc)
    , AyCalib(_alloc)
    , AzCalib(_alloc)
    , Ax(_alloc)
    , Ay(_alloc)
    , Az(_alloc)
    , AxRaw(_alloc)
    , AyRaw(_alloc)
    , AzRaw(_alloc)
    , Vx(_alloc)
    , Vy(_alloc)
    , Vz(_alloc)
    , Gx(_alloc)
    , Gy(_alloc)
    , Gz(_alloc)
    , currTime(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Float64_<ContainerAllocator>  _AxCalib_type;
  _AxCalib_type AxCalib;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _AyCalib_type;
  _AyCalib_type AyCalib;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _AzCalib_type;
  _AzCalib_type AzCalib;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Ax_type;
  _Ax_type Ax;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Ay_type;
  _Ay_type Ay;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Az_type;
  _Az_type Az;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _AxRaw_type;
  _AxRaw_type AxRaw;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _AyRaw_type;
  _AyRaw_type AyRaw;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _AzRaw_type;
  _AzRaw_type AzRaw;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Vx_type;
  _Vx_type Vx;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Vy_type;
  _Vy_type Vy;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Vz_type;
  _Vz_type Vz;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Gx_type;
  _Gx_type Gx;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Gy_type;
  _Gy_type Gy;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _Gz_type;
  _Gz_type Gz;

   typedef  ::std_msgs::Float64_<ContainerAllocator>  _currTime_type;
  _currTime_type currTime;





  typedef boost::shared_ptr< ::sensors::IMUData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sensors::IMUData_<ContainerAllocator> const> ConstPtr;

}; // struct IMUData_

typedef ::sensors::IMUData_<std::allocator<void> > IMUData;

typedef boost::shared_ptr< ::sensors::IMUData > IMUDataPtr;
typedef boost::shared_ptr< ::sensors::IMUData const> IMUDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sensors::IMUData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sensors::IMUData_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sensors::IMUData_<ContainerAllocator1> & lhs, const ::sensors::IMUData_<ContainerAllocator2> & rhs)
{
  return lhs.AxCalib == rhs.AxCalib &&
    lhs.AyCalib == rhs.AyCalib &&
    lhs.AzCalib == rhs.AzCalib &&
    lhs.Ax == rhs.Ax &&
    lhs.Ay == rhs.Ay &&
    lhs.Az == rhs.Az &&
    lhs.AxRaw == rhs.AxRaw &&
    lhs.AyRaw == rhs.AyRaw &&
    lhs.AzRaw == rhs.AzRaw &&
    lhs.Vx == rhs.Vx &&
    lhs.Vy == rhs.Vy &&
    lhs.Vz == rhs.Vz &&
    lhs.Gx == rhs.Gx &&
    lhs.Gy == rhs.Gy &&
    lhs.Gz == rhs.Gz &&
    lhs.currTime == rhs.currTime;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sensors::IMUData_<ContainerAllocator1> & lhs, const ::sensors::IMUData_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sensors

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sensors::IMUData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensors::IMUData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensors::IMUData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensors::IMUData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensors::IMUData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensors::IMUData_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sensors::IMUData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e854ee703c7cc2b23f6a5df92872cf41";
  }

  static const char* value(const ::sensors::IMUData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe854ee703c7cc2b2ULL;
  static const uint64_t static_value2 = 0x3f6a5df92872cf41ULL;
};

template<class ContainerAllocator>
struct DataType< ::sensors::IMUData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sensors/IMUData";
  }

  static const char* value(const ::sensors::IMUData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sensors::IMUData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Float64 AxCalib\n"
"std_msgs/Float64 AyCalib\n"
"std_msgs/Float64 AzCalib\n"
"std_msgs/Float64 Ax\n"
"std_msgs/Float64 Ay\n"
"std_msgs/Float64 Az\n"
"std_msgs/Float64 AxRaw\n"
"std_msgs/Float64 AyRaw\n"
"std_msgs/Float64 AzRaw\n"
"std_msgs/Float64 Vx\n"
"std_msgs/Float64 Vy\n"
"std_msgs/Float64 Vz\n"
"std_msgs/Float64 Gx\n"
"std_msgs/Float64 Gy\n"
"std_msgs/Float64 Gz\n"
"std_msgs/Float64 currTime\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Float64\n"
"float64 data\n"
;
  }

  static const char* value(const ::sensors::IMUData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sensors::IMUData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.AxCalib);
      stream.next(m.AyCalib);
      stream.next(m.AzCalib);
      stream.next(m.Ax);
      stream.next(m.Ay);
      stream.next(m.Az);
      stream.next(m.AxRaw);
      stream.next(m.AyRaw);
      stream.next(m.AzRaw);
      stream.next(m.Vx);
      stream.next(m.Vy);
      stream.next(m.Vz);
      stream.next(m.Gx);
      stream.next(m.Gy);
      stream.next(m.Gz);
      stream.next(m.currTime);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct IMUData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sensors::IMUData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sensors::IMUData_<ContainerAllocator>& v)
  {
    s << indent << "AxCalib: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.AxCalib);
    s << indent << "AyCalib: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.AyCalib);
    s << indent << "AzCalib: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.AzCalib);
    s << indent << "Ax: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Ax);
    s << indent << "Ay: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Ay);
    s << indent << "Az: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Az);
    s << indent << "AxRaw: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.AxRaw);
    s << indent << "AyRaw: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.AyRaw);
    s << indent << "AzRaw: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.AzRaw);
    s << indent << "Vx: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Vx);
    s << indent << "Vy: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Vy);
    s << indent << "Vz: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Vz);
    s << indent << "Gx: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Gx);
    s << indent << "Gy: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Gy);
    s << indent << "Gz: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.Gz);
    s << indent << "currTime: ";
    s << std::endl;
    Printer< ::std_msgs::Float64_<ContainerAllocator> >::stream(s, indent + "  ", v.currTime);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SENSORS_MESSAGE_IMUDATA_H