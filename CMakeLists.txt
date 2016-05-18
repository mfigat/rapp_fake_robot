cmake_minimum_required(VERSION 2.8.3)
project(rapp_fake_robot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
message_generation
)

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   Say.srv
   Record.srv
   RecognizeWord.srv
   SpeechRecognitionSphinx4ConfigureSrv.srv
   SpeechRecognitionSphinx4Srv.srv
   SpeechRecognitionSphinx4TotalSrv.srv
 )


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rapp_fake_robot
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY launch/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch )

