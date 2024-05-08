### Basic Terraform configuration to instantiate
### a server from Hertzner.
###
### State files are hosted in a bucket on GCS.


# Get terraform state files from Google Cloud Storage
# terraform.tfstate and terraform.tfstate.backup
terraform {
  required_providers {
    hcloud = {
      source = "hetznercloud/hcloud"
    }
  }
  required_version = ">= 0.13"

  backend "gcs" {
    bucket  = "<my-bucket>"
    prefix  = "<path-to-folder>"
  }
}

# Set the variable value in *.tfvars file
# or using the -var="hcloud_token=..." CLI option
variable "hcloud_token" {}

# Configure the Hetzner Cloud Provider
provider "hcloud" {
  token = var.hcloud_token
}

# Create a server, "epdl-backend" is the resource name for terraform
# This name can be used for further reference in the file, such as
# to bind volumes
resource "hcloud_server" "<some-resource-name>" {
  name        = "<server-name>"
  image       = "ubuntu-24.04"
  location    = "nbg1"
  server_type = "cax11"
  ssh_keys    = ["<name-of-ssh-key>"]
}

