resource "local_file" "pets" {
  filename = "${path.module}/pets.txt"
  content = "This is a local file created by Terraform."
  file_permission = "0777"
  directory_permission = "0777"
}