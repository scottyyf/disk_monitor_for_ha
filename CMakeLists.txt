cmake_minimum_required (VERSION 3.12)
project(disk_percent VERSION 1.0)


install(FILES disk.py DESTINATION /opt/ha/dist-packages/pyagent/disk_percent)
install(FILES meta-data.xml __init__.py DESTINATION /opt/ha/resource/resources/disk_percent/disk)
install(FILES __init__.py DESTINATION /opt/ha/resource/resources/disk_percent)

set(CPACK_PACKAGING_INSTALL_PREFIX /opt/ha/)

set(CPACK_RPM_COMPONENT_INSTALL ON)
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "SkybilityHA disk percent monitor resource for skybiltiyha 2.8")
set(CPACK_PACKAGE_NAME "skybilityhadiskpercent")
set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${PROJECT_VERSION_MAJOR}-${PROJECT_VERSION_MINOR}.${CMAKE_SYSTEM_PROCESSOR}")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}")
set(CPACK_RPM_PACKAGE_ARCHITECTURE "x86_64")
set(CPACK_RPM_PACKAGE_RELEASE 1%{?dist})
set(CPACK_RPM_PACKAGE_LICENSE MIT)
set(CPACK_PACKAGE_VENDOR "scott yyf")
set(CPACK_RPM_PACKAGE_GROUP "SkybilityHA Team")
set(CPACK_PACKAGE_CONTACT "support@skybilityha.com")

set(CPACK_RPM_PACKAGE_URL "https://www.gitlab.skybilityha.com")
set(CPACK_RPM_PACKAGE_DESCRIPTION "This is a disk space monitor script by yangyingfa@skybility.com")
set(CPACK_RPM_PACKAGE_REQUIRES "python >= 2.7.0")
set(CPACK_RPM_CHANGELOG_FILE "${CMAKE_SOURCE_DIR}/changelog.txt")
set(CPACK_RPM_POST_UNINSTALL_SCRIPT_FILE "${CMAKE_SOURCE_DIR}/uninstall.sh")

include (CPack)

