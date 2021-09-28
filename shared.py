import os

def find_command_file(lang, gl_version, command):
  if lang == "en":
    command_file = gl_version + "/" + command + ".xhtml"
  else:
    command_file = lang + "/" + gl_version + "/" + command + ".xhtml"
    
  while not os.path.isfile(command_file):
    if gl_version[:2] == 'gl' and int(gl_version[2]) <= 2:
      return False
      
    if gl_version[:2] == 'es' and int(gl_version[2]) < 1:
      return False

    gl_version = gl_version[:2] + str(int(gl_version[2]) - 1)
    if lang == "en":
      command_file = gl_version + "/" + command + ".xhtml"
    else:
      command_file = lang + "/" + gl_version + "/" + command + ".xhtml"
      
  return command_file

