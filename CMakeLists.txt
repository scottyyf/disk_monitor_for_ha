cmake_minimum_required (VERSION 3.12)
project(disk_percent VERSION 1.0)

set(CPACK_COMPONENTS_ALL ha)
list(APPEND CPACK_COMPONENTS_ALL hadr)

set(CPACK_GENERATOR RPM DEB)
set(CMAKE_INSTALL_PREFIX "/opt/ha")
SET(CPACK_PACKAGING_INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})
set(CPACK_RPM_PACKAGE_AUTOREQPROV " no")

set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}")
set(CPACK_RPM_PACKAGE_RELEASE 1.1)
set(CPACK_RPM_PACKAGE_LICENSE MIT)
set(CPACK_RPM_PACKAGE_REQUIRES "python >= 2.7.0")
set(CPACK_RPM_CHANGELOG_FILE "${CMAKE_SOURCE_DIR}/changelog.txt")
set(CPACK_PACKAGE_VENDOR "scott yyf")
set(CPACK_RPM_PACKAGE_GROUP "SkybilityHA Team")
set(CPACK_PACKAGE_CONTACT "yangyingfa@skybility.com")
set(CPACK_RPM_PACKAGE_URL "https://www.skybilityha.com/download/")
set(CPACK_RPM_PACKAGE_DESCRIPTION "This is a disk space monitor script by yangyingfa@skybility.com")
set(CPACK_RPM_PACKAGE_ARCHITECTURE "x86_64")

add_subdirectory(resource)
add_subdirectory(src)
add_subdirectory(hadr)

include (CPack)

