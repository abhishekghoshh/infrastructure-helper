variable "pets_filename" {
  description = "The name of the pets file"
  type        = string
}

variable "pets_content" {
  description = "The content of the pets file"
  type        = string
}

variable "file_names" {
  type        = list(string)
  description = "List of file names to be created"
  default = [
    "file1.txt",
    "file2.txt",
    "file3.txt"
  ]
}

variable "tuple_of_files" {
  type        = tuple([string, string, string])
  description = "Tuple of file names to be created"
  default = [
    "file1.txt",
    "file2.txt",
    "file3.txt"
  ]
}

variable "set_of_files" {
  type        = set(string)
  description = "Set of file names to be created"
  default = [
    "file1.txt",
    "file2.txt",
    "file3.txt"
  ]
}


variable "file_details" {
  type        = map(string)
  description = "Map of file names to their content"
  default = {
    "file1.txt" = "Content for file 1"
    "file2.txt" = "Content for file 2"
    "file3.txt" = "Content for file 3"
  }
}

variable "file_objects" {
  type = object({
    filename             = string
    content              = string
    file_permission      = optional(string, "0777")
    directory_permission = optional(string, "0777")
  })
  description = "Object containing file name and content"
  default = {
    filename = "file1.txt"
    content  = "Content for file 1"
  }
}