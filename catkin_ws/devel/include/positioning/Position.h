// Generated by gencpp from file positioning/Position.msg
// DO NOT EDIT!


#ifndef POSITIONING_MESSAGE_POSITION_H
#define POSITIONING_MESSAGE_POSITION_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace positioning
{
template <class ContainerAllocator>
struct Position_
{
  typedef Position_<ContainerAllocator> Type;

  Position_()
    : latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)  {
    }
  Position_(const ContainerAllocator& _alloc)
    : latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)  {
  (void)_alloc;
    }



   typedef double _latitude_type;
  _latitude_type latitude;

   typedef double _longitude_type;
  _longitude_type longitude;

   typedef double _altitude_type;
  _altitude_type altitude;





  typedef boost::shared_ptr< ::positioning::Position_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::positioning::Position_<ContainerAllocator> const> ConstPtr;

}; // struct Position_

typedef ::positioning::Position_<std::allocator<void> > Position;

typedef boost::shared_ptr< ::positioning::Position > PositionPtr;
typedef boost::shared_ptr< ::positioning::Position const> PositionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::positioning::Position_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::positioning::Position_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::positioning::Position_<ContainerAllocator1> & lhs, const ::positioning::Position_<ContainerAllocator2> & rhs)
{
  return lhs.latitude == rhs.latitude &&
    lhs.longitude == rhs.longitude &&
    lhs.altitude == rhs.altitude;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::positioning::Position_<ContainerAllocator1> & lhs, const ::positioning::Position_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace positioning

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::positioning::Position_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::positioning::Position_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::positioning::Position_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::positioning::Position_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::positioning::Position_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::positioning::Position_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::positioning::Position_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c48027a852aeff972be80478ff38e81a";
  }

  static const char* value(const ::positioning::Position_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc48027a852aeff97ULL;
  static const uint64_t static_value2 = 0x2be80478ff38e81aULL;
};

template<class ContainerAllocator>
struct DataType< ::positioning::Position_<ContainerAllocator> >
{
  static const char* value()
  {
    return "positioning/Position";
  }

  static const char* value(const ::positioning::Position_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::positioning::Position_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 latitude\n"
"float64 longitude\n"
"float64 altitude\n"
;
  }

  static const char* value(const ::positioning::Position_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::positioning::Position_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.latitude);
      stream.next(m.longitude);
      stream.next(m.altitude);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Position_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::positioning::Position_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::positioning::Position_<ContainerAllocator>& v)
  {
    s << indent << "latitude: ";
    Printer<double>::stream(s, indent + "  ", v.latitude);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
    s << indent << "altitude: ";
    Printer<double>::stream(s, indent + "  ", v.altitude);
  }
};

} // namespace message_operations
} // namespace ros

#endif // POSITIONING_MESSAGE_POSITION_H
