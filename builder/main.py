# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
##########################################################################
#
#   WizIO 2020 Georgi Angelov
#       http://www.wizio.eu/
#       https://github.com/Wiz-IO/platform-sam-lora
# 
##########################################################################

from os.path import join
from SCons.Script import (AlwaysBuild, Default, DefaultEnvironment)
from colorama import Fore

env = DefaultEnvironment()
print( Fore.GREEN + '<<<<<<<<<<<< ' + env.BoardConfig().get("name").upper() + " 2019 Georgi Angelov >>>>>>>>>>>>" + Fore.BLACK )

elf = env.BuildProgram()
bin = env.CreateBin( join("$BUILD_DIR", "${PROGNAME}"), elf ) 
hex = env.CreateHex( join("$BUILD_DIR", "${PROGNAME}"), elf ) 
AlwaysBuild( hex, bin )

#env.Depends(hex, env.CreateBin( join("$BUILD_DIR", "${PROGNAME}"), elf ))

upload = env.Alias("upload", hex, [ env.VerboseAction("$UPLOADCMD", "\n"), env.VerboseAction("", "\n") ] )
AlwaysBuild( upload )    

Default( hex, bin )