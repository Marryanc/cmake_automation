import os

def get_path():
  full_path = os.getcwd();
  path_array = full_path.split("/")
  project_name = path_array[len(path_array) - 1]

  return full_path, project_name

def create_make_list():
  obj = get_path()

  all_files = os.listdir(obj[0])

  array_to_compile = []

  for file in all_files:
    if file.endswith(".c"):
      array_to_compile.append(file)

  if not len(array_to_compile) > 0:
      status = "No c files to compile [ERROR]"
      exit([status])

  files_to_compile = " \n  ".join(array_to_compile)

  cmake_string = f"""
  cmake_minimum_required(VERSION 3.10)

  project({obj[1]} C)

  set(CMAKE_C_STANDARD 99)
  set(CMAKE_C_STANDARD_REQUIRED True)

  set(CMAKE_BUILD_TYPE Debug)

  add_executable(my_program
    {files_to_compile}
  )
  """
  return cmake_string

def create_build_directory():
  try:
    os.makedirs("build")
    print("Build Directory Created [SUCCESS]")
  except:
    status = "Build Directory already exists [ERROR]"
    exit([status])

def create_make_file(makelist):
  try:
    file = open("CMakeLists.txt", "w")
    file.write(makelist)
    file.close()
  except:
    status = "Failed to write to file [ERROR]"
    exit([status])

def run_make_commands():
  path = get_path()
  file_path = path[0]+"/build"
  try:
    os.chdir(file_path)
    os.system("cmake ..")
    os.system("cmake --build .")
  except:
    status = "Could not run CMake commands [ERROR]"
    exit([status])

def main():
  create_build_directory()
  create_make_file(create_make_list())
  run_make_commands()

if __name__ == "__main__":
    main()