from coal import CoalFile
from util import cp, git_clone, glob
from os import path

class RecastFile(CoalFile):
    url = "https://github.com/memononen/recastnavigation.git"
    exports = ["include", "src"]

    def prepare(self):
        git_clone(self.url, 'master', 'repo')
    def package(self):
        cp('repo/Recast/Include/*.h', 'include/')
        cp('repo/Detour/Include/*.h', 'include/')
        cp('repo/DetourCrowd/Include/*.h', 'include/')
        cp('repo/DetourTileCache/Include/*.h', 'include/')
        cp('repo/Recast/Source/*.cpp', 'src/')
        cp('repo/Detour/Source/*.cpp', 'src/')
        cp('repo/DetourCrowd/Source/*.cpp', 'src/')
        cp('repo/DetourTileCache/Source/*.cpp', 'src/')
    def info(self, generator):
        generator.add_include_dir('include/')
        generator.add_source_files(*glob('src/*'))
