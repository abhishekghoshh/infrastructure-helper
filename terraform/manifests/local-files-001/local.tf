resource "random_pet" "my-pet" {
  prefix    = "Mrs"
  separator = "."
  length    = "1"
}

resource "local_file" "pets" {
  filename             = "${path.module}/${var.pets_filename}"
  content              = var.pets_content
  file_permission      = "0777"
  directory_permission = "0777"
  depends_on           = [random_pet.my-pet]
}

resource "local_file" "pets_list" {
  for_each             = var.file_details
  filename             = "${path.module}/${each.key}"
  content              = each.value
  file_permission      = "0777"
  directory_permission = "0777"
}

