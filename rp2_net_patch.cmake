# CMake minimum required version
cmake_minimum_required(VERSION 3.12)

# Find git
find_package(Git)

if(NOT Git_FOUND)
    message(FATAL_ERROR "Could not find 'git' tool rp2_network patching")
endif()

message("RP2040-HAT-MicroPython patch utils found")

set(MICROPY_DIR "libraries")
set(RP2040_HAT_MP_PATCH_DIR "patches")
set(PICO_SDK_LIB_DIR "${MICROPY_DIR}/lib/pico-sdk")
set(AXTLS_LIB_DIR "${MICROPY_DIR}/lib/axtls")

execute_process(COMMAND ${GIT_EXECUTE} -C ${CMAKE_SOURCE_DIR}/libraries submodule update --init)
if(EXISTS "${MICROPY_DIR}/.git")
	message("cleaning MicroPython Lib...")
	execute_process(COMMAND ${GIT_EXECUTABLE} -C ${MICROPY_DIR} clean -fdx)
	execute_process(COMMAND ${GIT_EXECUTABLE} -C ${MICROPY_DIR} reset --hard)
	message(" MicroPython Lib cleaned")
endif()

# Delete untracked files in pico-sdk
if(EXISTS "${PICO_SDK_LIB_DIR}/.git")
	message("cleaning pico-sdk...")
	execute_process(COMMAND ${GIT_EXECUTABLE} -C ${PICO_SDK_LIB_DIR} clean -fdx)
	execute_process(COMMAND ${GIT_EXECUTABLE} -C ${PICO_SDK_LIB_DIR} reset --hard)
	message("pico-sdk cleaned")
endif()

# Delete untracked files in axtls
if(EXISTS "${AXTLS_LIB_DIR}/.git")
	message("cleaning axtls...")
	execute_process(COMMAND ${GIT_EXECUTABLE} -C ${AXTLS_LIB_DIR} clean -fdx)
	execute_process(COMMAND ${GIT_EXECUTABLE} -C ${AXTLS_LIB_DIR} reset --hard)
	message("axtls cleaned")
endif()

execute_process(COMMAND make submodules WORKING_DIRECTORY ${MICROPY_DIR}/ports/rp2 )
execute_process(COMMAND ${GIT_EXECUTABLE} config core.filemode false )

file(GLOB RP2040_HAT_MP_PATCHES 
	"${RP2040_HAT_MP_PATCH_DIR}/0001-Added-WIZnet-Chip-library.patch" 
	)


foreach(RP2040_HAT_MP_PATCHE IN LISTS RP2040_HAT_MP_PATCHES)
	message("Running patch ${RP2040_HAT_MP_PATCHE}")
	execute_process(
		COMMAND ${GIT_EXECUTABLE} apply --whitespace=nowarn ${RP2040_HAT_MP_PATCHE}
		WORKING_DIRECTORY ${MICROPY_DIR}
	)
endforeach()
file(GLOB RP2040_HAT_AX_PATCHES 
	"${RP2040_HAT_MP_PATCH_DIR}/0002-Added-AXTLSlibrary.patch"
	)

foreach(RP2040_HAT_AX_PATCHE IN LISTS RP2040_HAT_AX_PATCHES)
	message("Running patch ${RP2040_HAT_AX_PATCHE}")
	execute_process(
		COMMAND ${GIT_EXECUTABLE} apply --whitespace=nowarn ${RP2040_HAT_AX_PATCHE}
		WORKING_DIRECTORY ${AXTLS_LIB_DIR}
	)
endforeach()
